from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Kivy app that dynamically creates one Label per name."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Basic data (model): a simple list of names
        self.names = ["Ada","Gideon","Grace","Linux","Ken"]

    def build(self):
        """Build the Kivy GUI ."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create Labels from data and add them to the GUI."""
        for name in self.names:
            self.root.ids.main.add_widget(Label(text=name))
DynamicLabelsApp().run()
