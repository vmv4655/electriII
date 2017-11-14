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

class GetTipoTrifasica(Popup):
	pass

class GetCargaDelta(Popup):
	pass

class GetCargaEstrella(Popup):
	pass

class GetTipoMotor(Popup):
	pass

class GetCargaMotorTrifase(Popup):
	pass

class GetCargaMotorMonofase(Popup):
	pass

class GetCargaMonofase(Popup):
	pass


class AppLayout(FloatLayout):
	listaCargas  = [None]
	listaFuentes = [None]
	fuente       = None
	tipoFuente   = ""
	tmpTipoCarga = ""
	

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
		if(self.listaFuentes[0] == None):
			print('nothing here')
		else:
			getTipoCarga = SelectCarga()
			getTipoCarga.open()

	def setTipoCarga(self, trifase, monofase, motor):
		print(trifase)
		print(monofase)
		print(motor)
		
		if(trifase == True):
			getTipoTrifasica = GetTipoTrifasica()
			getTipoTrifasica.open()
		
		elif(monofase == True):
			getCargaMonofase = GetCargaMonofase()
			getCargaMonofase.open()
		
		elif(motor == True):
			getTipoMotor = GetTipoMotor()
			getTipoMotor.open()

		else:
			print("selecciona alguno imbecil")

	def setTipoMotor(self, monofase, trifase):
		if(monofase == True):
			getCargaMotorMonofase = GetCargaMotorMonofase()
			getCargaMotorMonofase.open()
		
		elif(trifase == True):
			getCargaMotorTrifase = GetCargaMotorTrifase()
			getCargaMotorTrifase.open()
		
		else:
			print("error")

	def setTipoCargaTrifase(self, estrella, delta):
		if(estrella == True):
			getCargaEstrella = GetCargaEstrella()
			getCargaEstrella.open()
		
		elif(delta == True):
			getCargaDelta = GetCargaDelta()
			getCargaDelta.open()
		
		else:
			print('ERROR')

	def addCargaMonoFase(self, cantidad, a1Selected, a2Selected, b1Selected, b2Selected, c1Selected, c2Selected, n1Selected, n2Selected, potenciaActive, zActive, pAparente, pReactiva, pReal, fp, adelantoActive, atrasoActive, zReal, zComplejo):
		print('agregandoCargaMonoFase')
		cargaMonofasica = CargaMonofasica(self.listaFuentes[0])
		if(cantidad != ""):
			cantidad = float(cantidad)
		else:
			cantidad = 1

		if(fp == ""):
			fp = 1
		
		conexion = ""
		if(a1Selected):
			if(b2Selected):
				conexion = "AB"
			elif(c2Selected):
				conexion = "CA"
			elif(n2Selected):
				conexion = "AN"
		elif(b1Selected):
			if(a2Selected):
				conexion = "AB"
			elif(c2Selected):
				conexion = "BC"
			elif(n2Selected):
				conexion = "BN"

		elif(c1Selected):
			if(a2Selected):
				conexion = "CA"
			elif(b2Selected):
				conexion = "BC"
			elif(n2Selected):
				conexion = "CN"
		cargaMonofasica.setConexion(conexion)

		if(potenciaActive == True):
			if((pAparente != "" or pReactiva != "" or pReal != "") and fp != ""):
				fp = float(fp)
				if(pAparente != ""):
					pAparente = float(pAparente)
					if(adelantoActive):
						cargaMonofasica.setDatosMonofase(None, None, pAparente, fp, "Adelanto", cantidad, None)
					
					elif(atrasoActive):
						cargaMonofasica.setDatosMonofase(None, None, pAparente, fp, "Atraso", cantidad, None)
					
					else:
						print('FUCK YOU')
				elif(pReactiva != ""):
					pReactiva = float(pReactiva)
					if(adelantoActive):
						cargaMonofasica.setDatosMonofase(None, pReactiva, None, fp, "Adelanto", cantidad, None)
					
					elif(atrasoActive):
						cargaMonofasica.setDatosMonofase(None, pReactiva, None, fp, "Atraso", cantidad, None)
					else:
						print('FUCK YOU')

				elif(pReal != ""):
					pReal = float(pReal)
					if(adelantoActive):
						cargaMonofasica.setDatosMonofase(pReal, None, None, fp, "Adelanto", cantidad, None)
					
					elif(atrasoActive):
						cargaMonofasica.cargaMonofasica.setDatosMonofase(pReal, None, None, fp, "Atraso", cantidad, None)

					else:
						print('FUCK YOU')
					
			else:
				print('ERROR, NO DATOS')


		elif(zActive == True):
			if(zReal != "" and zComplejo != ""):
				z = complex(float(zReal), float(zComplejo))
				cargaMonofasica.setDatosMonofase(None, None, None, None, None, cantidad, z)
			else:
				print('ERROR')

		else:
			print('ERROR DEBE SELECICONAR ALGUNO')


		print(cargaMonofasica.getIL())

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
