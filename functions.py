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
def getVFaseDelta(voltaje, secuencia, vin, vout):
	if(isRecComplex(voltaje)):
		value = None
		if(secuencia == "+"):
			value = getRecFromPol(math.sqrt(3), 30)
		elif(sencuencia == "-"):
			value = getRecFromPol(math.sqrt(3), -30)

		if(vin == "AB"):
			
		elif(vin == "BC"):

		elif(vin == "AC"):


class FuenteDelta(object):

	def __init__(self, Van = None , Vbn = None, Vcn = None, Vab = None, Vbc = None, Vca = None, secuencia = "ABC"):
		self.Van = Van
		self.Vbn = Vbn
		self.Vcn = Vcn
		self.Vab = Van
		self.Vbc = Vbc
		self.Vca = Vca
		self.secuencia = secuencia

		#Datos iniciales
		#Si tenemos Vab
		if(Vab != None):
			#Si la secuencia es positiva
			if(secuencia == "ABC"):
				if(Vbc == None):
					#Vbc = #mismo voltaje angulo menos 120
				if(Vca == None):
					#Vca = #mismo voltaje angulo mas 120
			#Secuencia negativa
			if(secuencia == "ACB"):
				if(Vbc == None):
					#Vbc = #mismo voltaje angulo mas 120
				if(Vca == None):
					#Vca = #mismo voltaje angulo menos 120
		
		#Si tenemos Vbc
		if(Vbc != None):
			#Si la secuencia es positiva
			if(secuencia == "ABC"):
				if(Vab == None):
					#Vab = #mismo voltaje angulo mas 120
				if(Vca == None):
					#Vca = #mismo voltaje angulo mas 240
			#Secuencia negativa
			if(secuencia == "ACB"):
				if(Vab == None):
					#Vbc = #mismo voltaje angulo menos 120
				if(Vca == None):
					#Vca = #mismo voltaje angulo menos 240

		#Si tenemos Vca
		if(Vca != None):
			#Si la secuencia es positiva
			if(secuencia == "ABC"):
				if(Vab == None):
					#Vab = #mismo voltaje angulo menos 120
				if(Vbc == None):
					#Vbc = #mismo voltaje angulo menos 240
			#Secuencia negativa
			if(secuencia == "ACB"):
				if(Vab == None):
					#Vab = #mismo voltaje angulo mas 120
				if(Vbc == None):
					#Vbc = #mismo voltaje angulo mas 240

		def getVLinea(vConocido, vDesconocido, secuencia):
			vDeLineas = ["Vab", "Vbc", "Vca"]
			if(vConocido != None):
				if(secuencia == "ABC"):
					
				if(secuencia == "ACB"):




