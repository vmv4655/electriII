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
		return False; 


#retorna un numero rectangular de uno polar
#el angulo debe estar en grados!!
def getRecFromPol(magnitud, angulo):
	if( isFloatOrInt(magnitud) and isFloatOrInt(angulo) ):
		radianes = degToRad(angulo)
		return cmath.rect(magnitud, radianes)
	else:
		return False




#Determina voltajes de fase a partir de voltajes
#de linea para una conexion de fuentes en delta.
##Entradas
#voltaje: voltaje entre dos puntos Vab, Vbc, Vca... en formato rectangular
#secuencia 
"""def getVFaseDelta(voltaje, secuencia, vin, vout):
	if(isRecComplex(voltaje)):
		value = None
		if(secuencia == "+"):
			value = getRecFromPol(math.sqrt(3), 30)
		elif(sencuencia == "-"):
			value = getRecFromPol(math.sqrt(3), -30)

		if(vin == "AB"):
			
		elif(vin == "BC"):

		elif(vin == "AC"):"""


class FuenteDelta(object):
	def __init__(self, Van = None , Vbn = None, Vcn = None, Vab = None, Vbc = None, Vca = None, secuencia = "ABC"):
		self.Van = Van
		self.Vbn = Vbn
		self.Vcn = Vcn
		self.Vab = Vab
		self.Vbc = Vbc
		self.Vca = Vca
		self.secuencia = secuencia

		def calcularAnguloVoltajes(v, operacion, valor):
			angulo = getPolFromRec(v)
			angulo = angulo[1]
			magnitud = getPolFromRec(v)
			magnitud = magnitud[0]
			if(operacion == "+"):
				angulo += valor
			elif(operacion == "-"):
				angulo -= valor
			return getRecFromPol(magnitud, angulo)

		def calcularVFases(v, secuencia):
			if(secuencia == "ABC"):
				cte = getRecFromPol(math.sqrt(3), 30)
			elif(secuencia == "ACB"):
				cte = getRecFromPol(math.sqrt(3), -30)
			res = v/cte
			return res
		#Calculando voltajes a partir de datos iniciales
		#Si tenemos Vab
		if(self.Vab != None):
			#Si la secuencia es positiva
			if(self.secuencia == "ABC"):
				#Calculando voltajes de linea
				if(self.Vbc == None):
					#Vbc = #mismo voltaje angulo menos 120
					self.Vbc = calcularAnguloVoltajes(self.Vab, "-", 120)
				if(self.Vca == None):
					#Vca = #mismo voltaje angulo mas 120
					self.Vca = calcularAnguloVoltajes(self.Vab, "+", 120)

			#Secuencia negativa
			if(self.secuencia == "ACB"):
				#Calculando voltajes de linea
				if(self.Vbc == None):
					#Vbc = #mismo voltaje angulo mas 120
					self.Vbc = calcularAnguloVoltajes(self.Vab, "+", 120)
				if(self.Vca == None):
					#Vca = #mismo voltaje angulo menos 120
					self.Vca = calcularAnguloVoltajes(self.Vab, "-", 120)
		

		#Si tenemos Vbc
		if(self.Vbc != None):
			#Si la secuencia es positiva
			if(self.secuencia == "ABC"):
				#Calculando voltajes de linea
				if(self.Vab == None):
					#Vab = #mismo voltaje angulo mas 120
					self.Vab = calcularAnguloVoltajes(self.Vbc, "+", 120)
				if(self.Vca == None):
					#Vca = #mismo voltaje angulo mas 240
					self.Vca = calcularAnguloVoltajes(self.Vbc, "+", 240)

			#Secuencia negativa
			if(self.secuencia == "ACB"):
				#Calculando voltajes de linea
				if(self.Vab == None):
					#Vab = #mismo voltaje angulo menos 120
					self.Vab = calcularAnguloVoltajes(self.Vbc, "-", 120)
				if(self.Vca == None):
					#Vca = #mismo voltaje angulo menos 240
					self.Vca = calcularAnguloVoltajes(self.Vbc, "-", 240)


		#Si tenemos Vca
		if(self.Vca != None):
			#Si la secuencia es positiva
			if(self.secuencia == "ABC"):
				#Calculando voltajes de linea
				if(self.Vab == None):
					#Vab = #mismo voltaje angulo menos 120
					self.Vab = calcularAnguloVoltajes(self.Vca, "-", 120)
				if(self.Vbc == None):
					#Vbc = #mismo voltaje angulo menos 240
					self.Vbc = calcularAnguloVoltajes(self.Vca, "-", 240)

			#Secuencia negativa
			if(self.secuencia == "ACB"):
				#Calculando voltajes de linea
				if(self.Vab == None):
					#Vab = #mismo voltaje angulo mas 120
					self.Vab = calcularAnguloVoltajes(self.Vca, "+", 120)
				if(self.Vbc == None):
					#Vbc = #mismo voltaje angulo mas 240
					self.Vbc = calcularAnguloVoltajes(self.Vca, "+", 240)

		#Calculando voltajes de fase
		if(self.Van == None):
			#Van = Vab/sqrt(3)<30 
			self.Van = calcularVFases(self.Vab, self.secuencia)
		if(self.Vbn == None):
			#Vbn = Vbc/sqrt(3)<30
			self.Vbn = calcularVFases(self.Vbc, self.secuencia)
		if(self.Vcn == None):
			#Vcn = Vca/sqrt(3)<30
			self.Vcn = calcularVFases(self.Vca, self.secuencia)


	#getters
	def getVab(self):
		return self.Vab
	def getVbc(self):
		return self.Vbc
	def getVca(self):
		return self.Vca
	def getVan(self):
		return self.Van
	def getVbn(self):
		return self.Vbn
	def getVcn(self):
		return self.Vcn

