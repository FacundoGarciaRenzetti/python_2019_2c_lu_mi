from Estructura import *
nuevo(0,"inicio");
#################################################################
def Ej_ya_hechos():
	#Con tab colocaremos aqui las precticas hechas
	pass
print("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║                                                                                  ║
║                              Funciones y Metodos                                 ║
║                              -------------------                                 ║
║                                                                                  ║
║          Funciones    Description                                                ║
║                   lambda                                                         ║
║                                                                                  ║
║                                                                                  ║
║          Metodos son finciones dentro de clases donde se deberia instanciar      ║
║                   a la clase con self                                            ║
║                                                                                  ║
╠══════════════════════════════════════════════════════════════════════════════════╣
║                                                                                  ║
║                              Funciones,  Metodos                                 ║
║                                                                                  ║
║                                  y Generadores                                   ║
║                                                                                  ║
║                                                                                  ║
╚══════════════════════════════════════════════════════════════════════════════════╝

https://www.w3schools.com/python/python_ref_list.asp
https://www.w3schools.com/python/python_lists.asp
https://python-para-impacientes.blogspot.com/2014/02/programacion-funcional-funciones-de.html
https://python-para-impacientes.blogspot.com/2014/02/funciones.html
""")
nuevo(0,"inicio");
#################################################################
#Clase_Funciones_Ej_001
print("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║                                                                                  ║
║                              Funciones,  Metodos                                 ║
║                                                                                  ║
╚══════════════════════════════════════════════════════════════════════════════════╝
""")
#                          como funcion
def funcion (var_1, var_2):
	return (var_1 *var_2)
print (funcion (2,4))
mi_array=(3,6)
print (funcion (*mi_array))# ver el "*"
#                          como Metodo
class Clase1:# ver el nombre con mayuscula en su primer caracter que no debe ser numerico
	resultado= 0
	def metodo(self,var_1,var_2):
		self.var_1=  var_1
		self.var_2=  var_2
		self.resultado= (var_1 *var_2)
ej=Clase1()
ej.metodo(6,5)
print (ej.resultado)
nuevo(1);
#################################################################
#Clase_Funciones_Ej_002
print("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║                                                                                  ║
║                                     Metodos                                      ║
║                                                                                  ║
╚══════════════════════════════════════════════════════════════════════════════════╝
""")
class Clase2:# ver el nombre con mayuscula en su primer caracter que no debe ser numerico
	resultado= 0
	def __init__(self):#construye los objetos
		self.var_1=  0
		self.var_2=  0
	def metodo(self,var_1,var_2):
		self.var_1=  var_1
		self.var_2=  var_2
		self.resultado= (var_1 *var_2)

ej=Clase2()
print ("al inicio con valores 'self'",ej.resultado)
ej.metodo(6,5)
print ("al final con datos modificado por metodo",ej.resultado)
nuevo(2);
#################################################################
#Clase_Funciones_Ej_003
print("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║                                                                                  ║
║                                    Generadores                                   ║
║                                                                                  ║
╚══════════════════════════════════════════════════════════════════════════════════╝
""")
def Llenar_lista():
	salida=0
	dato_entrada = [1,2,3,4,5,6,7,8,9]
	for elementos in dato_entrada:
		salida+= int(elementos)**2
		print (elementos)
	print (salida)
Llenar_lista()
salida2=0
generada = (elementos for elementos in range(10))
for elementos in generada:
	salida2 += int(elementos)**2
	print (elementos)
print (salida2)

generada2 = (elementos for elementos in range(10) if elementos%20 == 0)
for elementos in generada2:
	salida2 += int(elementos)**2
	print (elementos)
print (salida2)

generada2 = (min(elementos,5) for elementos in range(10))
for elementos in generada2:
	salida2 += int(elementos)**2
	print (elementos)
print (salida2)

nuevo(3);
#################################################################
#Clase_Funciones_Ej_004
print("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║                                                                                  ║
║                                       Lambda                                     ║
║                                                                                  ║
╚══════════════════════════════════════════════════════════════════════════════════╝
""")

area_triangulo =lambda base,altura:(base*altura)/2
base = float(input("Ingrese la base :"))
altura = float(input("Ingrese la altura :"))
print(area_triangulo(base,altura))
nuevo(4);
#################################################################
#Clase_Funciones_Ej_005

class Counter:
	Count = 0   # This represents the count of objects of this class
	def __init__(self, name):
		self.name = name
		print (name, 'created')
		Counter.Count += 1
	def __del__(self):
		print (self.name, 'deleted')
		Counter.Count -= 1
		if Counter.Count == 0:
			print ('Last Counter object deleted')
		else:
			print (Counter.Count, 'Counter objects remaining')
x = Counter("First")
y = Counter("second")
del x

"""
Without the final del, you get an exception. Shouldn’t the normal cleanup process take care of this?

From the Python docs regarding __del__:

    Warning: Due to the precarious circumstances under which __del__() methods are invoked, exceptions that occur during their execution are ignored, and a warning is printed to sys.stderr instead. Also, when __del__() is invoked in response to a module being deleted (e.g., when execution of the program is done), other globals referenced by the __del__() method may already have been deleted. For this reason, __del__() methods should do the absolute minimum needed to maintain external invariants.

Without the explicit call to del, __del__ is only called at the end of the program, Counter and/or Count may have already been GC-ed by the time __del__ is called (the order in which objects are collected is not deterministic). The exception means that Counter has already been collectd. You can’t do anything particularly fancy with __del__.

There are two possible solutions here.

    1. Use an explicit finalizer method, such as close() for file objects.

        Use weak references.
"""
nuevo(5,"fin");
#################################################################









