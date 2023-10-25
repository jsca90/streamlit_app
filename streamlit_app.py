import streamlit as st



# Three columns with different widths
col1, col2, col3 = st.columns([3,1,1])
# col1 is wider

# Using 'with' notation:
with col1:
  st.date_input('Date input')

with col2:
  st.date_input('Date input')

with col3:
  st.text('g')
