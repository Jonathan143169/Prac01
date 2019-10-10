from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934


class ConvertMToKmApp(App):
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert miles to kilometers"
        self.root = Builder.load_file('convert_m_to_km.kv')
        return self.root

    def convert_to_miles(self):
        # number_value = self.get_miles()
        number_value = self.get_miles()
        answer = number_value * MILES_TO_KM
        self.root.ids.output_label.text = str(answer)

    def up_miles(self, value):
        number_value = float(self.root.ids.input_text.text)
        number_value = number_value + value
        self.root.ids.input_text.text = str(number_value)
        self.convert_to_miles()

    def get_miles(self):
        try:
            input_value = float(self.root.ids.input_text.text)
            return input_value
        except ValueError:
            return 0


ConvertMToKmApp().run()
