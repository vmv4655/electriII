import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup

class AppLayout(FloatLayout):
	pass

class mainApp(App):

	def build(self):
		return AppLayout()

if __name__ == '__main__':
    mainApp().run()
		
