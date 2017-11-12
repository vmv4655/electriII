import cmath, math

#Verifica si un valor es de tipo entero o flotante
def isFloatOrInt(number):
	if( isinstance(number, (float, int)) ):
		return True
	else:
		return False

#Convierte de grados a radianes
def degToRad(number):
	if(isFloatOrInt(number)):
		radianes = number*(math.pi/180)
		return radianes
	else:
		return False

#convierte de radianes a grados
def radToDeg(number):
	if (isFloatOrInt(number)):
		grados = number*(180/math.pi)
		return grados
	else:
		return False

#Determinma si un numero es un complejo
#rectangular.
def isRecComplex(complexNumber):
	if(type(complexNumber) == complex ):
		return True
	else:
		return False

#Devuelve una tupla compuesta de la magnitud y
#angulo (en grados) del numero polar a partir de un numero
#complejo rectangular. Falso si el parametro de
#entrada no es un numero complejo.
def getPolFromRec(complexNumber):
	if( isRecComplex(complexNumber) ):
		polar = cmath.polar(complexNumber)
		angle = radToDeg(polar[1]);
		return (polar[0], angle) 
	else:
		return False

#Devuelve una tupla compuesta de la magnitud y
#angulo (en grados) del numero polar a partir de un numero
#complejo rectangular (valores redondeados). Falso si el parametro de
#entrada no es un numero complejo.
def getPolFromRecToGUI(complexNumber):
	if( isRecComplex(complexNumber) ):
		polar  = cmath.polar(complexNumber)
		angle  = radToDeg(polar[1]);
		result = str(round(polar[0],4)) + " < " + str(round(angle, 4))
		#return (round(polar[0],4), round(angle, 4)) 
		return result
	else:
		return False


#retorna un numero rectangular de uno polar
#el angulo debe estar en grados!!
def getRecFromPol(magnitud, angulo):
	if( isFloatOrInt(magnitud) and isFloatOrInt(angulo) ):
		radianes = degToRad(angulo)
		return cmath.rect(magnitud, radianes)
	else:
		return False

#Convierte Hp a Watts
def HpToWatts (hp):
	if( isFloatOrInt(hp)):
		W = hp*746
		return W
	else: 
		return False

#Clase padre para modelar tanto la fuente delta como la estrella
#se utiliza herencia porque ambas fuentes van a tener los mismos
#metodos
class Fuente(object):
	Van = None
	Vbn = None
	Vcn = None
	Vab = None
	Vbc	= None
	Vca	= None

	#Devuelve el valor de una fase a partir de otra
	def calcularAnguloVoltajes(self, v, operacion, valor):
		angulo = getPolFromRec(v)
		angulo = angulo[1]
		magnitud = getPolFromRec(v)
		magnitud = magnitud[0]
		if(operacion == "+"):
			angulo += valor
		elif(operacion == "-"):
			angulo -= valor
		return getRecFromPol(magnitud, angulo)

	#Devuelve un un voltaje de fase a partir de un voltaje de linea
	def calcularVFases(self, v, secuencia):
		if(secuencia == "ABC"):
			cte = getRecFromPol(math.sqrt(3), 30)
		elif(secuencia == "ACB"):
			cte = getRecFromPol(math.sqrt(3), -30)
		res = v/cte
		return res

	#Devuelve un voltaje de linea a partir de un voltaje de fase
	def calcularVLinea(self, v, secuencia):
		if(secuencia == "ABC"):
			cte = getRecFromPol(math.sqrt(3), 30)
		elif(secuencia == "ACB"):
			cte = getRecFromPol(math.sqrt(3), -30)
		res = v*cte
		return res

	#Calcula todos los voltajes de fase y de linea a partir de uno dado
	def calcularVoltajes(self, Van = None , Vbn = None, Vcn = None, Vab = None, Vbc = None, Vca = None, secuencia = "ABC"):
		self.Van = Van
		self.Vbn = Vbn
		self.Vcn = Vcn
		self.Vab = Vab
		self.Vbc = Vbc
		self.Vca = Vca
		self.secuencia = secuencia

		#Calculando voltajes a partir de datos iniciales
		#Si tenemos Vab
		if(self.Vab != None):
			#Si la secuencia es positiva
			if(self.secuencia == "ABC"):
				#Calculando voltajes de linea
				if(self.Vbc == None):
					#Vbc = #mismo voltaje angulo menos 120
					self.Vbc = self.calcularAnguloVoltajes(self.Vab, "-", 120)
				if(self.Vca == None):
					#Vca = #mismo voltaje angulo mas 120
					self.Vca = self.calcularAnguloVoltajes(self.Vab, "+", 120)

			#Secuencia negativa
			if(self.secuencia == "ACB"):
				#Calculando voltajes de linea
				if(self.Vbc == None):
					#Vbc = #mismo voltaje angulo mas 120
					self.Vbc = self.calcularAnguloVoltajes(self.Vab, "+", 120)
				if(self.Vca == None):
					#Vca = #mismo voltaje angulo menos 120
					self.Vca = self.calcularAnguloVoltajes(self.Vab, "-", 120)
		

		#Si tenemos Vbc
		if(self.Vbc != None):
			#Si la secuencia es positiva
			if(self.secuencia == "ABC"):
				#Calculando voltajes de linea
				if(self.Vab == None):
					#Vab = #mismo voltaje angulo mas 120
					self.Vab = self.calcularAnguloVoltajes(self.Vbc, "+", 120)
				if(self.Vca == None):
					#Vca = #mismo voltaje angulo mas 240
					self.Vca = self.calcularAnguloVoltajes(self.Vbc, "+", 240)

			#Secuencia negativa
			if(self.secuencia == "ACB"):
				#Calculando voltajes de linea
				if(self.Vab == None):
					#Vab = #mismo voltaje angulo menos 120
					self.Vab = self.calcularAnguloVoltajes(self.Vbc, "-", 120)
				if(self.Vca == None):
					#Vca = #mismo voltaje angulo menos 240
					self.Vca = self.calcularAnguloVoltajes(self.Vbc, "-", 240)


		#Si tenemos Vca
		if(self.Vca != None):
			#Si la secuencia es positiva
			if(self.secuencia == "ABC"):
				#Calculando voltajes de linea
				if(self.Vab == None):
					#Vab = #mismo voltaje angulo menos 120
					self.Vab = self.calcularAnguloVoltajes(self.Vca, "-", 120)
				if(self.Vbc == None):
					#Vbc = #mismo voltaje angulo menos 240
					self.Vbc = self.calcularAnguloVoltajes(self.Vca, "-", 240)

			#Secuencia negativa
			if(self.secuencia == "ACB"):
				#Calculando voltajes de linea
				if(self.Vab == None):
					#Vab = #mismo voltaje angulo mas 120
					self.Vab = self.calcularAnguloVoltajes(self.Vca, "+", 120)
				if(self.Vbc == None):
					#Vbc = #mismo voltaje angulo mas 240
					self.Vbc = self.calcularAnguloVoltajes(self.Vca, "+", 240)
		#Si tenemos algun voltaje de lineas, calculamos los de fase
		if(self.Vab != None or self.Vbc != None or self.Vca != None):
			#Calculando voltajes de fase
			if(self.Van == None):
				#Van = Vab/sqrt(3)<30 
				self.Van = self.calcularVFases(self.Vab, self.secuencia)
			if(self.Vbn == None):
				#Vbn = Vbc/sqrt(3)<30
				self.Vbn = self.calcularVFases(self.Vbc, self.secuencia)
			if(self.Vcn == None):
				#Vcn = Vca/sqrt(3)<30
				self.Vcn = self.calcularVFases(self.Vca, self.secuencia)


		#Si nos dan un voltaje de fase, calcular todos los otros ademas de los de linea
		if(self.Van != None):
			if(self.secuencia == "ABC"):
				if(self.Vbn == None):
					self.Vbn = self.calcularAnguloVoltajes(self.Van, "-", 120)

				if(self.Vcn == None):
					self.Vcn = self.calcularAnguloVoltajes(self.Van, "+", 120)
			
			if(self.secuencia == "ACB"):
				if(self.Vbn == None):
					self.Vbn = self.calcularAnguloVoltajes(self.Van, "+", 120)
				if(self.Vcn == None):
					self.Vcn = self.calcularAnguloVoltajes(self.Van, "-", 120)


		if(self.Vbn != None):
			if(self.secuencia == "ABC"):
				if(self.Van == None):
					self.Van = self.calcularAnguloVoltajes(self.Vbn, "+", 120)
				if(self.Vcn == None):
					self.Vcn = self.calcularAnguloVoltajes(self.Vbn, "+", 240)
			
			if(self.secuencia == "ACB"):
				if(self.Van == None):
					self.Van = self.calcularAnguloVoltajes(self.Vbn, "-", 120)
				if(self.Vcn == None):
					self.Vcn = self.calcularAnguloVoltajes(self.Vbn, "-", 240)


		if(self.Vcn != None):
			if(self.secuencia == "ABC"):
				if(self.Van == None):
					self.Van = self.calcularAnguloVoltajes(self.Vcn, "-", 120)
				if(self.Vbn == None):
					self.Vbn = self.calcularAnguloVoltajes(self.Vcn, "-", 240)
			
			if(self.secuencia == "ACB"):
				if(self.Van == None):
					self.Van = self.calcularAnguloVoltajes(self.Vcn, "+", 120)
				if(self.Vbn == None):
					self.Vbn = self.calcularAnguloVoltajes(self.Vcn, "+", 240)


		#Si tenemos algun voltaje de fase calculamos los de lineas
		if(self.Van != None or self.Vbn != None or self.Vcn != None):
			if(self.Vab == None):
			#Vab = Van*sqrt(3)<30
				self.Vab = self.calcularVLinea(self.Van, self.secuencia)
			if(self.Vbc == None):
				#Vbc = Vbn*sqrt(3)<30
				self.Vbc = self.calcularVLinea(self.Vbn, self.secuencia)
			if(self.Vca == None):
				#Vca = Vcn*sqrt(3)<30
				self.Vca = self.calcularVLinea(self.Vcn, self.secuencia)

	#getters
	#Retorna el voltaje de linea Vab
	def getVab(self):
		return self.Vab
	#Retorna el voltaje de linea Vbc 
	def getVbc(self):
		return self.Vbc
	#Retorna el voltaje de linea Vca
	def getVca(self):
		return self.Vca
	#Retorna el voltaje de fase Van
	def getVan(self):
		return self.Van
	#Retorna el voltaje de fase Vbn
	def getVbn(self):
		return self.Vbn
	#Retorna el voltaje de fase Vcn
	def getVcn(self):
		return self.Vcn

class FuenteDelta(Fuente):
	pass

class FuenteEstrella(Fuente):
	pass

