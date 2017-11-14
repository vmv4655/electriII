from functions import *
import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.listview import ListItemButton
from kivy.core.window import Window
from kivy.properties import ObjectProperty

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

class BotonListaCargas(ListItemButton):
	pass


class AppLayout(FloatLayout):
	fuente       = None
	listaFuentes = [None]
	listaCargas  = []
	secuencia    = ""
	tipoFuente   = ""
	tmpTipoCarga = ""
	displaylistaCargas = ObjectProperty()

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
	
	def updateCorrientesPantalla(self):
		if(len(self.listaCargas) == 0):
			return
		else:
			self.displayIa.text   = str( getPolFromRecToGUI( getCargasLinea(self.listaCargas, self.secuencia)[0] ))
			self.displayIb.text   = str( getPolFromRecToGUI( getCargasLinea(self.listaCargas, self.secuencia)[1] ))
			self.displayIc.text   = str( getPolFromRecToGUI( getCargasLinea(self.listaCargas, self.secuencia)[2] ))
			self.displayIn.text   = str( "N/A" )
			self.displayFP.text   = str( "N/A" )
			self.displayL3W.text  = str( "N/A" )
			self.displayL2W.text  = str( "N/A" )

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
					self.secuencia = "ABC"				
					if(self.tipoFuente == "Estrella"):
						self.fuente = FuenteEstrella()
						self.fuente.calcularVoltajes(None , None, None, Vab, None, None, "ABC")
		
					elif(self.tipoFuente == "Delta"):
						self.fuente = FuenteDelta()
						self.fuente.calcularVoltajes(None , None, None, Vab, None, None, "ABC")

				elif(secuenciaState == 'normal'): #Secuencia ACB
					if(self.tipoFuente == "Estrella"):
						self.secuencia = "ACB"
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

	##Lets do the magic##

	def addCargaMonoFase(self, cantidad, a1Selected, a2Selected, b1Selected, b2Selected, c1Selected, c2Selected, n1Selected, n2Selected, potenciaActive, zActive, pAparente, pReactiva, pReal, fp, adelantoActive, atrasoActive, zReal, zComplejo):
		print('agregandoCargaMonoFase')
		cargaMonofasica = CargaMonofasica(self.listaFuentes[0])
		
		if(cantidad != ""):
			cantidad = float(cantidad)
		else:
			cantidad = 1.0

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
						dataCarga = "x%d Cargas monofasicas agregadas, FP: %s en %s, potencia: %s VA, lineas: %s" %(cantidad, fp, "adelanto", pAparente, conexion)
					elif(atrasoActive):
						cargaMonofasica.setDatosMonofase(None, None, pAparente, fp, "Atraso", cantidad, None)
						dataCarga = "x%d Cargas monofasicas agregadas, FP: %s en %s, potencia: %s VA, lineas: %s" %(cantidad, fp, "atraso", pAparente, conexion)
					else:
						print('error')
					
				elif(pReactiva != ""):
					pReactiva = float(pReactiva)
					if(adelantoActive):
						cargaMonofasica.setDatosMonofase(None, pReactiva, None, fp, "Adelanto", cantidad, None)
						dataCarga = "x%d Cargas monofasicas agregadas, FP: %s en %s, potencia: %s VAr, lineas: %s" %(cantidad, fp, "adelanto", pReactiva, conexion)
					elif(atrasoActive):
						cargaMonofasica.setDatosMonofase(None, pReactiva, None, fp, "Atraso", cantidad, None)
						dataCarga = "x%d Cargas monofasicas agregadas, FP: %s en %s, potencia: %s VAr, lineas: %s" %(cantidad, fp, "atraso", pReactiva, conexion)
					else:
						print('error')
					
				elif(pReal != ""):
					pReal = float(pReal)
					if(adelantoActive):
						cargaMonofasica.setDatosMonofase(pReal, None, None, fp, "Adelanto", cantidad, None)
						dataCarga = "x%d Cargas monofasicas agregadas, FP: %s en %s, potencia: %s W, lineas: %s" %(cantidad, fp, "adelanto", pReal, conexion)
					elif(atrasoActive):
						cargaMonofasica.setDatosMonofase(pReal, None, None, fp, "Atraso", cantidad, None)
						dataCarga = "x%d Cargas monofasicas agregadas, FP: %s en %s, potencia: %s W, lineas: %s" %(cantidad, fp, "atraso", pReal, conexion)

					else:
						print('error')
				self.listaCargas.append(cargaMonofasica)
				self.updateCorrientesPantalla()
				print(self.listaCargas)
					
			else:
				print('ERROR, NO DATOS')


		elif(zActive == True):
			if(zReal != "" and zComplejo != ""):
				z = complex(float(zReal), float(zComplejo))
				cargaMonofasica.setDatosMonofase(None, None, None, None, None, cantidad, z)
				dataCarga = "x%d Cargas monofasicas agregadas, Z: %s, lineas: %s" %(cantidad, z, conexion)
				self.listaCargas.append(cargaMonofasica)
				self.updateCorrientesPantalla()
				print(self.listaCargas)
			else:
				print('ERROR')

		else:
			print('ERROR DEBE SELECICONAR ALGUNO')
		self.displaylistaCargas.adapter.data.extend([dataCarga])#["Carga monofasica agregada"])
		print(cargaMonofasica.getIL())

	#def addMotorMonofase(self, cantidad, a1Selected, a2Selected, b1Selected, b2Selected, c1Selected, c2Selected, n1Selected, n2Selected, potenciaActive, HpActive, pAparente, pReactiva, pReal, fp, adelantoActive, atrasoActive, Hps, n):
	def addMotorMonofase(self, cantidad, a1Selected, a2Selected, b1Selected, b2Selected, c1Selected, c2Selected, n1Selected, n2Selected, fp, adelantoActive, atrasoActive, Hps, n):
		print('Agregando Motor Monofase')
		motorMonofase = CargaMonofasica(self.listaFuentes[0])
		
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
		motorMonofase.setConexion(conexion)

		"""if(potenciaActive):
			if((pAparente != "" or pReactiva != "" or pReal != "") and fp != "" and n != ""):
				fp = float(fp)
				n  = float(n)
				if(pAparente != ""):
					pAparente = float(pAparente)
					if(adelantoActive):
						cargaMonofasica.setDatosMotorMonofase(Cantidad, Hp, fp, n, direccion):
					
					elif(atrasoActive):
						cargaMonofasica.setDatosMotorMonofase(Cantidad, Hp, fp, n, direccion):
					
					else:
						print('error')
				elif(pReactiva != ""):
					pReactiva = float(pReactiva)
					if(adelantoActive):
						cargaMonofasica.setDatosMotorMonofase(Cantidad, Hp, fp, n, direccion):
					
					elif(atrasoActive):
						cargaMonofasica.setDatosMotorMonofase(Cantidad, Hp, fp, n, direccion):
					else:
						print('error')

				elif(pReal != ""):
					pReal = float(pReal)
					if(adelantoActive):
						cargaMonofasica.setDatosMotorMonofase(Cantidad, Hp, fp, n, direccion):
					
					elif(atrasoActive):
						cargaMonofasica.cargaMonofasica.setDatosMotorMonofase(Cantidad, Hp, fp, n, direccion):

					else:
						print('ddddd')
					
			else:
				print('ERROR, NO DATOS')"""


		
		if(Hps != "" and n != "" and fp != ""):
			Hps = float(Hps)
			n   = float(n)
			fp  = float(fp)

			if(adelantoActive):
				motorMonofase.setDatosMotorMonofase(cantidad, Hps, fp, n, "Adelanto")
			elif(atrasoActive):
				motorMonofase.setDatosMotorMonofase(cantidad, Hps, fp, n, "Atraso")
			else:
				print('ERROR')

			self.listaCargas.append(motorMonofase)
			dataCarga = "x%d Motores monofasicos agregados, %s HP, eficiencia: %s, lineas: %s" %(cantidad, Hps, n, conexion)
			self.updateCorrientesPantalla()
			print(self.listaCargas)

		else:
			print('ERROR DEBE SELECICONAR ALGUNO')

		print(motorMonofase.getIL())
		self.displaylistaCargas.adapter.data.extend([dataCarga])

	def addCargaMotorTrifasico(self, cantidad, fp, Hp, n):
		print('agregandoCargaMotorTrifasico')
		cargaMotorTrifasico = CargaMotorTrifasico(self.listaFuentes[0])
		
		if(cantidad != ""):
			cantidad = float(cantidad)
		else:
			cantidad = 1

		if(fp != ""):
			fp = float(fp)
		else:
			fp = 1

		if (Hp != "" and n != "" and fp != ""):
			Hp = float(Hp)
			n = float(n)
			cargaMotorTrifasico.Il_motor(cantidad,Hp,fp,n)

			self.listaCargas.append(cargaMotorTrifasico)
			dataCarga = "x%d Motores trifasicos agregados, %s HP, FP: %s, eficiencia: %s" %(cantidad, Hp, fp, n)
			self.updateCorrientesPantalla()
			print(self.listaCargas)

		else:
			print('ERROR, NO DATOS')

		self.displaylistaCargas.adapter.data.extend([dataCarga])
		print(cargaMotorTrifasico.getIA())
		print(cargaMotorTrifasico.getIB())
		print(cargaMotorTrifasico.getIC())

	def addCargaDelta(self, potenciaActive, zActive, balancActive, desbalancActive, pAparente, pReactiva, pReal, fp, adelantoActive, atrasoActive, zRealAB, zComplejoAB, zRealBC, zComplejoBC,zRealCA, zComplejoCA):
		print('addCargaDelta')
		cargaDeltaDesbal = CargaDeltaDesbal(self.listaFuentes[0])
		cargaDeltaBalanceada = CargaDeltaBalanceada(self.listaFuentes[0])

		if(fp == ""):
			fp = 1

		if (potenciaActive == True):
			cargaDeltaBalanceada = CargaDeltaBalanceada(self.listaFuentes[0])
			if((pAparente != "" or pReactiva != "" or pReal != "") and fp != ""):
				fp = float(fp)
				if(pAparente != ""):
					pAparente = float(pAparente)
					if(adelantoActive):
						cargaDeltaBalanceada.getiDesdePotencia(None, None, pAparente, fp, "Adelanto")
						dataCarga = "Carga delta balanceada agregada, Potencia: %s VA, FP: %s, en %s" %(pAparente, fp, "adelanto")
					
					elif(atrasoActive):
						cargaDeltaBalanceada.getiDesdePotencia(None, None, pAparente, fp, "Atraso")
						dataCarga = "Carga delta balanceada agregada, Potencia: %s VA, FP: %s, en %s" %(pAparente, fp, "atraso")
					else:
						print('ERROR')
				elif(pReactiva != ""):
					pReactiva = float(pReactiva)
					if(adelantoActive):
						cargaDeltaBalanceada.getiDesdePotencia(None, pReactiva, None, fp, "Adelanto")
						dataCarga = "Carga delta balanceada agregada, Potencia: %s VAr, FP: %s, en %s" %(pReactiva, fp, "adelanto")
					elif(atrasoActive):
						cargaDeltaBalanceada.getiDesdePotencia(None, pReactiva, None, fp, "Atraso")
						dataCarga = "Carga delta balanceada agregada, Potencia: %s VAr, FP: %s, en %s" %(pReactiva, fp, "atraso")
					else:
						print('ERROR')

				elif(pReal != ""):
					pReal = float(pReal)
					if(adelantoActive):
						cargaDeltaBalanceada.getiDesdePotencia(pReal, None, None, fp, "Adelanto")
						dataCarga = "Carga delta balanceada agregada, Potencia: %s W, FP: %s, en %s" %(pReal, fp, "adelanto")
					elif(atrasoActive):
						cargaDeltaBalanceada.getiDesdePotencia(pReal, None, None, fp, "Atraso")
						dataCarga = "Carga delta balanceada agregada, Potencia: %s W, FP: %s, en %s" %(pReal, fp, "atraso")
					else:
						print('ERROR')
				self.displaylistaCargas.adapter.data.extend([dataCarga])
				self.listaCargas.append(cargaDeltaBalanceada)
				self.updateCorrientesPantalla()
				print(self.listaCargas)

		elif(zActive == True):
			if(balancActive == True):
				cargaDeltaBalanceada = CargaDeltaBalanceada(self.listaFuentes[0])

				if(zRealAB != "" and zComplejoAB != ""):
					zAB = complex(float(zRealAB), float(zComplejoAB))
					cargaDeltaBalanceada.getiDesdeZ(zAB)
					dataCarga = "Carga delta balanceada agregada, Z: %s" %(zAB)
					self.displaylistaCargas.adapter.data.extend([dataCarga])
					self.listaCargas.append(cargaDeltaBalanceada)
					self.updateCorrientesPantalla()
					print(self.listaCargas)
					
			elif(desbalancActive == True):
				cargaDeltaDesbal = CargaDeltaDesbal(self.listaFuentes[0])
				if(zRealAB != "" and zComplejoAB != "" and zRealBC != "" and zComplejoBC != "" and zRealCA != "" and zComplejoCA != ""):
					zAB = complex(float(zRealAB), float(zComplejoAB))
					zBC = complex(float(zRealBC), float(zComplejoBC))
					zCA = complex(float(zRealCA), float(zComplejoCA))
					dataCarga = "Carga delta desbalanceada agregada, ZAB: %s, ZBC: %s, ZCA: %s" %(zAB, zBC, zCA)
					cargaDeltaDesbal.corrienteLinea(zAB,zBC,zCA)

					self.displaylistaCargas.adapter.data.extend([dataCarga])
					self.listaCargas.append(cargaDeltaDesbal)
					self.updateCorrientesPantalla()
					print(self.listaCargas)

			else:
				print('ERROR')

		else:
			print('ERROR DEBE SELECICONAR ALGUNO')
		
		print('===========================')
		print(cargaDeltaBalanceada.getIAn())
		print(cargaDeltaBalanceada.getIBn())
		print(cargaDeltaBalanceada.getICn())
		print(cargaDeltaBalanceada.getIAB())
		print(cargaDeltaBalanceada.getIBC())
		print(cargaDeltaBalanceada.getICA())

		print(cargaDeltaDesbal.getIAn())
		print(cargaDeltaDesbal.getIBn())
		print(cargaDeltaDesbal.getICn())
		print(cargaDeltaDesbal.getIAB())
		print(cargaDeltaDesbal.getIBC())
		print(cargaDeltaDesbal.getICA())

	def addCargaEstrella(self, pActive, zActive, pAparente, pReactiva, pReal, fp, adelantoActive, atrasoActive, zRealA, zComplejoA,zRealB, zComplejoB,zRealC, zComplejoC,neutroSi,neutroNo,balActive,desbalActive):
		print('agregandoTrifasica')
		cargaEstrellaBalanceada = CargaEstrellaBalanceada(self.listaFuentes[0])
		cargaEstrellaDesbalFuenteDelta = CargaEstrellaDesbalFuenteDelta(self.listaFuentes[0])
		cargaEstrellaDesbalConNeutro = CargaEstrellaDesbalConNeutro(self.listaFuentes[0])
		cargaEstrellaDesbalSinNeutro = CargaEstrellaDesbalSinNeutro(self.listaFuentes[0])

		if(fp == ""):
			fp = 1

		if(pActive):
			cargaEstrellaBalanceada = CargaEstrellaBalanceada(self.listaFuentes[0])
			if((pAparente != "" or pReactiva != "" or pReal != "") and fp != ""):
				fp = float(fp)
				if(pAparente != ""):
					pAparente = float(pAparente)
					if(adelantoActive):
						cargaEstrellaBalanceada.getiDesdePotencia(None, None, pAparente, fp, "Adelanto")
						dataCarga = "Carga estrella balanceada agregada, Potencia: %s VA, FP: %s, en %s" %(pAparente, fp, "adelanto")
					elif(atrasoActive):
						cargaEstrellaBalanceada.getiDesdePotencia(None, None, pAparente, fp, "Atraso")
						dataCarga = "Carga estrella balanceada agregada, Potencia: %s VA, FP: %s, en %s" %(pAparente, fp, "atraso")
				elif(pReactiva != ""):
					pReactiva = float(pReactiva)
					if(adelantoActive):
						cargaEstrellaBalanceada.getiDesdePotencia(None, pReactiva, None, fp, "Adelanto")
						dataCarga = "Carga estrella balanceada agregada, Potencia: %s VAr, FP: %s, en %s" %(pReactiva, fp, "adelanto")
					elif(atrasoActive):
						cargaEstrellaBalanceada.getiDesdePotencia(None, pReactiva, None, fp, "Atraso")
						dataCarga = "Carga estrella balanceada agregada, Potencia: %s VAr, FP: %s, en %s" %(pReactiva, fp, "atraso")

				elif(pReal != ""):
					pReal = float(pReal)
					if(adelantoActive):
						cargaEstrellaBalanceada.getiDesdePotencia(pReal, None, None, fp, "Adelanto")
						dataCarga = "Carga estrella balanceada agregada, Potencia: %s W, FP: %s, en %s" %(pReal, fp, "adelanto")
					elif(atrasoActive):
						cargaEstrellaBalanceada.getiDesdePotencia(pReal, None, None, fp, "Atraso")
						dataCarga = "Carga estrella balanceada agregada, Potencia: %s W, FP: %s, en %s" %(pReal, fp, "atraso")
				else:
					print('error')

				self.displaylistaCargas.adapter.data.extend([dataCarga])
				self.listaCargas.append(cargaEstrellaBalanceada)
				self.updateCorrientesPantalla()
				print(self.listaCargas)

			else:
				print('error')

		if(zActive):
			if(balActive):
				cargaEstrellaBalanceada = CargaEstrellaBalanceada(self.listaFuentes[0])
				if(zRealA != "" and zComplejoA != ""):
					z = complex(float(zRealA), float(zComplejoA))
					cargaEstrellaBalanceada.getiDesdeZ(z)
					dataCarga = "Carga estrella balanceada agregada, Z: %s" %(z)
					self.displaylistaCargas.adapter.data.extend([dataCarga])
					self.listaCargas.append(cargaEstrellaBalanceada)
					self.updateCorrientesPantalla()
					print(self.listaCargas)

				else:
					print('error')

			elif(desbalActive):
				if(neutroSi):
					if(self.tipoFuente == "Delta"):
						cargaEstrellaDesbalFuenteDelta = CargaEstrellaDesbalFuenteDelta(self.listaFuentes[0])
						if(zRealA != "" and zComplejoA != "" and zRealB != "" and zComplejoB != "" and zRealC != "" and zComplejoC != "" ):
							zAn = complex(float(zRealA), float(zComplejoA))
							zBn = complex(float(zRealB), float(zComplejoB))
							zCn = complex(float(zRealC), float(zComplejoC))
							cargaEstrellaDesbalFuenteDelta.corrientesLinea(zAn, zBn,zCn)
							dataCarga = "Carga estrella desbalanceada agregada, ZAB: %s, ZBC: %s, ZCA %s" %(zAn, zBn, zCn)
							self.displaylistaCargas.adapter.data.extend([dataCarga])
							self.listaCargas.append(cargaEstrellaDesbalFuenteDelta)
							self.updateCorrientesPantalla()
							print(self.listaCargas)
						else:
							print('error')

					elif(self.tipoFuente == "Estrella"):
						cargaEstrellaDesbalConNeutro = CargaEstrellaDesbalConNeutro(self.listaFuentes[0])
						if(zRealA != "" and zComplejoA != "" and zRealB != "" and zComplejoB != "" and zRealC != "" and zComplejoC != "" ):
							zAn = complex(float(zRealA), float(zComplejoA))
							zBn = complex(float(zRealB), float(zComplejoB))
							zCn = complex(float(zRealC), float(zComplejoC))
							cargaEstrellaDesbalConNeutro.corrientesLinea(zAn, zBn,zCn)
							dataCarga = "Carga estrella desbalanceada con neutro agregada, ZAB: %s, ZBC: %s, ZCA %s" %(zAn, zBn, zCn)
							self.displaylistaCargas.adapter.data.extend([dataCarga])
							self.listaCargas.append(cargaEstrellaDesbalConNeutro)
							self.updateCorrientesPantalla()
							print(self.listaCargas)

						else:
							print('error')

				elif(neutroNo): #CargaEstrellaDesbalSinNeutro
					cargaEstrellaDesbalSinNeutro = CargaEstrellaDesbalSinNeutro(self.listaFuentes[0])
					if(zRealA != "" and zComplejoA != "" and zRealB != "" and zComplejoB != "" and zRealC != "" and zComplejoC != "" ):
						zAn = complex(float(zRealA), float(zComplejoA))
						zBn = complex(float(zRealB), float(zComplejoB))
						zCn = complex(float(zRealC), float(zComplejoC))
						cargaEstrellaDesbalSinNeutro.corrientesLinea(zAn, zBn,zCn)
						dataCarga = "Carga estrella desbalanceada sin neutro agregada, ZAB: %s, ZBC: %s, ZCA %s" %(zAn, zBn, zCn)
						self.displaylistaCargas.adapter.data.extend([dataCarga])
						self.listaCargas.append(cargaEstrellaDesbalSinNeutro)
						self.updateCorrientesPantalla()
						print(self.listaCargas)

					else:
						print('error')
					
				else:
					print('error')


			else:
				print('error')
		else:
			print('erro')

		print(cargaEstrellaBalanceada.getIA())
		print(cargaEstrellaBalanceada.getIB())
		print(cargaEstrellaBalanceada.getIC())

		print(cargaEstrellaDesbalFuenteDelta.getIA())
		print(cargaEstrellaDesbalFuenteDelta.getIB())
		print(cargaEstrellaDesbalFuenteDelta.getIC())

		print(cargaEstrellaDesbalConNeutro.getIA())
		print(cargaEstrellaDesbalConNeutro.getIB())
		print(cargaEstrellaDesbalConNeutro.getIC())
		print("in")
		print(cargaEstrellaDesbalConNeutro.getIN())

		print(cargaEstrellaDesbalSinNeutro.getIA())
		print(cargaEstrellaDesbalSinNeutro.getIB())
		print(cargaEstrellaDesbalSinNeutro.getIC())		

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
