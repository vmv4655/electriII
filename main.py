from functions import *
import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.core.window import Window

class SelecFuente(Popup):
	pass

class SelecVab(Popup):
	pass

class SelectCarga(Popup):
	pass

class SelectTipoTrifasica(Popup):
	pass

class GetCargaDelta(Popup):
	pass

class GetCargaEstrella(Popup):
	pass

class GetCargaMonofase(Popup):
	pass

class GetCargaMotor(Popup):
	pass

class AppLayout(FloatLayout):
	listaCargas  = [None]
	listaFuentes = [None]
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
		if(self.listaFuentes[0] == None):
			return
		else:
			self.displayVan.text = str( getPolFromRecToGUI( self.listaFuentes[0].getVan() ))
			self.displayVbn.text = str( getPolFromRecToGUI( self.listaFuentes[0].getVbn() ))
			self.displayVcn.text = str( getPolFromRecToGUI( self.listaFuentes[0].getVcn() ))
			self.displayVab.text = str( getPolFromRecToGUI( self.listaFuentes[0].getVab() ))
			self.displayVbc.text = str( getPolFromRecToGUI( self.listaFuentes[0].getVbc() ))
			self.displayVca.text = str( getPolFromRecToGUI( self.listaFuentes[0].getVca() ))
			
	
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
				selecVab = SelecVab(title = "Todos los campos son requeridos, digite Vab", title_color = [1, 0, 0, 1] )
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

		#Guardando fuente en una lista...
		self.listaFuentes = [self.fuente]
		self.updateVoltajesPantalla()

	def getTipoCarga(self):
		getTipoCarga = SelectCarga()
		getTipoCarga.open()

	def probarPupups(self):
		prueba = GetCargaMonofase()
		prueba.open()
	
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
