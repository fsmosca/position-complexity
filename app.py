from pygwalker.api.streamlit import init_streamlit_comm
import pygwalker as pyg
import streamlit as st
import streamlit.components.v1 as components
import streamlit as st
from streamlit import session_state as ss
from modules.pygwalker import get_df, VIS_SPEC
from modules.menu import get_menu


st.set_page_config(
    page_title="Tournament Visualizer",
    layout="wide",
    page_icon='📈'
)


if 'selected_pos' not in ss:
    ss.selected_pos = None


def main():
    init_streamlit_comm()

    get_menu()

    st.title('✨ Data Visualizer')

    st.markdown('''
**:trophy: [Freestyle Chess](https://www.freestyle-chess.com/) G.O.A.T. Challenge 2024** 
                ''')
    # renderer = get_pyg_renderer()
    # renderer.render_explore()

    df = get_df()
    pyg_html = pyg.to_html(df, spec=VIS_SPEC)
    components.html(pyg_html, height=1000, scrolling=True)


if __name__ == '__main__':
    main()
