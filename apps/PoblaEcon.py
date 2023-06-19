import streamlit as st
import ee
import geemap.foliumap as geemap
import folium

ee.Authenticate()
ee.Initialze()
#st.set_page_config(layout='wide')


def app():
    st.title('Población Economicamente Activa')
    Map= geemap.Map(center=[20.4064,-88.4738],zoom= 7)
    Map.add_basemap('HYBRID')
    
    legend_dict = {
    'Poca poblacion economicamente activa': '#008000',
    'Poblacion economicamente activa- Bajo': '#41DE07',
    'Poblacion economicamente activa- Medio Bajo': '#FFFF00',
    'Poblacion economicamente activa- Medio Alto': '#FFA533',
    'Mayor poblacion economicamente activa': '#FF3333'
}
    
    
    markdown= """
        
        Entre las principales actividades productivas que se llevan a cabo en el estado se encuentran: comercio; construcción; industria alimentaria; información en medios masivos; y servicios inmobiliarios y de alquiler de bienes muebles e intangibles. Juntas representan el 62.0% del PIB estatal.
        
El Producto Interno Bruto (PIB) de Yucatán en 2015 representó el 1.5% y ocupó el lugar 23, con respecto al total nacional y en comparación con el año anterior tuvo una variación en valores constantes de 3.97%1
Entre las principales actividades se encuentran: comercio (21.8%); construcción (11.4%); industria alimentaria (11.7%); información en medios masivos (4.2%); servicios inmobiliarios y de alquiler de bienes muebles e intangibles (12.9%). Juntas representan el 62.0% del PIB estatal

        ACTIVIDADES PRIMARIAS

En el cuarto trimestre de 2021, las Actividades Primarias (agricultura, cría y explotación de
animales, aprovechamiento forestal, pesca y caza) reportaron un aumento anual de 26.2%,
principalmente por el comportamiento de la agricultura. Con ello Yucatán se situó en el 2º lugar
a nivel nacional, como lo muestra la gráfica.

        ACTIVIDADES SECUNDARIAS

Las Actividades Secundarias corresponden a los sectores dedicados a la industria de la
minería, manufacturas, construcción y electricidad. El ascenso anual de 5.5% de las
Actividades Secundarias ubicó a Yucatán en el onceavo lugar entre las 32 entidades
federativas del país.

        ACTIVIDADES TERCIARIAS

Las Actividades Terciarias incluyen a los sectores dedicados a la distribución de bienes y aquellas actividades vinculadas con operaciones de información y de activos, así como con servicios afines al conocimiento y experiencia personal. Incluyen también los relacionados con la recreación y con la parte gubernamental, entre otros. En el cuarto trimestre de 2021, Yucatán registró en estas actividades una variación anual de 3%, lo cual ubica a este estado en el lugar 11 a nivel nacional.

        
    """
    
    st.markdown(markdown)
    capa1= ee.Image('users/emiliogonzalez/Pobla_Econ1')
    #capa2= ee.Image('')
    #capa3= ee.Image('')
    #capa4= ee.Image('')
    #capa5= ee.Image('')
    #capa6= ee.Image('')

    vis1= {'palette':['#008000','#41DE07','#FFFF00','#FFA533','#FF3333'], 'min':1,'max':5}
    
    Map.add_legend(legend_dict=legend_dict)
    
    Map.addLayer(capa1,vis1,'Transporte')
    
    Map.to_streamlit(height=750)