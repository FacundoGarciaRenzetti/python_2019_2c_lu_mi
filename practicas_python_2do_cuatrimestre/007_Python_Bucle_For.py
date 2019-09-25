from Estructura import *
nuevo(0,"inicio");
#################################################################
def Echos():
	#Con tab colocaremos aqui las precticas hechas
	pass
print("""
╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                                        ║
║                                   Bucles // for                                                                        ║
║                                                                                                                        ║
╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
""");
nuevo(0,"inicio");
#################################################################
#Clase_For_Ej_01 
for i in range(5):
	print ("Valor "+str(i));
nuevo(1);
#################################################################
#Clase_For_Ej_02
for i in range(5,20):
	print ("Valor "+str(i));
for i in range(5,20,4):
	print ("Valor "+str(i));
nuevo(2);
#################################################################
#Clase_For_Ej_03
for i in [1,2,3,4,5]:
	print ("valor de la lista "+str(i));
nuevo(3);
#################################################################
#Clase_For_Ej_04
print("In II Lista");
for i in ["Nombre_1","Nombre_2","Nombre_3","Nombre_4"]:
	print ("valor de la lista "+str(i));
nuevo(4);
#################################################################
#Clase_For_Ej_05
for i in "casillaMail@hotmail.com":
	print ("valor del string "+str(i));
nuevo(5);
#################################################################
#Clase_For_Ej_06
arroba = False
for i in "casillaMail@hotmail.com":
	
	print ("valor del string "+str(i));
	if str(i)=="@":
		arroba = True
if arroba==True:
	print ("tiene @ puede ser mail");
else:
	print ("No puede ser mail");
nuevo(6);
#################################################################
#Clase_For_Ej_07
arroba = False
for i in "casillaMail@hotmail.com":
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
#Clase_For_Ej_08
print ("verificar si tiene @ y como minimo un punto.");
nuevo(8);
#################################################################
#Clase_For_Ej_09
print ("verificar si tiene mas de un @ y como minimo un punto.");
nuevo(9);
#################################################################
#Clase_For_Ej_10
print ("verificar si tiene mas de un @ y como minimo un punto. y caracteres alfanumericos");
nuevo(10);
#################################################################
#Clase_For_Ej_11
capitales = { "France":"Paris", "Netherlands":"Amsterdam", "Germany":"Berlin", "Switzerland":"Bern", "Austria":"Vienna"}
for pais in capitales:
	print("Aprendan: la capital de " + pais + " es " + capitales[pais])
nuevo(11,"fin");
#################################################################
