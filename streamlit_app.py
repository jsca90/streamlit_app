
import streamlit as st
import pandas as pd
import numpy as np

# df = pd.read_excel('excel.xlsx', header=None)
# df = df.rename(columns=df.iloc[0]).drop(index=0).reset_index(drop=True)
# df = df.astype(int)

# arr = np.array(df)
# u, indices = np.unique(arr, return_index=True)
# values, counts = np.unique(arr, return_counts=True)

# st.title("Lotto Analysis")
# df.columns = df.columns.astype(str)

values= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
        20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
        37, 38, 39, 40, 41, 42, 43, 44, 45]
counts = [174, 163, 161, 168, 151, 156, 158, 154, 132, 162, 160, 169, 172,
        164, 158, 158, 172, 168, 153, 166, 160, 130, 141, 162, 149, 164,
        174, 143, 139, 151, 160, 142, 169, 177, 155, 156, 163, 162, 168,
        163, 142, 156, 180, 157, 158]

res = pd.DataFrame(index=values, data=counts)
st.dataframe(res, height=400, width=400)

st.bar_chart(res, height=400, width=400)




# df = pd.DataFrame(
#      np.random.randn(1000, 2) / [50, 50] + [36.819044, 127.114893],
#      columns=['lat', 'lon'])

# st.map(df)
