import streamlit as st
from datetime import datetime
import folium
from streamlit_folium import st_folium
from geopy.geocoders import Nominatim
import requests

st.set_page_config(page_title="Universal KI", layout="wide")

st.title("Universal KI Assistent")

geolocator = Nominatim(user_agent="universal_ki")

command = st.text_input("Gib einen Befehl ein")

def show_city(city):
    location = geolocator.geocode(city)

    if location:
        m = folium.Map(
            location=[location.latitude, location.longitude],
            zoom_start=12
        )
        st_folium(m, width=900, height=500)
        return f"Stadtplan von {city}"
    return "Stadt nicht gefunden"

def execute(command):
    cmd = command.lower()

    if "uhrzeit" in cmd:
        return datetime.now().strftime("%H:%M")

    elif "datum" in cmd:
        return str(datetime.now().date())

    elif "stadtplan" in cmd:
        city = cmd.replace("stadtplan", "").strip()
        return show_city(city)

    elif "rechne" in cmd:
        expression = cmd.replace("rechne", "").strip()
        try:
            return str(eval(expression))
        except:
            return "Fehler in der Rechnung"

    elif "hallo" in cmd:
        return "Hallo! Ich bin deine KI."

    else:
        return "Befehl nicht erkannt"

if st.button("Ausführen"):
    result = execute(command)
    st.success(result)
