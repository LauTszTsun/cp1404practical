from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934
class MilesConvertApp(App):
    """MilesConvertApp is for converting miles to kilometres"""
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_m_km_solution.kv')
        return self.root

    def handle_calculate(self):
        """calculate number of kilometres"""
        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, difference):
        """handle increase or decrease miles"""
        value = self.get_validated_miles() + difference
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def get_validated_miles(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesConvertApp().run()
