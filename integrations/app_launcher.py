import os
import platform
import subprocess


class AppLauncher:
    def launch(self, app_name: str):
        if not app_name:
            print("No app name provided.")
            return

        app_name = app_name.strip().lower()

        system = platform.system().lower()

        if app_name in {"browser", "chrome", "google chrome"}:
            self._launch_browser(system)
            return

        if system == "windows":
            os.startfile(app_name)
        elif system == "darwin":
            subprocess.Popen(["open", app_name])
        else:
            subprocess.Popen(["xdg-open", app_name])

        print(f"Launching app: {app_name}")

    def _launch_browser(self, system: str):
        if system == "windows":
            subprocess.Popen(["cmd", "/c", "start", "", "https://www.google.com"])
        elif system == "darwin":
            subprocess.Popen(["open", "https://www.google.com"])
        else:
            subprocess.Popen(["xdg-open", "https://www.google.com"])

        print("Opening browser to Google")
