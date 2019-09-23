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
print("##      Unidad 4 - Listas, Tuplas y Diccionarios                          ##");
print("##         Listas                                                         ##");
print("##            * Índices                                                   ##");
print("##            * Recorrer listas                                           ##");
print("##         Tuplas                                                         ##");
print("##            * Índices                                                   ##");
print("##            * Recorrer Tuplas                                           ##");
print("##         Diccionarios                                                   ##");
print("##            * Funcionamiento de diccionarios                            ##");
print("##            * Estructuras tipo JSON                                     ##");
print("##                                                                        ##");
print("############################################################################");
print("##                                                                        ##");
print("##                     Python tuples/Array Methods                        ##");
print("##                     ---------------------------                        ##");
print("##                                                                        ##");
print("##     Method    Description                                              ##");
print("##                                                                        ##");
print("##     count()   Returns the number of elements with the specified value  ##");
print("##                                                                        ##");
print("##     index()   Returns the index of the first element with the specified##");
print("##               value.Searches the tuple for a specified value and       ##");
print("##               returns the position of where it was found               ##");
print("##                                                                        ##");
print("############################################################################");
print("##                                                                        ##");
print("##                               Tuplas                                   ##");
print("##                                                                        ##");
print("############################################################################");
print("https://www.w3schools.com/python/python_ref_tuple.asp");
print("\nhttps://www.w3schools.com/python/python_tuples.asp");
print("#########################################################");
Nombre_tupla_1 = ["linea 1","linea 2","linea 3","linea 4","linea 5","linea 6","linea 7","linea 8","linea 9","linea 1"]
Nombre_lista_1 = (" ")
Nombre_tupla_2 = [" "]
# Ej 006_1
print("Inicio ej006_1 -  tupla a listas con tuple")
print ("valores tupla 1"+str(Nombre_tupla_1))
print ("valores lista 1"+str(Nombre_lista_1))
print ("paso los datos de mi tupla a mi lista")
Nombre_lista_1=tuple(Nombre_tupla_1)
print ("Nuevos valores lista 1"+str(Nombre_lista_1))
print (input("Fin ej006_1 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 006_2
print("Inicio ej006_2 -  lista a tuple con list")
print ("valores tupla 2"+str(Nombre_tupla_2))
print ("paso los datos de mi lista a mi tupla 2")
Nombre_tupla_2=list(Nombre_lista_1)
print ("Nuevos valores tupla 2"+str(Nombre_tupla_2))
print (input("Fin ej006_2 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 006_3
print("Inicio ej006_3 - posiciones") 
print (Nombre_tupla_1)
print ("posicion [1]  "+Nombre_tupla_1[1])
print ("posicion [5]  "+Nombre_tupla_1[5])
print ("posicion [7]  "+Nombre_tupla_1[7])
print ("posicion [0]  "+Nombre_tupla_1[0])
print ("posicion [9]  "+Nombre_tupla_1[9])
print (input("Fin ej006_3 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 006_4
print("Inicio ej006_4 - posiciones negativas") 
print (Nombre_tupla_1)
print ("posicion [-1]  "+Nombre_tupla_1[-1])
print ("posicion [-2]  "+Nombre_tupla_1[-2])
print ("posicion [-3]  "+Nombre_tupla_1[-9])
print (input("Fin ej006_4 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 006_5
print("Inicio ej006_5 - sectores o porsiones") 
print (Nombre_tupla_1)
print ("posicion [4 al 8]  "+str(Nombre_tupla_1[4:8]))
print ("posicion [0 al -2]  "+str(Nombre_tupla_1[0:-2]))
print ("posicion [-3 al 5]  "+str(Nombre_tupla_1[-3:5])+"error")
print (input("Fin ej006_5 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 006_6
print("Inicio ej006_6 - operadores varios") 
print (Nombre_tupla_1)
print ("cantidad de datos totales "+str(len(Nombre_tupla_1)))
print ("cantidad de datos 'ĺinea 1' es " +str(Nombre_tupla_1.count("linea 1")))
print (input("Fin ej006_6 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 006_7
print("Inicio ej006_7 - busco (si existe) un dato en la tupla")
print (Nombre_tupla_1)
print ("Busco si el dato 'linea 3' esta en mi tupla??")
print ("linea 3" in  Nombre_tupla_1)
print (input("Fin ej006_7 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 006_8
print("Inicio ej006_8 - busco (si existe) un dato en la tupla")
print ("Busco si el dato 'columna 3' esta en mi tupla??")
print ("viejo" in  Nombre_tupla_1)
print (input("Fin ej006_8 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 006_9
print("Inicio ej006_9 - Ubicar la posicion un dato en el index" )
print (Nombre_tupla_1)
print ("Ubicar la posicion de 'linea 3' en el index y es : ")
print (Nombre_tupla_1.index("linea 3"))
print (input("Fin ej006_9 \n		continuar?"));
limpiar();
"""
print("#########################################################");
# Ej 006_10
#print("Inicio ej006_10 ")
#print (input("Fin ej006_10 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 006_11
#print("Inicio ej006_11 ")
#print (input("Fin ej006_11 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 006_12
#print("Inicio ej006_12 ")
#print (input("Fin ej006_12 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 006_13
#print("Inicio ej006_13 ")
#print (input("Fin ej006_13 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 006_14
#print("Inicio ej006_14")
#print (input("Fin ej006_14"); print("")
"""
