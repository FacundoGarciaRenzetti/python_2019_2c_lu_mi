from Estructura import *
nuevo(0,"inicio");
#################################################################
import math
def Echos():
	#Con tab colocaremos aqui las precticas hechas
	pass
print("""
╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                                        ║
║                                   Bucles // while                                                                      ║
║                                                                                                                        ║
╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
""");
nuevo(0,"inicio");
#################################################################
#Clase_While_Ej_01 
contador = 1
while contador<10:
	print (contador);
	contador +=1
print ("FIN");
nuevo(1);
#################################################################
#Clase_While_Ej_02
edad=0
print ("venta de alcohol en boliches");
edad=int(input("ingrese su edad :"));
while edad<18:
	print ("Cometio un error al ingresar la edad o es menor y debe retirarse");
	edad=int(input("ingrese su edad :"));
else:
	print("que desea beber.......fin....");
nuevo(2);
#################################################################
#Clase_While_Ej_03
print(" break" );
print ("venta de alcohol en boliches");
edad=int(input("ingrese su edad :"));
while edad<18:
	print ("Cometio un error al ingresar la edad o es menor debe ingresar un valor'<10' y retirarse");
	edad=int(input("ingrese su edad :"));
	if edad<=10:
		print ("toma una cindor y Adios");
		break
else:
	print("que desea beber.......fin....");
nuevo(3);
#################################################################
#Clase_While_Ej_04
print("solos rehacer el ej anterior 10 intentos");
nuevo(4);
#################################################################
#Clase_While_Ej_05
valor=0
print("Inicio ej004_2_5 - math");
valor=int(input("Ingrese numero para sacar raiz cuadrada:"));
while valor<0:
	valor=int(input("Ingreso un numero negativo. Ingrese un numero para sacar raiz cuadrada:"));
resultado = math.sqrt(valor);
print ("la raiz cuadrada de :"+str(valor));
print ("son : + -"+str(resultado));
nuevo(5);
#################################################################
#Clase_While_Ej_06
arroba = False
for i in "email_@hotmail.com":
	print ("valor del string "+str(i));
	if str(i)=="@":
		arroba = True
if arroba==True:
	print ("tiene @ puede ser mail");
else:
	print ("No puede ser mail");
nuevo(6);
#################################################################
#Clase_While_Ej_07
arroba = False
for i in "email_@hotmail.com":
	print ("valor del string "+str(i));
	if str(i)=="@":
		arroba = True
		break
if arroba==True:
	print ("tiene @ puede ser mail");
else:
	print ("No puede ser mail");
nuevo(7);
#################################################################
#Clase_While_Ej_08
print ("verificar si tiene @ y como minimo un punto.");
nuevo(8);
#################################################################
#Clase_While_Ej_09
print ("verificar si tiene mas de un @ y como minimo un punto.");
nuevo(9);
#################################################################
#Clase_While_Ej_10
print ("verificar si tiene mas de un @ y como minimo un punto. y caracteres alfanumericos");
nuevo(10);
#################################################################
#Clase_While_Ej_11
multiplica =[]
for n in range(1,16):
	multiplica.append(n**3)
print("Ej 1",multiplica)
multiplica = [n**3 for n in range(1,16)]
print("Ej 2",multiplica)
nuevo(11);
#################################################################
#Clase_While_Ej_12
print("Ej 1",multiplica)
for i in range(1, 11):
    for n in range(1, 11):
        multiplica.append(i*n)
print(multiplica)

multiplica = [i*n for i in range(1,11) for n in range(1,11)]
print("Ej 2",multiplica)
print("Ej 3", [i*n for i in range(1,11) for n in range(1,11)])
nuevo(12);
#################################################################
#Clase_While_Ej_13
matrix = [
	[1, 2, 3, 4],
	[5, 6, 7, 8],
	[9, 10, 11, 12],]
transpose = []
for i in range(4):
	temp = []
	for row in matrix:
		temp.append(row[i])
	transpose.append(temp)
#transpose = [[row[n] for row in matrix] for n in range(4)]
print(transpose)

nuevo(13);
#################################################################
#Clase_While_Ej_14
cadena = "Python"
for caracter in cadena:# Recorrer los caracteres de una cadena:
    print(caracter)

for caracter in cadena[::-1]:# Recorrer caracteres de cadena anterior, en sentido inverso.
    print(caracter)

lista = ['una', 'lista', 'es', 'un', 'iterable']# Recorrer los elementos de una lista
for palabra in lista:
    print(palabra)

for palabra in lista[::-1]:# Recorrer los elementos de la lista anterior, al revés
    print(palabra)

for indice in range(len(lista)):# Obtener índice para recorrer todos los elementos de la lista
    print (indice, lista[indice])

artistas = { 'Lorca' : 'Escritor', 'Goya' : 'Pintor'}# Recorrer las claves de un diccionario
for clave, valor in artistas.items():
    print(clave,':',valor)

for linea in open("datos.txt"):# Leer las líneas de un archivo de texto, una a una
    print(linea.rstrip())
nuevo(14);
#################################################################
#Clase_While_Ej_15

print("""LEER \n https://python-para-impacientes.blogspot.com/2015/08/bucles-eficientes-con-itertools.html \n
Funciones que devuelven iterables infinitos
Agrupa un conjunto de funciones Itertools que devuelven un iterable que no se interrumpirá si no se fuerza un final, por ejemplo, cuando se cumpla una determinada condición.

count()
-------
Devuelve un objeto iterable en la que el primer elemento tendrá el valor inicial (start) y los sucesivos se irán incrementando/decrementado con el valor del paso (step), de manera ininterrumpida.
									itertools.count(start=0 [, step=1])
En el siguiente ejemplo cuando se alcanza un valor determinado se fuerza la interrupción del bucle:
""");
from itertools import *
for valor in count(5, 3):
    print(valor, end = ' ')
    if valor == 20: break
print("""
cycle()
-------
Devuelve un objeto iterable con los elementos (de principio a fin) del iterable de entrada, que se reproducirán una y otra vez mientras no se fuerce un final.
									itertools.cycle(iterable)
cycle() con una cadena:
-----------------------
""");
contador = 0 
for elemento in cycle("Python"):
    print(elemento, end = ' ')
    contador += 1
    if contador == 12: break
print("""
cycle() con una lista:
----------------------
""");
contador = 0
for elemento in cycle([10, 12, 14]):
    print(elemento, end = ' ')
    contador += 1
    if contador == 5: break
print("""
cycle() con un diccionario:
-----------------------
""");
contador = 0
for elemento in cycle({'x':1, 'y':2, 'z': 3}):
    print(elemento, end = ' ')
    contador += 1
    if contador == 9: break
print("""
repeat()
--------
Devuelve el objeto completo, una y otra vez, de manera indefinida a menos que se especifique el número de veces (times) que hay que ejecutar el bucle.
									itertools.repeat(object[, times])
repeat() con un entero:
-----------------------
""");
for elemento in repeat(3, 5):
    print(elemento, end = ' ')
print("""
repeat() con map():
-----------------------
""");
print(list(map(pow, range(5), repeat(3))))
print("""
Agrupa funciones del módulo Itertools que devuelven iterables que finalizan con la secuencia de entrada más corta.
accumulate()
------------
La función devuelve un iterable con sumas acumuladas o totales acumulados derivados de los resultados obtenidos al aplicar alguna función (func).
Los elementos del objeto iterable se evalúan tomando el primer elemento con el segundo; después el resultado obtenido de ambos elementos con el tercero y así sucesivamente.
									itertools.accumulate(iterable[, func])
La función que se incluya debe tener dos argumentos (uno por cada elemento que se evalúa) y los elementos de la entrada iterable, necesariamente, serán del tipo que acepte dicha función. Además, si la entrada iterable está vacía la salida también lo estará.
accumulate() con la función implícita que acumula sumas:
--------------------------------------------------------
""");
for acumulado in accumulate([1, 2, 3, 4, 5]):
    print(acumulado, end = ' ')
print("""
accumulate() con función max para 'acumular' el valor máximo:
-------------------------------------------------------------
""");
for valor_maximo in accumulate([1, 3, 2, 5, 4], max):
    print(valor_maximo, end = ' ')
print("""
acumulate() con función lambda:
-------------------------------
""");
for diferencia in accumulate([10, 30, 50], lambda a, b: b-a):
    print(diferencia, end = ' ')
print("""
chain()
-------
La función devuelve un iterable construido con todos los elementos de los objetos iterables de entrada.
									itertools.chain(*iterables)""");
for elemento in chain([1, 2], [3, 4, 5]):
    print(elemento ** 2, end = ' ')
print("""

chain.from_iterable()
---------------------
Es similar a chain() pero solo admite un argumento iterable.
									classmethod chain.from_iterable(iterable)""");
for elemento in chain.from_iterable(["un","dos","tres"]):
    print(elemento, end = ' ')

print("""
compress()
----------
La función devuelve un iterable a partir de los elementos de data que tienen cada uno un valor asociado en selectors que actúan como un filtro. Todos los elementos con el valor True o 1 serán los utilizados para construir el iterable. El proceso finaliza cuando se agoten los elementos en data o en selectors.
									itertools.compress(data, selectors)""");

for elemento in compress("iterable", [1,0,1,0,1,0,0,1]):
    print(elemento, end = ' ')
print("""
dropwhile()
-----------
Construye un iterable a partir del iterable de entrada sin devolver ningún elemento hasta que la condición del predicado sea falsa. Después de ese momento se devuelven todos los elementos que resten.

									dropwhile(predicate, iterable)""");
for elemento in dropwhile(lambda valor: valor == 'x', 
                          ['x','x','y','z','x','x']):
    print(elemento, end = ' ')    
print("""
filterfalse()
-------------
Esta función devuelve un iterable con los elementos del iterable de entrada que no cumplan la condición expresada en el predicado. Si el predicado es None devuelve los elementos con valor False o 0.

									itertools.filterfalse(predicate, iterable)""");
for elemento in filterfalse(lambda valor: valor == 'x', 
                            ['x','x','y','z','x','x']):
    print(elemento, end = ' ')
print("""
groupby()
---------
Devuelve un iterable con los elementos del iterable de entrada agrupados por el dato utilizado como clave (key).
									itertools.groupby(iterable, key=None)
groupby() con lista ordenada:
----------------------------
En el siguiente ejemplo la lista de tuplas contiene ciudades de diferentes países ordenados alfabéticamente:""");
ciudades = [("Bolivia", "Sucre"), ("Bolivia", "La Paz"), 
            ("Chile", "Valdivia"), ("Chile", "Arica"), 
            ("España", "Cádiz"), ("Perú", "Cusco"), 
            ("Perú", "Lima")]
for clave, grupo in groupby(ciudades, lambda x: x[0]):
    print(clave, list(grupo))
"""
Salida:
Bolivia [('Bolivia', 'Sucre'), ('Bolivia', 'La Paz')]
Chile [('Chile', 'Valdivia'), ('Chile', 'Arica')]
España [('España', 'Cádiz')]
Perú [('Perú', 'Cusco'), ('Perú', 'Lima')]
"""
print("""
groupby() y itemgetter() con lista desordenada:
-----------------------------------------------
En el siguiente ejemplo la lista de tuplas contiene ciudades de diferentes países que no están ordenados alfabéticamente.
Para que se pueda agrupar la información de cada país es necesario ordenar la lista. Para ello se utiliza la función sorted() con la función itemgetter() del módulo operator. Esta función permite establecer el criterio de ordenación. En el ejemplo, como cada tupla contiene dos elementos (país, ciudad) itemgetter(0) establece que el criterio de orden será el primer elemento de la tupla, es decir, el país.
""");
from operator import itemgetter
ciudades = [("Perú", "Cusco"), ("Chile", "Valdivia"), 
            ("Bolivia", "Sucre"), ("Bolivia", "La Paz"), 
            ("España", "Cádiz"), ("Chile", "Arica"), 
            ("Perú", "Lima")]

ciudades = sorted(ciudades, key=itemgetter(0))
for clave, grupo in groupby(ciudades, itemgetter(0)):
    print(clave, list(grupo))

"""
Salida:
Bolivia [('Bolivia', 'Sucre'), ('Bolivia', 'La Paz')]
Chile [('Chile', 'Valdivia'), ('Chile', 'Arica')]
España [('España', 'Cádiz')]
Perú [('Perú', 'Cusco'), ('Perú', 'Lima')]
"""
print("""
islice()
--------
La función devuelve un iterable con una selección de elementos del iterable de entrada. Permite retornar un número de elementos partiendo desde el inicio del iterable o un rango específico.
									itertools.islice(iterable, stop)

Devuelve elementos partiendo desde el comienzo:
""");
for elemento in islice("KLMNOPQRST", 5):
    print(elemento, end = ' ')
print("""
									itertools.islice(iterable, start, stop [, step])
Devuelve los elementos que hay desde una posición inicial a una final:
""");
for elemento in islice("KLMNOPQRST", 5, 7):
    print(elemento, end = ' ') 

print("""
Devuelve los elementos que hay desde una posición inicial a una final, separados entre sí por un valor fijo de elementos:
""");
for elemento in islice("1234567890", 0, 8, 2):
    print(elemento, end = ' ') 

print("""
starmap()
---------
Construye un objeto iterable aplicando una función que utiliza como argumentos los elementos del iterable de entrada, devolviendo una secuencia con los resultados obtenidos.
									itertools.starmap(function, iterable)
En el ejemplo se recorre una lista de tuplas y se construye el iterable a devolver con el valor más alto de los elementos que hay en cada una de ellas:""");
for elemento in starmap(max, 
                        [(10,2),(2,32),(63,54),(4,45)]):
    print(elemento, end = ' ') 
print("""
takewhile()
-----------
Construye un iterable a partir del iterable de entrada devolviendo elementos mientras la condición del predicado es verdadera. En el momento que cambie a falsa no devolverá más elementos aunque exista alguno que cumpla la condición.
									itertools.takewhile(predicate, iterable)
En el ejemplo se recorre una lista de cadenas comprobando si su longitud es igual a 1:""");
for elemento in takewhile(lambda x: len(x) == 1, 
                          ['a','b','ab','bc','c']):
    print(elemento, end = ' ')
print("""
tee()
-----
Devuelve varios iterables independientes (por defecto, 2) sobre la base de una sola entrada original.
									itertools.tee(iterable, n=2)""");
a, b = tee([1,2,3,4])
for elemento1, elemento2 in zip(a, b):
    print("a:", elemento1)
    print("b:", elemento2)

print("""
zip_longest()
-------------
Devuelve un iterable que agrega elementos de cada uno de los iterables de entrada. Si los iterables de entrada tienen distinta longitud se completará utilizando el valor de fillvalue, hasta que se alcance el final del iterable que tenga una longitud mayor.
									itertools.zip_longest(*iterables, fillvalue=None)""");

for elemento in zip_longest(['x','y','z'], ['0','1'], 
                            fillvalue='#'):
    print(elemento, end = ' ')
nuevo(15);
#################################################################
#Clase_While_Ej_16
print("""
Generadores para combinatoria
=============================
Agrupa una serie de funciones que generan iterables como resultado de operaciones de combinatoria en las que se utilizan otros iterables de entrada.

product()
---------
Realiza el producto cartesiano con los elementos de los iterables de entrada devolviendo un iterable basado en tuplas con el resultado.
									itertools.product(*iterables, repeat=1)""");
for elemento in product("XYZ", "mn"):
    print(elemento, end = ' ')

for elemento in product("X", repeat = 4):
    print(elemento, end = ' ')

for elemento in product("XYZ", repeat = 2):
    print(elemento, end = ' ')

print("""
permutations()
--------------
Devuelve un objeto iterable basado en tuplas con permutaciones de longitud r a partir de los elementos del objeto de entrada.
									itertools.permutations(iterable, r=None)""");
for elemento in permutations("123", 2):
    print(elemento, end = ' ')
print("""
combinations()
--------------
Devuelve un objeto iterable basado en tuplas con las combinaciones sin repetición posibles, de una longitud r, a partir de los elementos del objeto de entrada.
									itertools.combinations(iterable, r)""");
for elemento in combinations("123", 2):
    print(elemento, end = ' ')
print("""
combinations_with_replacement()
-------------------------------
Devuelve un objeto iterable basado en tuplas con las combinaciones con repetición posibles, de una longitud r, a partir de los elementos del objeto de entrada.
									itertools.combinations_with_replacement(iterable, r)""");
for elemento in combinations_with_replacement("123", 2):
    print(elemento, end = ' ')
nuevo(16);
#################################################################
