import heapq
# Parte de la sesión 3
# Aqui probaré mis soluciones con mochilas enteras y fraccionadas (que se pueden partir) y
# tambien sus implementaciones con listas y monticulos

def mochila_entera_lista(objetos,peso_soportado):
    # Creo mi lista de ratios donde almacenare tuplas con la relacion entre los
    # pesos y valores de cada objeto
    lista_ratios = []

    for id_objeto, dato in objetos.items():
        peso = dato[0]
        valor = dato[1]
        ratio = valor / peso
        lista_ratios.append((ratio,id_objeto,peso,valor))
    
    # Ordenamos la lista de mayor a menor para tener los mejores elementos en la cima
    lista_ratios.sort(reverse= True)
    peso_actual = 0
    mochila_resultado = []

    for ratio,id_objeto,peso,valor in lista_ratios:
        # Metemos el objeto si cabe entero
        if peso_actual + peso <= peso_soportado:
            mochila_resultado.append(id_objeto)
            peso_actual+= peso
    return mochila_resultado

def mochila_entera_monticulo(objetos,peso_soportado):
    # ver dar_la_vuelta_monticulo para entender la explicación del uso del max_heap
    max_heap = []

    # metemos los valores en el monticulo, almacenando tuplas con la relacion entre los 
    # pesos y valores de cada objeto
    for id_objeto, dato in objetos.items():
        peso = dato[0]
        valor = dato[1]
        ratio = valor / peso
        heapq.heappush(max_heap,(-ratio,id_objeto,peso,valor))
    
    peso_actual = 0
    mochila_resultado = []

    while len(max_heap) > 0:
        # Obtenemos cada objeto
        objeto = heapq.heappop(max_heap)
        peso = objeto[2]
        id_objeto = objeto[1]
        # Metemos el objeto si cabe entero
        if peso_actual + peso <= peso_soportado:
            mochila_resultado.append(id_objeto) # Agregamos solamente el id o nombre del objeto
            peso_actual+= peso
    return mochila_resultado

def mochila_fraccionada_lista(objetos,peso_soportado):
    # Creo mi lista de ratios donde almacenare tuplas con la relacion entre los
    # pesos y valores de cada objeto
    lista_ratios = []

    for id_objeto, dato in objetos.items():
        peso = dato[0]
        valor = dato[1]
        ratio = valor / peso
        lista_ratios.append((ratio,id_objeto,peso,valor))
    
    # Ordenamos la lista de mayor a menor para tener los mejores elementos en la cima
    lista_ratios.sort(reverse= True)
    peso_actual = 0
    # En este caso, el resultado será un diccionario, donde la clave será el id del objeto y el
    # valor el porcentaje cogido
    mochila_resultado = {}
    
    for ratio,id_objeto,peso,valor in lista_ratios:
        # Lo metemos si cabe entero
        if peso_actual + peso <= peso_soportado:
            mochila_resultado[id_objeto] = 1.0 # si lo metemos entero
            peso_actual+= peso
        # Si no cabe entero, tenemos que partirlo
        else:
            espacio_restante = peso_soportado - peso_actual
            # La proporcion que podemos meter es la siguiente:
            fraccion = espacio_restante / peso
            mochila_resultado[id_objeto] = round(fraccion,2)
            peso_actual+= espacio_restante
            # Ahora rompemos el bucle dado que la mochila ya se llenó
            break
    return mochila_resultado


def mochila_fraccionada_monticulo(objetos,peso_soportado):
    max_heap = []

    for id_objeto, dato in objetos.items():
        peso = dato[0]
        valor = dato[1]
        ratio = valor / peso
        heapq.heappush(max_heap,(-ratio,id_objeto,peso,valor))
    
    peso_actual = 0
    mochila_resultado = {}

    while len(max_heap) > 0:
        # Obtenemos cada uno de los objetos
        objeto = heapq.heappop(max_heap)
        peso = objeto[2]
        id_objeto = objeto[1]
        # Si el objeto cabe entero, lo metemos
        if peso_actual + peso < peso_soportado:
            mochila_resultado[id_objeto] = 1.0
            peso_actual+= peso
        # Si no cabe entero, lo partimos
        else:
            espacio_restante = peso_soportado - peso_actual
            # Calculamos la porción que podemos meter
            fraccion = espacio_restante / peso
            mochila_resultado[id_objeto] = round(fraccion,2)
            peso_actual+= espacio_restante
            break
    return mochila_resultado

# ZONA DE PRUEBA: MOCHILA 0/1 (OBJETOS ENTEROS)

# Definimos el botín: { 'Nombre': (Peso, Valor) }
botin_museo = {
    'Anillo de Diamante': (1, 200),  # Ratio: 200 €/kg
    'Estatua de Oro': (4, 400),      # Ratio: 100 €/kg
    'Estatua de Plata': (5, 300),    # Ratio: 60 €/kg
    'Cuadro Antiguo': (3, 150)       # Ratio: 50 €/kg
}
# Nuestra mochila solo aguanta 5 kilos
capacidad_mochila = 5

print("\n--- INICIANDO ROBO (MOCHILA 0/1) ---")
print(botin_museo)
print(f"Capacidad máxima: {capacidad_mochila} kg\n")

print(">> Probando versión con Listas:")
resultado_lista = mochila_entera_lista(botin_museo, capacidad_mochila)
print(f"Me llevo en la mochila: {resultado_lista}")

print("\n>> Probando versión con Montículo:")
resultado_heap = mochila_entera_monticulo(botin_museo, capacidad_mochila)
print(f"Me llevo en la mochila: {resultado_heap}")