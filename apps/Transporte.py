import streamlit as st
import ee
import geemap.foliumap as geemap
import folium

ee.Authenticate('egonzalezllamas@gmail.com')
ee.Initialize()
#st.set_page_config(layout='wide')


def app():
    st.title('Transporte')
    Map= geemap.Map(center=[20.4064,-88.4738],zoom= 7)
    Map.add_basemap('HYBRID')
    
    
    legend_dict = {
    'Vias cercanas': '#008000',
    'Vias cercanas - Medio Alto': '#41DE07',
    'Vias cercanas - medio Bajo': '#FFFF00',
    'Lejano': '#FFA533',
    'Muy Lejano': '#FF3333'
}
    
    markdown= """
        
        La infraestructura vial en Yucatán se ha fortalecido en los últimos años para mejorar la movilidad y la seguridad tanto para peatones como para automovilistas. El Programa Sectorial de Infraestructura para el Desarrollo Sustentable 2013-2018 tiene como objetivo impulsar un Yucatán competitivo mediante la construcción de infraestructura. La península de Yucatán cuenta con una infraestructura de transporte que incluye una red vial y ejes troncales para el movimiento de mercancías y personas. La ciudad de Mérida cuenta con varias arterias viales, entre las más importantes está la carretera federal núm. 180, que viene de la ciudad de Campeche, y la autopista que enlaza a la entidad con la ciudad de Cancún.
        
        1.- Ferroviaria
En México está compuesta por: 17,360 km de vía principal y secundaria concesionada, 4,474 km de vía auxiliar (patios y laderos) y 1,555 km de vías particulares, las cuales en conjunto suman un total de 23,389 km de vía operada.

Impulsar la modernización estratégica de las vías ferroviarias en el estado.

Líneas de acción:

• Modernizar las vías férreas existentes en el estado para el traslado de pasajeros y carga.

• Impulsar el uso de la infraestructura ferroviaria en el estado.

• Impulsar la rehabilitación y modernización de las vías férreas de la línea Mayab.

• Gestionar libramientos ferroviarios en zonas urbanas.

• Impulsar la conexión intermodal y multimodal.

• Fomentar el uso de la infraestructura ferroviaria para carga y pasajeros.

En Yucatán hay 609 km de vía férrea

        2.- Marítima
Permite enviar y recibir todo tipo de cargas, desde fluidos petroquímicos hasta graneles minerales o agrícolas y carga general de contenedores y grupajes. Actualmente existen 117 puertos a lo largo de toda nuestra zona costera

        3.- Terrestre (carreteras)
Desde 2020 se cuenta con una red de carretera de extensión 407,958 km, de los cuales; 51,197 km corresponden a la Red Carretera Federal y 356,761 km integran la red rural y alimentadora

La infraestructura terrestre es un factor determinante para el fomento del desarrollo económico y mejorar la calidad de vida de la población. Asimismo, esta brinda comunicación permanente entre los centros de población con los polos regionales de desarrollo, centros de producción y consumo.

Como medio de comunicación imprescindible para lograr una eficiencia logística contribuye a elevar la competitividad, reducir los costos y el tiempo de transporte, así como facilitar el acceso a mercados e integrar cadenas productivas, a la vez que contribuye al bienestar de la población, pues facilita el acceso a los servicios de educación, salud entre otros; y con ello disminuir los desequilibrios regionales.

Contribuye significativamente a la integración territorial y al desarrollo de las actividades productivas, facilita el traslado de personas y el intercambio de bienes y servicios, y ayuda a reducir costos que conducen al mejoramiento de la competitividad.

Con una conectividad terrestre de calidad, permitirá la disminución de accidentes, lo que se traducirá en un estado más seguro y comunicado, con una mayor cobertura que acercará a comunidades alejadas, y reducirá la brecha social existente. Con esto, se mejorará no solo la competitividad, sino se fomentará el desarrollo económico, generación de empleo a través de la construcción, modernización y mantenimiento de infraestructura estratégica.

Objetivos:

1.- Modernizar la carretera en el estado.

2.- Construir y modernizar los tramos carreteros federales.

3.- Conservar la superficie de rodamiento de la red de carretera.
        
    """
    
    st.markdown(markdown)
    capa1= ee.Image('users/emiliogonzalez/Transporte1')
    #capa2= ee.Image('')
    #capa3= ee.Image('')
    #capa4= ee.Image('')
    #capa5= ee.Image('')
    #capa6= ee.Image('')

    vis1= {'palette':['#008000','#41DE07','#FFFF00','#FFA533','#FF3333'], 'min':1,'max':5}
    
    Map.add_legend(legend_dict=legend_dict)
    
    Map.addLayer(capa1,vis1,'Transporte')
    
    Map.to_streamlit(height=750)