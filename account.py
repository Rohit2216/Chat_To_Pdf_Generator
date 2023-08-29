import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

# Initialize Firebase
cred = credentials.Certificate('chattopdf-f142c-435381ca7cbe.json')
# firebase_admin.initialize_app(cred)

# Create a Streamlit app
def app():
    st.title('Welcome to  :violet[Chat 2 PDF]')

    choice = st.selectbox('Login/Signup', ['Login', 'Sign Up'])

    if choice == 'Login':
        email = st.text_input('Email Address')
        password = st.text_input('Password', type='password')

        if st.button('Login'):
            try:
                user = auth.get_user_by_email(email)
                st.success('Login Successfully')

                # Set the username in session state
                st.session_state.username = user.uid  # You can change this based on your use case

            except auth.UserNotFoundError:
                st.warning('Login failed. User not found.')
            except auth.InvalidPasswordError:
                st.warning('Login failed. Invalid password.')

    else:
        email = st.text_input('Email Address')    
        password = st.text_input('Password', type='password')
        username = st.text_input('Enter your unique username')

        if st.button('Create my account'):
            try:
                user = auth.create_user(email=email, password=password, uid=username)
                st.success('Account created Successfully')
                st.markdown('Please Login using your Email and password')

                # Set the username in session state
                st.session_state.username = username  # Assuming 'username' is unique

            except auth.EmailAlreadyExistsError:
                st.warning('Account creation failed. Email already exists.')
