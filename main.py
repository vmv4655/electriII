from functions import *
import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.core.window import Window

#Variables globales#
fuente = []
cargas = []

class SelecFuente(Popup):
	pass

class SelecVab(Popup):
	pass

class AppLayout(FloatLayout):
	def setVoljateAB(self):
		selecVab = SelecVab()
		selecVab.open()

	def crearFuente(self):
		selecVab = SelecVab()
		selecVab.open()

	def setTipoFuente(self):
		selecFuente = SelecFuente()
		selecFuente.open()
		selecFuente.bind(on_dismiss=setTipoFuente())
class mainApp(App):
	
	def build(self):
		#selecFuente = SelecFuente()
		#selecFuente.open()
		#selecVab = SelecVab()
		#selecVab.open()
		#fuenteDelta = FuenteDelta()
		Window.clearcolor = (.4, .4, .4, 1)
		return AppLayout()

if __name__ == '__main__':
    mainApp().run()





