import streamlit as st
import folium
from streamlit_folium import st_folium
from geopy.geocoders import Nominatim
from datetime import datetime

st.set_page_config(page_title="Universal KI", layout="wide")

st.title("Universal KI")

geolocator = Nominatim(user_agent="universal_ki")

if "map_data" not in st.session_state:
    st.session_state.map_data = None

command = st.text_input("Befehl eingeben")

def show_city(city):
    location = geolocator.geocode(city)

    if location:
        st.session_state.map_data = {
            "lat": location.latitude,
            "lon": location.longitude,
            "name": city
        }
        return f"Stadtplan von {city} geladen"
    return "Stadt nicht gefunden"

def execute(cmd):
    cmd = cmd.lower()

    if "uhrzeit" in cmd:
        return datetime.now().strftime("%H:%M")

    elif "stadtplan" in cmd:
        city = cmd.replace("stadtplan", "").strip()
        return show_city(city)

    elif "hallo" in cmd:
        return "Hallo!"

    return "Befehl nicht erkannt"

if st.button("Ausführen"):
    result = execute(command)
    st.success(result)

if st.session_state.map_data:
    data = st.session_state.map_data

    m = folium.Map(
        location=[data["lat"], data["lon"]],
        zoom_start=12
    )

    folium.Marker(
        [data["lat"], data["lon"]],
        popup=data["name"]
    ).add_to(m)

    st_folium(m, width=1000, height=600)
