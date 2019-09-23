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
print("Inicio ej015_1 -  ");
import mysql.connector
import json
print("#########################################################");
#print ("C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>python -m pip install mysql-connector");
print("https://www.w3schools.com/python/python_mysql_create_db.asp");
print("http://infocenter.sybase.com/help/index.jsp?topic=/com.sybase.infocenter.dc36272.1550/html/commands/X72692.htm")
print("############################################################################");
print("##                                                                        ##");
print("##         Unidad 5 - MySQL, Parte 1                                      ##");
print("##            * INSERT, UPDATE, DELETE, SELECT                            ##");
print("##            * FECHAS Y HORAS                                            ##");
print("##            * %LIKE%                                                    ##");
print("##            * JOIN                                                      ##");
print("##                                                                        ##");
print("##         Unidad 6 - MySQL, Parte 2                                      ##");
print("##            * MySQL en Python                                           ##");
print("##            * Cursor y verificación de consultas                        ##");
print("##                                                                        ##");
print("############################################################################");
print("##                                                                        ##");
print("##                     libreria mysql.connector                           ##");
print("##                                                                        ##");
print("############################################################################");
print("Inicio ej015_1 -  ");
import mysql.connector
print("#########################################################");
print("https://www.w3schools.com/python/python_mysql_create_db.asp")


def crear_base(nombre_base_MySQL):
	print ("Conectamos con MySQL")
	conectarse = mysql.connector.connect(host="localhost",user="root", passwd="mysql2019")#database='AGT',
	puntero = conectarse.cursor()
	puntero.execute("CREATE DATABASE "+str(nombre_base_MySQL))
	print ("Creamos la base de datos "+str(nombre_base_MySQL))
	print ("cerramos coneccion")
	puntero.close
def listar_bases():
	print ("Conectamos con MySQL")
	conectarse = mysql.connector.connect(host="localhost",user="root", passwd="mysql2019")
	puntero = conectarse.cursor()
	puntero.execute("SHOW DATABASES")
	lista_de_bases=[]
	print ("cargamos el listado de nombres de bases")
	for lista_bases in (puntero):
		lista_nombres_bases=str(lista_bases)
		lista_nombres_bases_largo=len(lista_bases)-4
		lista_nombres_bases=lista_nombres_bases[2:lista_nombres_bases_largo]
		print ("*"+lista_nombres_bases+"*")
		lista_de_bases.append(lista_nombres_bases);
	print (lista_de_bases)
	print ("cerramos coneccion")
	puntero.close
	return (lista_de_bases)

def chequear_base_existe(nombre_base_MySQL_input):
	print ("Conectamos con MySQL")
	conectarse = mysql.connector.connect(host="localhost",user="root", passwd="mysql2019")
	puntero = conectarse.cursor()
	puntero.execute("SHOW DATABASES")
	lista_de_bases=[]
	print ("cargamos el listado de nombres de bases")
	for lista_bases in (puntero):
		nombre_base_MySQL_para_chequear=str(lista_bases)
		nombre_largo=len(lista_bases)-4
		nombre_base_MySQL_para_chequear=nombre_base_MySQL_para_chequear[2:nombre_largo]
		lista_de_bases.append(nombre_base_MySQL_para_chequear);
	puntero.close
	print ("cerramos coneccion")
	print (lista_de_bases)
	lista_bases_2=json.loads(lista_bases);
	lista_de_bases_2.append(lista_bases_2);
	print(lista_de_bases);
	print(lista_de_bases_2);
	base_nueva=False
	while base_nueva==False:
		for nombre_base_MySQL in (lista_de_bases):
			if nombre_base_MySQL_input == nombre_base_MySQL:
				nombre_base_MySQL_input= input("Ingrese un nuevo nombre de la base de datos MySQL "+str(nombre_base_MySQL_input)+" ya existe :")
				break
			else:
				if len(nombre_base_MySQL) == len(lista_de_bases):
					print (f"Genial '{nombre_base_MySQL_input}' no existe. pasamos a crear la base de datos en MySQL")
					base_nueva=True
	return (nombre_base_MySQL_input)
	
def listar_tablas(nombre_base_MySQL_input):
	print ("Conectamos con MySQL")
	print (nombre_base_MySQL_input)
	conectarse = mysql.connector.connect(host="localhost",user="root", passwd="mysql2019", database=nombre_base_MySQL_input,)
	puntero = conectarse.cursor()
	puntero.execute("SHOW TABLES")
	lista_de_tablas=[]
	print ("cargamos el listado de tabla de la base"+str(nombre_base_MySQL_input))
	for lista_tablas in (puntero):
		print(lista_tablas)
		lista_nombres_tablas=str(lista_tablas)
		print ("*"+str(lista_nombres_tablas)+"*")
		lista_de_tablas.append(lista_nombres_tablas);
	puntero.close
	return (lista_de_tablas)

def borrar_base(nombre_base_MySQL_input):
	limpiar()
	listar_bases()
	print ("Conectamos con MySQL")
	conectarse = mysql.connector.connect(host="localhost",user="root", passwd="mysql2019")
	puntero = conectarse.cursor()
	puntero.execute("DROP DATABASE "+str(nombre_base_MySQL_input))
	puntero.close

limpiar()
while True:
	print ("\n\n\n");	
	print ("L) listar Base");
	print ("C) Crear Base");
	print ("A) Abrir Base");
	print ("B) Borrar Base");	
	print ("Z) Salir del programa")
	opcion= input("Opcion : ")
	opcion=opcion.upper()
	if opcion =="C":
		limpiar()
		nombre_base_MySQL= input("Ingrese el nombre de la base de datos a CREAR : ")
		crear_base(nombre_base_MySQL)
	elif opcion =="L":
		limpiar()
		listar_bases()
	elif opcion =="A":
		limpiar()
		nombre_base_MySQL= input("Ingrese el nombre de la base de datos a ABRIR : ")
		listar_tablas(nombre_base_MySQL)
	elif opcion =="B":
		limpiar()
		nombre_base_MySQL= input("Ingrese el nombre de la base de datos a BORRAR : ")
		borrar_base(nombre_base_MySQL)
	elif opcion =="Z":
		limpiar()
		break
		
		

"""

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x) 
#print(f"Hola {nombre_base_MySQL} se que tenes {edad} años.")

#func_crear(nuevo_nombre_base_MySQL)
"""
"""
def check_base_existe(nombre_base_MySQL_input):
	print ("Conectamos con MySQL")
	conectarse = mysql.connector.connect(host="localhost",user="root", passwd="mysql2019")
	puntero = conectarse.cursor()
	puntero.execute("SHOW DATABASES")
	lista_de_bases=[]
	
	print ("cargamos el listado de nombres de bases")
	for lista_bases in (puntero):
		nombre_base_MySQL_para_chequear=str(lista_bases)
		nombre_largo=len(lista_bases)-4
		nombre_base_MySQL_para_chequear=nombre_base_MySQL_para_chequear[2:nombre_largo]
#		print ("*"+nombre_base_MySQL_para_chequear+"*", "*"+nombre_base_MySQL_input+"*")
		lista_de_bases.append(nombre_base_MySQL_para_chequear);
	puntero.close
	print ("cerramos coneccion")
	print (lista_de_bases)
	c=0
	base_nueva=False
	while base_nueva==False:
		input("while"+str(base_nueva))
		c +=1
		print (c)
		for nombre_base_MySQL in (lista_de_bases):
			if nombre_base_MySQL_input == nombre_base_MySQL:
				print ("*"+nombre_base_MySQL_input+"*", "*"+nombre_base_MySQL+"*         ==")
				input("=="+str(base_nueva))
				nombre_base_MySQL_input= input("Ingrese un nuevo nombre de la base de datos MySQL "+str(nombre_base_MySQL_input)+" ya existe :")
				break
			else:
				if len(nombre_base_MySQL) == len(lista_de_bases):
					print (f"Genial '{nombre_base_MySQL_input}' no existe. pasamos a crear la base de datos en MySQL")
					base_nueva=True
				else:
					print ("*"+nombre_base_MySQL_input+"*", "*"+nombre_base_MySQL+"*         =/=")
					input("=/="+str(base_nueva))
		input("Fin"+str(base_nueva))
	print (lista_de_bases)
	print (nombre_base_MySQL_input)
	return (nombre_base_MySQL_input)
nombre_base_MySQL= "mysql"#input("Ingrese el nombre de la base de datos MySQL : ")
print(check_base_existe(nombre_base_MySQL))
"""
