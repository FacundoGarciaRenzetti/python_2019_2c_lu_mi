from Estructura import *
nuevo(0,"inicio");
#################################################################
def Echos():
	#Con tab colocaremos aqui las precticas hechas
	pass
print("""
╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                                        ║
║                                    break  // continue // range                                                         ║
║                                                                                                                        ║
╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
""");
nuevo(0,"inicio");
#################################################################
#Clase_break/continue/range_Ej_01 
print("Inicio ej007_1 - for continue / break /else ");
cadena_de_caracteres=" "
cont_de_a =0
cont_de_b =0
cont_de_c =0
otras_letras =0
contador_de_letras = 0
cadena_de_caracteres=str(input("Ingrese una frase dato_2 # al final "));
for letra in cadena_de_caracteres:
	if letra==" ":
		continue
	contador_de_letras = contador_de_letras + 1
	if letra=="#":
		print ("break");
		fin=True
		break
	if letra=="a":
		cont_de_a +=1
	elif letra=="b":
		cont_de_b +=1
	elif letra=="c":
		cont_de_c +=1
	else:
		otras_letras +=1
else:
	fin=False
print (str("hay "+str(contador_de_letras)+" letras en" + str(cadena_de_caracteres)));
print (str("hay "+str(cont_de_a)+" 'A' en" + str(cadena_de_caracteres)));
print (str("hay "+str(cont_de_b)+" 'B' en" + str(cadena_de_caracteres)));
print (str("hay "+str(cont_de_c)+" 'C' en" + str(cadena_de_caracteres)));
print (str("hay "+str(otras_letras)+" 'otras letras' en" + str(cadena_de_caracteres)));
if fin:
	print("el programa se bloqueo con #");
else:
	print("el programa llego al fin");
nuevo(1);
#################################################################
#Clase_break/continue/range_Ej_02
Nombre_lista_1 = ["linea 1","linea 2","linea 3","linea 4","linea 5","linea 6","linea 7","linea 8","linea 9","linea 10"]
print("Inicio ej008_2");
for dato_1 in Nombre_lista_1:
  print(dato_1)
  if dato_1 == "linea 5":
    break
nuevo(2);
#################################################################
#Clase_break/continue/range_Ej_03
print('Exit the loop when dato_1 is "linea 5", but this time the break comes before the print:');
for dato_1 in Nombre_lista_1:
  if dato_1 == "linea 5":
    break
  print(dato_1)
nuevo(3);
#################################################################
#Clase_break/continue/range_Ej_04
print('The continue Statement');
print('With the continue statement we can stop the current iteration of the loop, and continue with the next:');
print('Do not print linea 5:');
for dato_1 in Nombre_lista_1:
	if dato_1 == "linea 5":
		print("hey UTN's aqui esta");
		continue
	print(dato_1)
nuevo(4);
#################################################################
#Clase_break/continue/range_Ej_05
print('The range() Function');
print('To loop through a set of code a specified number of times, we can use the range() function,');
print('The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.');
print('Using the range() function:');
for dato_1 in range(6):
  print(dato_1)
print('Note that range(6) is not the values of 0 to 6, but the values 0 to 5.');
nuevo(5);
#################################################################
#Clase_break/continue/range_Ej_06
print('The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):');
print('Using the start parameter:');
for dato_1 in range(2, 6):
  print(dato_1)
nuevo(6);
#################################################################
#Clase_break/continue/range_Ej_07
print('The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):');
print('Increment the sequence with 3 (default is 1):');
for dato_1 in range(2, 30, 3):
  print(dato_1)
print('Else in For Loop');
print('The else keyword in a for loop specifies a block of code to be executed when the loop is finished:');
nuevo(7);
#################################################################
#Clase_break/continue/range_Ej_08
print('Print all numbers from 0 to 5, and print a message when the loop has ended:');
for dato_1 in range(6):
  print(dato_1)
else:
  print("terminado")
nuevo(8);
#################################################################
#Clase_break/continue/range_Ej_09
print('Nested Loops');
print('A nested loop is a loop inside a loop.');
print('The "inner loop" will be executed one time for each iteration of the "outer loop":');
print("Print each adjective for every list:");
Nombre_lista_1 = ["linea 1","linea 2","linea 3","linea 4","linea 5","linea 6","linea 7","linea 8","linea 9","linea 10"]
Nombre_lista_2 = ["columna 1","columna 2","columna 3","columna 4","columna 5","columna 6","columna 7","columna 8","columna 9","columna 10"]
for dato_1 in Nombre_lista_1:
  for dato_2 in Nombre_lista_2:
    print(dato_1, dato_2);
nuevo(1);
#################################################################
