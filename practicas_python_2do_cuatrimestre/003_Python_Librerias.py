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
print("""
lenguajes de programacion hacia 2020
https://www.youtube.com/channel/UCX9NJ471o7Wie1DQe94RVIg
Javascript moviles pequeñas aplicaciones de desktop
Rust--(mozilla)-web
Dart (google) app moviles
swift-(Apples)-ios-compidado
Java (oracle) moviles pequeñas aplicaciones de desktop
Python +big data ingenieria, ciencia, seguridad informatica, backend
C++-backend/app escritorio o ontencivas
Go/Golang (google) backend en servidores pero compilado, tipeadoestatico
C# (Microsoft)
haskell
ocaml
erlang
ML
CLojure
Elexir

en caida PHP, Ruby

https://codigofacilito.com/articulos/librerias_python
#\033[1;34;41m Librerías más populares de Python \033[0m


\033[4;35m pygame \033[0m
Pygame es una librería de código abierto la cual nos permite crear aplicaciones multimedia. Aunque su principal enfoque es crear videojuegos, nosotros podemos dejar aun lado esto y realizar otro tipo de aplicaciones, aplicaciones donde necesitemos trabajar con imágenes, animaciones, música, texto, eventos, tanto del teclado como del mouse, entre otros.
Es de suma importancia mencionar que Pygame no cuenta con soporte para implementar física avanzada, por lo que esto queda por parte del desarrollador.

\033[4;35m request \033[0m
Request es una librería que nos permite realizar peticiones HTTP sin muchas complicaciones. Extremadamente útil cuando de consumir servicios web se refiere.
Con esta librería podemos trabajar con los diferentes métodos del protocolo HTTP, así como crear, enviar y recibir paquetes, modificar su contenido, trabajar con sesiones, cookies, formularios e inclusive trabajar con autenticación OAuth.
Si necesitas consurmir algún tipo de servicio web, quizás un API, esta librería sin duda te será de mucha ayuda.

\033[4;35m pillow \033[0m
Pillow o PIL (Python Image Library) me atrevería a decir que es la librería más popular de este listado. Con esta librería podemos trabajar con imágenes de una forma muy sencilla.
Podemos abrir, modificar y almacenar imágenes de diferentes formatos, así como manipular los pixeles, trabajar con máscaras, transparencias, dimensiones, agregar texto, aplicar filtros, por mencionar algunas acciones.

\033[4;35m sqlAlchemy \033[0m
Trabajar con base de datos ya no es una opción, prácticamente todas nuestras aplicaciones funcionan con una. sqlAlchemy es una librería la cual nos permite trabajar con las bases de datos mediante objetos, es decir, es un ORM.
Con esta librería podemos crear, modificar, consultar y eliminar nuestras tablas, así como crear, leer, actualizar y eliminar nuestros registros. El poder de SqlAlchemy no se limita únicamente esto. Podemos crear modelos con diferentes relaciones, uno a uno, uno a muchos, muchos a muchos inclusive relaciones polimórficas.
Podemos trabajar con joins, ordenamiento, conteo, commits, roollback etc... todo lo que hagas comúnmente en SQL lo podrás hacer con esta librería.

\033[4;35m Peewee \033[0m
Al igual que sqlAlchemy, Peewee es un ORM que nos permite trabajar con diferentes de gestores de base de datos. Destacando Postgres, MySQL y SQLite.
Si eres nuevo en el mundo de base de datos y python te recomiendo comiences con este ORM. De forma personal considero que Peewee tiene una curva de aprendizaje muy baja. Además que si tu objetivo es utilizar un Framework Web como Django trasladar los conocimientos de Peewee se te será muy sencillo.
A Diferencia de las librerías mencionadas anteriormente, re no necesita instalación alguna, ya que esta, se encuentra lista para ser usada con un simple import, claro, siempre y cuando hayas instalado Python.

\033[4;35m import re \033[0m
con re podemos trabajar con expresiones regulares, podemos crearlas y aplicarlas.
Si necesitas validar algun formato, quizás un correo electronico, que mejor que hacerlo con una expresión regular.
El tema de expresiones regulares es muy amplio, si te interesa puedes leer más en la documentación oficial.

\033[4;35m collections \033[0m
Al igual que re, collections es una librería la cual ya se encuentra lista para usar. Esta librería nos permite trabajar con listas, tuplas, diccionarios entre otras estructuras de datos.
Las acciones que podemos realizar con esta librería son muchas así como variadas, desde ordenar diccionarios, agrupar objetos hasta combinar estructuras y concatenarlas.
>>> import collections
>>> c = collections.Counter('helloworld')
>>> c

Counter({'l': 3, 'o': 2, 'e': 1, 'd': 1, 'h': 1, 'r': 1, 'w': 1})
""")
