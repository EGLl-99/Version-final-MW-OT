import streamlit as st
import ee
import geemap.foliumap as geemap
import folium

ee.Authenticate()
#st.set_page_config(layout='wide')


def app():
    st.title('Agricultura')
    Map= geemap.Map(center=[20.4064,-88.4738],zoom= 7)
    Map.add_basemap('HYBRID')
    
    
    legend_dict = {
    'Apto para cultivo': '#008000',
    'Requiere de un estudio': '#FFFF00',
    'No es apto para cultivo': '#FF3333'
}
    
    
    
    markdown= """
        
La priorización obtenida de la evaluación se rige por factores tales como: 

        Físicos	

La composición física de un suelo es importante para la agricultura por varias razones. A continuación, se presentan algunos de los motivos:

- Estructura: La estructura del suelo influye en su capacidad para retener agua y nutrientes, así como en su capacidad para permitir la penetración de las raíces de las plantas. Un suelo con una buena estructura es esencial para el crecimiento y desarrollo de las plantas.

- Textura: La textura del suelo influye en su capacidad para retener agua y nutrientes, así como en su capacidad para permitir la penetración de las raíces de las plantas. Un suelo con una textura adecuada es esencial para el crecimiento y desarrollo de las plantas.
- Porosidad: La porosidad del suelo influye en su capacidad para retener agua y permitir la penetración de las raíces de las plantas. Un suelo con una buena porosidad es esencial para el crecimiento y desarrollo de las plantas.

- Erosión: La composición física del suelo también puede influir en su capacidad para resistir la erosión. Un suelo con una buena estructura y porosidad es más resistente a la erosión y, por lo tanto, más adecuado para la agricultura.

En resumen, la composición física del suelo es importante para la agricultura porque influye en su capacidad para retener agua y nutrientes, permitir la penetración de las raíces de las plantas y resistir la erosión. La estructura, textura y porosidad del suelo son factores clave en su composición física y son esenciales para el crecimiento y desarrollo de las plantas.

        Químicos

La composición química de un suelo es importante para la agricultura por varias razones. A continuación, se presentan algunos de los motivos:

- Nutrientes: La composición química del suelo influye en la cantidad y calidad de los nutrientes disponibles para las plantas. Los nutrientes esenciales como el nitrógeno, el fósforo y el potasio son necesarios para el crecimiento de las plantas, y su disponibilidad en el suelo es fundamental para el éxito de la agricultura.

- Fertilidad: La fertilidad del suelo es un factor clave en la producción agrícola. La composición química del suelo influye en su capacidad para retener nutrientes y en su capacidad para mantener la estructura adecuada para el crecimiento de las plantas.

- Plaguicidas: La composición química del suelo también puede influir en la efectividad de los plaguicidas y otros productos químicos utilizados en la agricultura. Los suelos con una composición química adecuada pueden ayudar a reducir la necesidad de productos químicos y mejorar su eficacia.

- Erosión: La composición química del suelo también puede influir en su capacidad para resistir la erosión. Los suelos con una composición química adecuada pueden ser más resistentes a la erosión y, por lo tanto, más adecuados para la agricultura.

En resumen, la composición química del suelo es importante para la agricultura porque influye en la cantidad y calidad de los nutrientes disponibles para las plantas, la fertilidad del suelo, la efectividad de los productos químicos utilizados en la agricultura y la capacidad del suelo para resistir la erosión.

        Biológicos

La composición biológica de un suelo es importante para la agricultura por varias razones. A continuación, se presentan algunos de los motivos:

- Nutrientes: La biota del suelo, incluyendo los microorganismos, descomponen la materia orgánica y liberan nutrientes esenciales para las plantas. Los microorganismos también ayudan a fijar el nitrógeno atmosférico en el suelo, lo que es esencial para el crecimiento de las plantas.

- Fertilidad: La biota del suelo también influye en la fertilidad del suelo. Los microorganismos ayudan a mantener la estructura del suelo y a retener nutrientes, lo que es esencial para el crecimiento de las plantas.

- Plagas y enfermedades: La biota del suelo también puede influir en la presencia de plagas y enfermedades en los cultivos. Los microorganismos beneficiosos pueden ayudar a controlar las plagas y enfermedades, mientras que los microorganismos perjudiciales pueden contribuir a su propagación.

- Erosión: La biota del suelo también puede influir en la capacidad del suelo para resistir la erosión. Los microorganismos beneficiosos pueden ayudar a mantener la estructura del suelo y a reducir la erosión.

En resumen, la composición biológica de un suelo es importante para la agricultura porque influye en la disponibilidad de nutrientes para las plantas, la fertilidad del suelo, la presencia de plagas y enfermedades en los cultivos y la capacidad del suelo para resistir la erosión. La biota del suelo, incluyendo los microorganismos, es esencial para mantener la salud del suelo y el éxito de la agricultura.

        
    """
    
    st.markdown(markdown)
    capa1= ee.Image('users/emiliogonzalez/Geomorfologia1')
    #capa2= ee.Image('')
    #capa3= ee.Image('')
    #capa4= ee.Image('')
    #capa5= ee.Image('')
    #capa6= ee.Image('')

    vis1= {'palette':['#008000','#FFFF00','#FF3333'], 'min':1,'max':5}
    
    Map.add_legend(legend_dict=legend_dict)
    
    Map.addLayer(capa1,vis1,'Agricultura')
    
    Map.to_streamlit(height=750)