def Angulo(x,y):
    if int(x)==0:
        x=int(0)
    import math
    
    if x==0 and y>0:
        ang=90
        return(ang)
    
    elif x==0 and y<0:
        ang=-90
        return(ang)
    else:
        ang=math.atan(y/x)*180/math.pi
        if x>0 and y>=0:
             ang=ang
        elif x<0 and y<0:
            ang=ang-180
        elif x>0 and y<=0:
            ang=ang
        elif x<0 and y>0:
            ang=ang+180
        else:
            ang=270
        return (ang)
#Funcion para pasar de polar a rectangular apartir de un voltage y angulo  
def polar_rectangular(v,ang):
    import math
    x=v*(math.cos(ang*math.pi/180))
    y=v*(math.sin(ang*math.pi/180))
    com=complex(x,y)
    return(com)
#Funcion para pasar de rectangular a polar apartir de un voltage y angulo  
def rectangular_polar(rec):
    import math
    valor=math.sqrt((rec.real)**2+(rec.imag)**2)
    ang=Angulo(rec.real,rec.imag)
    return(valor,ang)

#para secuencia positiva voltage AN,BN,CN
def vfase_fuenteT(a,b):
    import math
    AN=polar_rectangular(a,b)
    BN=AN*(complex(-0.5,-0.8660254038))
    CN=AN*(complex(-0.5,+0.8660254038))
    return AN,BN,CN

#para secuencia positiva voltage AN
def vfase_fuente():
    import math
    a=int(input("Digite la magnitud voltage de fase AN : "))
    b=int(input("Digite el angulo del voltage de fase AN : "))
    AN=polar_rectangular(a,b)
    BN=AN*(complex(-0.5,-0.8660254038))
    CN=AN*(complex(-0.5,+0.8660254038))
    ANp,a1=rectangular_polar(AN)
    BNp,a2=rectangular_polar(BN)
    CNp,a3=rectangular_polar(CN)
    print("voltages de fase:")
    print("AN= ",int(ANp),"∡",round(a1,0))
    print("BN= ",int(BNp),"∡",round(a2,0))
    print("CN= ",int(CNp),"∡",round(a3,0))


#voltage de fase para secuencia negativa AN
def vfase_fuenteN():
    import math
    a=int(input("Digite la magnitud voltage de fase AN : "))
    b=int(input("Digite el angulo del voltage de fase AN : "))
    AN=polar_rectangular(a,b)
    CN=AN*(complex(-0.5,-0.8660254038))
    BN=AN*(complex(-0.5,+0.8660254038))
    ANp,a1=rectangular_polar(AN)
    BNp,a2=rectangular_polar(BN)
    CNp,a3=rectangular_polar(CN)
    print("voltages de fase:")
    print("AN= ",int(ANp),"∡",round(a1,0))
    print("BN= ",int(BNp),"∡",round(a2,0))
    print("CN= ",int(CNp),"∡",round(a3,0))  
    
#voltage de LINEA para fuente en ESTRELLA secuencia positiva
def v_lineaFuenteE(a,b):
    import math
    AN=polar_rectangular(a,b)
    CN=AN*(complex(-0.5,-0.8660254038))
    BN=AN*(complex(-0.5,+0.8660254038))
    
    Vab=AN*(complex(1.5,0.8660254038))
    Vbc=BN*(complex(1.5,0.8660254038))
    Vca=CN*(complex(1.5,0.8660254038))
    return Vab,Vbc,Vca
#voltage de LINEA para fuente en ESTRELLA secuencia negativa
def v_lineaFuenteEN(a,b):
    import math
    AN=polar_rectangular(a,b)
    CN=AN*(complex(-0.5,-0.8660254038))
    BN=AN*(complex(-0.5,+0.8660254038))
    
    Vab=AN*(complex(1.5,-0.8660254038))
    Vbc=BN*(complex(1.5,-0.8660254038))
    Vca=CN*(complex(1.5,-0.8660254038))
    return Vab,Vbc,Vca
    
#voltages de LINEA para una fuente en DELTA secuencia positiva
def v_lineaFuenteD(a,b):
    vab,vbc,vca=vfase_fuenteT(a,b)
    
    
#FUNCIONES PARA CARGAS BALANCEADAS CONECTADAS A FUENTES ESTRELLA
    
#funcion para corrientes en una CARGA BALANCEADA en ESTRELLA conectada a fuente en estrella
def Il_cargaBestrella(a,b,z):#"z" es la carga de entrada
    EaN,EbN,EcN=vfase_fuenteT(a,b)
    Ia=AN/z
    Ib=BN/z
    Ic=CN/z
    return Ia,Ib,Ic
#corrientes de FASE para CARGA DELTA BALNCEADA conectada a fuente en estrella(secuencia +)
def IFase_cargaBdelta(a,b,z):
    vab,vbc,vca=v_lineaFuenteE(a,b)
    IAB=vab/z
    IBC=vbc/z
    ICA=vca/z
    return IAB,IBC,ICA
#corrientes de LINEA para CARGA DELTA BALANCEADA conectada a fuente en estrella(secuencia +)
def ILinea_cargaBdelta(a,b,z):
    IAB,IBC,ICA=IFase_cargaBdelta(a,b,z)
    Ia=IAB*(complex(1.5,-0.8660254038))
    Ib=IBC*(complex(1.5,-0.8660254038))
    Ic=ICA*(complex(1.5,-0.8660254038))
    return Ia,Ib,Ic

#FUNCIONES PARA CARGAS DESBALANCEADAS CONECTADAS A FUENTES ESTRELLA

#funcion para corrientes LINEA en una CARGA BALANCEADA en ESTRELLA conectada a fuente en estrella
def Il_cargaDestrella(a,b,za,zb,zc):#"za,zb,zc" son las cargas de entrada
    AN,AN,EN=vfase_fuenteT(a,b)
    Ia=AN/za
    Ib=BN/zb
    Ic=CN/zc
    return Ia,Ib,Ic

#corrientes de FASE para CARGA DELTA DESBALNCEADA conectada a fuente en estrella(secuencia +)
def IFase_cargaDdelta(a,b,za,zb,zc):
    vab,vbc,vca=v_lineaFuenteE(a,b)
    IAB=vab/za
    IBC=vbc/zb
    ICA=vca/zc
    return IAB,IBC,ICA
#corrientes de LINEA para CARGA DELTA DESBALANCEADA conectada a fuente en estrella(secuencia +)
def ILinea_cargaDdelta(a,b,za,zb,zc):
    IAB,IBC,ICA=IFase_cargaBdelta(a,b,za,zb,zc)
    Ia=IAB*(complex(1.5,-0.8660254038))
    Ib=IBC*(complex(1.5,-0.8660254038))
    Ic=ICA*(complex(1.5,-0.8660254038))
    return Ia,Ib,Ic

#CORRIENTES LINEA PARA CARGAS MONOFASICAS APARTIR DE POTENCIA Y FP

#Conexion AB
def IMon_ABs(a,b,s,fp):# s=potencia aparente fp=factor_potencia
    import math
    EaN,EbN,EcN=vfase_fuenteT(a,b)
    sf=polar_rectangular(s,θ)
    Il=sf/EaN
    Iln,an=rectangular_polar(Il)
    ann=-an
    ilf=polar_rectangular(Iln,ann)
    return(ilf)
    
def IMon_ABp(a,b,p,fp):# p=potencia real fp=factor_potencia
    import math
    EaN,EbN,EcN=vfase_fuenteT(a,b)
    θ=math.degrees(math.acos(fp))
    s=p/fp
    sf=polar_rectangular(s,θ)
    Il=sf/EaN
    Iln,an=rectangular_polar(Il)
    ann=-an
    ilf=polar_rectangular(Iln,ann)
    return(ilf)
def IMon_ABQ(a,b,Q,fp):# q=potencia reactiva fp=factor_potencia
    import math
    EaN,EbN,EcN=vfase_fuenteT(a,b)
    θ=math.degrees(math.acos(fp))
    s=Q/math.sin(θ*math.pi/180)
    sf=polar_rectangular(s,θ)
    Il=sf/EaN
    Iln,an=rectangular_polar(Il)
    ann=-an
    ilf=polar_rectangular(Iln,ann)
    return(ilf)
#Conexion BC
def IMon_BCs(a,b,s,fp):# s=potencia aparente fp=factor_potencia
    import math
    EaN,EbN,EcN=vfase_fuenteT(a,b)
    sf=polar_rectangular(s,θ)
    Il=sf/EbN
    Iln,an=rectangular_polar(Il)
    ann=-an
    ilf=polar_rectangular(Iln,ann)
    return(ilf)
def IMon_BCp(a,b,p,fp):# Q=potencia real fp=factor_potencia
    import math
    EaN,EbN,EcN=vfase_fuenteT(a,b)
    θ=math.degrees(math.acos(fp))
    s=p/fp
    sf=polar_rectangular(s,θ)
    Il=sf/EbN
    Iln,an=rectangular_polar(Il)
    ann=-an
    ilf=polar_rectangular(Iln,ann)
    return(ilf)
    
def IMon_BCQ(a,b,Q,fp):# Q=potencia reactiva fp=factor_potencia
    import math
    EaN,EbN,EcN=vfase_fuenteT(a,b)
    θ=math.degrees(math.acos(fp))
    s=Q/math.sin(θ*math.pi/180)
    sf=polar_rectangular(s,θ)
    Il=sf/EbN
    Iln,an=rectangular_polar(Il)
    ann=-an
    ilf=polar_rectangular(Iln,ann)
    return(ilf)
#Conexion BC
def IMon_CAs(a,b,s,fp):# s=potencia aparente fp=factor_potencia
    import math
    EaN,EbN,EcN=vfase_fuenteT(a,b)
    sf=polar_rectangular(s,θ)
    Il=sf/EcN
    Iln,an=rectangular_polar(Il)
    ann=-an
    ilf=polar_rectangular(Iln,ann)
    return(ilf)
def IMon_CAp(a,b,p,fp):# p=potencia real fp=factor_potencia
    import math
    EaN,EbN,EcN=vfase_fuenteT(a,b)
    θ=math.degrees(math.acos(fp))
    s=p/fp
    sf=polar_rectangular(s,θ)
    Il=sf/EcN
    Iln,an=rectangular_polar(Il)
    ann=-an
    ilf=polar_rectangular(Iln,ann)
    return(ilf)
def IMon_CAQ(a,b,Q,fp):# Q=potencia reactiva fp=factor_potencia
    import math
    EaN,EbN,EcN=vfase_fuenteT(a,b)
    θ=math.degrees(math.acos(fp))
    s=Q/math.sin(θ*math.pi/180)
    sf=polar_rectangular(s,θ)
    Il=sf/EcN
    Iln,an=rectangular_polar(Il)
    ann=-an
    ilf=polar_rectangular(Iln,ann)
    return(ilf)

#Para motores,Apartir de Potencia,cantidad,Hp,FP,D,Eficiencia
#D=direccion(1=adelanto,0=atraso)
def Il_motor(a,b,p,c,Hp,fp,D,E): 
    import math
    EaN,EbN,EcN=vfase_fuenteT(a,b)
    θ=math.degrees(math.acos(fp))
    if D==1:
        θ=-θ
    else:
        θ==θ
    Ef=E/100
    PΦ=c*Hp*746*p*(1/Ef)
    PIΦ=PΦ/3
    s=PIΦ/fp
    sf=polar_rectangular(s,θ)
    Il=sf/EaN
    Iln,an=rectangular_polar(Il)
    ann=-an
    ilf=polar_rectangular(Iln,ann)
    IA=ilf
    IB=ilf*(complex(-0.5,-0.8660254038))
    IC=ilf*(complex(-0.5,+0.8660254038))
    return IA,IB,IC

#MEDICION DE POTENCIA
##METODO DE 2 VATIMETROS FUENTE ESTRELLA
"""def dos_vatimetrosE(a,b,C):#C=punto comun
 import math
    vab,vbc,vca=v_lineaFuenteE(a,b)
    LWI=0
    LWII=0
    if C==str("a") or C==str("A"):
        Vbc,ang1=rectangular_polar(vbc)
        Vca,ang2=rectangular_polar(vca)
        LWI=vab*IB*math.cos(ang1+180-)
        LWII=vca*IC*math.cos(ang2-)
    elif C=str("b")or C==str("B"):
        Vab,ang1=rectangular_polar(vab)
        Vca,ang2=rectangular_polar(vca)
        LWI=vab*IA*math.cos(ang1-)
        LWII=vca*IC*math.cos(ang2+180-)
    elif C=str("c")or C==str("C"):
        Vab,ang1=rectangular_polar(vab)
        Vbc,ang2=rectangular_polar(vbc)
        LWI=vab*IA*math.cos(ang1+180-)
        LWII=vbc*IB*math.cos(ang2+180-)
    P=LWI+LWII
    return p"""
##METODO DE 3 VATIMETROS FUENTE ESTRELLA
"""def tres_vatimetrosE(a,b):
 EaN,EbN,EcN=vfase_fuenteT(a,b)
    VaN,ang1=rectangular_polar(EaN)
    VbN,ang2=rectangular_polar(EbN)
    VcN,ang3=rectangular_polar(EcN)
    IAv,ang4=ItotalF()
    IBv,ang5=ItotalF()
    ICv,ang6=ItotalF()
    LWI=EaN*IA*cos(ang1-ang4)
    LWII=EbN*IB*cos(ang2-ang5)
    LWIII=EcN*IC*cos(ang3-ang6)"""

    
    
    
        
        
    
    
    
    

                   
                   
            





            

    
    


