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
print("##         Unidad 7 - Fechas, Horas, Archivos                             ##");
print("##            * Modulo time, datetime                                     ##");
print("##            * Manejo de fechas y horas                                  ##");
print("##            * Operaciones con archivos                                  ##");
print("##                                                                        ##");
print("############################################################################");     
print("##                                                                        ##");
print("##                                archivar                                ##")
print("##                                                                        ##");
print("############################################################################");
# Ej 009_4
print("Inicio ej 009_4 - manejo desde un archivo separado")

from Python_Metodos_propia import *
valor1=0.1
valor2=0.1
while True:
	try:
		valor1=float(input("valor 1 : "))
		valor2=float(input("valor 2 : "))
		break
	except ValueError:
		print("Error. solo nomeros")
print ("resultado suma : "+str(resultado_suma_metodo(valor1,valor2)))
print ("resultado resta : "+str(resultado_resta_metodo(valor1,valor2)))
print ("resultado multiplicacion : "+str(resultado_multiplica_metodo(valor1,valor2)))
print ("resultado divicion : "+str(resultado_divide_metodo(valor1,valor2)))
print ("resultado portenciacion : "+str(resultado_portenciacion_metodo(valor1,valor2)))
print ("resultado radicacion2 : "+str(resultado_radicacion2_metodo(valor1,valor2)))
print ("resultado porcentage : "+str(resultado_porcentage_metodo(valor1,valor2)))
print ("resultado cociente : "+str(resultado_cociente_metodo(valor1,valor2)))
print ("resultado resto : "+str(resultado_resto_metodo(valor1,valor2)))
print (input("ej 009-1        continuar?"));
from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)
def iniciar_pantalla_raiz():
	iniciar_pantalla_raiz=Tk()#                                Define la ventana principal de la aplicación
	iniciar_pantalla_raiz.title("Mi primer pantalla")#         ancho   x alto
	iniciar_pantalla_raiz.geometry("640x480")#                 Define las dimensiones de la ventana, que se ubicará en el centro de la pantalla. Si se omite esta línea la # ventana se adaptará a los widgets que se coloquen en ella. 
	iniciar_pantalla_raiz.configure(bg = "white")#				 Asigna un color de fondo a la ventana.
	#ttk.Button(iniciar_pantalla_raiz, text='Exit', command=quit).pack(side=BOTTOM)
	#iniciar_pantalla_raiz.iconbitmap("icono.png")
	#frame1_iniciar_pantalla_raiz(iniciar_pantalla_raiz)

	# Define un botón en la parte inferior de la ventana que cuando sea presionado hará que termine el programa.
	# El primer parámetro indica el nombre de la ventana 'iniciar_pantalla_raiz' donde se ubicará el botón

	iniciar_pantalla_raiz.title('Aplicación')
	etiqueta_pantalla_raiz = Label(iniciar_pantalla_raiz,bg = "white", text="resultado suma : "+str(resultado_suma_metodo(valor1,valor2)))
	etiqueta_pantalla_raiz.pack()
	etiqueta_pantalla_raiz = Label(iniciar_pantalla_raiz,bg = "white", text="resultado suma : "+str(resultado_suma_metodo(valor1,valor2)))
	etiqueta_pantalla_raiz.pack()
	etiqueta_pantalla_raiz = Label(iniciar_pantalla_raiz,bg = "white", text="resultado resta : "+str(resultado_resta_metodo(valor1,valor2)))
	etiqueta_pantalla_raiz.pack()
	etiqueta_pantalla_raiz = Label(iniciar_pantalla_raiz,bg = "white", text="resultado multiplicacion : "+str(resultado_multiplica_metodo(valor1,valor2)))
	etiqueta_pantalla_raiz.pack()
	etiqueta_pantalla_raiz = Label(iniciar_pantalla_raiz,bg = "white", text="resultado divicion : "+str(resultado_divide_metodo(valor1,valor2)))
	etiqueta_pantalla_raiz.pack()
	etiqueta_pantalla_raiz = Label(iniciar_pantalla_raiz,bg = "white", text="resultado portenciacion : "+str(resultado_portenciacion_metodo(valor1,valor2)))
	etiqueta_pantalla_raiz.pack()
	etiqueta_pantalla_raiz = Label(iniciar_pantalla_raiz,bg = "white", text="resultado radicacion2 : "+str(resultado_radicacion2_metodo(valor1,valor2)))
	etiqueta_pantalla_raiz.pack()
	etiqueta_pantalla_raiz = Label(iniciar_pantalla_raiz,bg = "white", text="resultado porcentage : "+str(resultado_porcentage_metodo(valor1,valor2)))
	etiqueta_pantalla_raiz.pack()
	etiqueta_pantalla_raiz = Label(iniciar_pantalla_raiz,bg = "white", text="resultado cociente : "+str(resultado_cociente_metodo(valor1,valor2)))
	etiqueta_pantalla_raiz.pack()
	etiqueta_pantalla_raiz = Label(iniciar_pantalla_raiz,bg = "white", text="resultado resto : "+str(resultado_resto_metodo(valor1,valor2)))
	etiqueta_pantalla_raiz.pack()

	img = PhotoImage(file="brazo_robotico.png")
	widget = Label(iniciar_pantalla_raiz, image=img).pack()

	# Define un botón en la parte inferior de la frame_iniciar_pantalla_raiz
	# que cuando sea presionado hará que termine el programa.
	# El primer parámetro indica el nombre de la frame_iniciar_pantalla_raiz 'raiz'
	# donde se ubicará el botón
	ttk.Button(iniciar_pantalla_raiz, text='Salir', command=iniciar_pantalla_raiz.destroy).pack(side=BOTTOM)
	#ttk.Button(iniciar_pantalla_raiz, text='terminar programa', command=quit).pack(side=BOTTOM)

	# Después de definir la frame_iniciar_pantalla_raiz principal y un widget botón
	# la siguiente línea hará que cuando se ejecute el programa
	# construya y muestre la frame_iniciar_pantalla_raiz, quedando a la espera de 
	# que alguna persona interactúe con ella.

	# Si la persona presiona sobre el botón Cerrar 'X', o bien,
	# sobre el botón 'Salir' el programa llegará a su fin.



	iniciar_pantalla_raiz.mainloop()

iniciar_pantalla_raiz();
