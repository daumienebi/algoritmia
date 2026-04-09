import heapq
# Parte de la sesión 3

# Implementación del algoritmo de dar la vuelta con una lista
def dar_la_vuelta_lista(cambio,valores_monedas):
    # Primero ordenamos la lista de mayor a menor y le damos la vuelta
    # de esta forma, aseguramos la complejjidad (O(n log n))
    monedas = sorted(valores_monedas,reverse=True)

    # Recorremos cada moneda
    for moneda in monedas:
        # Paramos si no hay nada mas que devolver
        if cambio == 0:
            break
        #Calculamos cuantas monedas de ese tipo caben con la división exacta
        cantidad_monedas = cambio // moneda

        # Si cabe esa moneda en los cambios, lo devolvemos una a una
        if cantidad_monedas > 0:
            for i in range(int(cantidad_monedas)):
                yield moneda
        # Actualizamos el valor del cambio que queda por devolver
        cambio = round(cambio % moneda, 2)

# Implementación del algoritmo de dar la vuelta con un monticulo
def dar_la_vuelta_monticulo(cambio,valores_monedas):
    # En este caso, queremos un max_heap porque queremos las monedas mas grandes 
    # encima de la pila
    max_heap = []
    # Agregamos las monedas al monticulo
    for moneda in valores_monedas:
        # Utilizamos un valor negativo a la hora de insertar la moneda en el monticulo dado que
        # que la implementación por defecto del heapq es un min-heap, donde los elementos mas pequeños
        # se encuentren en la cima. De esta forma, si introducimos 2€,3€ y 5€, se convierte en 
        # -2€, -3€, y -5€ y como -5€ es el más pequeño, se queda en la cima. A la hora de sacar el dato
        # del monticulo, lo volvemos a multiplicar por -1 para obtener el valor positivo.
        heapq.heappush(max_heap,(moneda * -1))
    
    # Mientras hay cambio que devolver, y valores en el monticulo
    while cambio > 0 and len(max_heap) > 0:
        # Multiplicamos la moneda por -1 para obtener el valor positivo.
        moneda = heapq.heappop(max_heap) * -1

        # Calculamos cuantos de esta moneda cabe
        cantidad_monedas = cambio // moneda

        if cantidad_monedas > 0:
            for i in range(int(cantidad_monedas)):
                yield moneda
        
        cambio = round(cambio % moneda, 2)

# ZONA DE PRUEBAS
cambio_a_devolver = 3.80
sistema_de_monedas = [2, 1, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]

print("Intentando devolver:", cambio_a_devolver, "€")

# Llamamos a la función. Usamos list() para extraer todos los 'yield' de golpe
resultado = list(dar_la_vuelta_lista(cambio_a_devolver, sistema_de_monedas))

print("Monedas usadas:", resultado)
print("Total de monedas entregadas:", len(resultado))