import random

import streamlit as st
from modules.chess960 import get_chess960_positions
from modules.menu import get_menu


st.set_page_config(
    page_title="Position Generator",
    layout="centered",
    page_icon='📈'
)


def main():
    get_menu()

    st.title('🎲 Random Generator')
    st.markdown('Generates chess960 position randomly')

    if st.button('Generate random position', type='primary'):
        df = get_chess960_positions()

        random_number = random.randint(1, 960)
        result = df.loc[df['posnum'] == random_number, 'epd'].head(1).values
        epd = result[0]
        st.markdown(
            f'''
            fen:  
            **{epd} 0 1**

            pos:  
            **{random_number}**
            '''
        )


if __name__ == '__main__':
    main()
