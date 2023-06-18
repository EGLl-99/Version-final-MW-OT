import streamlit as st
from multiapp import MultiApp
from apps import (
    Clima,
    Cons,
    Geol,
    PoblaEcon,
    prior,
    Transporte,
    #gee_datasets,
    #heatmap,
    #home,
    #housing,
    # hurricane,
    #plotly_maps,
    #raster,
    #timelapse,
    #vector,
    #wms,
    #xy,
)

st.set_page_config(layout="wide")


apps = MultiApp()

# Add all your application here

apps.add_app("Clima", Clima.app)
apps.add_app("Cons", Cons.app)
# apps.add_app("Hurricane Mapping", hurricane.app)
apps.add_app("Geol", Geol.app)
apps.add_app("PoblaEcon", PoblaEcon.app)
apps.add_app("prior", prior.app)
apps.add_app("Transporte", Transporte.app)
#apps.add_app("Search Basemaps", basemaps.app)
# apps.add_app("Pydeck Gallery", deck.app)
# apps.add_app("Heatmaps", heatmap.app)
# apps.add_app("Add Points from XY", xy.app)
# apps.add_app("Add Web Map Service (WMS)", wms.app)
# apps.add_app("Google Earth Engine (GEE)", gee.app)
# apps.add_app("Awesome GEE Community Datasets", gee_datasets.app)
# apps.add_app("Geolocation", device_loc.app)
# apps.add_app("Cesium 3D Map", cesium.app)
# apps.add_app("Plotly", plotly_maps.app)

# The main app
apps.run()
