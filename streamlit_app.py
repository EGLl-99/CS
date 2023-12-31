import streamlit as st
from streamlit_option_menu import option_menu
from Apps import ClasSup  # import your app modules here

st.set_page_config(page_title="Streamlit Geospatial Analysis", layout="wide")


apps = [
    {"func": ClasSup.app, "title": "Resultado Clasificacón Supervisada", "icon": "map"}
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
        "Main Menu",
        options=titles,
        icons=icons,
        menu_icon="cast",
        default_index=default_index,
    )

    st.sidebar.title("About")
    st.sidebar.info(
        "A ver"
    )

for app in apps:
    if app["title"] == selected:
        app["func"]()
        break
