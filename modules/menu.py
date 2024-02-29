import streamlit as st


def get_menu():
    st.sidebar.page_link('app.py', label='Home', icon='🏡')
    st.sidebar.page_link('pages/explorer.py', label='Explorer', icon='🏝️')
    st.sidebar.page_link('pages/positions.py', label='Positions', icon='💫')
    st.sidebar.page_link('pages/generator.py', label='Generator', icon='🌀')
    st.sidebar.page_link('pages/download.py', label='Downloads', icon='📥')
    