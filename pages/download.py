import streamlit as st
from streamlit import session_state as ss
from modules.menu import get_menu


st.set_page_config(
    page_title="Download",
    layout="centered",
    page_icon='📈'
)


def main():
    get_menu()

    st.markdown(
    '''
    # 🗃️📂 Download files
    '''
    )    

    with open("./static/chess960_startpos.epd", "r") as file:
        st.download_button(
            label="📜 Download chess960 startpos epd file",
            data=file,
            file_name="chess960_startpos.epd",
            mime="text/epd"
        )

    with open("./static/chess960_startpos.fen", "r") as file:
        st.download_button(
            label="🗒️ Download chess960 startpos fen file",
            data=file,
            file_name="chess960_startpos.fen",
            mime="text/fen"
        )

    with open("./static/chess960_start.pgn", "r") as file:
        st.download_button(
            label="📚 Download chess960 startpos pgn file",
            data=file,
            file_name="chess960_start.pgn",
            mime="text/pgn"
        )
    

if __name__ == '__main__':
    main()