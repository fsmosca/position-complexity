import streamlit as st
from streamlit import session_state as ss
import streamlit.components.v1 as components
from modules.chess960 import get_chess960_positions
from modules.menu import get_menu


st.set_page_config(
    page_title="Chess960 Positions",
    layout="wide",
    page_icon='📈'
)


if 'selected_pos' not in ss:
    ss.selected_pos = None


st.markdown(
    """
    <style>
    [data-testid="stElementToolbar"] {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)


def sel_pos():
    ss.selected_pos = ss.pos


def main():
    get_menu()

    st.markdown(
    '''
    # 👑 Chess960 Positions  
    **Each position is analysed by Stockfish 16.1 at multipv 5.**
    '''
    )

    df = get_chess960_positions()
    df['header'] = df['posnum'].astype(str) + ', ' + df['epd']
    st.slider('Score', value=(-50, 100), min_value=-200, max_value=200, key='score')

    df = df[(df['score'] >= ss.score[0]) & (df['score'] <= ss.score[1])]
    header = df['header'].unique()

    # ui_board = st.empty()
    st.selectbox('Select position', options=header, key='pos', label_visibility='collapsed', on_change=sel_pos)

    if not ss.selected_pos and ss.pos:
        ss.selected_pos = ss.pos

    if ss.selected_pos:
        epd = ss.selected_pos.split(', ')[1]
        # board_svg = chess.svg.board(board=chess.Board(epd, chess960=True), size=500)

        # cols = st.columns([1, 2])
        # with cols[0]:
        #     st.image(board_svg)  

        # with cols[1]:
        # embed streamlit docs in a streamlit app
        base_url = 'https://lichess.org/analysis/chess960/'
        url = f'{base_url}{epd.replace(" ", "_")}'
        components.iframe(url, height=310, width=550, scrolling=True)  
    
        df = df[df['epd'] == epd]

        st.dataframe(
            df,
            column_config={
                'header': None,
                'top': None,
            },
            use_container_width=True,
            hide_index=True
        )


if __name__ == '__main__':
    main()
