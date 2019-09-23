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
print("##         Unidad 7 - Fechas, Horas, Archivos                             ##");
print("##            * Operaciones con archivos                                  ##");
print("##                                                                        ##");
print("############################################################################");     
print("##                                                                        ##");
print("##                      Ingreso - salida de datos                         ##");
print("##                                                                        ##");
print("##                                                                        ##");
print("##                      otros archivos de texto                           ##");
print("##                      -----------------------                           ##");
print("##                                                                        ##");
print("##                           crear archivos de texto                      ##");
print("##                                                                        ##");
print("##                           escribir un texto                            ##");
print("##                                                                        ##");
print("##                   escribir una linea al final                          ##");
print("##                                                                        ##");
print("##                   leer un texto                                        ##");
print("##                                                                        ##");
print("##                   leer una linea                                       ##");
print("##                                                                        ##");
print("##                           cerrar archivos                              ##");
print("##                                                                        ##");
print("############################################################################");
print("##                                                                        ##");
print("##                  IO  -  TIPO  o CVS 'text.txt                          ##");
print("##                                                                        ##");
print("##                Unidad 7 - Fechas, Horas, Archivos                      ##");
print("##                      * Operaciones con archivos                        ##");
print("##                                                                        ##");
print("##                Unidad 4 - Listas, Tuplas y Diccionarios                ##");
print("##                      * Operaciones con archivos                        ##");
print("##                      libreria   pickle                                 ##");
print("##                                                                        ##");
print("############################################################################"); 
print("##                                                                        ##");
print("##         r      read   Lectura                                          ##");
print("##         r+     read+  Lectura/Escritura simultánea                     ##");
print("##         w      write  Sobreescritura. Si no existe archivo se creará   ##");
print("##         a      append Añadir. Escribe al final del archivo             ##");
print("##                EN BINARIO                                              ##");
print("##         rb     read   Lectura binaria                                  ##");
print("##         r+b    read+  Lectura/Escritura binaria simultánea             ##");
print("##         wb     write  Sobreescritura binaria                           ##");
print("##                                                                        ##");
print("##         U            Salto de línea                                    ##");
print("##                                                                        ##");
print("############################################################################"); 

def limpiar():
    import os
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
print(input("continuar?"));
print("Un módulo es un fichero que contiene codigo PYTHON. Su extensión es .py. Almacena declaración de variables e implementación de funciones. Posibilidad de hacer referencia a otros módulos (mediante la instrucción import).")
print("Inicio ej 002-2_1 - salida de datos a otro archivo write");
from io import *
archivo_de_texto=open("text.txt","w")# abre el archivo text.txt para escritura y si no existe lo crea
texto_en_memoria="TEXT\nLenguaje interpretado\n Un lenguaje interpretado es un lenguaje de programación para el que la mayoría de sus implementaciones ejecuta las instrucciones directamente, sin una previa compilación del programa a instrucciones en lenguaje máquina.\n El intérprete ejecuta el programa directamente, traduciendo cada sentencia en una secuencia de una o más subrutinas ya compiladas en código máquina.\n Los términos lenguaje interpretado y lenguaje compilado no están bien definidos porque, en teoría, cualquier lenguaje de programación puede ser interpretado o compilado.\n Cada vez es más popular, en las implementaciones más modernas de un lenguaje de programación, ofrecer ambas opciones.\n Los lenguajes interpretados también pueden diferenciarse de los lenguajes de máquina.\n Funcionalmente, tanto la ejecución y la interpretación significan lo mismo -obtener la siguiente instrucción/sentencia del programa y su ejecución-.\n Aunque el bytecode (código byte) interpretado es además idéntico a su forma en código máquina y tiene una representación en ensamblador, el término 'interpretado' se reserva en la práctica para lenguajes 'procesados por software' (como las máquinas virtuales o emuladores) por encima del procesado nativo (por ejemplo, por hardware).\n En principio, los programas de muchos lenguajes se pueden compilar o interpretar, emular o ejecutar nativamente, así que esta designación se aplica solamente a la implementación práctica más usual, en vez de representar una propiedad esencial del lenguaje.\n De forma parecida al microcódigo del procesador, muchos intérpretes, internamente recaen en una compilación en tiempo de ejecución.\n Evitando la compilación, los programas interpretados son más fáciles de evolucionar durante el desarrollo y la ejecución (transformándose en ocasiones de uno en la otra).\n De otra parte, ya que la compilación implica una traducción a un formato más amigable con la máquina, los programas interpretados corren más lentamente y menos eficientemente (es decir, gastan considerablemente más energía).\n Esto es especialmente verdad para los lenguajes de guion, cuyas sentencias son más complejas de analizar comparadas con las instrucciones máquina.\n Muchos lenguajes se han implementado usando tanto compiladores como intérpretes, incluyendo BASIC, C, Lisp, Pascal y Python. Java y C# se compilan a código byte, el lenguaje interpretado específico para la máquina virtual.\n Muchas implementaciones de Lisp pueden mezclar libremente código interpretado y compilado. "
archivo_de_texto.write(texto_en_memoria);
archivo_de_texto.close();
print (input("Fin ej 002_2_1 \n		continuar?"));
limpiar();
print("############################################################################"); 
# Ej 002_2_2
print("Inicio ej 002_2_2 - salida de datos a otro archivo append");
archivo_de_texto=open("text.txt","a")# abre el archivo text.txt para agregar datos
linea_texto_en_memoria="\n fuente wikipedia : https://es.wikipedia.org/wiki/Int%C3%A9rprete_(inform%C3%A1tica)#Eficiencia"
archivo_de_texto.write(linea_texto_en_memoria);
archivo_de_texto.close();
print (input("Fin ej 002-2_2 \n		continuar?"));
limpiar();
print("############################################################################"); 
# Ej 002_2_3
print("Inicio ej 002_2_3 - ingreso lectura de bloque de datos desde otro archivo read");
archivo_de_texto=open("text.txt","r")# abre el archivo text.txt para lectura en bloque
texto_a_memoria=archivo_de_texto.read();
print(texto_a_memoria);
archivo_de_texto.close();
print (input("Fin ej 002_2_3 \n		continuar?"));
limpiar();
print("############################################################################"); 
# Ej 002_2_4
print("Inicio ej 002_2_4 - ingreso lectura por lineas de datos desde otro archivo readlines");
archivo_de_texto=open("text.txt","r")# abre el archivo text.txt para lectura en lineas
linea_texto_a_memoria=archivo_de_texto.readlines();
print(linea_texto_a_memoria[2]);
archivo_de_texto.close();
print (input("Fin ej 002_2_4 \n		continuar?"));
####################                  BINARIOS "binario.dat"
print("############################################################################"); 
print("##                                                                        ##");
print("##                       BINARIOS 'binario.dat'                           ##");
print("##                                                                        ##");
print("##                Unidad 7 - Fechas, Horas, Archivos                      ##");
print("##                      * Operaciones con archivos                        ##");
print("##                                                                        ##");
print("##                Unidad 4 - Listas, Tuplas y Diccionarios                ##");
print("##                      * Operaciones con archivos                        ##");
print("##                      libreria   pickle                                 ##");
print("##                                                                        ##");
print("############################################################################"); 

import pickle
# Ej 002_2_5
binario_en_memoria="PICKLE\nLenguaje interpretado\n Un lenguaje interpretado es un lenguaje de programación para el que la mayoría de sus implementaciones ejecuta las instrucciones directamente, sin una previa compilación del programa a instrucciones en lenguaje máquina.\n El intérprete ejecuta el programa directamente, traduciendo cada sentencia en una secuencia de una o más subrutinas ya compiladas en código máquina.\n Los términos lenguaje interpretado y lenguaje compilado4​ no están bien definidos porque, en teoría, cualquier lenguaje de programación puede ser interpretado o compilado.\n Cada vez es más popular, en las implementaciones más modernas de un lenguaje de programación, ofrecer ambas opciones.\n Los lenguajes interpretados también pueden diferenciarse de los lenguajes de máquina.\n Funcionalmente, tanto la ejecución y la interpretación significan lo mismo -obtener la siguiente instrucción/sentencia del programa y su ejecución-.\n Aunque el bytecode (código byte) interpretado es además idéntico a su forma en código máquina y tiene una representación en ensamblador, el término 'interpretado' se reserva en la práctica para lenguajes 'procesados por software' (como las máquinas virtuales o emuladores) por encima del procesado nativo (por ejemplo, por hardware).\n En principio, los programas de muchos lenguajes se pueden compilar o interpretar, emular o ejecutar nativamente, así que esta designación se aplica solamente a la implementación práctica más usual, en vez de representar una propiedad esencial del lenguaje.\n De forma parecida al microcódigo del procesador, muchos intérpretes, internamente recaen en una compilación en tiempo de ejecución.\n Evitando la compilación, los programas interpretados son más fáciles de evolucionar durante el desarrollo y la ejecución (transformándose en ocasiones de uno en la otra).\n De otra parte, ya que la compilación implica una traducción a un formato más amigable con la máquina, los programas interpretados corren más lentamente y menos eficientemente (es decir, gastan considerablemente más energía).\n Esto es especialmente verdad para los lenguajes de guion, cuyas sentencias son más complejas de analizar comparadas con las instrucciones máquina.\n Muchos lenguajes se han implementado usando tanto compiladores como intérpretes, incluyendo BASIC, C, Lisp, Pascal y Python. Java y C# se compilan a código byte, el lenguaje interpretado específico para la máquina virtual.\n Muchas implementaciones de Lisp pueden mezclar libremente código interpretado y compilado. "
print("Inicio ej 002_2_5 - salida de datos a otro archivo binario write wr ");
from io import *
archivo_de_binario=open("binario.dat","wb")# abre el archivo binario para escritura y si no existe lo crea
pickle.dump(binario_en_memoria,archivo_de_binario);
archivo_de_binario.close();
del archivo_de_binario
print (input("Fin ej 002_2_5 \n		continuar?"));
limpiar();
print("############################################################################"); 
# Ej 002_2_6
print("Inicio ej 002_2_6 - ingreso lectura de bloque de datos desde otro archivo binario read - rw");
archivo_de_binario=open("binario.dat","rb")# abre el archivo binario para lectura en bloque
binario_a_memoria=pickle.load(archivo_de_binario);
print(binario_a_memoria);
archivo_de_binario.close();
del archivo_de_binario
print (input("Fin ej 002_2_6 \n		continuar?"));
limpiar();
print("############################################################################"); 
# Ej 002_2_7
print("Inicio ej 002_2_7 - ingreso lectura por lineas de datos desde otro archivo binario readlines");
archivo_de_binario=open("binario.dat","rb")# abre el archivo binario para lectura en lineas
linea_binario_a_memoria=archivo_de_binario.readlines();
print(linea_binario_a_memoria[5]);
archivo_de_binario.close();
del archivo_de_binario
print (input("Fin ej 002_2_7 \n		continuar?"));

####################                  JSON (JavaScript Object Notation)."binario.dat"
print("############################################################################"); 
print("##                                                                        ##");
print("##                JSON (JavaScript Object Notation).                      ##");
print("##                                                                        ##");
print("##                Unidad 7 - Fechas, Horas, Archivos                      ##");
print("##                      * Operaciones con archivos                        ##");
print("##                                                                        ##");
print("##                Unidad 4 - Listas, Tuplas y Diccionarios                ##");
print("##                      * Operaciones con archivos                        ##");
print("##                      libreria json                                     ##");
print("##                                                                        ##");
print("##                JSON                 Python                             ##");
print("##                -----                ------                             ##");
print("##                object                dict                              ##");
print("##                array                 list                              ##");
print("##                string                unicode                           ##");
print("##                number (int)          int, long                         ##");
print("##                number (real)         float                             ##");
print("##                true                  True                              ##");
print("##                false                 False                             ##");
print("##                null                  None                              ##");
print("##                                                                        ##");
print("############################################################################"); 
import json
# Ej 002_2_8
json_en_memoria="JSON\nLenguaje interpretado\n Un lenguaje interpretado es un lenguaje de programación para el que la mayoría de sus implementaciones ejecuta las instrucciones directamente, sin una previa compilación del programa a instrucciones en lenguaje máquina.\n El intérprete ejecuta el programa directamente, traduciendo cada sentencia en una secuencia de una o más subrutinas ya compiladas en código máquina.\n Los términos lenguaje interpretado y lenguaje compilado4​ no están bien definidos porque, en teoría, cualquier lenguaje de programación puede ser interpretado o compilado.\n Cada vez es más popular, en las implementaciones más modernas de un lenguaje de programación, ofrecer ambas opciones.\n Los lenguajes interpretados también pueden diferenciarse de los lenguajes de máquina.\n Funcionalmente, tanto la ejecución y la interpretación significan lo mismo -obtener la siguiente instrucción/sentencia del programa y su ejecución-.\n Aunque el bytecode (código byte) interpretado es además idéntico a su forma en código máquina y tiene una representación en ensamblador, el término 'interpretado' se reserva en la práctica para lenguajes 'procesados por software' (como las máquinas virtuales o emuladores) por encima del procesado nativo (por ejemplo, por hardware).\n En principio, los programas de muchos lenguajes se pueden compilar o interpretar, emular o ejecutar nativamente, así que esta designación se aplica solamente a la implementación práctica más usual, en vez de representar una propiedad esencial del lenguaje.\n De forma parecida al microcódigo del procesador, muchos intérpretes, internamente recaen en una compilación en tiempo de ejecución.\n Evitando la compilación, los programas interpretados son más fáciles de evolucionar durante el desarrollo y la ejecución (transformándose en ocasiones de uno en la otra).\n De otra parte, ya que la compilación implica una traducción a un formato más amigable con la máquina, los programas interpretados corren más lentamente y menos eficientemente (es decir, gastan considerablemente más energía).\n Esto es especialmente verdad para los lenguajes de guion, cuyas sentencias son más complejas de analizar comparadas con las instrucciones máquina.\n Muchos lenguajes se han implementado usando tanto compiladores como intérpretes, incluyendo BASIC, C, Lisp, Pascal y Python. Java y C# se compilan a código byte, el lenguaje interpretado específico para la máquina virtual.\n Muchas implementaciones de Lisp pueden mezclar libremente código interpretado y compilado. "
print("Inicio ej 002_2_8 - salida de datos a otro archivo JavaScript_Object_Notation write wr ");
from io import *
archivo_de_json=open("JavaScript_Object_Notation.json","w")# abre el archivo JavaScript_Object_Notation para escritura y si no existe lo crea
json.dump(json_en_memoria,archivo_de_json);
archivo_de_json.close();
del archivo_de_json
print (input("Fin ej 002_2_8 \n		continuar?"));
limpiar();
print("############################################################################"); 
# Ej 002_2_9
print("Inicio ej 002_2_9 - ingreso lectura de bloque de datos desde otro archivo JavaScript_Object_Notation read - rw");
archivo_de_json=open("JavaScript_Object_Notation.json","r")# abre el archivo JavaScript_Object_Notation para lectura en bloque
json_en_memoria=json.load(archivo_de_json);
print(json_en_memoria);
archivo_de_json.close();
del archivo_de_json
print (input("Fin ej 002_2_9 \n		continuar?"));
limpiar();
print("############################################################################"); 
# Ej 002_2_10
print("############################################################################"); 
print("##                                                                        ##");
print("##                Unidad 7 - Fechas, Horas, Archivos                      ##");
print("##                      * Operaciones con archivos                        ##");
print("##                                                                        ##");
print("##                Unidad 4 - Listas, Tuplas y Diccionarios                ##");
print("##                      * Operaciones con archivos                        ##");
print("##                                                                        ##");
print("##                      metodo 'WITH'                                     ##");
print("##                                                                        ##");
print("############################################################################"); 
# Ej 002_2_5
import pickle
print("Inicio ej 002_2_5 - salida de datos con metodo WITH a otro archivo binario write wr ");
binario_en_memoria2="PICKLE_WITH\nLenguaje interpretado\n Un lenguaje interpretado es un lenguaje de programación para el que la mayoría de sus implementaciones ejecuta las instrucciones directamente, sin una previa compilación del programa a instrucciones en lenguaje máquina.\n El intérprete ejecuta el programa directamente, traduciendo cada sentencia en una secuencia de una o más subrutinas ya compiladas en código máquina.\n Los términos lenguaje interpretado y lenguaje compilado4​ no están bien definidos porque, en teoría, cualquier lenguaje de programación puede ser interpretado o compilado.\n Cada vez es más popular, en las implementaciones más modernas de un lenguaje de programación, ofrecer ambas opciones.\n Los lenguajes interpretados también pueden diferenciarse de los lenguajes de máquina.\n Funcionalmente, tanto la ejecución y la interpretación significan lo mismo -obtener la siguiente instrucción/sentencia del programa y su ejecución-.\n Aunque el bytecode (código byte) interpretado es además idéntico a su forma en código máquina y tiene una representación en ensamblador, el término 'interpretado' se reserva en la práctica para lenguajes 'procesados por software' (como las máquinas virtuales o emuladores) por encima del procesado nativo (por ejemplo, por hardware).\n En principio, los programas de muchos lenguajes se pueden compilar o interpretar, emular o ejecutar nativamente, así que esta designación se aplica solamente a la implementación práctica más usual, en vez de representar una propiedad esencial del lenguaje.\n De forma parecida al microcódigo del procesador, muchos intérpretes, internamente recaen en una compilación en tiempo de ejecución.\n Evitando la compilación, los programas interpretados son más fáciles de evolucionar durante el desarrollo y la ejecución (transformándose en ocasiones de uno en la otra).\n De otra parte, ya que la compilación implica una traducción a un formato más amigable con la máquina, los programas interpretados corren más lentamente y menos eficientemente (es decir, gastan considerablemente más energía).\n Esto es especialmente verdad para los lenguajes de guion, cuyas sentencias son más complejas de analizar comparadas con las instrucciones máquina.\n Muchos lenguajes se han implementado usando tanto compiladores como intérpretes, incluyendo BASIC, C, Lisp, Pascal y Python. Java y C# se compilan a código byte, el lenguaje interpretado específico para la máquina virtual.\n Muchas implementaciones de Lisp pueden mezclar libremente código interpretado y compilado. "
with open("binario_metodo_with.dat","wb") as write_file:# abre el archivo binario para escritura y si no existe lo crea
	pickle.dump(binario_en_memoria2, write_file, pickle.HIGHEST_PROTOCOL)
print (input("Fin ej 002_2_5 \n		continuar?"));
# Ej 002_2_6
print("Inicio ej 002_2_6 - ingreso lectura de bloque de datos con metodo WITH desde otro archivo binario read - rw");
with open("binario_metodo_with.dat", "rb") as read_file:# abre el archivo binario para lectura en bloque  
    binario_a_memoria2 = pickle.load(read_file)
print(binario_a_memoria2);
print (input("Fin ej 002_2_6 \n		continuar?"));
limpiar();
print("############################################################################"); 
# Ej 002_2_8
import json
json_en_memoria2="JSON_WITH\nLenguaje interpretado\n Un lenguaje interpretado es un lenguaje de programación para el que la mayoría de sus implementaciones ejecuta las instrucciones directamente, sin una previa compilación del programa a instrucciones en lenguaje máquina.\n El intérprete ejecuta el programa directamente, traduciendo cada sentencia en una secuencia de una o más subrutinas ya compiladas en código máquina.\n Los términos lenguaje interpretado y lenguaje compilado4​ no están bien definidos porque, en teoría, cualquier lenguaje de programación puede ser interpretado o compilado.\n Cada vez es más popular, en las implementaciones más modernas de un lenguaje de programación, ofrecer ambas opciones.\n Los lenguajes interpretados también pueden diferenciarse de los lenguajes de máquina.\n Funcionalmente, tanto la ejecución y la interpretación significan lo mismo -obtener la siguiente instrucción/sentencia del programa y su ejecución-.\n Aunque el bytecode (código byte) interpretado es además idéntico a su forma en código máquina y tiene una representación en ensamblador, el término 'interpretado' se reserva en la práctica para lenguajes 'procesados por software' (como las máquinas virtuales o emuladores) por encima del procesado nativo (por ejemplo, por hardware).\n En principio, los programas de muchos lenguajes se pueden compilar o interpretar, emular o ejecutar nativamente, así que esta designación se aplica solamente a la implementación práctica más usual, en vez de representar una propiedad esencial del lenguaje.\n De forma parecida al microcódigo del procesador, muchos intérpretes, internamente recaen en una compilación en tiempo de ejecución.\n Evitando la compilación, los programas interpretados son más fáciles de evolucionar durante el desarrollo y la ejecución (transformándose en ocasiones de uno en la otra).\n De otra parte, ya que la compilación implica una traducción a un formato más amigable con la máquina, los programas interpretados corren más lentamente y menos eficientemente (es decir, gastan considerablemente más energía).\n Esto es especialmente verdad para los lenguajes de guion, cuyas sentencias son más complejas de analizar comparadas con las instrucciones máquina.\n Muchos lenguajes se han implementado usando tanto compiladores como intérpretes, incluyendo BASIC, C, Lisp, Pascal y Python. Java y C# se compilan a código byte, el lenguaje interpretado específico para la máquina virtual.\n Muchas implementaciones de Lisp pueden mezclar libremente código interpretado y compilado. "
print("Inicio ej 002_2_8 - salida de datos con metodo WITH  a otro archivo JavaScript_Object_Notation write wr ");
with open("JavaScript_Object_Notation_with.json", "w") as write_file:# abre el archivo JavaScript_Object_Notation para escritura y si no existe lo crea
	json.dump(json_en_memoria2, write_file)
print (input("Fin ej 002_2_7 \n		continuar?"));
# Ej 002_2_9
print("Inicio ej 002_2_9 - ingreso lectura de bloque de datos con metodo WITH  desde otro archivo JavaScript_Object_Notation read - rw");
with open("JavaScript_Object_Notation_with.json","r") as read_file:# abre el archivo JavaScript_Object_Notation para lectura en bloque
	json_en_memoria2 = json.load(read_file);
print(json_en_memoria2);
print (input("Fin ej 002_2_9 \n		continuar?"));
print("https://docs.python.org/3/library/pickle.html")
