#!/usr/bin/env python
# -*- coding: utf-8 -*-
# AGT
# Copyright 2019 Ariel H Garcia Traba <ariel.garcia.traba@gmail.com>
def limpiar():
    import os
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
print("""
############################################################################
##                                                                        ##
##      Unidad 1 -¿Qué es Python?                                         ##
##            * Instalación y configuración                               ##
##            * Errores sintácticos y lógicos                             ##
##            * Programación secuencial                                   ##
##            * Estructuras condicionales simples, compuestas y anidadas  ##
##            * Estructuras repetitivas                                   ##
##                                                                        ##
##      Unidad 2 - Variables, Listas                                      ##
##            * Tipos de variables                                        ##
##            * Procesamiento de cadenas                                  ##
##            * Listas                                                    ##
##            * Diccionarios                                              ##
##                                                                        ##
##      Unidad 3 - Funciones                                              ##
##            * Parámetros                                                ##
##            * Retorno de datos                                          ##
##            * Return de listas                                          ##
##            * Parámetros con valor por defecto                          ##
##                                                                        ##
##      Unidad 4 - Listas, Tuplas y Diccionarios                          ##
##         Listas                                                         ##
##            * Índices                                                   ##
##            * Recorrer listas                                           ##
##         Tuplas                                                         ##
##            * Índices                                                   ##
##            * Recorrer Tuplas                                           ##
##         Diccionarios                                                   ##
##            * Funcionamiento de diccionarios                            ##
##            * Estructuras tipo JSON                                     ##
##                                                                        ##
##         Unidad 5 - MySQL, Parte 1                                      ##
##            * INSERT, UPDATE, DELETE, SELECT                            ##
##            * FECHAS Y HORAS                                            ##
##            * %LIKE%                                                    ##
##            * JOIN                                                      ##
##                                                                        ##
##         Unidad 6 - MySQL, Parte 2                                      ##
##            * MySQL en Python                                           ##
##            * Cursor y verificación de consultas                        ##
##            * Manejo de errores                                         ##
##                                                                        ##
##         Unidad 7 - Fechas, Horas, Archivos                             ##
##            * Modulo time, datetime                                     ##
##            * Manejo de fechas y horas                                  ##
##            * Operaciones con archivos                                  ##
##                                                                        ##
##         Unidad 8 - OPEN CV                                             ##
##            * Procesamiento de imágenes en OpenCV                       ##
##            * Detección y descripción de imágenes                       ##
##            * Detección de objetos                                      ##
##                                                                        ##
##         Unidad 9 - Programación de eventos                             ##
##            * Módulo sched                                              ##
##            * Declaración de programadores                              ##
##            * Programar eventos y poner en marcha el programador        ##
##            * Programación de eventos considerando prioridades          ##
##            * Cancelación de eventos                                    ##
##                                                                        ##
##         Unidad 10 - GIT Colaborativo -Pair Programming                 ##
##            * Introducción a CVS y comparativa con SVN                  ##
##            * Creando un repositorio con GIT, clonar, crear branches    ##
##            * Borrar, guardar (stash), recuperar (pop)                  ##
##            * Configuración de remote                                   ##
##            * Configuración de Git avanzada                             ##
##                                                                        ##
############################################################################

https://unipython.com/numpy-algebra/""");
print("""
    ndarray.ndim –> Proporciona el número de dimensiones de nuestro array.
    ndarray.dtype –> Es un objeto que describe el tipo de elementos del array.
    ndarray.shape –> Devuelve la dimensión del array, es decir, una tupla de enteros indicando el tamaño del array en cada dimensión. Para una matriz de n filas y m columnas obtendremos (n,m).
    ndarray.data –> El buffer contiene los elementos actuales del array.
    ndarray.itemsize –> devuelve el tamaño del array en bytes.
    ndarray.size –> Es el número total de elementos del array.
    
    
		import numpy as np # Importamos numpy como el alias np
		miArray = np.arange(10) # Creamos un array de 0 a 9 separados de uno en uno
		print(type(miArray))
		numdim= miArray.ndim
		dim=miArray.shape
		tam= miArray.size
		byte=miArray.itemsize

 

    identity(n,dtype) –>Devuelve la matriz identidad, es decir, uma matriz cuadrada nula excepto en su diagonal principal que es unitaria. n es el número de filas (y columnas) que tendrá la matriz y dtype es el tipo de dato. Este argumento es opcional. Si no se establece, se toma por defecto como flotante.
    ones(shape,dtype) –>Crea un array de 1 compuesto de shape elementos.
    zeros(shape, dtype) –>Crea un array de 0 compuesto de “shape” elementos”.
    linspace(start,stop,num,endpoint=True,retstep=False) –>Crea un array con valor inicial start, valor final stop y num elementos.
    empty(shape, dtype) –>Crea un array de ceros compuesto de “shape” elementos” sin entradas.
    meshgrid(x,y) –>Genera una malla a partir de dos los arrays x, y.
    eye(N, M, k, dtype) –>Crea un array bidimensional con unos en la diagonal k y ceros en el resto. Es similar a identity. Todos los argumentos son opcionales. N es el número de filas, M el de columnas y k es el índice de la diagonal. Cuando k=0 nos referimos a la diagonal principal y por tanto eye es similar a identity.
    arange([start,]stop[,step,],dtype=None) –>Crea un array con valores distanciados step entre el valor inicial star y el valor final stop. Si no se establece step python establecerá uno por defecto.

		import numpy as np # Importamos numpy como el alias np
		g=np.zeros( (3,4) )
		print(g)
		k=np.linspace( 1, 4, 9 )
		print(k)
		X,Y=np.meshgrid([1,2,3],[7,9,34])
		print(X)
		print(Y)
    
 """);
print (input("ej         continuar?"));limpiar();


import numpy
 
a = numpy.array([[1, 2, 3], [4, 5, 6]])
b = numpy.array([[400], [800]])
print("antes\n",a)
print("antes\n",b)
c = a+b;
print("+\n",c)
c = a*b;
print("*\n",c)
newArray = numpy.append(a, b, axis = 1)
print("despues\n",newArray)
newArray = numpy.insert(a, 1, 90)
print("despues\n",newArray)
a = numpy.array([[1, 2, 3], [4, 5, 6]])
#-------------------------------
print (input("ej         continuar?"));limpiar();limpiar();
print("antes\n",a)
newArray = numpy.append(a, [[50, 60, 70]], axis = 0)
print("despues\n",newArray)
a = numpy.array([1, 2, 3])
newArray = numpy.delete(a, 1, axis = 0)
print("despues\n",newArray)
a = numpy.array([[1, 2, 3], [4, 5, 6], [10, 20, 30]])
print("antes\n",a)
newArray = numpy.delete(a, 1, axis = 0)
print("despues\n",newArray)
#-------------------------------
a = numpy.array([1, 2, 3, 4, 5])
print("original\n",a)
index = numpy.where(a == 5)
print("'5' se encuentra en index nº: ", index[0])
#-------------------------------
print (input("ej         continuar?"));limpiar();
limpiar();
a = numpy.array([1, 2, 3, 4, 5, 6, 7, 8])
print("original\n",a)
print("Seccion del array = ", a[2:5])
#-------------------------------
a = numpy.array([1, 2, 3, 4, 5, 6, 7, 8])
print("original\n",a)
print("Seccion del array = ", a[-3:])
#-------------------------------
addition = lambda x: x + 2
a = numpy.array([1, 2, 3, 4, 5, 6])
print("original\n",a)
print("Array desde funcion de suma: ", addition(a))
#-------------------------------
print (input("ej         continuar?"));limpiar();
a = numpy.array([1, 2, 3, 4, 5, 6])
print("The size of array = ", a.size)
l = [1, 2, 3, 4, 5]
a = numpy.array(l)
print("original\n",a)
print("genero un array NumPy desde una lista de Python  = ", a)
#-------------------------------
t = (1, 2, 3, 4, 5)
print("original\n",t)
a = numpy.array(t)
print("original\n",a)
print("genero un array NumPy desde una tuple de Python = ", a)
#-------------------------------
a = numpy.array([1, 2, 3, 4, 5])
print("original\n",a)
print("Array listado = ", a.tolist())
#-------------------------------
print (input("ej         continuar?"));limpiar();
a = numpy.array([1, 2, 3, 4, 5])
print("original\n",a)
numpy.savetxt("mi_Array.csv", a)#modificar el nombre del archivo
a = numpy.array([16, 3, 2, 6, 8, 10, 1])
print("Ordenar el array = ", numpy.sort(a))
#-------------------------------
x= numpy.array([400, 800, 200, 700, 1000, 2000, 300])
print("original\n",x)
xmax = x.max()
xmin = x.min()
x = (x - xmin)/(xmax - xmin)
print("Luego de la modificacion del array x = \n", x)
#-------------------------------
a = numpy.array([20, 13, 42, 86, 81, 9, 11])
print("original\n",a)
print("Element at index 3 = ", a[3])
print (input("ej         continuar?"));limpiar();
#-------------------------------
a = numpy.array([[20, 13, 42], [86, 81, 9]])
print("original\n",a)
print("Elementos en el index a[1][2] = ", a[1][2])
#-------------------------------
a = numpy.array([1, 2, 3, 4, 5])
print("original\n",a)
b = numpy.array([10, 20, 30, 40, 50])
print("original\n",b)
newArray = numpy.append(a, b)
print("Array modificado = ", newArray)
#-------------------------------
print (input("ej         continuar?"));limpiar();
g=numpy.matrix( [[3,4,-9], [7,4,-5] ,[1,3,9]] )
print(g)
b=numpy.matrix( [[-9], [-5] ,[9]] )
print(b)
c=g*b
print(c)
bt=b.T #traspuestas
print("\ntraspuestas\n",bt)
bh=b.H #traspuestas y conjudaga
print("\ntraspuestas y conjudaga\n",bh)
gi=g.I #inversa
print("\ninversa\n",gi)
detgi=numpy.linalg.det(gi) #calculo del determinante
print("\ndeterminante\n",detgi)
tragi=numpy.trace(gi) #calculo de la traza
print("\ntraza\n",tragi)
#-------------------------------
print (input("ej         continuar?"));limpiar();
a = numpy.array([[8, 1, 4]])
print("antes\n",a)
b= numpy.array([[3, 7, 4]])
print("antes\n",b)
c= numpy.cross(a, b) # Producto vectorial
print("\nProducto vectorial ",c)
d=numpy.outer(a, b) # Producto exterior
print("\nProducto exterior ",d)
#-------------------------------
print (input("ej         continuar?"));limpiar();
x=numpy.linspace(0,1,100)
y=numpy.sin(x)
print ("\nTransformada de Fourier:\n",numpy.fft.fft(y))
