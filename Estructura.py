#!/usr/bin/env python
# -*- coding: utf-8 -*-
# AGT
# Copyright 2019 Ariel H Apellido_1 Traba <cursos.arT@gmail.com>
def nuevo(numero,estado=None):
	import os
	if estado!="inicio":
		print(f"\n\t\tFin del ejercicio Nº {numero}")    
		x=input("Presione una tecla para continuar")
		if os.name == 'nt':
			os.system('cls')
		else:
			os.system('clear');
	if estado!="fin":
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
		print(f"\n\t\tInicio del ejercicio Nº {numero+1}")    
	if estado=="inicio":
		print("""\n
╔══════════════════════════════════════════════════════════════════════════════════╗ ▒ ▓ ┌┐┤│├└┘┴┬─┼╔╗╠╬╣║╚╝╩╦═¤
║TEMARIO:                                                                          ║
║--------                                                                          ║
║Unidad 1 - Introducción                                                           ║
║● ¿Qué es Python?                                                                 ║
║● Ventajas y desventajas                                                          ║
║● Ecosistema Python y Comunidad –Librerías extendidas                             ║
║● Descarga –Opensource                                                            ║
║● Instalación, configuración y hardware necesario                                 ║
║● Errores sintácticos y lógicos, localización en pantalla y correcciones          ║
║● Importancia del versionado                                                      ║
║● GIT Colaborativo –Pair Programming                                              ║
║   o Introducción a GIT                                                           ║
║   o Creando un repositorio, clonar, branches                                     ║
║   o Borrar, guardar (STASH), requperar (POP)                                     ║
╠══════════════════════════════════════════════════════════════════════════════════╣
║Unidad 2 – Software                                                               ║
║Características de Python                                                         ║
║● Software libre                                                                  ║
║● Alto nivel                                                                      ║
║● Multiparadigma                                                                  ║
║● Portable                                                                        ║
║● Programación Secuencial y Orientada a Objetos                                   ║
║● Multiplataforma                                                                 ║
║● Interpretado                                                                    ║
║● Tipado dinámico                                                                 ║
║● Estructura (TAB)                                                                ║
║                                                                                  ║
║Entorno de Desarrollo Intérprete – IDEs                                           ║
║● Elección según el propósito del trabajo:                                        ║
║	PyCharm, PyDev, Atom, Spyder, PyScripter, Eclipse, IPython.                    ║
║● Entornos especiales: Anaconda (Data Science Platform),  Jupyter (Notebooks).    ║
║● Consola, pantalla gráfica y entorno                                             ║
║● Salida de datos por pantalla                                                    ║
║   o Sentencias: print ()                                                         ║
║● Ingreso de datos por teclado                                                    ║
║● Sentencias: input ()                                                            ║
╚══════════════════════════════════════════════════════════════════════════════════╝
		""");
