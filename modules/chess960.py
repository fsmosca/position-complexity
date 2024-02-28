import streamlit as st
import pandas as pd


@st.cache_data
def get_chess960_positions():
    return pd.read_csv('./static/chess960_analysis.csv')