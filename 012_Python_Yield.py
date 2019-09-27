from Estructura import *
nuevo(0,"inicio");
#################################################################
def Ej_ya_hechos():
	#Con tab colocaremos aqui las precticas hechas
	pass
print("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║                                                                                  ║
║                 Generadores                                                      ║
║                 ------------                                                     ║
╚══════════════════════════════════════════════════════════════════════════════════╝
Los generadores son una forma sencilla y potente de iterador.
Un generador es una función especial que produce secuencias completas de resultados en lugar de ofrecer un único valor. 
n apariencia es como una función típica pero en lugar de devolver los valores con return lo hace con la declaración yield.
Hay que precisar que el término generador define tanto a la propia función como al resultado que produce.
Una característica importante de los generadores es que tanto las variables locales como el punto de inicio de la ejecución se guardan automáticamente
entre las llamadas sucesivas que se hagan al generador, es decir, a diferencia de una función común, una nueva llamada a un generador no inicia la ejecución al principio de la función,
sino que la reanuda inmediatamente después del punto donde se encuentre la última declaración yield (que es donde terminó la función en la última llamada). 

""");
nuevo(0,"inicio");
#################################################################
#Clase_yield_Ej_001

def numeros(max):
    contador=0
    while contador < max:
            yield contador
            contador+=1
resultados = numeros(5)
for variable in resultados:
    print(variable)
nuevo(1);
#################################################################
#Clase_yield_Ej_002

def numeros_pares(maximo):
	contador = 1
	while contador<maximo:
		yield contador*2
		contador=contador+1
resultados = numeros_pares(10)
for variable in resultados:
	print (variable)

nuevo(2);
#################################################################
#Clase_yield_Ej_003
# Declara generador

def gen_basico():
    yield "uno"   
    yield "dos"
    yield "tres"
   
for valor in gen_basico():
    print(valor)  # uno, dos, tres

# Crea objeto generador y muestra tipo de objeto

generador = gen_basico()
print(generador)  			# generator object gen_basico at 0x7f75ffad55e8
print(type(generador))  	# class 'generator'

# Convierte a lista el objeto generador y muestra elementos

lista = list(generador)
print(lista)  # ['uno', 'dos', 'tres']
print(type(lista))  # class 'list'
nuevo(3);
#################################################################
#Clase_yield_Ej_004
def gen_diez_numeros(inicio):
	fin = inicio + 10    
	while inicio < fin:
		inicio+=1
		yield inicio, fin
		print("sigo")
for inicio, fin in gen_diez_numeros(14):
    print(inicio, fin)
nuevo(4);
#################################################################

print ("""TIP
Un generados seria todo lo *contrarío* a usar listas.

Una lista tienes todos los elementos en memoria y vas iterando sobre cada elemento.
En cambio un generador cada elemento se va *generando* en cada iteracion. Y obviamente al ser generado no puedes usar indices.
Otra diferencia es que una lista es finita, pero un generador no. Ademas es mas eficiente en términos de memoria y de I/O un generador que una lista.
""")
