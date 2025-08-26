import streamlit as st
from components.chat import ChatInterface
from components.sidebar import create_sidebar
from utils.ai_handler import process_football_query
from utils.session_state import initialize_session_state
from dotenv import load_dotenv

load_dotenv()

def inject_custom_css():
    with open("static/styles/custom.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def main():
    st.set_page_config(
        page_title="FOOTBALL GENIUS",
        page_icon="⚽",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    inject_custom_css()
    initialize_session_state()

    create_sidebar()

    with st.container():
        st.markdown("""
        <div class="main-header">
            <h1>⚽ FOOTBALL GENIUS</h1>
            <h3>Your Ultimate Football Companion</h3>
        </div>
        """, unsafe_allow_html=True)

        chat = ChatInterface()

        if not st.session_state.get("welcomed", False):
            welcome_message = """
            👋 Welcome to Football Genius! I'm your AI football expert, ready to discuss:
            <br><br>
            - Tactical analysis <br>
            - Player statistics <br>
            - Historical matches <br>
            - Latest football news <br>
            - Transfer rumors <br>
            - And much more! <br><br>
            ⚡ Ask me anything about football!
            """
            st.markdown(f"<div class='chat-welcome'>{welcome_message}</div>", unsafe_allow_html=True)
            st.session_state.welcomed = True

        user_input = chat.get_user_input()

        if user_input:
            with st.spinner("⚽ Analyzing..."):
                try:
                    response = process_football_query(
                        query=user_input,
                        model="gemini-2.5-flash"  
                    )
                    chat.display_message(user_input, response)
                except Exception:
                    st.error("⚠️ Sorry, I couldn't process that request. Please try again.")

    st.markdown("""
    <div class="footer">
        ⚡ Powered by <strong>Pranjal D Bisen</strong>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()