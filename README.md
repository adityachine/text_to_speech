# 🇮🇳 IndianVoiceAI - Text to Speech Tool

**IndianVoiceAI** is a simple and interactive Python script that converts written text into spoken words using a voice with an Indian English accent (if available). It uses the `pyttsx3` text-to-speech library for offline voice synthesis.

## 🎯 Features

- 🎤 Speak any input text aloud with Indian accent
- ⚙️ Change the speaking rate dynamically
- 📜 List all available system voices
- 🖥️ Simple terminal/command-line interface
- 🔌 Fully offline (no internet required)

## 🛠️ Requirements

- Python 3.6 or higher
- `pyttsx3` library

Install dependencies:
```bash
pip install pyttsx3
🚀 Usage
Run the script:
python indian_voice_ai.py
Menu Options:
Speak text - Type and listen to your custom text.

Change speaking rate - Set how fast or slow the voice should speak.

List available voices - View and try all installed voices on your system.

Exit - Close the program.

💡 Notes
On Windows, the default voice engine is SAPI5. Indian voices may not be available by default.

On Linux/macOS, voices depend on the speech engine available (espeak, nsss, etc.).

If an Indian accent is not detected, the app will fall back to a generic English voice.

🧠 Improvements You Can Add
Voice selection by number (after listing voices)

Save speech to audio file (MP3/WAV) using pyttsx3.save_to_file()

GUI version using Tkinter or PyQt5

Language support for Hindi, Tamil, etc. using gTTS or TTS libraries

Speech input (STT) for two-way interaction

📂 File Structure
indian_voice_ai/
├── indian_voice_ai.py      # Main application script
└── README.md               # Project documentation
👨‍💻 Author
Made by [Your Name] with ❤️

📃 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 🔧 Suggestions for Advanced Features

Here are a few **advanced enhancements** you can implement:

1. **Voice Selection by Index**  
   Let the user choose a voice from the list and set it dynamically.

2. **Save Speech to Audio File**  
   Add the option to save the spoken output to a `.mp3` or `.wav` file:
   ```python
   self.engine.save_to_file(text, 'output.wav')
GUI Interface
Build a GUI using tkinter, PyQt5, or streamlit for a more user-friendly experience.

Speech Recognition Integration
Use speech_recognition to take voice input and respond with speech (two-way voice assistant).

Multilingual Support
Integrate gTTS or TTS (coqui-ai) to support Indian regional languages.

