# AI Language Translation Tool

A web application that translates text between multiple languages using Python, Streamlit, and Google Translate API.

## Project Overview

This application allows users to:

- Enter text for translation
- Select source and target languages
- Translate text instantly
- Copy translated text
- Listen to translated text using text-to-speech
- Download the translated text as a file

## Technologies Used

- Python
- Streamlit
- Googletrans
- gTTS
- Pyperclip

## Project Structure

```text
CodeAlpha_LanguageTranslationTool/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── screenshots/
```

## Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/CodeAlpha_LanguageTranslationTool.git
cd CodeAlpha_LanguageTranslationTool
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
streamlit run app.py
```

The application will run on:

```text
http://localhost:8501
```

## Features

- Real-time language translation
- Multiple language support
- Text-to-speech functionality
- Copy translated text to clipboard
- Download translated text
- Simple and responsive user interface

## Supported Languages

- English
- Hindi
- French
- Spanish
- German
- Japanese
- Russian
- Chinese
- Arabic
- Italian
- Portuguese
- Bengali
- Punjabi
- Tamil
- Telugu
- Korean


## Requirements

```text
streamlit
googletrans==4.0.0rc1
gtts
pyperclip
```

## Internship Information

Project developed as part of the CodeAlpha Artificial Intelligence Internship.

Task: Language Translation Tool

## Author

Vansh Sharma

B.Tech Computer Science and Engineering (Artificial Intelligence)  
Noida Institute of Engineering and Technology (NIET)


## License

This project is available for educational and learning purposes.