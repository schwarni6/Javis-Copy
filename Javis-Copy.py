import streamlit as st
from geopy.geocoders import Nominatim
from datetime import datetime

st.set_page_config(layout="wide")
st.title("Universal KI Assistent")

geolocator = Nominatim(user_agent="universal_ki")

command = st.text_input("Befehl eingeben")

def execute(cmd):
    cmd = cmd.lower()

    if "hallo" in cmd:
        st.success("Hallo! Ich bin deine KI.")
        return

    elif "uhrzeit" in cmd:
        now = datetime.now().strftime("%H:%M")
        st.success(f"Es ist {now} Uhr")
        return

    elif "datum" in cmd:
        st.success(str(datetime.now().date()))
        return

    elif "rechne" in cmd:
        try:
            expression = cmd.replace("rechne", "").strip()
            result = eval(expression)
            st.success(f"Ergebnis: {result}")
        except:
            st.error("Rechenfehler")
        return

    elif "stadtplan" in cmd:
        city = cmd.replace("stadtplan", "").strip()

        location = geolocator.geocode(city)

        if location:
            lat = location.latitude
            lon = location.longitude

            st.success(f"Stadtplan von {city}")

            map_url = f"https://www.openstreetmap.org/export/embed.html?bbox={lon-0.05},{lat-0.05},{lon+0.05},{lat+0.05}&layer=mapnik&marker={lat},{lon}"

            st.components.v1.iframe(
                map_url,
                width=1200,
                height=700
            )
        else:
            st.error("Stadt nicht gefunden")
        return

    else:
        st.warning("Befehl nicht erkannt")

if st.button("Ausführen"):
    execute(command)
