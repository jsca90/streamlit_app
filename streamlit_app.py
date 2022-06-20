
import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_excel('excel.xlsx', header=None)
df = df.rename(columns=df.iloc[0]).drop(index=0).reset_index(drop=True)
df = df.astype(int)

arr = np.array(df)
u, indices = np.unique(arr, return_index=True)
values, counts = np.unique(arr, return_counts=True)

st.title("Lotto Analysis")
df.columns = df.columns.astype(str)


res = pd.DataFrame(index=values, data=counts)
st.dataframe(res, height=400, width=400)

st.bar_chart(res, height=400, width=400)




# df = pd.DataFrame(
#      np.random.randn(1000, 2) / [50, 50] + [36.819044, 127.114893],
#      columns=['lat', 'lon'])

# st.map(df)
