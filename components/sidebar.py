import streamlit as st

def create_sidebar():
    with st.sidebar:
        st.image("static/images/football.jpg", width=250) 

        st.markdown("""
        <div class="sidebar-title">
            ⚽ FOOTBALL GENIUS
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<h3 class='sidebar-section'>Quick Access</h3>", unsafe_allow_html=True)
        st.markdown("""
        <ul class="sidebar-list">
            <li>🏆 Latest Scores</li>
            <li>📊 Statistics</li>
            <li>🎯 Predictions</li>
            <li>📚 Football History</li>
        </ul>
        """, unsafe_allow_html=True)

        # Featured Topics
        st.markdown("<h3 class='sidebar-section'>Featured Topics</h3>", unsafe_allow_html=True)
        st.markdown("""
        <ul class="sidebar-list">
            <li>⭐ Champions League</li>
            <li>🌍 World Cup</li>
            <li>🏆 Premier League</li>
            <li>🌟 Top Players</li>
        </ul>
        """, unsafe_allow_html=True)