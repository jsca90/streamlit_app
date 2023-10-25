import streamlit as st


start = st.date_input(label='Start: ',
              value=datetime.datetime(year=2022, month=5, day=20, hour=16, minute=30),
              key='#start',
              help="The start date time",
                      on_change=lambda : None)

# end = st.date_input(label='End: ',
#               value=datetime.datetime(year=2022, month=5, day=30, hour=16, minute=30),
#               key='#end',
#               help="The end date time",
#                     on_change=lambda : None)
# st.write('Start: ', start, "End: ", end)
