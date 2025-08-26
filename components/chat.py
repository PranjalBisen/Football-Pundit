import streamlit as st

class ChatInterface:
    def __init__(self):
        if "messages" not in st.session_state:
            st.session_state.messages = []

    def get_user_input(self):
        return st.chat_input("⚽ Ask anything about football...")

    def display_message(self, user_input: str, response: str):
        """Display messages with better UI spacing"""
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.session_state.messages.append({"role": "assistant", "content": response})

        for message in st.session_state.messages:
            if message["role"] == "user":
                with st.container():
                    st.markdown(
                        f"<div class='user-message'>🤔 <b>You:</b> {message['content']}</div>",
                        unsafe_allow_html=True
                    )
                    st.markdown("<br>", unsafe_allow_html=True)  # gap
            else:
                with st.container():
                    st.markdown(
                        f"<div class='assistant-message'>⚽ <b>Football Genius:</b><br>{message['content']}</div>",
                        unsafe_allow_html=True
                    )
                    st.markdown("<hr>", unsafe_allow_html=True)  