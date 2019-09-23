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
#print("https://www.w3schools.in/python-tutorial/gui-programming/")
print("############################################################################");
print("##                                                                        ##");
print("##                       * Manejo de errores                              ##");
print("##                                                                        ##");
print("############################################################################");     
print("try:");
print("     cociente = dividendo / divisor");
print(" except:");
print('     print "No se permite la división por cero"');
print("#########################################################");
def limpiar():
    import os
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
# Ej 008_2
print("Inicio ej008_2");
try:
	maximo = int(input("ingrese la cantidad de numeros :"));
except:
	print ("ha ocurrio un Error. pero sigo von un valor = 10");
	maximo = 10
if maximo>0:
	def numeros_pares(maximo):
		contador = 1
		lista_de_pares=[]
		while contador<=maximo:
			lista_de_pares.append(contador*2);
			contador+=1
		return lista_de_pares
	print (numeros_pares(maximo));
print (input("Fin ej008_2 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 008_3
print("Inicio ej008_3 - ");
valor1=0,1
valor2=0,1
while True:
	try:
		valor1=float(input("valor 1 : "));
		valor2=float(input("valor 2 : "));
		break
	except ValueError:
		print("Error. solo nomeros");
def resultado_suma(valor_1,valor_2):
	return valor_1+valor_2
def resultado_resta(valor_1,valor_2):
	return  valor_1-valor_2
def resultado_multiplica(valor_1,valor_2):
	return valor_1*valor_2
def resultado_divide(valor_1,valor_2):
	
	try:
		return valor_1/valor_2
	except ZeroDivisionError:
		print ("No dividiras por 0");
		return ("error...... pero sigo");

import math
def resultado_suma(valor_1,valor_2):
	return valor_1+valor_2
def resultado_resta(valor_1,valor_2):
	return  valor_1-valor_2
def resultado_multiplica(valor_1,valor_2):
	return valor_1*valor_2
def resultado_divide(valor_1,valor_2):
	try:
		return valor_1/valor_2
	except ZeroDivisionError:
		print ("No dividiras por 0");
		return ("error...... pero sigo");
def resultado_portenciacion(valor_1,valor_2):
	return valor_1**valor_2
def resultado_radicacion2(valor_1,valor_2):
	return  math.sqrt(valor_2);
def resultado_porcentage(valor_1,valor_2):
	return valor_1/valor_2*100
def resultado_cociente(valor_1,valor_2):
	return valor_1//valor_2
def resultado_resto(valor_1,valor_2):
	return valor_1%valor_2

print ("resultado suma : "+str(resultado_suma(valor1,valor2)));
print ("resultado resta : "+str(resultado_resta(valor1,valor2)));
print ("resultado multiplicacion : "+str(resultado_multiplica(valor1,valor2)));
print ("resultado divicion : "+str(resultado_divide(valor1,valor2)));
print ("resultado portenciacion : "+str(resultado_portenciacion(valor1,valor2)));
print ("resultado radicacion2 : "+str(resultado_radicacion2(valor1,valor2)));
print ("resultado porcentage : "+str(resultado_porcentage(valor1,valor2)));
print ("resultado cociente : "+str(resultado_cociente(valor1,valor2)));
print ("resultado resto : "+str(resultado_resto(valor1,valor2)));
print (input("Fin ej008_3 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 008_4
print("Inicio ej008_4 - manejo errores");
from AGT_Ej_009_Metodo import *
valor1=0,1
valor2=0,1
while True:
	try:
		valor1=float(input("valor 1 : "));
		valor2=float(input("valor 2 : "));
		break
	except ValueError:
		print("Error. solo nomeros");
print ("resultado suma : "+str(resultado_suma_metodo(valor1,valor2)));
print ("resultado resta : "+str(resultado_resta_metodo(valor1,valor2)));
print ("resultado multiplicacion : "+str(resultado_multiplica_metodo(valor1,valor2)));
print ("resultado divicion : "+str(resultado_divide_metodo(valor1,valor2)));
print ("resultado portenciacion : "+str(resultado_portenciacion_metodo(valor1,valor2)));
print ("resultado radicacion2 : "+str(resultado_radicacion2_metodo(valor1,valor2)));
print ("resultado porcentage : "+str(resultado_porcentage_metodo(valor1,valor2)));
print ("resultado cociente : "+str(resultado_cociente_metodo(valor1,valor2)));
print ("resultado resto : "+str(resultado_resto_metodo(valor1,valor2)));
print (input("Fin ej008_4 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 008_5
print("Inicio ej008_5- manejo errores");

variable = "variable original"
def variable_global():
	print ("INGERSO A LA FUNCION")
	global variable1
	variable = "variable global modificada desde dentro de una funcion"

print ("variable original: ",end=(""))
print (variable)
variable_global()
print ("variable global modificada: ",end=(""))
print (variable)
print (input("Fin ej008_5 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 008_6
print("Inicio ej008_6 - manejo derrores");
try:
	x = 10
	y = 0
	print(x/y)
except Exception as e:
	print("Exeception occured:{}".format(e))
finally:
	x = 10
	y = 2
	print(x/y)
print ("continuo")
print ("continuo")
print ("continuo")

print (input("Fin ej008_6 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 008_7
print("Inicio ej008_7 - manejo derrores");
#try:
    # aquí ponemos el código que puede lanzar excepciones
#except:
    # ERROR de sintaxis, esta sentencia no puede estar aquí,
    # sino que debería estar luego del except IOError.
#except IOError:
    # Manejo de la excepción de entrada/salida
print (input("Fin ej008_7 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 008_8
print("Inicio ej008_8 - manejo derrores");
#try:
#    archivo = open("miarchivo.txt")
    # procesar el archivo
#except IOError:
#    print "Error de entrada/salida."
    # realizar procesamiento adicional
#except:
    # procesar la excepción
#finally:
    # si el archivo no está cerrado hay que cerrarlo
#    if not(archivo.closed):
#        archivo.close()
print (input("Fin ej008_8 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 008_9
#print("Inicio ej008_9 - manejo derrores");
lista = [10, 100, 1000, 10000]
iterador = iter(lista)
try:
    while True:
        print(iterador.__next__())        
except StopIteration:
    print("Se ha alcanzado el final de la lista")
