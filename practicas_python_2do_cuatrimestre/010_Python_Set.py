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
print("##                      Python Set /Array Methods                         ##");
print("##                     ---------------------------                        ##");
print("##                                                                        ##");
print("##     Method    Description                                              ##");
print("##                                                                        ##");
print("##     add()     Adds an element to the set                               ##");
print("##     clear()   Removes all the elements from the set                    ##");
print("##     copy()    Returns a copy of the set                                ##");
print("##     difference()	Returns a set containing the difference between two  ##");
print("##               or more sets                                             ##");
print("##     difference_update()	Removes the items in this set that are also  ##");
print("##                included in another, specified set                      ##");
print("##     discard()	Remove the specified item                                ##");
print("##     intersection()	Returns a set, that is the intersection of two   ##");
print("##                other sets                                              ##");
print("##     intersection_update()	Removes the items in this set that are not   ##");
print("##               present in other, specified set(s)                       ##");
print("##     isdisjoint()	Returns whether two sets have a intersection or      ##");
print("##                not                                                     ##");
print("##     issubset()	Returns whether another set contains this set or     ##");
print("##                not                                                     ##");
print("##     issuperset()	Returns whether this set contains another set or     ##");
print("##                not                                                     ##");
print("##     pop()	Removes an element from the set                              ##");
print("##     remove()	Removes the specified element                            ##");
print("##     symmetric_difference()	Returns a set with the symmetric         ##");
print("##                differences of two sets                                 ##");
print("##     symmetric_difference_update()	inserts the symmetric differences    ##");
print("##                from this set and another                               ##");
print("##     union()	Return a set containing the union of sets                ##");
print("##     update()	Update the set with the union of this set and others     ##");
print("##                                                                        ##");
print("############################################################################");
print("##                                                                        ##");
print("##                                  SET                                   ##");
print("##                                                                        ##");
print("##  Un conjunto es una lista de elementos donde ninguno de ellos está     ##");
print("##  repetido. A partir de una lista, en la que pueden haber elementos     ##");
print("##  repetidos, con set es posible crear otra lista con todos los          ##");
print("##  elementos pero sin repetir ninguno. Además, si tenemos varias         ##");
print("##  listas podemos realizar operaciones de conjuntos de unión,            ##");
print("##  diferencia, intersección y diferencia simétrica                       ##");
print("##                                                                        ##");
print("############################################################################");
print("https://www.w3schools.com/python/python_sets.asp");
print (input("Fin    continuar?"));
Nombre_set_1 = {"linea 1","linea 2","linea 3","linea 4","linea 5","linea 6","linea 7","linea 8","linea 9","linea 1"}
print("#########################################################");
# Ej 005_1
print("Inicio 005_SET_1")
print("Access Items\nYou cannot access items in a set by referring to an indedato_set, since sets are unordered the items has no indedato_set.");
print("But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.");
print("Loop through the set, and print the values:")
for dato_set in Nombre_set_1:  print(dato_set)
print (input("Fin Fin ej005_SET_1 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 005_2
print("Inicio 005_SET_2")
print("Check");
print("----------");
print("Check if 'linea 5' is present in the set:")
print("linea 2" in Nombre_set_1)
if ("linea 2" in Nombre_set_1):  print("Si, esta en lista!")
print (input("Fin Fin ej005_SET_2 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 005_3
print("Inicio 005_SET_3")
print("Change Items");
print("Once a set is created, you cannot change its items, but you can add new items.");
print("Add Items");
print("---------");
print("Add an item to a set, using the add() method:");
print(Nombre_set_1)
Nombre_set_1.add("linea 0")
print(Nombre_set_1)
print (input("Fin Fin ej005_SET_3 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 005_4
print("Inicio 005_SET_4")
print("Add multiple items to a set, using the update() method:");
print(Nombre_set_1)
Nombre_set_1.update(["linea 11", "linea 12", "linea 13"])
print(Nombre_set_1)
print (input("Fin Fin ej000_SET_4 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 005_5
print("Inicio 005_SET_5")
print("Get the Length of a Set");
print("-----------------------");
print("To determine how many items a set has, use the len() method.");
print("Get the number of items in a set:");
print(len(Nombre_set_1))
print (input("Fin Fin ej000_SET_5 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 005_6
print("Inicio 005_SET_6")
print("Remove Item");
print("-----------");
print("To remove an item in a set, use the remove(), or the discard() method.");
print("Remove 'linea 4' by using the remove() method:");
print(Nombre_set_1)
Nombre_set_1.remove("linea 4")
print(Nombre_set_1)
print("Note: If the item to remove does not erase all list, remove() will raise an error.");
print (input("Fin Fin ej000_SET_6 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 005_7
print("Inicio 005_SET_7")
print("Remove 'linea 3' by using the discard() method:");
print(Nombre_set_1)
Nombre_set_1.discard("linea 3")
print(Nombre_set_1)
print("Note: If the item to remove does erase all list, discard() will NOT raise an error.");
print (input("Fin Fin ej000_SET_7 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 005_8
print("Inicio 005_SET_8")
print("You can also use the pop(), method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will not know what item that gets removed.");
print("The return value of the pop() method is the removed item.");
print("Remove the last item by using the pop() method:");
dato_set = Nombre_set_1.pop()
print(dato_set)
print(Nombre_set_1)
print("Note: Sets are unordered, so when using the pop() method, you will not know which item that gets removed.");
print (input("Fin Fin ej000_SET_8 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 005_9
print("Inicio 005_SET_9")
print("Clear Item");
print("----------");
print("The clear() method empties the set:");
Nombre_set_1.clear()
print(Nombre_set_1)
print("The del keyword will delete the set completely:");
print (input("Fin Fin ej000_SET_9 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 005_10
print("Inicio 005_SET_10")

lista = ['vino', 'cerveza', 'agua', 'vino']					# define lista
bebidas = set(lista)										# define conjunto a partir de una lista
print('vino' in bebidas)									# True, 'vino' está en el conjunto
print('anis' in bebidas)									# False, 'anis' no está en el conjunto
print(bebidas)												# imprime {'agua', 'cerveza', 'vino'}
bebidas2 = bebidas.copy()									# crea nuevo conjunto a partir de copia
print(bebidas2)												# imprime {'agua', 'cerveza', 'vino'}
bebidas2.add('anis')										# añade un nuevo elemento 
print(bebidas2.issuperset(bebidas)) 						# True, bebidas es subconjunto
bebidas.remove('agua')										# borra elemento
print(bebidas & bebidas2)									# imprime elementos comunes
tapas = ['croquetas', 'solomillo', 'croquetas']				# define lista
conjunto = set(tapas)										# crea conjunto (sólo una de croquetas)
if 'croquetas' in conjunto:	pass							# evalúa si croquetas está
conjunto1 = set('Python');									# define conj: P,y,t,h,o,n 
conjunto2 = set('Pitonisa');								# define conj: P,i,t,o,n,s,a
print(conjunto2 - conjunto1)								# aplica diferencia: s, i, a
print(conjunto1 | conjunto2)								# aplica unión: P,y,t,h,o,n,i,s,a 
print(conjunto1 & conjunto2)								# intersección: P,t,o,n
print(conjunto1 ^ conjunto2)								# diferencia simétrica: y,h,i,s,a
print (input("Fin Fin ej000_SET_10 \n		continuar?"));
