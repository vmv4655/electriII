from functions import *
import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.core.window import Window

#Variables globales#
fuente = [None]
cargas = []

class SelecFuente(Popup):
	pass

class SelecVab(Popup):
	pass

class AppLayout(FloatLayout):
	tipoFuente = ""
	fuente     = None

	def getTipoFuente(self):
		selecFuente = SelecFuente()
		selecFuente.open()

	def setTipoFuente(self, tipoFuente):#self, tipo, a, b, secuencia):
		self.tipoFuente = tipoFuente
		self.tipoDeFuente.text = tipoFuente
		self.getVoltajeAB()

	def getVoltajeAB(self):
		selecVab = SelecVab()
		selecVab.open()

	def updateVoltajesPantalla(self):
		if(fuente[0] == None):
			return
		else:
			self.Van.text = fuente[0].getPolFromRec( getVan() )
			self.Vbn.text = fuente[0].getPolFromRec( getVbn() )
			self.Vcn.text = fuente[0].getPolFromRec( getVcn() )
			self.Vab.text = fuente[0].getPolFromRec( getVab() )
			self.Vbc.text = fuente[0].getPolFromRec( getVbc() )
			self.Vca.text = fuente[0].getPolFromRec( getVca() )
			
	
	def setVoltajeAB(self, secuenciaState, recOrPolState, magnitud, angulo, real, imaginario ):
		Vab = None
		print(secuenciaState)
		print(recOrPolState)
		print(magnitud)
		print(angulo)
		print(real)
		print(imaginario)

		if(recOrPolState == 'down'): #Forma Polar
			print('POLAR')
			#Verificar que tenemos datos
			if(magnitud == "" or angulo == ""):
				selecVab = SelecVab(title = "Todos los campos son requeridos", title_color = [1, 0, 0, 1] )
				selecVab.open()
				return
			else:
				Vab = getRecFromPol(float(magnitud), float(angulo))
				print(Vab)
				if(secuenciaState == 'down'): #Secuencia ABC
					if(self.tipoFuente == "Estrella"):
						self.fuente = FuenteEstrella()
						self.fuente.calcularVoltajes(None , None, None, Vab, None, None, "ABC")
		
					elif(self.tipoFuente == "Delta"):
						self.fuente = FuenteDelta()
						self.fuente.calcularVoltajes(None , None, None, Vab, None, None, "ABC")

				elif(secuenciaState == 'normal'): #Secuencia ACB
					if(self.tipoFuente == "Estrella"):
						self.fuente = FuenteEstrella()
						self.fuente.calcularVoltajes(None , None, None, Vab, None, None, "ACB")
		
					elif(self.tipoFuente == "Delta"):
						self.fuente = FuenteDelta()
						self.fuente.calcularVoltajes(None , None, None, Vab, None, None, "ACB")


		
		

		elif(recOrPolState == 'normal'): #Forma Rectangular
			print('RECTANGULAR')
			#Verificar que tenemos datos
			if(real == "" or imaginario == ""):
				selecVab = SelecVab(title = "Todos los campos son requeridos", title_color = [1, 0, 0, 1] )
				selecVab.open()
				return

			else:
				Vab = complex(float(real), float(imaginario))
				print(Vab)
				if(secuenciaState == 'down'): #Secuencia ABC
					if(self.tipoFuente == "Estrella"):
						pass
		
					elif(self.tipoFuente == "Delta"):
						pass

				elif(secuenciaState == 'normal'): #Secuencia ACB
					if(self.tipoFuente == "Estrella"):
						pass
		
					elif(self.tipoFuente == "Delta"):
						pass

		fuente = [self.fuente]
		self.updateVoltajesPantalla()

	
class mainApp(App):
	appLayout = None
	#appLayout = AppLayout();
	def build(self):
		self.appLayout = AppLayout();
		return self.appLayout#self.appLayout

	def on_start(self):
		self.appLayout.getTipoFuente()

if __name__ == '__main__':
    mainApp().run()
