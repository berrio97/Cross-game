#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Berrio Galindo, Alvaro
# Calvo Madurga, Alberto
import random

def golpe(fila, columna):
    # FUNCION QUE SELECCIONA LAS CASILLAS A GOLPEAR#
    matriz[fila][columna]+=1
    matriz[fila + 2][columna - 1]+=1
    matriz[fila + 2][columna]+=1
    matriz[fila + 2][columna + 1]+=1
    matriz[fila + 1][columna - 2]+=1
    matriz[fila + 1][columna - 1]+=1
    matriz[fila + 1][columna]+=1
    matriz[fila + 1][columna + 1]+=1
    matriz[fila + 1][columna + 2]+=1
    matriz[fila][columna - 2]+=1
    matriz[fila][columna - 1]+=1
    matriz[fila][columna + 1]+=1
    matriz[fila][columna + 2]+=1
    matriz[fila - 1][columna - 2]+=1
    matriz[fila - 1][columna - 1]+=1
    matriz[fila - 1][columna]+=1
    matriz[fila - 1][columna + 1]+=1
    matriz[fila - 1][columna + 2] +=1
    matriz[fila - 2][columna - 1]+=1
    matriz[fila - 2][columna]+=1
    matriz[fila - 2][columna + 1]+=1
def impMat(z,fil,col): #FUNCION QUE IMPRIME LA MATRIZ
    print"   ",
    for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print i,
    print
    print("   ____________________")
    for i in range(2, fil + 2):
        print (z[i - 2] + " |"),
        for j in range(2, col + 2):
            if (matriz[i][j]%2 == 0):
                print ".",
            else:
                print "X",
        print ("|")
    print("   --------------------")
def puntuaciones(cont,listafich,lvl):#FUNCION QUE ESCRIBE EN EL FICHERO SOLO SI LA PUNTUACION DEL NIVEL ACTUAL ES MENOR QUE LA QUE ESTABA
    pfich=int(listafich[lvl-1])
    if cont<pfich or pfich==0:
        print ("NUEVO RECORD             Puntuacion nueva = "+str(cont))
        listafich[lvl-1]=str(cont)+"\n"
        arch=open("Puntuacion.txt","w+")
        arch.writelines(listafich)
        arch.close()
    else:
        print("No has superado tu record")
def completado(fil,col,bool): #FUNCION QUE COMPRUEBA SI SE HA COMPLETADO EL NIVEL
    for i in range(2, fil + 2):
        for j in range(2, col + 2):
            if (matriz[i][j]%2 != 0):
                bool = False,
                return bool
    bool = True
    return bool


matriz = []
d = []  # EN ESTA LISTA ALMACENAMOS LOS GOLPES QUE INTRODUCE EL USUARIO PARA LUEGO DESHACERLOS
z = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
contd = 0 #SE USA PARA ALMACENAR EL CONTADOR LOS GOLPES AL DESHACER
fil = 10
col = 10
for i in range(14):
    matriz.append([0] * 14)
level = int(raw_input("Escribe el nivel\n"))
lvl = level
while level < 1: #GENERADOR DE GOLPES DE NIVEL
    print ("Introduzca un nivel positivo\n")
    level = int(raw_input("Escribe el nivel\n"))
cont = 0
bool = False
arch=open("Puntuacion.txt","a") #CREACION DEL FICHERO
arch.close()
arch=open("Puntuacion.txt","r") #AUMENTA LA DIMENSION NECESARIA DE LA LISTA
listafich=arch.readlines()
while len(listafich)<lvl :
    listafich.append(str(0)+"\n")
arch.close()

while (level != 0): #LLEVA LA CUENTA DE LOS GOLPES AL CREAR EL NIVEL
    fila = random.randrange(10) + 2
    columna = random.randrange(10) + 2
    golpe(fila, columna)
    level -= 1


while completado(fil,col,bool) != True: #DENTRO DE ESTE WHILE SE ALMACENA EL MENU QUE VE EL USUARIO Y SUS OPCIONES
    print ("MENU DEL JUEGO\n----------------------------------------------------------\nOPCIONES: 1.'DESHACER'   2.'SALIR'   3.Introducir el golpe\n----------------------------------------------------------")
    impMat(z,fil,col)
    print
    print ("Numero de golpes hasta el momento = " + str(cont))
    print
    golpetazo = str(raw_input("Introduzca la letra de la fila junto con la de la columna. Ejemplo: G6, H7, B2\n"))
    bien=False
    if golpetazo[0] in z:
        bien=True
    while(len(golpetazo)!=2 and golpetazo!="DESHACER" and golpetazo!="SALIR"):
        golpetazo = str(raw_input("Golpe mal introducido. Ejemplo: G6, H7, B2\n"))
    while (bien==False and golpetazo!="DESHACER" and golpetazo!="SALIR"):
        golpetazo = str(raw_input("Golpe mal introducido. Ejemplo: G6, H7, B2\n"))
        if golpetazo[0] in z:
            bien=True
        if(len(golpetazo)!=2 and golpetazo!="DESHACER" and golpetazo!="SALIR"):
            bien=False
    if golpetazo == "DESHACER": #PRIMER IF: DESHACE EL GOLPE MEDIANTE UNA LISTA QUE ALMACENA LAS COORDENADAS DEL GOLPE ANTERIOR
        longd=len(d)
        if(contd-2>=0 and contd-1>=1 and longd-1>=1 and longd-2>=0):
            print ("Ha deshecho el movimiento(Se conserva el contador de movimientos)")
            fila = d[contd - 2] + 2
            columna = d[contd - 1] + 2
            contd -= 2
            golpe(fila, columna)
            d.pop(longd-1) #DESTRUYE EL ELEMENTO INDICADO DE LA LISTA DE GOLPES
            d.pop(longd-2)
        else:
            print("No se pueden deshacer mas golpes\n")
    elif golpetazo == "SALIR": #SEGUNDO IF : PONE LA MATRIZ A CERO PARA LLAMAR A LA FUNCION COMPLETADO Y QUE ASI SE ACABE EL JUEGO
        for i in range(2, fil + 2):
            for j in range(2, col + 2):
                matriz[i][j] = 0
        completado(fil,col,bool)
    else:                       #TERCER IF: JUEGO NORMAL DEL USUARIO
        ifil = z.index(golpetazo[0])
        icol = int(golpetazo[1])
        fila = ifil + 2
        columna = icol + 2
        d.append(ifil) #ALMACENA EN LA LISTA EL GOLPE INTRODUCIDO PARA UNA POSIBLE OPERACION DE DESHACER
        d.append(icol)
        contd += 2
        golpe(fila,columna)
        cont += 1
        if completado(fil,col,bool) == True:
            impMat(z,fil,col)
            print
            print ("Nivel " + str(lvl) + " completado.\n")
            print ("Numero de golpes empleados: " + str(cont) + "\n")
            puntuaciones(cont,listafich,lvl)
print ("Fin del juego")