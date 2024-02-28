import pygwalker as pyg
from pygwalker.api.streamlit import init_streamlit_comm
import streamlit as st
from streamlit import session_state as ss
from modules.pygwalker import get_pyg_renderer


st.set_page_config(
    page_title="Explorer",
    layout="wide",
    page_icon='📈'
)


if 'selected_pos' not in ss:
    ss.selected_pos = None


init_streamlit_comm()


st.sidebar.page_link('app.py', label='Home', icon='🏡')
st.sidebar.page_link('pages/explorer.py', label='Explorer', icon='🏝️')
st.sidebar.page_link('pages/positions.py', label='Positions', icon='💫')
st.sidebar.page_link('pages/generator.py', label='Generator', icon='🌀')
 
# Add Title
st.title("Explorer")
st.markdown(':blue[**Drag and drop**] fields into the Y and X axes or to filters, colors, etc.')

renderer = get_pyg_renderer()
renderer.render_explore()
