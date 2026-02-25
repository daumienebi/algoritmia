from collections.abc import Iterable
# Nos indican que tambien funciona sin abc
print("Hello world, this is Algoritmia")

print("\ITERADORES\n")
print("-------------------")
'''
    Lo que se hace aqui es meter distintos tipos de objetos en un
    una estructura para luego mostrar si son iterables o no con un bucle
'''
for objeto in [list(), range(50),5,0.9,"una cadena de texto"]:
    if(isinstance(objeto,Iterable)):
        print(type(objeto).__name__, "es iterable")
    else:
        print(type(objeto).__name__, "no es es iterable")

# Operaciones con los iteradores
lista = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

iterador = iter(lista)
x = int(0)
print("\nImprimiendo con iterador\n")
while True:
    try:
        elemento = next(iterador)
        # mostramos el elemento o cualquier otra accion
        x+=1
        # Muestro la cadena formateada
        print(f'Elemento {x} es {elemento}')
    except StopIteration:
        break
# con bucle for
print("\nImprimiendo con bucle for \n")
for elemento in lista:
    print(f'Elemento {x} es {elemento}')

print("\nGENERADORES\n")
print("-------------------")

print(range(0,100,2),end="\n\n")
# Lo muestra ahora que lo queremos para una lista
print(list(range(0,100,2)))


def pares(hasta = 100):
    i = 0
    while i <= hasta:
        if i%2 == 0:
            # El yield devuelve el valor de la funcion
            yield i
        i+= 1
#llamamos la funcion
pares()

pares_ = []
for _ in pares(200):
    pares_.append(_)
print(pares_)

# comprobando que se genera uno a uno
for v in pares(10**1000):
    if v >= 100:
        break
print("Se ha generado de uno en uno")