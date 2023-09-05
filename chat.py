import streamlit as st
import pickle
import os
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback
from dotenv import load_dotenv
import spacy

# Initialize session state as a dictionary
if 'pdf_data' not in st.session_state:
    st.session_state.pdf_data = {}
if 'current_pdf' not in st.session_state:
    st.session_state.current_pdf = None

# Load a spaCy NLP model for text processing
nlp = spacy.load("en_core_web_sm")

# ...

def generate_suggested_questions(text, max_questions=3, max_question_length=7):
    # Use spaCy to extract sentences from the text
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents if len(sent.text.strip()) > 10]  # Filter out very short sentences

    # Generate questions by converting sentences to questions
    suggested_questions = []
    for i, sentence in enumerate(sentences):
        if len(suggested_questions) < max_questions:
            # Split the sentence into words
            words = sentence.split()
            if 5 <= len(words) <= max_question_length:
                question = " ".join(words)
                suggested_questions.append(question)

    return suggested_questions

# ...



def upload_new_pdf():
    new_pdf = st.file_uploader("Upload a New PDF", type='pdf')

    if new_pdf is not None:
        pdf_reader = PdfReader(new_pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_text(text=text)

        store_name = new_pdf.name[:-4] if new_pdf.name else "default"  # Handle the case when pdf.name is None

        if store_name not in st.session_state.pdf_data:
            embeddings = OpenAIEmbeddings()
            VectorStore = FAISS.from_texts(chunks, embedding=embeddings)
            st.session_state.pdf_data[store_name] = VectorStore

            # Save the PDF data to a pickle file
            with open(f"{store_name}.pkl", "wb") as file:
                pickle.dump(VectorStore, file)

            # Set the current PDF to the newly uploaded PDF
            st.session_state.current_pdf = store_name

            # Generate suggested questions (limit to 2-3 questions)
            suggested_questions = generate_suggested_questions(text, max_questions=3)
            if suggested_questions:
                st.write("Suggested Questions:")
                for i, question in enumerate(suggested_questions):
                    st.write(f"{i + 1}. {question}")

def app():
    st.markdown(
        """
        <h1 style='display: flex; align-items: center;'>
            <span style='font-size: 48px; color: orange;'>📝PDF </span>
            <span style='font-size: 48px; color: white;'>Query</span>
            <span style='font-size: 48px; color: green;'>Assistant</span>
            
        </h1>
        """,
        unsafe_allow_html=True
    )
    load_dotenv()
    
    if st.session_state['username']:
        st.write('User Details: '+st.session_state['username'] )
        # Create tabs for "PDF History" and "Upload New PDF"
        selected_tab = st.radio("Select Tab", ["PDF History", "Upload New PDF"])

        if selected_tab == "PDF History":
    # Display the history of uploaded PDFs
            pdf_names = list(st.session_state.pdf_data.keys())
            if pdf_names:
                st.session_state.current_pdf = st.selectbox("Select PDF from History", pdf_names)
                remove = st.button("Remove Selected PDF")
                if remove:
                    # Remove the selected PDF data and associated pickle file
                    st.session_state.pdf_data.pop(st.session_state.current_pdf, None)
                    os.remove(f"{st.session_state.current_pdf}.pkl")
                    st.session_state.current_pdf = None
            else:
                st.write("No PDFs in History")

        elif selected_tab == "Upload New PDF":
            # Upload a new PDF file
            upload_new_pdf()

        # Input section for asking questions
        query = st.text_input("Ask Questions About your Pdf File:", key="question_input")

        if query:
            if st.session_state.current_pdf is not None:  # Add this check
                docs = st.session_state.pdf_data[st.session_state.current_pdf].similarity_search(query=query, k=3)
                llm = OpenAI(model_name='gpt-3.5-turbo')
                chain = load_qa_chain(llm=llm, chain_type="stuff")
                with get_openai_callback() as cb:
                    response = chain.run(input_documents=docs, question=query)
                st.write(response)
            else:
                st.warning("Please select a PDF from the history or upload a new PDF.")

    else:
        st.title(":blue[Welcome! Please] login :blue[to continue.]")    

if __name__ == '__main__':
    app()
