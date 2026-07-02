import streamlit as st
from googletrans import Translator
from gtts import gTTS
import pyperclip
import os

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Language Translator",
    page_icon="🌍",
    layout="centered"
)

# ---------------- Custom CSS ----------------
st.markdown("""
<style>
.main {
    background-color: #0E1117;
}

.stButton>button {
    width: 100%;
    border-radius: 10px;
    height: 3em;
    background-color: #4CAF50;
    color: white;
    font-weight: bold;
}

.result-box {
    padding: 20px;
    border-radius: 10px;
    background-color: #1E293B;
    color: white;
    font-size: 22px;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Translator ----------------
translator = Translator()

languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja",
    "Russian": "ru",
    "Chinese": "zh-cn",
    "Arabic": "ar",
    "Italian": "it",
    "Portuguese": "pt",
    "Bengali": "bn",
    "Punjabi": "pa",
    "Tamil": "ta",
    "Telugu": "te",
    "Korean": "ko"
}

# ---------------- Header ----------------
st.title(" AI Language Translation Tool")
st.write("Translate text instantly into multiple languages.")

st.divider()

# ---------------- Input ----------------
text = st.text_area(
    "Enter Text",
    height=180,
    placeholder="Type something here..."
)

st.caption(f"Characters: {len(text)}")

# ---------------- Language Selection ----------------
col1, col2 = st.columns(2)

with col1:
    source = st.selectbox(
        "Source Language",
        list(languages.keys())
    )

with col2:
    target = st.selectbox(
        "Target Language",
        list(languages.keys()),
        index=1
    )

# ---------------- Swap Button ----------------
if st.button(" Swap Languages"):
    source, target = target, source

st.write("")

# ---------------- Translate ----------------
if st.button(" Translate"):

    if text.strip() == "":
        st.warning("Please enter some text.")

    elif source == target:
        st.warning("Please select different languages.")

    else:
        try:
            translated = translator.translate(
                text,
                src=languages[source],
                dest=languages[target]
            )

            result = translated.text

            st.success("Translation Successful")

            st.markdown(
                f"""
                <div class='result-box'>
                    {result}
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write("")

            # Copy Button
            if st.button(" Copy Translation"):
                pyperclip.copy(result)
                st.success("Copied to Clipboard!")

            # Text to Speech
            tts = gTTS(result)
            tts.save("translation.mp3")

            audio_file = open("translation.mp3", "rb")
            st.audio(audio_file.read())

            # Download Translation
            st.download_button(
                "⬇ Download Translation",
                result,
                file_name="translation.txt"
            )

        except Exception as e:
            st.error(f"Error: {e}")