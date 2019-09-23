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
print("##                      Ingreso - salida de datos                         ##");
print("##                                                                        ##");
print("############################################################################");
def limpiar():
    import os
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
print("Inicio ej 002_1 - ingreso de datos por teclado");
nota_alumno_1 = int(input("Ingreso la nota del 1er parcial :"));
nota_alumno_2 = int(input("Ingreso la nota del 2d0 parcial :"));
print ("1er parcial : "+str(nota_alumno_1));
print ("2do parcial : "+str(nota_alumno_2));
print ("promedio : "+str((nota_alumno_1+nota_alumno_2)/2));
print (input("Fin ej 002_1 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 002_2
valor1=0.1;

valor2=0.1;
valor1=float(input("valor de la mercaderia 1 : "));
valor2=float(input("valor de la mercaderia 2 : "));

resultado_suma= valor1+valor2
resultado_resta=valor1-valor2
resultado_multiplica=valor1*valor2
resultado_divide=valor1/valor2

print ("la suma de los valores es "+str(resultado_suma)+" pesos");
print ("la devolucion genera una resta cuyo saldo es de "+str(resultado_resta)+" pesos");
print ("la multiplicacion de ambos valores es de " +str(resultado_multiplica)+" pesos", end=" ");
print (" y la deivion es de "+str(resultado_divide)+" aunque esto no sirve para nada");
print (input("Fin ej 002_2 \n		continuar?"));

# Ej 002_3
print("Inicio ej 002_3");
edad=int(input("Ingere su edad : "));
if edad<0:
	print("error");
if edad<=2:
	print("bebe");
if edad<=10:
	print("Chico");
if edad<=15:
	print("pavo");
if edad<=20:
	print("Ni ni");
if edad<=30:
	print("A laburar");
if edad>=40:
	print("te crece la panza y se cae todo, hasta el pelo");
print (input("Fin ej 002_3 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 002_4
print("Inicio ej 002_4");
print ("rehacer ej 002_03 con parametros de '>'");
print (input("Fin ej 002_4 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 002_5
valoracion="aprobado"
print("Inicio ej 002_5 - multiples condiciones en multiples lineas");
nota_alumno_1 = int(input("Ingreso la nota del 1er parcial :"));
nota_alumno_2 = int(input("Ingreso la nota del 2d0 parcial :"));
def evaluacion(nota1,nota2):
	valoracion="aprobado"
	if nota1<5 and nota2<5:
		valoracion="final obligatorio"
	elif nota1<5 and nota2>=5:
		valoracion="RECUPREA 1er parcial"
	elif nota1>=5 and nota2<5:
		valoracion="RECUPREA 2do parcial"
	elif nota1>=7 and nota2>=7:
		valoracion="Aprobado sin final"
	return valoracion
print(evaluacion((nota_alumno_1),(nota_alumno_2)));
print("promedio : "+str((nota_alumno_1+nota_alumno_2)/2));
print (input("Fin ej 002_5 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 002_6
Edad_alumno = 0
valoracion="ok"
print("Inicio ej 002_6 - condicion maximos y minimos en una linea (concatenados)");
Edad_alumno = int(input("Ingreso la edad del alumno :"));
print (Edad_alumno);
if 0<Edad_alumno<100:
	valoracion="ok"
else:
	valoracion="Error"
print (valoracion);
print (input("Fin ej 002_6 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 002_7
print("Inicio ej 002_7 - multiples condiciones en una linea (concatenados)");
nota_1 = int(input("Ingreso la nota del 1er bimestre :"));
nota_2 = int(input("Ingreso la nota del 2er bimestre :"));
nota_3 = int(input("Ingreso la nota del 3er bimestre :"));
nota_4 = int(input("Ingreso la nota del 4er bimestre :"));
if nota_1<nota_2<nota_3<nota_4:
	valoracion="MEJORANDO"
elif nota_1>nota_2>nota_3>nota_4:
	valoracion="DE MAL EN PEOR"
else:
	valoracion="Maso"	
print (valoracion);
print (input("Fin ej 002_7 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 002_8
print("Inicio ej 002_8 - multiples condiciones en una linea (concatenados)");
print (" el ej 002_7  con arreglos por notas");
print ("					<0 - out");
print ("				entre	0  y <4  - ");
print ("				entre	4  y <6  - ");
print ("				entre	6  y <8  - ");
print ("				entre	8  y <10  - ");
print ("					>10 - out");
print (input("Fin ej 002_8 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 002_9
print("Inicio ej 002_9 - isdigit ");
print("isalnum()	Returns true if string has at least 1 character and all characters are alphanumeric and false otherwise.");
print("isalpha()	Returns true if string has at least 1 character and all characters are alphabetic and false otherwise.");
print("isdigit()	Returns true if string contains only digits and false otherwise.");
print("islower()	Returns true if string has at least 1 cased character and all cased characters are in lowercase and false otherwise.");
print("isnumeric()	Returns true if a unicode string contains only numeric characters and false otherwise.");
print("leer\nhttp://pyspanishdoc.sourceforge.net/lib/string-methods.html");
texto_en_memoria="1973"
print("texto_en_memoria : "+str(texto_en_memoria));
print("isalnum : "+str(texto_en_memoria.isalnum()));
print("---------------------------------------------------------------------");
print("isalpha : "+str(texto_en_memoria.isalpha()));
print("---------------------------------------------------------------------");
print("isdigit : "+str(texto_en_memoria.isdigit()));
print("---------------------------------------------------------------------");
texto_en_memoria="arribaUTN"
print("texto_en_memoria : "+str(texto_en_memoria));
print("isalnum : "+str(texto_en_memoria.isalnum()));
print("---------------------------------------------------------------------");
print("isalpha : "+str(texto_en_memoria.isalpha()));
print("---------------------------------------------------------------------");
print("isdigit : "+str(texto_en_memoria.isdigit()));
print("---------------------------------------------------------------------");
texto_en_memoria="Arielnacioen1973"
print("texto_en_memoria : "+str(texto_en_memoria));
print("isalnum : "+str(texto_en_memoria.isalnum()));
print("---------------------------------------------------------------------");
print("isalpha : "+str(texto_en_memoria.isalpha()));
print("---------------------------------------------------------------------");
print("isdigit : "+str(texto_en_memoria.isdigit()));
print("---------------------------------------------------------------------");
print (input("Fin ej 002_9 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 002_9
#print("Inicio ej 002_9 -");

