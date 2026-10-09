from dataclasses import dataclass


@dataclass
class Intent:
    action: str
    target: str | None = None
    params: dict | None = None


class IntentParser:
    def __init__(self):
        self.keywords = {
            "open": ["open", "launch", "start"],
            "search": ["search", "find", "look up"],
            "run": ["run", "execute", "do"],
            "close": ["close", "quit", "exit"],
        }

    def parse(self, command: str):
        text = (command or "").strip().lower()

        if not text:
            return Intent(action="idle")

        if any(keyword in text for keyword in self.keywords["open"]):
            target = self._extract_target(text, "open")
            return Intent(action="open", target=target)

        if any(keyword in text for keyword in self.keywords["search"]):
            target = self._extract_target(text, "search")
            return Intent(action="search", target=target)

        if any(keyword in text for keyword in self.keywords["run"]):
            target = self._extract_target(text, "run")
            return Intent(action="run", target=target)

        if any(keyword in text for keyword in self.keywords["close"]):
            target = self._extract_target(text, "close")
            return Intent(action="close", target=target)

        return Intent(action="unknown", target=text)

    def _extract_target(self, text: str, action: str):
        for prefix in self.keywords[action]:
            if prefix in text:
                return text.split(prefix, 1)[1].strip()
        return text
