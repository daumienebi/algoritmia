import heapq
# Implementación de esta practica utilizando la representación de diccionario de 
# diccionarios
grafo_de_ejemplo = {
        'a': {'b': 1, 'c': 2},
        'b': {'a': 3, 'd': 6},
        'c': {'a': 5, 'b': 2},
        'd': {}
    }

# Funciones genéricas de grafos
def numero_nodos(grafo):
    """Número de nodos en el grafo"""
    return len(grafo)


def numero_arcos(grafo):
    """Número de arcos en el grafo"""
    contador = 0
    # Dado que cada nodo tiene conexiones a otros nodos, esas conexiones se realizan a través de
    # los "arcos", por cada conexión que tiene un nodo a otro, hay un arco
    for nodo,arcos in grafo.items():
        contador+= len(arcos)
    return contador

def peso_total(grafo):
    """Suma de los pesos de los arcos del grafo"""
    # Cuando un nodo se conecta a otro, tiene un valor de peso que indica
    suma = 0
    for origen,destino in grafo.items():
        for nodo,peso in destino.items():
            suma+= peso
    return suma

def arco(grafo, origen, destino):
    """
    Si hay un arco de origen a destino, devuelve su peso. 
    Si no hay, devuelve None.
    """
    # Primero comprobamos si el origen existe en el grafo
    if origen in grafo:
        # Luego comprobamos si ese origen tiene el destino
        if destino in grafo[origen]:
            return grafo[origen][destino]
        
    # Si no existe ese destino, devolvemos None
    return None

# Operaciones de modificación

def inserta_nodo(grafo, nodo):
    """
    Inserta el nodo en el grafo.
    Si ya estaba, no se modifica.
    Devuelve el propio grafo."""
    # Solamente metemos el nodo si no está en el grafo
    if nodo not in grafo:
        grafo[nodo] = {}
    return grafo

def inserta_arco(grafo, origen, destino, peso=1):
    """
    Inserta el arco en el grafo.
    Si ya estaba se actualiza el peso.
    Devuelve el propio grafo.
    """
    # Aseguramos que el origen exista en el dicconario principal
    if origen not in grafo:
        grafo[origen] = {}
    
    # Aseguramos que el destino tambien exista aunque no tenga ningún arco
    if destino not in grafo:
        grafo[destino] = {}
    
    # Creamos o actualizamos la conexión en el diccionario del nodo origen,
    # en Python, si una clave ya existe, se sobreescribe el valor que introducimos pero
    # no existe, crea la nueva entrada
    grafo[origen][destino] = peso

    return grafo

# Operaciones de consulta
def grado(grafo, nodo, salida=True):
    """
    Devuelve el grado de salida o entrada de un nodo del grafo.
    Estos grados son el número de arcos que salen o llegan al nodo.
    """
    if nodo not in grafo:
        return 0
    
    # Si es el grado de salida, devolvemos el numero de nodos a los que sale
    # el nodo en cuestion
    if salida == True:
        return len(grafo[nodo])
    else:
        grado = 0
        # Si es de entrada, tenemos que buscar en todo el grafo, a ver que nodos
        # aputan al nodo en cuestion
        for origen,vecinos in grafo.items():
            if nodo in vecinos:
                grado+= 1
    return grado

def pesos_adyacentes(grafo, nodo, salida=True):
    """
    Devuelve la suma de los pesos de los arcos adyacentes al nodo, 
    de salida o entrada.
    """
    if nodo not in grafo:
        return 0
    suma_pesos = 0
    # Si es de salida, sumamos todos los pesos de los destinos que podemos ir desde el nodo
    if salida == True:
        for destino, peso in grafo[nodo].items():
            suma_pesos+= peso
    # Si es de entrada, sumamos todos los pesos de los que apunta al nodo
    else:
        for origen, vecinos in grafo.items():
            if nodo in vecinos:
                suma_pesos+= vecinos[nodo]
    return suma_pesos

def coste_camino(grafo, camino):
    """
    Devuelve el coste del camino en el grafo.
    El camino viene dado como una secuencia de nodos.
    Si esa secuencia no forma un camino, devuelve None.
    """
    # el camino debe tener 2 nodos como minimmo
    if len(camino) < 2:
        return 0
    
    coste_total = 0
    # Recorremos la lista de caminos hasta el penultimo elemento
    for i in range(len(camino) - 1):
        origen = camino[i]
        destino = camino[i+1]
        # Obtenemos el peso
        peso = arco(grafo,origen,destino)
        if peso == None:
            # Si se corta el camino en algún momento, devolvemos None
            return None
        coste_total+= peso
    return coste_total


###################
# Habiendo creado las funciones anteriores, se pide implementar los siguientes métodos:
# Nota : Consideramos prim doblemente dirigido
def prim(grafo, inicial=None):
    """
    Implementa el algoritmo de Prim para obtener el árbol de expansión mínima de un grafo. Devuelve en el formato del grafo el árbol.

    Se recuerda que un árbol es un grafo sin bucles y conectado.

    El grafo que se va a recibir siempre será conexo y sin direcciones.
    """
    if inicial is None:
        # cogemos el primer nodo
        for nodo in grafo:
            inicial = nodo
            break
    # Definimos las estructuras necesarias
    visitados = set()
    arbol = {} # El grafo resultado
    cola = [] # Metemos tuplas (peso,origen,destino), min_heap

    # Empezamos en el nodo inicial
    visitados.add(inicial)
    # Metemos todos los nodos que salen del inicial en la cola
    for vecino,peso in grafo[inicial].items():
        heapq.heappush(cola,(peso,inicial,vecino))
    # Mientras queden nodos por conectar
    while cola:
        peso,origen,destino = heapq.heappop(cola)
        # Si el destino ya esta en el arbol, saltamos
        if destino in visitados:
            continue
        visitados.add(destino)
        # Aqui contruimos el arbol doblemente dirigido
        inserta_arco(arbol,origen,destino,peso)
        inserta_arco(arbol,destino,origen,peso)

        # Agregamos los nodos que salen del nuevo nodo destino a la cola
        for siguiente, peso in grafo[destino].items():
            if siguiente not in visitados:
                heapq.heappush(cola,(peso,destino,siguiente))
    return arbol

def dijkstra(grafo, inicial):
    """
    Implementa el algoritmo de Dijkstra
    Devuelve un diccionario con la distancia mínima desde el nodo inicial a cada uno de los nodos del grafo.
    """
    distancias = {}
    # Inicializamos las estructuras
    for nodo in grafo:
        distancias[nodo] = float('inf')

    # La distancia a nosotros mismo es cero
    distancias[inicial] = 0

    # Cola de prioridad (min_heap) con tuplas : (distancia_acc,nodo_actual)
    cola = []
    heapq.heappush(cola,(0,inicial))

    # Mientras hayan nodos que conectar...
    while cola:
        # Sacamos el nodo con la menor distancia acumulada
        dist_acc,nodo_actual = heapq.heappop(cola)

        # Si hemos encontrado un camino mas corto antes, ignoramos el dato
        if dist_acc > distancias[nodo_actual]:
            continue
        # Exploramos los vecinos
        for vecino,peso_arco in grafo[nodo_actual].items():
            nueva_dist = dist_acc + peso_arco
            # Comprobamos si el camino es mejor que la que teniamos
            if nueva_dist < distancias[nodo_actual]:
                distancias[vecino] = nueva_dist
                heapq.heappush(cola,(nueva_dist,vecino))
    return distancias

def obten_camino_minimo(inicial, final, caminos_pre_calculados):
    """
    Devuelve el camino mínimo entre dos nodos, a partir de la información obtenida con Dijkstra.
    Si no hay camino, devuelve None.
    """
    if final not in caminos_pre_calculados and final != inicial:
        return None
    camino = []
    actual = final

    # Vamos desde el final hasta llegar al inicio
    while actual is not None:
        camino.append(actual)
        actual = caminos_pre_calculados[actual]
        # La lista está al revés: [final, ..., inicial]
        # Le damos la vuelta para devolver [inicial, ..., final]
        camino.reverse()
    return camino

# Pruebas
n_arcos = numero_arcos(grafo_de_ejemplo)
print(f'Nª Arcos : {n_arcos}')
peso = peso_total(grafo_de_ejemplo)
print(f'Peso: {peso}')
res = arco(grafo_de_ejemplo,'a','s')
print(f'Arco: {res}')
grado = grado(grafo_de_ejemplo,'d',False)
print(f'Grado: {grado}')
pesos_adya = pesos_adyacentes(grafo_de_ejemplo,'a',True)
print(f'Pesos adya: {pesos_adya}')

