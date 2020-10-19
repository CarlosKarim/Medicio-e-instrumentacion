import csv
import math
import numpy 

def datos(a,b):
    listaA = []
    #En la ruta para que funcione, hay que cambiar la ruta en donde se guardo los archivos 
    with open('/Users/3PY37LA_RS3\Desktop/5to Semestre/Medicion e instrumentacion/Examen/estMat.csv') as fileA:
        lineasA = fileA.read().splitlines()
        lineasA.pop(0)

        for i in lineasA:
            lineaA=i.split(',')
            listaA.append( [float(lineaA[a])])

    listaB = []
    with open('/Users/3PY37LA_RS3\Desktop/5to Semestre/Medicion e instrumentacion/Examen/estPor.csv') as fileB:
        lineasB = fileB.read().splitlines()
        lineasB.pop(0)
        for i in lineasB:
            lineaB=i.split(',')
            listaB.append([float(lineaB[b])])
    
    lista_ordenadaA=[] 
    for i in listaA:
        lista_ordenadaA.append(i[0])
    nA=len(lista_ordenadaA)

    lista_ordenadaB=[]
    for i in listaB:
        lista_ordenadaB.append(i[0])
    nB=len(lista_ordenadaB)

    #Media
    sumaA=0
    sumaB=0
    for i in lista_ordenadaA:
        sumaA=sumaA+i
        mediaA = sumaA /nA
    VarA=numpy.var(lista_ordenadaA)
    desA=math.sqrt(VarA)
    print(f"La media del documento A es: {mediaA}")
    print(f"La varianza del documento A es: {VarA}")
    print(f"La desviación estándar del documento A es: {desA} ")
    for i in lista_ordenadaB:
        sumaB=sumaB+i
        mediaB = sumaB/nB
    VarB=numpy.var(lista_ordenadaB)
    desB=math.sqrt(VarB)
    print(f"La media del documento B es: {mediaB}")
    print(f"La varianza del documento B es: {VarB}")
    print(f"La desviación estándar del documento B es: {desB} ")

print("De acuerdo a la siguiente enumeracion selecciona tu opcion.")
print("age(3)   famsize(4)  Pstatus(5)  Medu(7) Fedu(8) traveltime(13)  studytime(14)   failures(15)")
print("famrel(24)   freetime(25)   goout(26)  Dalc(27)  Walc(28)  health(29)    absences(30)    G1(31)  G2(32)    G3(33)")
datoA=int(input("La opcion de los estudiantes de Matematicas:"))
datoB=int(input("La opcion de los estudiantes de Portugues:"))
datos(datoA-1,datoB-1)
 