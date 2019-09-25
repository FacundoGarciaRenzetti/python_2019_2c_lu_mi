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
║	o Borrar, guardar (STASH), requperar (POP)                                                                           ║
╠════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
║Unidad 2 – Software                                                                                                     ║
║Características de Python                                                                                               ║
║● Software libre - Open Source                                                                                          ║
║● Alto nivel                                                                                                            ║
║● Multiparadigma vs fines y estilos de programacion                                                                     ║
║● Portable                                                                                                              ║
║● Programación Secuencial y Orientada a Objetos                                                                         ║
║● Multiplataforma Unix, Linux, Windows, IO - Kivy App                                                                   ║
║● Interpretado / Compilado                                                                                              ║
║● Tipado dinámico                                                                                                       ║
║● Funcional Mutacion de tipos de variables                                                                              ║
║● Estructurado (TAB)                                                                                                    ║
║● Hilos (Complejo, opcion Celery)                                                                                       ║
║● Versatilida                                                                                                           ║
║                                                                                                                        ║
║Entorno de Desarrollo Intérprete – IDEs                                                                                 ║
║● Elección según el propósito del trabajo:                                                                              ║
║	PyCharm, PyDev, Atom, Spyder, PyScripter, Eclipse, IPython.                                                          ║
║● Entornos especiales: Anaconda (Data Science Platform),  Jupyter (Notebooks).                                          ║
║● Consola, pantalla gráfica y entorno                                                                                   ║
║● Salida de datos por pantalla                                                                                          ║
║	o Sentencias: print ()                                                                                               ║
║● Ingreso de datos por teclado                                                                                          ║
║	o Sentencias: input ()                                                                                               ║
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
║Download e instalación MSI, Linux, etc                                                                                  ║
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
#http://docs.fabfile.org/en/2.4/
print(input("continuar?"));
print("\n Durante el siglo XX, científicos como Alan Turing y Lorenzo Church fundaron las bases del cómputo, la programación y sus lenguajes. Los lenguajes de programación actuales, a diferencia de los lenguajes humanos tienen una morfología rígida y simplificada con el fin de ejecutar instrucciones específicas en los sistemas de cómputo. ");
print("\n Lenguajes de alto y bajo nivel. ");
print("\n Los lenguajes de bajo nivel constan de un conjunto básico de instrucciones que son ejecutados directamente por la unidad de procesamiento de un sistema de cómputo, tal como es el caso del lenguaje ensamblador. Dichos lenguajes están ligados intrínsecamente al tipo de procesador que los ejecuta y resultan ser muy complicados de elaborar e interpretar por las personas. ");
print("\n Por su parte, los lenguajes de alto nivel son más accesibles para el ser humano e incluso menos dependientes del tipo de hardware, pero deben de ser a su vez traducidos a lenguaje de de bajo nivel. ");
print("\n Lenguajes compilados e interpretados. ");
print("\n Los lenguajes de alto nivel interactúan con los sistema de cómputo de dos formas. ");
print("\n     Mediante un compilador, el cual traduce el código de un programa a lenguaje de bajo nivel, dando por resultado un 'archivo binario' el cual es susceptible de ser ejecutado. ");
print("\n     Mediante un intérprete, el cual ejecuta de inmediato las instrucciones que se ingresan. ");
print("\n Por lo general los lenguajes compilados son más rápidos y consumen menos recursos que los lenguajes interpretados en vista de que el archivo resultante es código de bajo nivel, mientras que los lenguajes interpretados deben seguir un proceso a través de varios niveles de abstracción hasta que las instrucciones son ejecutadas por el sistema. ");
print("\n Python es un lenguaje interpretado de alto nivel. ");
║     #######################################################################                                             ║
print(input("continuar?"));
limpiar();
║     #######################################################################                                             ║
print("* * * * * Ariel sinoptico* * * * * ");
print("\n * Programar, manipulacion de datos(objetos) tras su ingreso hasta su salida");
print("\n     Un lenguaje es un conjunto de cadenas de símbolos con los que se pueden crear mensajes. De ese modo los mensajes son transmitidos de un emisor a un receptor. Aún cuando en la naturaleza se pueden identificar ciertos lenguajes, los seres humanos hemos desarrollado lenguajes de diversos tipos y gran complejidad. ");
print("\n     Los lenguajes constan principamente de la gramática, la cual trata sobre la construcción del lenguaje, y la semántica, la cual trata sobre el significado del lenguaje. ");
print("\n        A su vez, la gramática consta de: ");
print("\n             Morfología: cómo se construyen las notaciones (género, tiempos, declinaciones). ");
print("\n            Sintaxis: cómo se deben escribir las notaciones (orden, estructura). ");
print("\n * Nombre, es la referencia de un dato en un tiempo y espàcio");
print("\n     Nombre : en =/= espacios ,  =  tiempo de ejecucion =/= datos");
print("\n     Nombre : en  =  espacios , =/= tiempo de ejecucion =/= datos");
print("\n * Objeto, es su espacio con nombre. Individualidad, con caracteristicas");
print("\n     es su materialización de algo incluso un dato");
print("\n     Posee atributos propios o heredados");
print("\n     Genera acciones propias o heredadas");
print("\n * Funcion-Metodo-Accion-Tarea-Proceso-Verbo");
print("\n     Es el verbo o accion perteneciente a un objeto");
print("\n     Los métodos son bloques de código (o funciones) de una clase que se utilizan para definir el comportamiento de los objetos.");
print("\n * Atributos definen las características propias del objeto y modifican su estado. Son datos asociados a las clases y a los objetos creados a partir de ellas.");
print("\n     De ello, se deducen los dos tipos de atributos o de variables existentes: variables de clase y variables de instancia (objetos).");
print("\n Tanto para acceder a los atributos como para llamar a los métodos se utiliza el método denominado de notación de punto que se basa en escribir el nombre del objeto o de la clase seguido de un punto y el nombre del atributo o del método con los argumentos que procedan: clase.atributo, objeto.atributo, objeto.método([argumentos]).");
print("\n * Instanciar, es crear objetos desde una clase.");
print("\n * Clase, es el razonamiento abstracto de un objeto. Trabajo en distintos capas, en equipo, en grupo, Fron end orientada (al usuario)/ back end (orientada al proceso)");
print("\n * Las clases en este contexto permiten definir los atributos y el comportamiento, mediante métodos, de los objetos de un programa. Una clase es una especie de plantilla o prototipo que se utiliza para crear instancias individuales del mismo tipo de objeto.");
print("\n * Ambito, es una region en el espacio donde los nombres (cuyos datos busco) son accesibles directamente.(Recordad que puede haber el mismo nombre como atributo como accion y en distintos ambitos");
print("\n * Ambito, es observable por estructuras de tabulacion");
print("\n ");
print("\n * Un espacio con un nombre hereda del Nombre ser la referencia a un dato en un tiempo y espàcio.");
print("\n     Si en el espacio nombrado su dato No cambia durante el tiempo de ejecucion se denomina * constante (constantes, tuple etc)");
print("\n     Si en el espacio nombrado su dato Si cambia durante el tiempo de ejecucion se denomina * variable (variable, lista, diccionario, etc");
print("\n     puede haber muchos espacio nombrado igual en distintos ambitos y sus datos podran ser distintos o no");
print("\n     Mutable: su contenido (o dicho valor) puede cambiarse en tiempo de ejecución.");
print("\n     Inmutable: su contenido (o dicho valor) no puede cambiarse en tiempo de ejecución.\n");
print("\n * Una variable es espacio que tendra un nombre para poder acceder a ella y sus caracteristicas seran dadas por el dato que se incorpore (* tipeado dinamico)");
print("\n * Una variable de clase es compartida por todas las instancias de una clase. Se definen dentro de la clase (después del encabezado de la clase) pero nunca dentro de un método. Este tipo de variables no se utilizan con tanta frecuencia como las variables de instancia.");
print("\n * Una variable de instancia se define dentro de un método y pertenece a un objeto determinado de la clase instanciada. ");
print("\n ");
print(input("continuar?"));
print("\n");
print("\n     Mutable: su contenido (o dicho valor) puede cambiarse en tiempo de ejecución.");
print("\n     Inmutable: su contenido (o dicho valor) no puede cambiarse en tiempo de ejecución.\n");
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
print(input("continuar?"));
print("https://pythonprogramming.net/");
print("http://docs.python.org.ar/tutorial/3/classes.html");
print("https://pythonista.io/cursos/py101");
print("Características de Python.");
print("\n");
print("\n A lo largo de estos cursos se explorarán y aprovecharán las características que hacen de Python un lenguaje tan popular y poderoso.");
print("\n ");
print("\n     Sintaxis muy clara y legible.");
print("\n     Fuerte capacidad de introspección.");
print("\n     Orientación a objetos intuitiva.");
print("\n     Expresión del código procedimental.");
print("\n     Altamente modular, soporta paquetes jerárquicos.");
print("\n     Enfocado en el uso de excepciones para el manejo de errores.");
print("\n     Tipos de datos dinámicos de muy alto nivel.");
print("\n     Extensa biblioteca estándar (STL) y módulos de terceros para prácticamente todas las tareas.");
print("\n     Extensiones y módulos fácilmente escritos en C, C + + (o Java para Jython, o. NET para IronPython).");
print("\n     Integrable dentro de las aplicaciones como una interfaz de scripting.");
print("\n ");
print(input("continuar?"));
print("\n Aplicaciones de Python.");
print("\n ");
print("\n Al ser un lenguaje multipropósito y altamente portable, Python se ha utilizado para desarrollar:");
print("\n ");
print("\n     Aplicaciones de escritorio.");
print("\n     Aplicaciones web.");
print("\n     Análisis de datos.");
print("\n     Administración de servidores.");
print("\n     Seguridad y análisis de penetración.");
print("\n     Cómputo en la nube.");
print("\n     Cómputo científico.");
print("\n     Análisis de lenguaje natural.");
print("\n     Visión artificial.");
print("\n     Animación, videojuegos e imágenes generadas por computadora.");
print("\n     Aplicaciones móviles.");
print(input("continuar?"));
print("\n ");
print("\n Distribuciones: ");
print(" ----------------- ");
print("\n Python ya viene con una gran biblioteca estándar, sin embargo existen algunas 'distribuciones' que pretenden extender al lenguaje con propósitos particulares. Aquí es posible consultar las diversas distribuciones de Python. ");
print("\n Instalación: ");
print(" -------------- ");
print(" Las principales distribuciones de GNU/Linux, los sistemas *BSD, así como Mac OS X y la mayoría de los UNIX vienen al menos con Python 2 preinstalado. Del mismo modo, las principales distribuciones de GNU/Linux cuentan con paquetes de instalación de Python 3. ");
print("\n Las versiones más recientes de Python pueden ser descargadas desde el sitio principal de Python incluyendo binarios para Mac OS X y Windows e incluso es posible descargar el código fuente. ");
print("\n  ");
print("\n NOTA Anaconda es una distribución de Python 2 y Python 3 especializada en cómputo científico, sin embargo es de muy fácil instalación y gestión tanto en Windows como en Mac OS X y GNU/Linux. Es una alternativa muy recomendable a las versiones oficiales de Python. ");
print("\n Breve introducción a los lenguajes de programación. ");
print("\n Un lenguaje es un conjunto de cadenas de símbolos con los que se pueden crear mensajes. De ese modo los mensajes son transmitidos de un emisor a un receptor. Aún cuando en la naturaleza se pueden identificar ciertos lenguajes, los seres humanos hemos desarrollado lenguajes de diversos tipos y gran complejidad. ");
print("\n Los lenguajes constan principamente de la gramática, la cual trata sobre la construcción del lenguaje, y la semántica, la cual trata sobre el significado del lenguaje. ");
print("\n  ");
print("\n A su vez, la gramática consta de: ");
print("\n     Morfología: cómo se construyen las notaciones (género, tiempos, declinaciones). ");
print("\n     Sintaxis: cómo se deben escribir las notaciones (orden, estructura). ");
print("\n  ");
print(input("continuar?"));
limpiar();
╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                                        ║
║           Unidad 1 -¿Qué es Python?                                                                                    ║
║                 * Instalación y configuración                                                                          ║
║                 * Errores sintácticos y lógicos                                                                        ║
║                 * Programación secuencial                                                                              ║
║                 * Estructuras condicionales simples, compuestas y anidadas                                             ║
║                 * Estructuras repetitivas                                                                              ║
║                                                                                                                        ║
╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
print("Gracias");
