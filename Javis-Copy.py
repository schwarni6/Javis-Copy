import streamlit as st
from datetime import datetime

st.title("Meine Sprach-KI")

command = st.text_input("Gib einen Befehl ein:")

def execute_command(command):
    command = command.lower()

    if "hallo" in command:
        return "Hallo! Wie kann ich helfen?"

    elif "uhrzeit" in command:
        now = datetime.now().strftime("%H:%M")
        return f"Es ist {now} Uhr."

    elif "youtube" in command:
        st.markdown("[YouTube öffnen](https://www.youtube.com)")
        return "YouTube-Link bereit."

    elif "google" in command:
        st.markdown("[Google öffnen](https://www.google.com)")
        return "Google-Link bereit."

    else:
        return "Diesen Befehl kenne ich noch nicht."

if st.button("Ausführen"):
    response = execute_command(command)
    st.success(response)
