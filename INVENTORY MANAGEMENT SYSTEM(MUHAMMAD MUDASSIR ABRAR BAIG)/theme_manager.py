class ThemeManager:
    def __init__(self, root):
        self.root = root
        self.theme = "light"

    def apply_theme(self):
        color = "white" if self.theme == "light" else "#2c2c2c"
        self.root.configure(bg=color)

    def toggle_theme(self):
        self.theme = "dark" if self.theme == "light" else "light"
        self.apply_theme()