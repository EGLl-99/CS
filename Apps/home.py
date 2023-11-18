import streamlit as st
import leafmap.foliumap as leafmap


def app():
    st.title("Home")

    m = leafmap.Map(locate_control=True)
    m.add_basemap("ROADMAP")
    m.to_streamlit(height=700)

    Map1= geemap.Map(center=[20.828,-103.411],zoom= 11)

    legend_dict = {
        '1 Agua': 'blue',
        '2 Bosque': 'green',
        '3 Pastizal': '#08e723',
        '4 Suelo': '#FF0000',
        '5 Urbano': 'yellow'
    }

    imagen= ee.Image('projects/ee-egonzalezllamas/assets/my_export_jalisco2')
    imagen2= ee.Image('projects/ee-egonzalezllamas/assets/my_export_21052000')

    Map.setCenter(20.828,-103.411,11)
    vis_clas2= {
        'palette':['blue','green','#08e723','#FF0000','yellow'],
        'min':1,
        'max':4
    }

    Map1.add_basemap('HYBRID')

    Map1.addLayer(imagen,vis_clas2,'Uso de Suelo 10-04-2020')
    Map1.addLayer(imagen2,vis_clas2,'Uso de Suelo 21-05-2000')
    Map1.add_legend(legend_dict=legend_dict)
    Map1
