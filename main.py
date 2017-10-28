import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup

#Variables globales#
fuente = []
cargas = []

class SelecFuente(Popup):
	pass

class SelecVab(Popup):
	pass

class AppLayout(FloatLayout):
	pass

class mainApp(App):

	def build(self):
		#selecFuente = SelecFuente()
		#selecFuente.open()
		#selecVab = SelecVab()
		#selecVab.open()
		return AppLayout()

if __name__ == '__main__':
    mainApp().run()
		





