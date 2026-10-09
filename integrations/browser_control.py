import webbrowser


class BrowserControl:
    def open_url(self, url: str):
        webbrowser.open(url)
        print(f"Opening browser: {url}")

    def search(self, query: str):
        if not query:
            print("No search query provided.")
            return

        url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
        self.open_url(url)

    def open_homepage(self):
        self.open_url("https://www.google.com")
