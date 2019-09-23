#!/usr/bin/env python
# -*- coding: utf-8 -*-
# AGT
# Copyright 2019 Ariel H Garcia Traba <cursos.arT@gmail.com>
def limpiar():
    import os
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
"""
╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗                                                                      ░ ▒ ▓ ┌┐┤│├└┘┴┬─┼╔╗╠╬╣║╚╝╩╦═¤
║TEMARIO:                                                                                                                ║
║--------                                                                                                                ║
║Unidad 1 - Introducción                                                                                                 ║
║● ¿Qué es Python?                                                                                                       ║
║● Ventajas y desventajas                                                                                                ║
║● Ecosistema Python y Comunidad –Librerías extendidas                                                                   ║
║● Descarga –Opensource                                                                                                  ║
║● Instalación, configuración y hardware necesario                                                                       ║
║● Errores sintácticos y lógicos, localización en pantalla y correcciones                                                ║
║● Importancia del versionado                                                                                            ║
║● GIT Colaborativo –Pair Programming                                                                                    ║
║	o Introducción a GIT                                                                                                 ║
║	o Creando un repositorio, clonar, branches                                                                           ║
║	oBorrar, guardar (STASH), requperar (POP)                                                                            ║
╠════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
║Unidad 2 – Software                                                                                                     ║
║Características de Python                                                                                               ║
║● Software libre                                                                                                        ║
║● Alto nivel                                                                                                            ║
║● Multiparadigma                                                                                                        ║
║● Portable                                                                                                              ║
║● Programación Secuencial y Orientada a Objetos                                                                         ║
║● Multiplataforma                                                                                                       ║
║● Interpretado                                                                                                          ║
║● Tipado dinámico                                                                                                       ║
║● Estructura (TAB)                                                                                                      ║
║                                                                                                                        ║
║Entorno de Desarrollo Intérprete – IDEs                                                                                 ║
║● Elección según el propósito del trabajo:                                                                              ║
║	PyCharm, PyDev, Atom, Spyder, PyScripter, Eclipse, IPython.                                                          ║
║● Entornos especiales: Anaconda (Data Science Platform),  Jupyter (Notebooks).                                          ║
║● Consola, pantalla gráfica y entorno                                                                                   ║
║● Salida de datos por pantalla                                                                                          ║
║	o Sentencias: print ()                                                                                               ║
║● Ingreso de datos por teclado                                                                                          ║
║● Sentencias: input ()                                                                                                  ║
╠════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
║Unidad 3 - Estructura y primeros Trabajos con datos                                                                     ║
║Variables, Constantes                                                                                                   ║
║● Flujo de datos, estructura, linealidad, condicionales, bucles                                                         ║
║● Estructuras condicionales simples, compuestas y anidadas                                                              ║
║● Sentencias: If , elif, else, :                                                                                        ║
║● Estructuras repetitivas                                                                                               ║
║● Sentencias:  for, range, while, else :                                                                                ║
║● Estructuras modificaciones                                                                                            ║
║● Sentencias:  break, continue, pass                                                                                    ║
║● Operadores:                                                                                                           ║
║● Comparación: ==, <, <=, >, >=, !=                                                                                     ║
║● Lógicos:  and, not, or                                                                                                ║
║● Aritméticos: +,-*, **, /, //, %, (ver librería math)                                                                  ║
║● Asignación: =, += , - = , *=  , ** , /= , //= , %=                                                                    ║
║● Especiales: is, is not,  in, not in                                                                                   ║
║Espacios, nombres, ámbitos, objetos                                                                                     ║
║● Variables y constantes - Tipos                                                                                        ║
║● Procesamiento de cadenas                                                                                              ║
║Listas [variables]                                                                                                      ║
║● Índices                                                                                                               ║
║● Recorrer listas                                                                                                       ║
║● Sentencias:  append(),  clear(), copy(), count(), extend(), index(), insert(), pop(), remove(), reverse(), sort(), etc║
║Tuplas (Constantes)                                                                                                     ║
║● Índices                                                                                                               ║
║● Recorrer Tuplas                                                                                                       ║
║● Sentencias:  index(), count(), etc.                                                                                   ║
║Diccionarios {clave:valor asociado}                                                                                     ║
║● Funcionamiento de diccionarios                                                                                        ║
║● Sentencias:  clear(), copy(), fromkeys(), get(), items(), keys(), pop(),                                              ║
║● popitem(), reverse(), setdefault(), update(), values(), etc.                                                          ║
║● Sets y otros                                                                                                          ║
╠════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
║Unidad 4 – Funciones                                                                                                    ║
║● Iterar: ejecución repetida de un conjunto de sentencias                                                               ║
║Sentencias:  def (): return                                                                                             ║
║● Parámetros de entrada de datos                                                                                        ║
║● Retorno de datos a la salida                                                                                          ║
║● Return de listas                                                                                                      ║
║● Parámetros con valor por defecto (=val;*;**)                                                                          ║
╠════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
║Unidad 5 – Módulos y Librerías                                                                                          ║
║● Uso de métodos y funciones de un archivo externo Sentencias: Import, from                                             ║
║● Generar un modulo                                                                                                     ║
║● Uso de librerías                                                                                                      ║
║● Generar archivos, leerlos, escribirlos (TXT - plano/ Binario) JSON (Javascript) Pickle (Python)                       ║
║● Instalación de librerías, ecosistema,                                                                                 ║
║Métodos: pip, conda,                                                                                                    ║
║Download e instalación MSI, Linuc, etc                                                                                  ║
╠════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
║Unidad 6 – Clases Sistema para empaquetar atributos de datos y funcionalidad métodos para instanciar                    ║
║Sentencias: class ():, self                                                                                             ║
║● Objetos clases                                                                                                        ║
║● Objetos instancias                                                                                                    ║
║● Objetos métodos                                                                                                       ║
║● Herencias, herencias múltiples                                                                                        ║
╠════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
║Unidad 7 – Entorno visual - WEB Django Pantallas graficas - Libreria: tkinter, numpy y matplotli                        ║
║● Pantallas, Frames, Labels, bottons,etc                                                                                ║
║● Ubicación de elementos, colores, formatos, tamaños, etc.                                                              ║
║● Ingreso de daros desde pantalla (get)                                                                                 ║
║● Salida de datos por pantalla                                                                                          ║
║● Acciones de botones para llamar a funciones                                                                           ║
║● Graficas de funciones matematicas y otros datos.( series, tortas, 3d, etc.)                                           ║
║● Python y “Django” e la web framework                                                                                  ║
║Ejemplos de uso intensivo de Django (Instagram, Pinterest, Mozilla, National Geografic, etc.)                           ║
╠════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
║Unidad 8 – Bases de Datos locales y en la nube                                                                          ║
║Tipo: SQL (Mysql) y NoSQL (Mongo)                                                                                       ║
║Librería: mysql.connector                                                                                               ║
║Librería: pymongo                                                                                                       ║
║● Python y “Big Data”                                                                                                   ║
║● Conexión                                                                                                              ║
║● cursor(), .execute(), .close                                                                                          ║
║● Crear Bases, tablas, columnas                                                                                         ║
║● Tipos de datos, caracteres, numéricos, fecha - hora                                                                   ║
║● Buscar, insertar, actualizar, borrar, seleccionar, elementos desde y hacia una base de datos                          ║
║● Where, from. %like%                                                                                                   ║
║● Firebase, Google Cloud IoT -u otro hub para OIT AWS (Amazon) Azure (MSoft)                                            ║
╠════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
║Unidad 9 – Fechas, Horas                                                                                                ║
║● Modulo time, datetime                                                                                                 ║
║● Manejo de fechas y horas                                                                                              ║
║● Uso en aplicaciones web, base de datos, multiplataforma, etc.                                                         ║
╠════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
║Unidad 10 – Internet Of Things – IOT                                                                                    ║
║● Programación de eventos - Timed Event                                                                                 ║
║Librería:                                                                                                               ║
║Scheduler                                                                                                               ║
║● Módulo sched / Scheduler                                                                                              ║
║● Declaración de programadores                                                                                          ║
║● Llamado a funciones como eventos                                                                                      ║
║● Programar eventos y poner en marcha el programador                                                                    ║
║● Programación de eventos considerando prioridades                                                                      ║
║● Cancelación de eventos                                                                                                ║
║● Python y Internet Of Things – IOT                                                                                     ║
║● Python y MicroControladores (un matrimonio perfecto)                                                                  ║
║	Librería:	Zerynth                                                                                                  ║
║	Ejemplos de uso intensivo de Raspberry Pi y NodeMCU (ESP8266)                                                        ║
║IOT Con BBDD, Python y Android                                                                                          ║
║● Python y Amazon - AWS IoT                                                                                             ║
║● Protocolo MQTT                                                                                                        ║
╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
"""
print("############################################################################");
print("##                                                                        ##");
print("##      Unidad 3 - Funciones                                              ##");
print("##            * Parámetros                                                ##");
print("##            * Retorno de datos                                          ##");
print("##            * Return de listas                                          ##");
print("##            * Parámetros con valor por defecto                          ##");
print("##                                                                        ##");
print("############################################################################");
print("##                                                                        ##");
print("##                         Funciones y Metodos                            ##");
print("##                         -------------------                            ##");
print("##                                                                        ##");
print("##     Funciones    Description                                           ##");
print("##              lambda                                                    ##");
print("##                                                                        ##");
print("##                                                                        ##");
print("##     Metodos son finciones dentro de clases donde se deberia instanciar ##");
print("##              a la clase con self                                       ##");
print("##                                                                        ##");
print("############################################################################");
print("##                                                                        ##");
print("##                         Funciones,  Metodos                            ##");
print("##                                                                        ##");
print("##                             y Generadores                              ##");
print("##                                                                        ##");
print("############################################################################");
def limpiar():
    import os
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
#print(input("continuar?"));
print("https://www.w3schools.com/python/python_ref_list.asp");
print("\nhttps://www.w3schools.com/python/python_lists.asp");
print("https://python-para-impacientes.blogspot.com/2014/02/programacion-funcional-funciones-de.html")
print("https://python-para-impacientes.blogspot.com/2014/02/funciones.html")
print("Inicio ej 002_3_1 ");
print("############################################################################");
print("##                                                                        ##");
print("##                         Funciones,  Metodos                            ##");
print("##                                                                        ##");
print("############################################################################");


#                          como funcion
def funcion (var_1, var_2):
	return (var_1 *var_2)
print (funcion (2,4))
mi_array=(3,6)
print (funcion (*mi_array))# ver el "*"
#                          como Metodo
class Clase1:# ver el nombre con mayuscula en su primer caracter que no debe ser numerico
	resultado= 0
	def metodo(self,var_1,var_2):
		self.var_1=  var_1
		self.var_2=  var_2
		self.resultado= (var_1 *var_2)
ej=Clase1()
ej.metodo(6,5)
print (ej.resultado)



print (input("Fin ej 002_3_1 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 002_3_2
print("Inicio ej 002_3_2 ");
print("############################################################################");
print("##                                                                        ##");
print("##                                Metodos                                 ##");
print("##                                                                        ##");
print("############################################################################");
class Clase2:# ver el nombre con mayuscula en su primer caracter que no debe ser numerico
	resultado= 0
	def __init__(self):#construye los objetos
		self.var_1=  0
		self.var_2=  0
	def metodo(self,var_1,var_2):
		self.var_1=  var_1
		self.var_2=  var_2
		self.resultado= (var_1 *var_2)

ej=Clase2()
print ("al inicio con valores 'self'",ej.resultado)
ej.metodo(6,5)
print ("al finalcon datos modificado por metodo",ej.resultado)
print (input("Fin ej 002_3_2 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 002_3_3
print("Inicio ej 002_3_3 ");
print("############################################################################");
print("##                                                                        ##");
print("##                             y Generadores                              ##");
print("##                                                                        ##");
print("############################################################################");
def Llenar_lista():
	salida=0
	dato_entrada = [1,2,3,4,5,6,7,8,9]
	for elementos in dato_entrada:
		salida+= int(elementos)**2
		print (elementos)
	print (salida)
Llenar_lista()
salida2=0
generada = (elementos for elementos in range(10))
for elementos in generada:
	salida2 += int(elementos)**2
	print (elementos)
print (salida2)

generada2 = (elementos for elementos in range(10) if elementos%20 == 0)
for elementos in generada2:
	salida2 += int(elementos)**2
	print (elementos)
print (salida2)

generada2 = (min(elementos,5) for elementos in range(10))
for elementos in generada2:
	salida2 += int(elementos)**2
	print (elementos)
print (salida2)

print (input("Fin ej 002_3_2 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 002_3_3
print("Inicio ej 002_3_3 ");
print("############################################################################");
print("##                                                                        ##");
print("##                                  Lambda                                ##");
print("##                                                                        ##");
print("############################################################################");

area_triangulo =lambda base,altura:(base*altura)/2
base = float(input("Ingrese la base :"))
altura = float(input("Ingrese la altura :"))
print(area_triangulo(base,altura))
print (input("Fin ej 002_3_3 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 002_3_4
print("Inicio ej 002_3_4 ");

class Counter:
	Count = 0   # This represents the count of objects of this class
	def __init__(self, name):
		self.name = name
		print (name, 'created')
		Counter.Count += 1
	def __del__(self):
		print (self.name, 'deleted')
		Counter.Count -= 1
		if Counter.Count == 0:
			print ('Last Counter object deleted')
		else:
			print (Counter.Count, 'Counter objects remaining')
x = Counter("First")
y = Counter("second")
del x

"""
Without the final del, you get an exception. Shouldn’t the normal cleanup process take care of this?

From the Python docs regarding __del__:

    Warning: Due to the precarious circumstances under which __del__() methods are invoked, exceptions that occur during their execution are ignored, and a warning is printed to sys.stderr instead. Also, when __del__() is invoked in response to a module being deleted (e.g., when execution of the program is done), other globals referenced by the __del__() method may already have been deleted. For this reason, __del__() methods should do the absolute minimum needed to maintain external invariants.

Without the explicit call to del, __del__ is only called at the end of the program, Counter and/or Count may have already been GC-ed by the time __del__ is called (the order in which objects are collected is not deterministic). The exception means that Counter has already been collectd. You can’t do anything particularly fancy with __del__.

There are two possible solutions here.

    1. Use an explicit finalizer method, such as close() for file objects.

        Use weak references.
"""










