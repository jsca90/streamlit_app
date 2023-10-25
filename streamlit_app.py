import streamlit as st


start = st.date_input(label='Start: ',
              value=None,
              key='#start',
              help="The start date time",
                      on_change=lambda : None)

end = st.date_input(label='End: ',
              value=None,
              key='#end',
              help="The end date time",
                    on_change=lambda : None)
st.write('Start: ', start, "End: ", end)
