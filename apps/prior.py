import streamlit as st
import ee
import geemap.foliumap as geemap
import folium
geemap.ee_initialize()
#st.set_page_config(layout='wide')


def app():
    st.title('Transporte')
    Map= geemap.Map(center=[20.4064,-88.4738],zoom= 7)
    Map.add_basemap('HYBRID')

def app():
    st.title('Capas Priorizadas')
    Map= geemap.Map(center=[20.4064,-88.4738],zoom= 7)
    Map.add_basemap('HYBRID')
    
    legend_dict = {
    'Factible': '#008000',
    'Medianamente factible': '#FFFF00',
    'No es factible': '#FF3333'
}
    
    markdown= """
        
  Evaluación multicriterio para la priorización de zonas económicas importantes en Yucatán
        
Para la evaluación multicriterio de la priorización de zonas económicas importantes en Yucatán se tomaron en cuenta los siguientes factores:
        
        Agricultura

- La producción agropecuaria y pesquera de Yucatán asciende a seis millones 521 mil 772 toneladas, de las cuales el 68.2% corresponde a la agricultura.

- La agricultura milpera es una práctica tradicional de los mayas de Yucatán, que consiste en el policultivo de maíz, camote, calabaza y leguminosas.

        Vías terrestres 

La infraestructura vial en Yucatán se ha fortalecido en los últimos años para mejorar la movilidad y la seguridad tanto para peatones como para automovilistas.

- La ciudad de Mérida cuenta con varias arterias viales, entre las más importantes está la carretera federal núm. 180, que viene de la ciudad de Campeche, y la autopista que enlaza a la entidad con la ciudad de Cancún.
Población económicamente activa 
La población económicamente activa en Yucatán es de 1,196,624 personas, lo que representa el 50.7% de la población total.

- El 95.2% de la población económicamente activa en Yucatán se dedica a algún tipo de actividad de producción de bienes o servicios.

        Clima 

El clima en Yucatán es cálido y subhúmedo en la mayor parte del estado, con lluvias en verano.

- La temperatura media anual es de 26°C, y la temperatura máxima promedio es alrededor de 36°C y se presenta en el mes de mayo, mientras que la temperatura mínima promedio es de 18°C y se presenta en enero. La humedad es alta y las temperaturas son elevadas y constantes.

        Conservación  

En Yucatán existen áreas naturales protegidas que son importantes para la conservación de la biodiversidad y el turismo. La valoración económica para las áreas naturales protegidas marinas del Parque Nacional Huatulco, Oaxaca, México, es un ejemplo de cómo se pueden valorar económicamente estas áreas.

        
    """
    
    st.markdown(markdown)
    capa1= ee.Image('users/emiliogonzalez/Priorizacion1')
    #capa2= ee.Image('')
    #capa3= ee.Image('')
    #capa4= ee.Image('')
    #capa5= ee.Image('')
    #capa6= ee.Image('')

    vis1= {'palette':['#008000','#41DE07','#FFA533','#FF3333'], 'min':1,'max':4}
    
    Map.add_legend(legend_dict=legend_dict)
    
    Map.addLayer(capa1,vis1,'Priorización')
    
    Map.to_streamlit(height=750)