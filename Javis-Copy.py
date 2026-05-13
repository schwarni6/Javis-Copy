import streamlit as st
import speech_recognition as sr
import webbrowser
from datetime import datetime

st.title("Voice KI Assistent")

recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        st.write("🎤 Ich höre...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio, language="de-DE")
        return command.lower()
    except:
        return "Ich konnte dich nicht verstehen."

def execute_command(command):
    if "hallo" in command:
        return "Hallo! Wie kann ich helfen?"

    elif "öffne google" in command:
        webbrowser.open("https://www.google.com")
        return "Google wird geöffnet."

    elif "uhrzeit" in command:
        now = datetime.now().strftime("%H:%M")
        return f"Es ist {now} Uhr."

    elif "youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "YouTube wird geöffnet."

    else:
        return "Diesen Befehl kenne ich noch nicht."

if st.button("🎙 Spracheingabe starten"):
    command = listen()
    st.write(f"**Du hast gesagt:** {command}")

    response = execute_command(command)
    st.success(response)
