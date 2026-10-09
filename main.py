from voice.speech_recognition import SpeechRecognizer
from voice.wake_word_detector import WakeWordDetector
from orchestration.intent_parser import IntentParser
from orchestration.task_executor import TaskExecutor


class IAgent:
    def __init__(self):
        self.speech = SpeechRecognizer()
        self.wake_detector = WakeWordDetector()
        self.intent_parser = IntentParser()
        self.task_executor = TaskExecutor()

    def run(self):
        print("I-Agent is ready. Say 'Hey I-Agent' to begin.")

        while True:
            transcript = self.speech.listen_once()
            if not transcript:
                continue

            if self.wake_detector.is_wake_word(transcript):
                print("Wake word detected.")
                command = self.speech.listen_once()
                if not command:
                    print("No command received.")
                    continue

                intent = self.intent_parser.parse(command)
                print(f"Intent detected: {intent}")
                self.task_executor.execute(intent)

                continue

            # Ignore all other speech until the wake word is heard.
            print(f"Ignored: {transcript}")


if __name__ == "__main__":
    agent = IAgent()
    agent.run()
