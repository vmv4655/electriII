import kivy

from kivy.app import App
from kivy.uix.button import Label
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

class CustomPopUp(Popup):
	pass
class MainBoxLayout(BoxLayout):
	pass
		
class Functions(object):
	def selectTipoDeFuente(self):
		 fuentePopUp = CustomPopUp()
		 fuentePopUp.open()
		
class mainApp(App):
	
	
	def build(self):
		#Cambiar color del fondo
		Window.clearcolor = (.4, .4, .4, 1)
		functions = Functions()
		functions.selectTipoDeFuente()
		mainBoxLayout = MainBoxLayout()
		return BoxLayout()

if __name__ == '__main__':
    mainApp().run()
		
