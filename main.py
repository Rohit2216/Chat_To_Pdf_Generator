import streamlit as st
from streamlit_option_menu import option_menu
import home, account, trending, about, chat

if 'pdf_data' not in st.session_state:
    st.session_state.pdf_data = {}


class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        with st.sidebar:
            app = option_menu(
                menu_title='Query Assistant',
                options=['Home', 'Account', 'Trending', '📝Query Assistant', 'About'],
                icons=['house-fill', 'person-circle', 'trophy-fill', 'chat-fill', 'info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px", "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )

        if app == "Home":
            home.app()
        if app == "Account":
            account.app()
        if app == "Trending":
            trending.app()
        if app == '📝Query Assistant':
            chat.app()
        if app == "About":
            about.app()

if __name__ == '__main__':
    multi_app = MultiApp()
    multi_app.run()
