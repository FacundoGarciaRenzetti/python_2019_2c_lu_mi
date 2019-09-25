from Estructura import *
nuevo(0,"inicio");
#################################################################
def Echos():
	#Con tab colocaremos aqui las precticas hechas
	pass
print("""
╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                                        ║
║                                Manejo de errores                                                                       ║
║                                                                                                                        ║
╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

https://www.w3schools.in/python-tutorial/gui-programming/


try:
     cociente = dividendo / divisor");
 except:
     print ("No se permite la división por cero");
     """);

nuevo(0,"inicio");
#################################################################
#Clase_Errores_Ej_001
try:
	maximo = int(input("ingrese la cantidad de numeros :"));
except:
	print ("ha ocurrio un Error. pero sigo von un valor = 10");
	maximo = 10
if maximo>0:
	def numeros_pares(maximo):
		contador = 1
		lista_de_pares=[]
		while contador<=maximo:
			lista_de_pares.append(contador*2);
			contador+=1
		return lista_de_pares
	print (numeros_pares(maximo));
nuevo(1);
#################################################################
#Clase_Errores_Ej_002
valor1=0,1
valor2=0,1
while True:
	try:
		valor1=float(input("valor 1 : "));
		valor2=float(input("valor 2 : "));
		break
	except ValueError:
		print("Error. solo nomeros");
def resultado_suma(valor_1,valor_2):
	return valor_1+valor_2
def resultado_resta(valor_1,valor_2):
	return  valor_1-valor_2
def resultado_multiplica(valor_1,valor_2):
	return valor_1*valor_2
def resultado_divide(valor_1,valor_2):
	
	try:
		return valor_1/valor_2
	except ZeroDivisionError:
		print ("No dividiras por 0");
		return ("error...... pero sigo");
nuevo(2);
#################################################################
#Clase_Errores_Ej_003
import math




def resultado_suma(valor_1,valor_2):
	return valor_1+valor_2
def resultado_resta(valor_1,valor_2):
	return  valor_1-valor_2
def resultado_multiplica(valor_1,valor_2):
	return valor_1*valor_2
def resultado_divide(valor_1,valor_2):
	try:
		return valor_1/valor_2
	except ZeroDivisionError:
		print ("No dividiras por 0");
		return ("error...... pero sigo");
def resultado_portenciacion(valor_1,valor_2):
	return valor_1**valor_2
def resultado_radicacion2(valor_1,valor_2):
	return  math.sqrt(valor_2);
def resultado_porcentage(valor_1,valor_2):
	return valor_1/valor_2*100
def resultado_cociente(valor_1,valor_2):
	return valor_1//valor_2
def resultado_resto(valor_1,valor_2):
	return valor_1%valor_2

print ("resultado suma : "+str(resultado_suma(valor1,valor2)));
print ("resultado resta : "+str(resultado_resta(valor1,valor2)));
print ("resultado multiplicacion : "+str(resultado_multiplica(valor1,valor2)));
print ("resultado divicion : "+str(resultado_divide(valor1,valor2)));
print ("resultado portenciacion : "+str(resultado_portenciacion(valor1,valor2)));
print ("resultado radicacion2 : "+str(resultado_radicacion2(valor1,valor2)));
print ("resultado porcentage : "+str(resultado_porcentage(valor1,valor2)));
print ("resultado cociente : "+str(resultado_cociente(valor1,valor2)));
print ("resultado resto : "+str(resultado_resto(valor1,valor2)));
nuevo(3);
#################################################################
#Clase_Errores_Ej_004
from Python_Metodos_propia import *
valor1=0,1
valor2=0,1
while True:
	try:
		valor1=float(input("valor 1 : "));
		valor2=float(input("valor 2 : "));
		break
	except ValueError:
		print("Error. solo nomeros");
print ("resultado suma : "+str(resultado_suma_metodo(valor1,valor2)));
print ("resultado resta : "+str(resultado_resta_metodo(valor1,valor2)));
print ("resultado multiplicacion : "+str(resultado_multiplica_metodo(valor1,valor2)));
print ("resultado divicion : "+str(resultado_divide_metodo(valor1,valor2)));
print ("resultado portenciacion : "+str(resultado_portenciacion_metodo(valor1,valor2)));
print ("resultado radicacion2 : "+str(resultado_radicacion2_metodo(valor1,valor2)));
print ("resultado porcentage : "+str(resultado_porcentage_metodo(valor1,valor2)));
print ("resultado cociente : "+str(resultado_cociente_metodo(valor1,valor2)));
print ("resultado resto : "+str(resultado_resto_metodo(valor1,valor2)));
nuevo(4);
#################################################################
#Clase_Errores_Ej_005

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
nuevo(5);
#################################################################
#Clase_Errores_Ej_006
try:
	x = 10
	y = 0
	print(x/y)
except Exception as e:
	print("Exeception occured:{}".format(e))
finally:
	x = 10
	y = 2
	print(x/y)
print ("continuo")
nuevo(7);
#################################################################
#Clase_Errores_Ej_007
print("""solos
try:
    # aquí ponemos el código que puede lanzar excepciones
except:
    # ERROR de sintaxis, esta sentencia no puede estar aquí,
    # sino que debería estar luego del except IOError.
except IOError:
    # Manejo de la excepción de entrada/salida
""")
nuevo(8);
#################################################################
#Clase_Errores_Ej_008
print("""solos
#try:
#    archivo = open("miarchivo.txt")
    # procesar el archivo
#except IOError:
#    print "Error de entrada/salida."
    # realizar procesamiento adicional
#except:
    # procesar la excepción
#finally:
# 	si el archivo no está cerrado hay que cerrarlo
#   if not(archivo.closed):
#	archivo.close()
""");
nuevo(9);
#################################################################
#Clase_Errores_Ej_010
lista = [10, 100, 1000, 10000]
iterador = iter(lista)
try:
    while True:
        print(iterador.__next__())        
except StopIteration:
    print("Se ha alcanzado el final de la lista")
nuevo(10);
#################################################################
#Clase_Errores_Ej_011
import mysql.connector#<------------------------------------------------debe estar disponible
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Electronics',
                                         user='pynative',
                                         password='pynative@#29')

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Your connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
nuevo(11,"fin");
#################################################################
