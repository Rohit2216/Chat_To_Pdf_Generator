import streamlit as st

# Set page configuration
# st.set_page_config(page_title="📝PDF Query Assistant 📝")

def app():
    st.title('About 📝PDF Query Assistant')
    
    st.markdown(
        "Welcome to **📝PDF Query Assistant**, a revolutionary platform designed to provide instant answers to questions from PDF documents. "
        "Our mission is to make information extraction from PDFs a seamless experience for users like you."
    )
    
    st.write("## Key Features:")
    st.write("- **PDF Upload**: Easily upload PDF documents to extract information from.")
    st.write("- **Smart Question-Answer**: Get answers to your questions related to the uploaded PDF.")
    st.write("- **Interactive Interface**: Our user-friendly interface ensures a hassle-free experience.")
    st.write("- **Customization**: Personalize your experience by setting preferences and themes.")
    
    st.write("## How it Works:")
    st.write("1. **Upload PDF**: Simply upload the PDF document you want to extract information from.")
    st.write("2. **Ask Questions**: Enter your questions related to the content of the PDF.")
    st.write("3. **Get Answers**: Receive instant answers generated from the PDF content.")
    
    st.write("## Meet the Team:")
    st.write("📝PDF Query Assistant is brought to you by a passionate team of developers committed to simplifying information retrieval:")
    st.markdown("- **Rohit Chauhan**: [GitHub](https://github.com/Rohit2216) | [Email](mailto:chauhanrohit716@gmail.com)")

    st.write("## Contact Us:")
    st.write("Have questions, feedback, or suggestions? We'd love to hear from you! Reach out to us via email:")
    st.markdown("[chauhanrohit716@gmail.com](mailto:chauhanrohit716@gmail.com)")
    
    st.write("## Legal Information:")
    st.write("📝PDF Query Assistant is a registered trademark. All rights reserved.")
    
    st.markdown("&copy; 2023 📝PDF Query Assistant. All Rights Reserved.")

# Run the app
app()
