import streamlit as st
import sys
from streamlit.config import on_config_parsed
from streamlit.web.cli import main

import sys

sys.path.insert(1, "c:/Users/egonz/anaconda3/envs/workshop/Lib/site-packages/streamlit_option_menu")

from streamlit_option_menu import option_menu


from apps import Transporte, prior, PoblaEcon, Geol, Cons, Clima # import your app modules here

st.set_page_config(page_title= 'Ordenamiento Territorial',page_icon=':tada:',layout='wide')

#Use local css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html= True)
        
        
local_css('style/style.css')

# st.sidebar.title("Ordenamiento Territorial")
# st.sidebar.info(
#     """
# El Ordenamiento Territorial en Yucatán es un instrumento de política ambiental que tiene como objetivo regular o inducir el uso del suelo y las actividades humanas en la región. A continuación, se presentan algunos detalles sobre cómo se aplica el Ordenamiento Territorial en Yucatán:

# - El gobierno del estado de Yucatán cuenta con una Secretaría de Desarrollo Sustentable (SDS) encargada de implementar el Ordenamiento Ecológico y Territorial en la región.+

# - El Ordenamiento Territorial en Yucatán se rige por la Ley de Ordenamiento Territorial y Desarrollo Urbano del Estado de Yucatán, que establece las bases para la planificación y gestión del territorio en la región.

# - El Plan de Gestión Territorial es un instrumento clave para la implementación del Ordenamiento Territorial en Yucatán. Este plan establece las directrices para el uso del suelo y las actividades humanas en la región, y se elabora a través de un protocolo específico.

# - El Ordenamiento Territorial en Yucatán se enfoca en la conservación de los recursos naturales y la biodiversidad de la región, así como en el desarrollo sustentable de las actividades humanas.

# - El Ordenamiento Territorial en Yucatán se lleva a cabo a través de un proceso participativo que involucra a las comunidades locales, las autoridades y otros actores relevantes en la región.

# En resumen, el Ordenamiento Territorial en Yucatán es un instrumento de política ambiental que busca regular el uso del suelo y las actividades humanas en la región, con el objetivo de promover el desarrollo sustentable y la conservación de los recursos naturales y la biodiversidad. Este proceso se lleva a cabo a través de un plan de gestión territorial y un proceso participativo que involucra a las comunidades locales y otros actores relevantes en la región.
#     """
# )

st.sidebar.title("En resumen")
st.sidebar.info(
    """
En este sitio se presenta el resultado de la evaluación de análisis multivariable en Yucatán. Cabe señalar que esta evaluación está enfocada en localizar las zonas con las condiciones óptimas para el desarrollo de la economía del estado yucateco. Este factor es de gran importancia ya que como uno de los objetivos prioritarios del ordenamiento territorial esta velar por una buena calidad de vida de las personas que habitan el territorio. 
    """
)


# A dictionary of apps in the format of {"App title": "App icon"}
# More icons can be found here: https://icons.getbootstrap.com

apps = [
    # {"func": home.app, "title": "Home", "icon": "house"},
    {"func": prior.app, "title": "Priorización", "icon": "map"},
    {"func": Cons.app, "title": "Conservación", "icon": "map"},
    {"func": Geol.app, "title": "Agricultura", "icon": "map"},
    {"func": PoblaEcon.app, "title": "Población Economicamente activa", "icon": "map"},
    {"func": Transporte.app, "title": "Transporte", "icon": "map"},
    {"func": Clima.app, "title": "Clima", "icon": "map"}
]

titles = [app["title"] for app in apps]
titles_lower = [title.lower() for title in titles]
icons = [app["icon"] for app in apps]

params = st.experimental_get_query_params()

if "page" in params:
    default_index = int(titles_lower.index(params["page"][0].lower()))
else:
    default_index = 0

with st.sidebar:
    selected = option_menu(
        "Menú Principal",
        options=titles,
        icons=icons,
        menu_icon="cast",
        default_index=default_index,
    )
    
    
    
 #Documentation Change email address
    contact_form = """ 
    
    <form action="https://formsubmit.co/egonzalezllamas@gmail.com" method="POST">
     <input type= 'hidden' name= '_captcha' value= 'false'>
     <input type="text" name="name" placeholder='Nombre' required>
     <input type="email" name="email" placeholder= 'Tu email' required>
     <textarea name= 'message' placeholder= 'Escriba el mensaje' required></textarea>
     <button type="submit">Enviar</button>
    </form>
    
    """
    
    
    

    st.sidebar.title("Contacto")
    st.sidebar.markdown(contact_form, unsafe_allow_html= True)


for app in apps:
    if app["title"] == selected:
        app["func"]()
        break