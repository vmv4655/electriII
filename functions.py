import cmath, math
#FUNCION PARA OBTENER EL FACTOR DE POTENCIA TOTAL
def FP (LWI,LWII,angulo1,angulo2):

       P      = LWI + LWII
       LWQ1   = LWI*((math.tan(angulo1*math.pi/180)))
       LWQ2   = LWII*((math.tan(angulo2*math.pi/180)))
       Q      = LWQ1+LWQ2
       angulo = math.atan(Q/P)
       Fp     = math.cos(angulo)
       print(Fp)
       print(P)
       print(Q)

# FUNCION PARA OBTENER LAS CORRIENTES DE LINEA DE LA FUENTE
def getCargasLinea(ListaCargas, secuencia):
	print('GETCARGASLINEA')
	ItrifasicaA = 0+0j
	ItrifasicaB = 0+0j
	ItrifasicaC = 0+0j
	for x in range(0,len(ListaCargas)):
		print('IN RANGE')

		carga=ListaCargas[x]
		print(carga.getTipoCarga())
		if (carga.getTipoCarga()=="Trifasica"):
			print("TRIFASICO")
			ItrifasicaA += carga.getIA()
			ItrifasicaB += carga.getIB()
			ItrifasicaC += carga.getIC()
		elif (carga.getTipoCarga()=="Monofasica"):
			print("ILILILIL")
			print(carga.getIL())
			if (carga.getConexion() == "AB" and secuencia== "ABC"):
				ItrifasicaA += carga.getIL()
			elif (carga.getConexion() == "AB" and secuencia== "ACB"):
				ItrifasicaB += carga.getIL()
			elif (carga.getConexion() == "BC" and secuencia== "ABC"):
				ItrifasicaB += carga.getIL()
			elif (carga.getConexion() == "BC" and secuencia== "ACB"):
				ItrifasicaC += carga.getIL()                        
			elif (carga.getConexion() == "CA" and secuencia== "ABC"):
				ItrifasicaC += carga.getIL()
			elif (carga.getConexion() == "CA" and secuencia== "ACB"):
				ItrifasicaA += carga.getIL()
			elif (carga.getConexion() == "AN"):
				ItrifasicaA += carga.getIL()
			elif (carga.getConexion() == "BN"):
				ItrifasicaB += carga.getIL()
			elif (carga.getConexion() == "CN"):
				ItrifasicaC += carga.getIL()
	return (ItrifasicaA, ItrifasicaB, ItrifasicaC)


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

#FUNCIONES PARA CARGAS MONOFASICAS(MOTORES MONOFASICOS,CARGAS RESISTIVAS)

#CORRIENTES LINEA PARA CARGAS MONOFASICAS 

class CargaMonofasica(object):
    tipo="Monofasica"
    conexion=None
    IL    = None
    voltaje=None
    EaN   = None
    EbN   = None
    EcN   = None
    Eab   = None
    Ebc   = None
    Eca   = None
    cita  = None

    def __init__(self, fuente):
        self.EaN   = fuente.getVab()
        self.EbN   = fuente.getVbc()
        self.EcN   = fuente.getVca()
        self.Eab   = fuente.getVan()
        self.Ebc   = fuente.getVbn()
        self.Eca   = fuente.getVcn()
    
    # sele pregunta al usuario el tipo de carga(motores, resistivas) Ademas de la conexion (AB, BC, CN, etc..)
    def setConexion(self, conexion):
        if (conexion == "AB"):  # SE ASIGNA UN VOLTAGE SEGUN SELLECCION DE CONECCION#
                self.voltaje =  self.EaN
                self.conexion="AB"
        if (conexion ==  "BC"):
                self.voltaje =  self.EbN 
                self.conexion="BC"   
        if (conexion == "CA"):
                self.voltaje =  self.EcN
                self.conexion="CA"
        if (conexion == "AN"):
                self.voltaje =  self.Eab  
                self.conexion="AN"
        if (conexion == "BN"):
                self.voltaje = self.Ebc 
                self.conexion="BN"
        if (conexion == "CN"):
                self.voltaje = self.Eca
                self.conexion="CN"
    #def setTipoCarga(self,  carga):
        #if (carga == "Monofasicas"):
            #self.tipocarga=carga
        #elif (carga=="Motores"):
            #self.tipocarga=carga


    def setDatosMonofase(self, P=None, Q=None, S=None, fp=None, direccion=None, Cantidad=None, Z=None):
        cita=None
        if (Z != None):
            self.IL=self.voltaje/Z
        else:
            if (direccion== "Adelanto"):
                cita  = -(math.acos(fp)*180/math.pi)
            else:
                if (direccion == "Atraso"):
                    cita  = (math.acos(fp)*180/math.pi)
            if (P==None and S==None):
                P=(Q/math.sin(cita*math.pi/180))*math.cos(cita*math.pi/180)
            elif (P==None and Q==None):
                P=S*fp
            print(getPolFromRec(self.voltaje))
            si  = (P/fp)*Cantidad
            sf  = getRecFromPol(1, cita)
            S   = si*sf
            Ilp = (S/self.voltaje)

            R   = Ilp.real
            I   = Ilp.imag
            self.IL  = complex(R, -I)

    def setDatosMotorMonofase(self, Cantidad, Hp, fp, n, direccion):
        cita=None
        if (direccion == "Adelanto"):
            cita  = -(math.acos(fp)*180/math.pi)
        else:
            if (direccion == "Atraso"):
                cita  = (math.acos(fp)*180/math.pi)
        Potencia   = Cantidad*Hp*746*1/n
        Si         = Potencia/fp
        Sf         = getRecFromPol(1, cita)
        S          = Si*Sf
        Ilp        = (S/self.voltaje)
        R          = Ilp.real
        I          = Ilp.imag
        self.IL    = complex(R, -I)   
            
    def getIL(self):
        return self.IL

    def getTipoCarga(self):
    	return self.tipo

    def getConexion(self):
    	return self.conexion

        
#FUNCINES PARA CARGAS TRIFASICA,(CONEXCIONES DELTA, ESTRELLA,MOTORES)

class CargaEstrellaBalanceada(object):

    tipo="Trifasica"
    IAB=None
    IBC=None
    ICA=None


    def __init__(self, fuente):
        self.EAn=fuente.getVan()
        self.EBn=fuente.getVbn()
        self.ECn=fuente.getVcn()
        self.EAB=fuente.getVab()
        self.EBC=fuente.getVbc()
        self.ECA=fuente.getVca()
    
    def getiDesdePotencia(self, P=None, Q=None, S=None, fp=None, direccion=None):
    	cita=None
    	if (direccion== "Adelanto"):
    		cita  = -(math.acos(fp)*180/math.pi)
    	else:
    		if (direccion == "Atraso"):
    			cita  = (math.acos(fp)*180/math.pi)
    	if (P==None and S==None):
    		P=((Q/math.sin(cita*math.pi/180))*math.cos(cita*math.pi/180))/3

    	elif (P==None and Q==None):
    		P=(S*fp)/3
    	si  = (P/fp)
    	sf  = getRecFromPol(1, cita)
    	S   = si*sf
    	Ilp = (S/self.EAB)
    	R   = Ilp.real
    	I   = Ilp.imag
    	self.IAB  = complex(R, -I)
    	self.IBC  = complex(R, -I)
    	self.ICA  = complex(R, -I)

    def getiDesdeZ(self,z):
        self.IAB=self.EAn/z
        self.IBC=self.EBn/z
        self.ICA=self.ECn/z

    def getIA(self):
        return self.IAB
    def getIB(self):
        return self.IBC
    def getIC(self):
        return self.ICA

    def getTipoCarga(self):
        return self.tipo
       
#PARA CARGAS ESTRELLA DESBALANCEADAS CON NEUTRO# 
class CargaEstrellaDesbalConNeutro(object):

    tipo="Trifasica"
    IA=None
    IB=None
    IC=None
    IN=None
    def __init__(self, fuente):
        self.EAn=fuente.getVan()
        self.EBn=fuente.getVbn()
        self.ECn=fuente.getVcn()
        self.Eab=fuente.getVab()
        self.Ebc=fuente.getVbc()
        self.Eca=fuente.getVca()
    def corrientesLinea(self,za,zb,zc):
        self.IA=self.EAn/za
        self.IB=self.EBn/zb
        self.IC=self.ECn/zc
        self.IN=self.IA+self.IB+self.IC
    def getIA(self):
        return self.IA
    def getIB(self):
        return self.IB
    def getIC(self):
        return self.IC 
    def getIN(self):
        return self.IN

    def getTipoCarga(self):
        return self.tipo
       
#PARA CARGAS ESTRELLA DESBALANCEADAS SIN NEUTRO CONECTADA A FUENTE ESTRELLA#
class CargaEstrellaDesbalSinNeutro(object):

    tipo="Trifasica"
    IA=None
    IB=None
    IC=None

    def __init__(self, fuente):

        self.EAB=fuente.getVab()
        self.EBC=fuente.getVbc()
        self.ECA=fuente.getVca()
    def corrientesLinea(self,za,zb,zc):
        self.IA=(self.EAB*zc-self.ECA*zb)/(za*zb+za*zc+zb*zc)
        self.IC=(self.ECA*zb-self.EBC*za)/(za*zb+za*zc+zb*zc)
        self.IB=(self.EBC*za-self.EAB*zc)/(za*zb+za*zc+zb*zc)
    def getIA(self):
        return self.IA
    def getIB(self):
        return self.IB
    def getIC(self):
        return self.IC 

    def getTipoCarga(self):
        return self.tipo
       



#PARA CARGAS ESTRELLA DESBALANCEADAS CONECTADA A DELTA(SIN NEUTRO)# 
class CargaEstrellaDesbalFuenteDelta(object):
    tipo="Trifasica"
    IA=None
    IB=None
    IC=None
    def __init__(self, fuente):
        self.EAB=fuente.getVab()
        self.EBC=fuente.getVbc()
        self.ECA=fuente.getVca()
    def corrientesLinea(self,za,zb,zc):
        self.IA=(self.EAB*zc-self.ECA*zb)/(za*zb+za*zc+zb*zc)
        self.IC=(self.ECA*zb-self.EBC*za)/(za*zb+za*zc+zb*zc)
        self.IB=(self.EBC*za-self.EAB*zc)/(za*zb+za*zc+zb*zc)
    def getIA(self):
        return self.IA
    def getIB(self):
        return self.IB
    def getIC(self):
        return self.IC 

    def getTipoCarga(self):
        return self.tipo    
               
#PARA CARGAS DELTA BALANCEADAS# 
class CargaDeltaBalanceada(object):
    tipo="Trifasica"
    IAB=None
    IBC=None
    ICA=None
    Ia=None
    Ib=None
    Ic=None
    def __init__(self, fuente):
        self.EAB=fuente.getVab()
        self.EBC=fuente.getVbc()
        self.ECA=fuente.getVca()
    def getiDesdePotencia(self, P=None, Q=None, S=None, fp=None, direccion=None):
    	cita=None
    	if (direccion== "Adelanto"):
    		cita  = -(math.acos(fp)*180/math.pi)
    	else:
    		if (direccion == "Atraso"):
    			cita  = (math.acos(fp)*180/math.pi)
    	if (P==None and S==None):
    		P=((Q/math.sin(cita*math.pi/180))*math.cos(cita*math.pi/180))/3

    	elif (P==None and Q==None):
    		P=(S*fp)/3
    	si  = (P/fp)
    	sf  = getRecFromPol(1, cita)
    	S   = si*sf
    	Ilp = (S/self.EAB)
    	R   = Ilp.real
    	I   = Ilp.imag
    	self.IAB  = complex(R, -I)
    	self.IBC  = complex(R, -I)
    	self.ICA  = complex(R, -I)
    	self.Ia=self.IAB*(complex(1.5,-0.8660254038))
    	self.Ib=self.IBC*(complex(1.5,-0.8660254038))
    	self.Ic=self.ICA*(complex(1.5,-0.8660254038))

    def getiDesdeZ(self,z):
        self.IAB=self.EAB/z
        self.IBC=self.EBC/z
        self.ICA=self.ECA/z
        self.Ia=self.IAB*(complex(1.5,-0.8660254038))
        self.Ib=self.IBC*(complex(1.5,-0.8660254038))
        self.Ic=self.ICA*(complex(1.5,-0.8660254038))
    
    def getIAn(self):
        return self.IAB
    def getIBn(self):
        return self.IBC
    def getICn(self):
        return self.ICA
    def getIAB(self):
        return self.Ia
    def getIBC(self):
        return self.Ib
    def getICA(self):
        return self.Ic

    def getIA(self):
        return self.Ia
    def getIB(self):
        return self.Ib
    def getIC(self):
        return self.Ic
    
    def getTipoCarga(self):
        return self.tipo

#PARA CARGA DELTA DESBALANCEADAS#
class CargaDeltaDesbal(object):
    tipo="Trifasica"
    IAB=None
    IBC=None
    ICA=None
    Ia=None
    Ib=None
    Ic=None
    def __init__(self, fuente):
        self.EAB=fuente.getVab()
        self.EBC=fuente.getVbc()
        self.ECA=fuente.getVca()
    def corrienteLinea(self, za, zb, zc):
        self.IAB=self.EAB/za
        self.IBC=self.EBC/zb
        self.ICA=self.ECA/zc
        self.Ia=self.IAB-self.ICA
        self.Ib=self.IBC-self.IAB
        self.Ic=self.ICA-self.IBC
    def getIAn(self):
        return self.IAB
    def getIBn(self):
        return self.IBC
    def getICn(self):
        return self.ICA
    def getIAB(self):
        return self.Ia
    def getIBC(self):
        return self.Ib
    def getICA(self):
        return self.Ic

    def getTipoCarga(self):
        return self.tipo

#Para motores,Apartir de Potencia,cantidad,Hp,FP,D,Eficiencia
#D=direccion(1=adelanto,0=atraso)
class CargaMotorTrifasico(object):
    tipo="Trifasica"
    IA=None
    IB=None
    Ic=None
    EAn=None
    EBn=None
    ECn=None
    def __init__(self, fuente):
        self.EAn=fuente.getVan()
        self.EBn=fuente.getVbn()
        self.ECn=fuente.getVcn()
    def polarTorectangular(v,ang):
        x=v*(math.cos(ang*math.pi/180))
        y=v*(math.sin(ang*math.pi/180))
        com=complex(x,y)
        return(com)
    def Il_motor(self,cantidad,Hp,fp,n): 
        cita=(math.degrees(math.acos(fp)))
        PIII=cantidad*Hp*746*(1/n)
        PI=PIII/3
        si  = (PI/fp)
        sf  = getRecFromPol(1, cita)
        S   = si*sf
        print(self.EAn)
        Ilp = (S/self.EAn)
        R   = Ilp.real
        I   = Ilp.imag
        self.IA  = complex(R, -I)
        self.IB=self.IA*(complex(-0.5,-0.8660254038))
        self.IC=self.IA*(complex(-0.5,+0.8660254038))
    def getIA(self):
        return self.IA
    def getIB(self):
        return self.IB
    def getIC(self):
        return self.IC

    def getTipoCarga(self):
        return self.tipo   
        
#FUNCIONES PARA CALCULAR LA POTENCIA ACTIVA Y REACTIVA CON METODO DE 2 Y 3 VATIMETROS


#MEDICION DE POTENCIA ACTIVA#
##METODO DE 2 VATIMETROS 
class dosVatimetrosactiva(object):
    Eab   = None
    Ebc  = None
    Eca   = None
    lectura=None
    def __init__(self, fuente):
        Eab=fuente.getVab()
        Ebc=fuente.getVbc()
        Eca=fuente.getVca()
    def dosVatimetrosE(self, Eab, Ebc, Eca, IAl, IBl, ICl, C):#C=punto comun
        LWI=0
        LWII=0
        if (C == str("A")):
               Vab, angA  = getPolFromRec(Eab)
               Vca, angB  = getPolFromRec(Eca)
               IB, angC   = getPolFromRec(IBl)
               IC, angD    = getPolFromRec(ICl)
               LWI  = Vab*IB*math.cos((ang1+180-angC)*math.pi/180)
               LWII = vca*IC*math.cos((ang2-angD)*math.pi/180) 

        elif (C == str("B")):
               Vab, angA = getPolFromRec(Eab)
               Vbc, angB = getPolFromRec(Ebc)
               IA, angC  = getPolFromRec(IAl)
               IC, angD  = getPolFromRec(ICl)
               LWI  = vab*IA*math.cos((angA-angC)*math.pi/180)
               LWII = vbc*IC*math.cos((angB+180-angD)*math.pi/180)

        elif (C == str("C")):
            Vca,angA = getPolFromRec(Eca)
            Vbc,angB = getPolFromRec(Ebc)
            IA, angC  = getPolFromRec(IAl)
            IB, angD  = getPolFromRec(IBl)

            LWI  = Vca*IA*math.cos((angA+180-angC)*math.pi/180)
            LWII = Vbc*IB*math.cos((angB-angD)*math.pi/180)

        self.lectura=LWI+LWII
    def getPotenciaActiva(self):
        return self.lectura
       
#METODO DE 3 VATIMETROS POTENCIA ACTIVA#
class tresVatimetrosactiva(object):
    Lectura = None
    Ean=None
    Ebn=None
    Ecn=None
    def __init__(self, fuente):
        self.Eab=fuente.getVan()
        self.Ebn=fuente.getVbn()
        self.Ecn=fuente.getVcn()

    
    def tresvatimetrosE(self, IA, IB, IC, Ean, Ebn, Ecn):
           EbC ,angB  = getPolFromRec(Ebn)
           EcA,angC = getPolFromRec(Ecn)
           EaB,angA = getPolFromRec(Ean)
           IA, angD  = getPolFromRec(IA)
           IB, angE  = getPolFromRec(IB)
           IC, angF  = getPolFromRec(IC)
           LWI      = EaB*IA*math.cos((angA-angD)*math.pi/180)
           LWII     = EbC*IB*math.cos((angB-angE)*math.pi/180)
           LWIII    = EcA*IC*math.cos((angC-angF)*math.pi/180)
           self.Lectura  = LWI+LWII+LWIII

    def getPotenciaActiva(self):
        return self.Lectura


#MEDICION DE POTENCIA RECTIVA#
##METODO DE 2 VATIMETROS 
class dosVatimetrosreactiva(object):
    Eab   = None
    Ebc   = None
    Eca   = None
    lectura=None
    def __init__(self, fuente):
        Eab=fuente.getVab()
        Ebc=fuente.getVbc()
        Eca=fuente.getVca()
   
    def dos_vatimetrosE(self,IAl, IBl, ICl, Eab, Ebc, Eca,C):#C=punto comun
        LWI=0
        LWII=0
        if (C == str("A")):
            Vab, angA  = getPolFromRec(Eab)
            Vca, angB  = getPolFromRec(Eca)
            IB, angC   = getPolFromRec(IBl)
            IC, angD    = getPolFromRec(ICl)
            
            LWI  = Vab*IB*math.sin((ang1+180-angC)*math.pi/180)
            LWII = vca*IC*math.sin((ang2-angD)*math.pi/180) 

        elif (C == str("B")):
            Vab, angA = getPolFromRec(Eab)
            Vbc, angB = getPolFromRec(Ebc)
            IA,  angC  = getPolFromRec(IAl)
            IC,  angD  = getPolFromRec(ICl)
            
            LWI  = vab*IA*math.sin((angA-angC)*math.pi/180)
            LWII = vbc*IC*math.sin((angB+180-angD)*math.pi/180)

        elif (C == str("C")):
            Vca, angA = getPolFromRec(Eca)
            Vbc, angB = getPolFromRec(Ebc)
            IA, angC  = getPolFromRec(IAl)
            IB, angD  = getPolFromRec(IBl)

            LWI  = Vca*IA*math.sin((angA+180-angC)*math.pi/180)
            LWII = Vbc*IB*math.sin((angB-angD)*math.pi/180)

        lecctura=LWI+LWII

    def getPotenciaReActiva(self):
        return self.lectura
        
#METODO DE 3 VATIMETROS POTENCIA ACTIVA#
class tresVatimetrosreactiva(object):
    Lectura = None
    Ean = None
    Ebn = None
    Ecn = None
    Lectura = None
    def __init__(self, fuente):
        Ean=fuente.getVan()
        Ebn=fuente.getVbn()
        Ecn=fuente.getVca()
  
    def tres_vatimetrosE(self, IAl, IBl, ICl, Ean, Ebn, Ecn):
           EaB, angA = getPolFromRec(Ean)
           EbC, angB = getPolFromRec(Ebn)
           EcA, angC = getPolFromRec(Ecn)

           IA, angD  = getPolFromRec(IAl)
           IB, angE  = getPolFromRec(IBl)
           IC, angF  = getPolFromRec(ICl)

           LWI      = EaB*IA*sin((angA-angD)*math.pi/180)
           LWII     = EbC*IB*sin((angB-angE)*math.pi/180)
           LWIII    = EcA*IC*sin((angC-angF)*math.pi/180)
           self.lectura  = LWI+LWII+LWIII

    def getPotenciaReActiva(self):
        return self.lectura
        
