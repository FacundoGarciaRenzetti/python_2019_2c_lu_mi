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
print("##      Unidad 2 - Variables, Listas                                      ##");
print("##            * Tipos de variables                                        ##");
print("##            * Procesamiento de cadenas                                  ##");
print("##                                                                        ##");
print("############################################################################");
print("##                                                                        ##");
print("##                                                                        ##");
print("##                                Objetos                                 ##");
print("##                                                                        ##");
print("##                               Variables                                ##");
print("##                       -----------------------                          ##");
print("##                                                                        ##");
print("##                       Crear archivos con extencion                     ##");
print("##                                                   .py                  ##");
print("##                                                   .pyc                 ##");
print("##                                                   .c                   ##");
print("##                                                                        ##");
print("##               and, as, assert, break, class, continue                  ##");
print("##               def, del, elif, else, except, exec                       ##");
print("##               finally, for, from, global, if, import                   ##");
print("##               in, is, lambda, nonlocal, not, or                        ##");
print("##               pass, raise, return, try, while, with                    ##");
print("##               yield, True, False, None                                 ##");
print("##                                                                        ##");
print("##                      tipos de variables                                ##");
print("##                                          Mutable                       ##");
print("##                                          Inmutable                     ##");
print("##                                                                        ##");
print("##                                          string                        ##");
print("##                                          float                         ##");
print("##                                          Intenger                      ##");
print("##                                          long...                       ##");
print("##                                                                        ##");
print("##            espacio en memoria                                          ##");
print("##                                                                        ##");
print("##            limites de entrega del valor                                ##");
print("##                                locales                                 ##");
print("##                                nonlocal                                ##");
print("##                                globales                                ##");
print("##                                                                        ##");
print("##            escribir un texto                                           ##");
print("##                                                                        ##");
print("##            texto desde una variable                                    ##");
print("##                                                                        ##");
print("##                                                                        ##");
print("############################################################################");
def limpiar():
    import os
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
print(input("continuar?"));
print("\n");
print("Mutable: su contenido (o dicho valor) puede cambiarse en tiempo de ejecución.");
print("Inmutable: su contenido (o dicho valor) no puede cambiarse en tiempo de ejecución.\n");
print("\n");
print("Categoría de tipo________Nombre______Descripción");
print("Números inmutables_______int_________entero");
print("_________________________long________entero largo");
print("_________________________float_______coma flotante");
print("_________________________complex_____complejo");
print("_________________________bool________booleano True / False");
print("Secuencias inmutables____str_________cadena de caracteres");
print("_________________________unicode_____cadena de caracteres Unicode");
print("_________________________tuple_______tupla");
print("_________________________xrange______rango inmutable");
print("Secuencias mutables______list________lista");
print("_________________________range_______rango mutable");
print("Mapeosprint______________dict________diccionario");
print("Conjuntos mutables_______set_________conjunto mutable");
print("Conjuntos inmutables_____frozenset___Conjunto inmutable");
print("\n");
print("\nhttp://docs.python.org.ar/tutorial/3/classes.html");
print("\n Objeto, es su materialización de algo incluso un dato");
print("\n Clase, es el razonamiento abstracto de un objeto");
print("\n Instanciar, es crear objetos desde una clase");
print("\n Las clases en este contexto permiten definir los atributos y el comportamiento, mediante métodos, de los objetos de un programa. Una clase es una especie de plantilla o prototipo que se utiliza para crear instancias individuales del mismo tipo de objeto.");
print("\n Los atributos definen las características propias del objeto y modifican su estado. Son datos asociados a las clases y a los objetos creados a partir de ellas.");
print("\n De ello, se deducen los dos tipos de atributos o de variables existentes: variables de clase y variables de instancia (objetos).");
print("\n Los métodos son bloques de código (o funciones) de una clase que se utilizan para definir el comportamiento de los objetos.");
print("\n Tanto para acceder a los atributos como para llamar a los métodos se utiliza el método denominado de notación de punto que se basa en escribir el nombre del objeto o de la clase seguido de un punto y el nombre del atributo o del método con los argumentos que procedan: clase.atributo, objeto.atributo, objeto.método([argumentos]).");
print("\n ");
print("\n Una variable de clase es compartida por todas las instancias de una clase. Se definen dentro de la clase (después del encabezado de la clase) pero nunca dentro de un método. Este tipo de variables no se utilizan con tanta frecuencia como las variables de instancia.");
print("\n Una variable de instancia se define dentro de un método y pertenece a un objeto determinado de la clase instanciada. ");
print("\n ");
print(input("continuar?"));
limpiar();
print("#########################################################");
# Ej 000_V_1
print("Inicio ej000_V_1");
print("http://docs.python.org.ar/tutorial/3/classes.html")
print ("https://www.python.org/downloads/");
print ("https://pythones.net/instalando-python-3-que-es-un-ide/");
print ("https://python-para-impacientes.blogspot.com/2016/02/variables-de-control-en-tkinter.html");
print ("https://pythones.net/instalando-python-3-que-es-un-ide/\n\n")
print("############################################################################");
print("##                                                                        ##");
print("##      Unidad 2 - Variables, Listas                                      ##");
print("##            * Tipos de variables                                        ##");
print("##            * Procesamiento de cadenas                                  ##");
print("##                                                                        ##");
print("############################################################################");     
print("  *String - Cadenas puede incorporar en cualquiera de los dos comillas simples (') o comillas dobles (\") o para multiplas lineas se usan comillas triples de cada una (''' o """);
cadena=('''"http://docs.python.org.ar/tutorial/3/classes.html"
"https://www.python.org/downloads/"
"https://pythones.net/instalando-python-3-que-es-un-ide/"
"https://python-para-impacientes.blogspot.com/2016/02/variables-de-control-en-tkinter.html"
"https://pythones.net/instalando-python-3-que-es-un-ide/")''');
print (cadena);
cadena=("Hola, todo el mundo!");print (type(cadena));
cadena=('Hola, todo el mundo!');print (type(cadena));
cadena=("17");print (type(cadena));
cadena=(17);print (type(cadena));
cadena=(3.2);print (type(cadena));
print (input("Fin continuar?"));
print("  *String - Cadenas con doble comillas pueden incluir  comilla simple dentro o viceversa");
cadena='UTN\n 2019'
print (cadena);
cadena=("UTN 2019")
print (cadena);
cadena='"hola" como va todo'
print (cadena);
cadena="'hola' como va todo"
print (cadena);
cadena='"hola" como va todo'
print (cadena);
print("  *String - Cadenas pueden tener (en ingles por ejemplo) 'detras de una letra por lo que hay que salbarla con '\'");
cadena='Cat\'s plate'
print (cadena);
cadena='It s\'nt a problem'
print (cadena);
print (3*"UTN 2019")
variable="UTN 2019"
print (variable)
print (variable[2])
print (variable[:4])
print (variable[4:])
print (variable[2:6])
variable1,variable2="UTN "," 2019"
a, b, c = 1, 2, 3
print ("a, b, c = 1, 2, 3")
print ("a = "+str(a))
print ("b = "+str(b))
print ("c = "+str(c))
print ("#--------------------------------")
print (variable1+variable2)
print (variable2)
print (variable1)
print (input("Fin Fin ej000_V_1 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 000_V_2
print("Inicio ej000_V_2");
var = "xxx"
def ej_000_V_3():
    var = "yyy"
    print(var);
ej_000_V_3();
print(var);
#--------------------------------
print("Ingrese datos alfa, numericos y mixtos")
for i in range (3):
	print("#--------------------------------");
	var_a = input("variable A:")
	var_b = input("variable B:")
	print ("variable a: "+var_a)
	print ("variable b: "+var_b)
	print ("variable a+b"+(var_a+var_b))
	print ("variable a+b"+(var_a*2+var_b))
#--------------------------------
print (input("Fin Fin ej000_V_2 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 000_V_3
print("Inicio ej000_V_3");
radio = input("¿Cuál es su radio?")
radio = float(radio)
area = 3.14159 * radio**2
print("El area es ", area)
#--------------------------------

nombre = "Facundo"
Nombre = "Joaquin"
print("nombre : "+nombre);
print("Nombre : "+Nombre);
print (input("Fin Fin ej000_V_3 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 000_V_4
print("Inicio ej000_V_4");
print("############################");
print("## a += b 	a = a + b    ##");
print("## a -= b 	a = a - b    ##");
print("## a *= b 	a = a * b    ##");
print("## a /= b 	a = a / b    ##");
print("## a **= b 	a = a ** b   ##");
print("## a //= b 	a = a // b   ##");
print("## a %= b 	a = a % b    ##");
print("############################");
a=8
b=5
print ("a = "+str(a));
print ("b = "+str(b));
a += b;print ("a += b");
print ("a = "+str(a));
a -= b;print ("a -= b");
print ("a = "+str(a));
a *= b;print ("a *= b");
print ("a = "+str(a));
a /= b;print ("a /= b");
print ("a = "+str(a));
a **= b;print ("a **= b");
print ("a = "+str(a));
a //= b;print ("a //= b");
print ("a = "+str(a));
a %= b;print ("a %= b");
print ("a = "+str(a));

print (input("Fin Fin ej000_V_4 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 000_V_5
print("Inicio ej000_V_5");


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

print (input("Fin Fin ej000_V_5 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 000_V_6
print("Inicio ej000_V_6");


cadena='"hola" como va todo AHORA DARE UN ERROR'
print (cadena);
del cadena
print (cadena);

print("\n por favor cargue 'AGT_Ej_000_Ambitos.py' ");
