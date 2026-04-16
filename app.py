import streamlit as st
from deep_translator import GoogleTranslator

st.title("🌍 AI Translator App")

text = st.text_area("Enter text")

languages = {
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "English": "en"
}

lang = st.selectbox("Select language", list(languages.keys()))

if st.button("Translate"):
    if text:
        translated = GoogleTranslator(source='auto', target=languages[lang]).translate(text)
        st.success(translated)
    else:
        st.warning("Enter text first")