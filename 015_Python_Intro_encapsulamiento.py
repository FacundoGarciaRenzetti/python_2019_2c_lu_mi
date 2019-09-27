from Estructura import *
nuevo(0,"inicio");
#################################################################
def Ej_ya_hechos():
	#Con tab colocaremos aqui las precticas hechas
	pass
print("""
╔══════════════════════════════════════════════════════════════════════════════════╗░ ▒ ▓ ┌┐┤│├└┘┴┬─┼╔╗╠╬╣║╚╝╩╦═¤
║                                                                                  ║
║                                     CLASES                                       ║
║                                    --------                                      ║
║                                                                                  ║
║          __init__(self, ...)                                                     ║
║              This method is called just before the newly created object is       ║
║              returned for usage.                                                 ║
║                                                                                  ║
║          __del__(self)                                                           ║
║              Called just before the object is destroyed (which has               ║
║              unpredictable timing, so avoid using this)                          ║
║                                                                                  ║
║          __str__(self)                                                           ║
║              Called when we use the print function or when str() is used.        ║
║                                                                                  ║
║          __lt__(self, other)                                                     ║
║              Called when the less than operator (<) is used. Similarly,          ║
║               there are special methods for all the operators (+, >, etc.)       ║
║                                                                                  ║
║          __getitem__(self, key)                                                  ║
║              Called when x[key] indexing operation is used.                      ║
║                                                                                  ║
║          __len__(self)                                                           ║
║              Called when the built-in len() function is used for                 ║
║              the sequence object.                                                ║
║                                                                                  ║
╠══════════════════════════════════════════════════════════════════════════════════╣
║                                                                                  ║
║                           Clases                                                 ║
║                                                                                  ║
║                           Class (object) Padre                                   ║
║                                                                                  ║
║                           Objetos                  	                           ║
║                                  estado                                          ║
║                                  propiedades                                     ║
║                                  comportamiento                                  ║
║                                                                                  ║
║                           Instancia                                              ║
║                                                                                  ║
║                           Modularizacion                                         ║
║                                                                                  ║
║                           Encapsulado                                            ║
║                                                                                  ║
║                           Herencia                                               ║
║                                                                                  ║
║                           Polimorfismo                                           ║
║                                                                                  ║
║                           def funcion (general)                                  ║
║                           def metodo (clase)                                     ║
║                                                                                  ║
╚══════════════════════════════════════════════════════════════════════════════════╝
""")
nuevo(0,"inicio");
#################################################################
#Clase_Clases_01 
class Mascota:
	def __init__(self,nombre, especie=None, raza=None, patas=4,  edad=None):
		self.nombre=nombre;
		self.especie=especie;	
		self.raza=raza;
		self.patas=patas;#self.__patas=patas;
		self.edad=edad;
	def nombrar(self, dato_nombre):
		self.nombre =dato_nombre;
	def datar(self,especie=None, raza=None, patas=4, nombre=None, edad=None):
		self.especie=especie;	
		self.raza=raza;
		self.patas=patas;#self.__patas=patas;
		self.nombre=nombre;
		self.edad=edad;
	def mostrar(self):
		print (f"Mi  mascota tiene las sig caracteristicas: ",self.especie,self.raza,self.patas,self.nombre,self.edad);
		#print (f"Mi  mascota tiene las sig caracteristicas: ",self.especie,self.raza,self.__patas,self.nombre,self.edad);
perro= Mascota("Wanda","Can","Weimaraner",4,6)
gato1= Mascota("Manchas","Felino","calle",4,5)
gato2 =Mascota("Grey")
perro.mostrar()
gato1.mostrar()
gato2.mostrar()
gato2.nombre="Grey"
gato2.especie="Felino"
gato2.raza="calle"
gato2.patas=4
gato2.edad=2
gato2.mostrar()
x=input("cuntinuar?")
gato2.nombre="Grey"
gato2.especie="Felino"
gato2.raza="calle"
gato2.patas=8#<--------------------------¿como?
gato2.edad=200#<--------------------------¿como?
gato2.mostrar()

x=input("cuntinuar?")
gato2.datar (nombre="Grey", especie="Felino", raza="calle", patas=4,  edad=2)
gato2.mostrar()
gato2.datar (nombre="Grey", especie="Felino", raza="angora", patas=8,  edad=2)
#                                                                  ^      
#                                                                  |______________¿como?
gato2.mostrar()

nuevo(0,"fin");
#################################################################
