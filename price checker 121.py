import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image

class SkinPriceChecker(App):

    api_key = '4D1F44D14444472D907117368F73052A'
    base_url = 'https://api.steampowered.com/ISteamMarket/GetAssetPrices/v1/'

    def get_skin_data(self, market_hash_name):
        params = {
            'key': self.api_key,
            'appid': 730,
            'market_hash_name': market_hash_name
        }

        response = requests.get(self.base_url, params=params)
        data = response.json()

        if 'prices' in data and data['success']:
            price = data['prices'][0]['price']
            image_url = data['prices'][0]['img']
            return price, image_url
        else:
            return 'Price not available', None

    def search_skin(self, instance):
        market_hash_name = self.search_input.text
        price, image_url = self.get_skin_data(market_hash_name)

        self.price_label.text = f'Price: {price}'

        if image_url:
            self.skin_image.source = image_url
        else:
            self.skin_image.source = ""  # Show no image if not found

    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.search_input = TextInput(hint_text='Enter Skin Name', multiline=False)
        search_button = Button(text='Search', background_color=[1, 0, 0, 1])
        search_button.bind(on_press=self.search_skin)
        self.price_label = Label(text='Price:')

        self.skin_image = Image()

        layout.add_widget(self.search_input)
        layout.add_widget(search_button)
        layout.add_widget(self.price_label)
        layout.add_widget(self.skin_image)

        return layout

if __name__ == '__main__':
    SkinPriceChecker().run()