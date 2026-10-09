from integrations.browser_control import BrowserControl
from integrations.app_launcher import AppLauncher
from integrations.system_commands import SystemCommands


class TaskExecutor:
    def __init__(self):
        self.browser = BrowserControl()
        self.apps = AppLauncher()
        self.system = SystemCommands()

    def execute(self, intent):
        action = intent.action

        if action == "open":
            self.apps.launch(intent.target or "browser")
            return

        if action == "search":
            self.browser.search(intent.target or "")
            return

        if action == "run":
            self.system.run_command(intent.target or "")
            return

        if action == "close":
            self.system.close_app(intent.target or "")
            return

        print(f"No handler for action: {action}")
