import random

import streamlit as st
from modules.chess960 import get_chess960_positions


st.set_page_config(
    page_title="Position Generator",
    layout="wide",
    page_icon='📈'
)


def main():
    st.sidebar.page_link('app.py', label='Home', icon='🏡')
    st.sidebar.page_link('pages/explorer.py', label='Explorer', icon='🏝️')
    st.sidebar.page_link('pages/positions.py', label='Positions', icon='💫')
    st.sidebar.page_link('pages/generator.py', label='Generator', icon='🌀')

    st.title('Random Generator')
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
