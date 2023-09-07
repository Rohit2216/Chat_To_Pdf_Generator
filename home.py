import streamlit as st

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

    st.write('Welcome to **PDF Query Assistant**, a platform designed to help you convert chat messages into PDF documents.')

    st.write('To get started, please login first and then select one of the options from the sidebar.')

    st.header('How it Works:')
    st.write('1. Login with your credentials using the sidebar option.')
    st.write('2. Once logged in, you can upload your chat messages or paste them directly into the application.')
    st.write('3. Customize the PDF settings, such as title and author name.')
    st.write('4. Click on the "Upload to PDF" button to generate the PDF document.')
    st.write('5. You can download the PDF or share it with others.')

    st.header('Features:')
    st.write('- Supports various chat message formats, including text, emojis, and media.')
    st.write('- Customizable PDF options for personalization.')
    st.write('- Download and share your chat history in a convenient PDF format.')
    st.write('- Simple and user-friendly interface.')

    st.header('Get Started:')
    st.write('If you are new to the application, click on the "Register" option in the sidebar to create an account.')
    st.write('If you already have an account, click on "Login" to access the application.')

    # You can add more content or instructions here as needed.

# Run the app
app()
