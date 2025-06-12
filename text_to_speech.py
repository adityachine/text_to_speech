import pyttsx3
import time

class IndianVoiceAI:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.voice_id = self.get_indian_voice()
        self.engine.setProperty('voice', self.voice_id)
        self.rate = 150
        self.engine.setProperty('rate', self.rate)

    def get_indian_voice(self):
        voices = self.engine.getProperty('voices')
        for voice in voices:
            if "en-in" in voice.id.lower() or "indian" in voice.name.lower():
                return voice.id
        # fallback to any English voice
        for voice in voices:
            if "english" in voice.name.lower():
                return voice.id
        return voices[0].id

    def set_rate(self, rate):
        self.rate = rate
        self.engine.setProperty('rate', self.rate)

    def speak(self, text):
        print(f"\n🗣️ Speaking with Indian accent...\n")
        self.engine.say(text)
        self.engine.runAndWait()

    def list_voices(self):
        voices = self.engine.getProperty('voices')
        print("\n🔊 Available Voices:\n")
        for idx, voice in enumerate(voices):
            print(f"[{idx}] {voice.name} - {voice.id}")
        print("")

def main():
    ai = IndianVoiceAI()
    print("\n=== 🎙️ Indian Voice AI - Text to Speech ===\n")

    while True:
        print("1. Speak text")
        print("2. Change speaking rate")
        print("3. List available voices")
        print("4. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            text = input("\nEnter the text to speak: ").strip()
            ai.speak(text)
            time.sleep(1)
        elif choice == "2":
            try:
                new_rate = int(input("Enter new rate (e.g., 120-180): "))
                ai.set_rate(new_rate)
                print(f"✅ Speaking rate updated to {new_rate}.\n")
            except ValueError:
                print("❌ Invalid input. Please enter a number.\n")
        elif choice == "3":
            ai.list_voices()
        elif choice == "4":
            print("\n👋 Exiting Indian Voice AI. Stay vocal!\n")
            break
        else:
            print("❌ Invalid option. Try again.\n")

if __name__ == "__main__":
    main()
