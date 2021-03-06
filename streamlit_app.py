import streamlit as st
import folium
import requests
import json
from streamlit_folium import st_folium

# @st.cache
# def load_data():
r = requests.get('https://raw.githubusercontent.com/jsca90/streamlit_app/main/cheonan.json')
c = r.content
emd = json.loads(c)
    # return emd

# emd = load_data()

st.write("천안시 Geo_Json")



m = folium.Map(
    location=[36.8044654, 127.2274944],
    zoom_start=11, 
    tiles='cartodbpositron',
    
)
try:
    for i in emd['features']:
      folium.GeoJson( i, tooltip=i['properties']['temp'].split()[1].replace(" ","") ).add_to(m)
#     for i in emd['features']:
#         if i['properties']['temp'].startswith('천안시'):
#             folium.GeoJson( i , tooltip=i['properties']['temp'].split()[1].replace(" ","")).add_to(m)
#       folium.GeoJson( emd,  ).add_to(m)
    
except Exception as e:
    print(e)

st_data = st_folium(m, width = 725)
