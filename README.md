# i-agent

A voice-powered personal automation agent for opening browsers, launching apps, and executing simple commands.

## What it does

- listens for a spoken wake phrase
- understands a basic command such as "open browser" or "search for Python tutorials"
- routes the command to browser, app, or system tool handlers

## Project structure

```text
i-agent/
├── voice/
│   ├── speech_recognition.py
│   └── wake_word_detector.py
├── orchestration/
│   ├── intent_parser.py
│   ├── task_executor.py
│   └── tool_registry.py
├── integrations/
│   ├── browser_control.py
│   ├── app_launcher.py
│   └── system_commands.py
├── config/
│   └── permissions.yaml
├── main.py
├── requirements.txt
└── README.md
```

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

## Example commands

- "Hey I-Agent, open browser"
- "Hey I-Agent, search for weather in London"
- "Hey I-Agent, launch Notepad"

## Notes

This is an early-stage personal automation project. Real deployments should add:

- secure permission checks
- confirmation for risky actions
- production-grade speech recognition
- browser automation via Playwright or Selenium
- stronger intent-handling and tool calling with an LLM
