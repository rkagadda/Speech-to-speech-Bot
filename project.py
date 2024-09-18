import streamlit as st
import speech_recognition as sr
import pyttsx3
import google.generativeai as genai 

# Replace this with your actual Google API key
GOOGLE_API_KEY = "AIzaSyDH5hByP9Okxe8IpO7UYHqImsH24M"

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Initialize session state for chat history if not already present
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def llm(text): 
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(text)
    return response.text.capitalize()

def recognize_speech_from_microphone(listening_placeholder):
    with sr.Microphone() as source:
        listening_placeholder.info("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        try:
            # Capture audio for a fixed duration (e.g., 5 seconds)
            audio = recognizer.record(source, duration=3)
            text = recognizer.recognize_google(audio)
            st.session_state.chat_history.append(f"You: {text}")
            listening_placeholder.empty()  # Clear the "Listening..." message
            return text
        except sr.UnknownValueError:
            listening_placeholder.error("Could not understand the audio")
        except sr.RequestError:
            listening_placeholder.error("Could not request results from the service")
        return None

def speak_text(text):
    if tts_engine._inLoop:  # Check if the event loop is already running
        tts_engine.endLoop()  # End the loop if it's running
    tts_engine.say(text)
    tts_engine.runAndWait()

# Streamlit app UI
st.subheader("Welcome to TensorGo!!How can I help you?")
st.write("Click the microphone button to speak.")
 
if st.button("🎤 Start Talking"):
    listening_placeholder = st.empty()  # Create a placeholder for the "Listening..." message
    recognized_text = recognize_speech_from_microphone(listening_placeholder)
    if recognized_text:
        with st.spinner("Processing..."):
            processed_text = llm(recognized_text)
            st.session_state.chat_history.append(f"Bot: {processed_text}")
        
        st.subheader("Chat History")
        for message in st.session_state.chat_history:
            st.code(message)
        speak_text(processed_text)
