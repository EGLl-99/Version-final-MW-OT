import streamlit as st
import ee
import geemap.foliumap as geemap
import folium

ee.Authenticate()
#st.set_page_config(layout='wide')


def app():
    st.title("Conservación ")

    Map= geemap.Map(center=[20.4064,-88.4738],zoom= 7)
    Map.add_basemap('HYBRID')
    
    
    legend_dict = {
    'Requiere un estudio': '#008000',
    'Turismo': '#FFFF00',
    'Prohibido': '#FF3333'
}
    
    markdown= """
        
       Yucatán es uno de los estados dentro de la República México donde se encuentra gran riqueza natural y cultural, debido a ello cuentan con estrategias y acciones implementadas para preservar y proteger los ecosistemas, la biodiversidad y el patrimonio cultural de la zona. 

Para la determinación de estas zonas de conservación y estrategias se basa en información como los son: 

 - Arenas Naturales Protegidas (ANP) - Estas son zonas donde no han sufrido alteraciones por actividades humanas y requieren ser preservadas. 

- Sitio prioritarios para la conservación de la biodiversidad terrestre (STP) - En esta se analizan factores de fauna y flora para determinar la importancia que tiene la zona y cuáles son sus metas de conservación. 

- Áreas de Importancia para la Conservación de las Aves (AICAS) - Con estas podemos identificar las especies que se encuentran en alguna zona determinada, así como la importancia de conservación de sus hábitats. 

Teniendo toda esta información recopilada se pueden generar estrategias que satisfagan las necesidades del estado para conservar su riqueza natural y cultural.
        
    """
    
    st.markdown(markdown)
    capa1= ee.Image('users/emiliogonzalez/Conservacion1')
    #capa2= ee.Image('')
    #capa3= ee.Image('')
    #capa4= ee.Image('')
    #capa5= ee.Image('')
    #capa6= ee.Image('')

    vis1= {'palette':['#008000','#FFFF00','#FF3333'], 'min':1,'max':5}
    
    Map.add_legend(legend_dict=legend_dict)
    
    Map.addLayer(capa1,vis1,'Conservación')
    
    Map.to_streamlit(height=750)