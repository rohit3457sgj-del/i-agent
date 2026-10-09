import speech_recognition as sr


class SpeechRecognizer:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen_once(self):
        """Listen once and return a transcript or an empty string."""
        try:
            with sr.Microphone() as source:
                print("Listening...")
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)

            try:
                transcript = self.recognizer.recognize_google(audio)
                print(f"You said: {transcript}")
                return transcript
            except sr.UnknownValueError:
                print("Could not understand the audio.")
                return ""
            except sr.RequestError as exc:
                print(f"Speech recognition request failed: {exc}")
                return ""
        except sr.WaitTimeoutError:
            print("Listening timed out. Please try again.")
            return ""
        except Exception as exc:
            print(f"Microphone error: {exc}")
            return ""
