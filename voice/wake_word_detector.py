class WakeWordDetector:
    def __init__(self, wake_phrases=None):
        if wake_phrases is None:
            wake_phrases = ["hey i-agent", "i-agent", "hey agent"]
        self.wake_phrases = [phrase.lower() for phrase in wake_phrases]

    def is_wake_word(self, transcript):
        text = (transcript or "").lower().strip()
        return any(phrase in text for phrase in self.wake_phrases)
