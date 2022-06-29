import streamlit as st
from streamlit_folium import st_folium
import folium
import requests
import json

r = requests.get('https://raw.githubusercontent.com/vuski/admdongkor/master/ver20220401/HangJeongDong_ver20220401.geojson')
c = r.content
emd = json.loads(c)

st.write("천안시 Geo_Json")

m = folium.Map(
    location=[36.8044654, 127.2274944],
    zoom_start=12, 
    tiles='cartodbpositron',
    
)
try:
    for i in emd['features']:
        if i['properties']['temp'].startswith('천안시'):
            folium.GeoJson( i , tooltip=i['properties']['temp']).add_to(m)
    
except Exception as e:
    print(e)

st_folium(m, width = 725)
