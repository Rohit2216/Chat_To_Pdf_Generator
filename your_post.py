import streamlit as st

def app():
    
    # Access the username from session state
    username = st.session_state.username

    if username:
        st.title('Posts by: ' + username)

        # Display the posts associated with the username
        # You can fetch and display the posts from Firebase here
        # Example: result = db.collection('Posts').document(username).get()
        # Then, display the posts as needed.

    else:
        st.warning('Please Login first')
