
import streamlit as st
import pandas as pd
import numpy as np


st.title("Home Page")

st.write("""
# My first App Hello world!*
""")




df = pd.DataFrame(
     np.random.randn(1000, 2) / [50, 50] + [36.819044, 127.114893],
     columns=['lat', 'lon'])

st.map(df)
