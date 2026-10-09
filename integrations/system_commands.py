import os
import platform
import subprocess


class SystemCommands:
    def run_command(self, command: str):
        if not command:
            print("No command provided.")
            return

        print(f"Running system command: {command}")
        try:
            if platform.system().lower() == "windows":
                subprocess.run(command, shell=True)
            else:
                subprocess.run(command, shell=True)
        except Exception as exc:
            print(f"Command failed: {exc}")

    def close_app(self, app_name: str):
        if not app_name:
            print("No app name provided.")
            return

        print(f"Closing app: {app_name}")
        if platform.system().lower() == "windows":
            os.system(f"taskkill /F /IM {app_name}.exe")
        else:
            os.system(f"pkill -f {app_name}")
