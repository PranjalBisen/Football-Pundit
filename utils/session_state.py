import streamlit as st

def initialize_session_state():
    """Initialize session state variables"""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    if "temperature" not in st.session_state:
        st.session_state.temperature = 0.7
    
    if "expertise" not in st.session_state:
        st.session_state.expertise = "Expert"