import streamlit as st
from geopy.geocoders import Nominatim
from datetime import datetime

st.set_page_config(
    page_title="Universal KI",
    page_icon="🤖",
    layout="wide"
)

geolocator = Nominatim(user_agent="universal_ki")

# Design
st.markdown("""
<style>
.main-title {
    font-size: 42px;
    font-weight: bold;
    text-align: center;
    color: #00BFFF;
}
.command-box {
    padding: 15px;
    border-radius: 15px;
    background-color: #1e1e1e;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">🤖 Universal KI Assistent</p>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("⚙️ Funktionen")
    st.write("✅ Stadtpläne")
    st.write("✅ Uhrzeit")
    st.write("✅ Datum")
    st.write("✅ Rechnen")
    st.write("✅ Begrüßung")

    st.divider()

    st.subheader("Beispiele")
    st.code("""
hallo
uhrzeit
datum
rechne 25*8
stadtplan lübeck
""")

# Eingabe
command = st.text_input("💬 Befehl eingeben")

# Layout
col1, col2 = st.columns([1, 2])

with col1:
    run = st.button("▶ Ausführen", use_container_width=True)

def execute(cmd):
    cmd = cmd.lower()

    if "hallo" in cmd:
        st.success("👋 Hallo! Ich bin deine KI.")
        return

    elif "uhrzeit" in cmd:
        st.info(f"🕒 {datetime.now().strftime('%H:%M')}")
        return

    elif "datum" in cmd:
        st.info(f"📅 {datetime.now().date()}")
        return

    elif "rechne" in cmd:
        try:
            expression = cmd.replace("rechne", "").strip()
            result = eval(expression)
            st.success(f"🧮 Ergebnis: {result}")
        except:
            st.error("Rechenfehler")
        return

    elif "stadtplan" in cmd:
        city = cmd.replace("stadtplan", "").strip()
        location = geolocator.geocode(city)

        if location:
            lat = location.latitude
            lon = location.longitude

            st.success(f"📍 Stadtplan von {city}")

            map_url = f"https://www.openstreetmap.org/export/embed.html?bbox={lon-0.05},{lat-0.05},{lon+0.05},{lat+0.05}&layer=mapnik&marker={lat},{lon}"

            st.components.v1.iframe(
                map_url,
                width=1000,
                height=650
            )
        else:
            st.error("Stadt nicht gefunden")
        return

    else:
        st.warning("Befehl nicht erkannt")

if run:
    execute(command)
