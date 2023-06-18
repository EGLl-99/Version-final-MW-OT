import streamlit as st 
import leafmap.foliumap as leafmap

def app():
    
    st.title('Evaluación Multicriterio Yucatan') 
    
    filepath= 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv'
    m= leafmap.Map(tiles= 'stamentoner')
    m.add_heatmap(
        filepath,
        latitude= 'latitude',
        longitude= 'longitude',
        value= 'pop_max',
        name= 'Mapa de calor',
        radius= 20,
    )
    m.to_streamlit(height=700)