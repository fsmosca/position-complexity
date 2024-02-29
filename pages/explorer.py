from pygwalker.api.streamlit import init_streamlit_comm
import streamlit as st
from streamlit import session_state as ss
from modules.pygwalker import get_pyg_renderer
from modules.menu import get_menu


st.set_page_config(
    page_title="Explorer",
    layout="wide",
    page_icon='📈'
)


if 'selected_pos' not in ss:
    ss.selected_pos = None


init_streamlit_comm()

get_menu()
 
# Add Title
st.title("🌍 Explorer")
st.markdown(':blue[**Drag and drop**] fields into the Y and X axes or to filters, colors, etc.')

renderer = get_pyg_renderer()
renderer.render_explore()
