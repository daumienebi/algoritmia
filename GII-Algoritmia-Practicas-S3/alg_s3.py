# # Algoritmia
# ## Práctica 3

# El objetivo de esta práctica es trabajar con los algoritmos de la mochila y dar la vuelta. 

# En el cuerpo de cada función hay una instrucción "pass", se debe sustituir por la implementación adecuada. 

# Para cada clase o función que se pide se proporcionan algunos tests. Las implementaciones deberían superar estos tests.

# Implementa dar la vuelta utilizando las recomendaciones de la diapositiva 5 de la presentación del tema 2 y comprueba si es más rápido que la implementación básica.

def dar_la_vuelta(cambio, valores_monedas):
    """
    Se recibe una cantidad de dinero y una lista de monedas. Se devuelve un generador de las monedas que se necesitan para dar ese cambio de forma que se minimice el número de monedas.

    Se han de devolver las monedas de mayor a menor valor.

    Nota: Para evitar el problema de los decimales en python se puede usar la función round() para redondear a dos decimales.
    """
    # Como puede que la lista de las monedas no venga ordenado, lo reordenamos de menor a mayor
    # y luego con el reverse = True, le damos la vuelta para que las monedas más grandes estén primero
    monedas = sorted(valores_monedas,reverse=True)    
    for moneda in monedas:
        # Si no hay que devolver nada, no iteramos directamente
        if cambio == 0:
            break
        while cambio >= moneda:
            cambio -= moneda
            yield moneda
            # Importante redondear aqui para evitar errores tontos de python con los decimales
            cambio = round(cambio,2)

# Solución sin partir los objetos
def algoritmo_mochila_voraz(objetos, peso_soportado):
    """
    Se recibe un diccionario de objetos, cada elemento del diccionario es una tupla (peso, valor)
    y una variable numérica, peso_soportado.
    Seleccionar las claves de los objetos cuya suma del peso no sea mayor que el peso soportado y se 
    maximice el valor usando un algoritmo voraz. Los objetos no pueden partirse.
    """
    #Nota del profe : Probar a que los objetos puedan partirse
    # Con el objeto.items(), nos devuelve los datos de un diccionario como una lista de tuplas (clave,valor)
    # entonces x[1] es la tupla (k,v)
    objetos = sorted(objetos.items(),key=lambda x : x[1][1] /x[1][0], reverse= True)
    peso = 0
    valor = 0
    candidatos = []
    for k, (p,v) in objetos:
        if peso + p <= peso_soportado:
            candidatos.append(k)
            peso+= p
            valor += v # mala practica, esta variable no se usa
         # Esta parte del else es en el caso de que se pudieras partir los objetos
         #else:
         #    parte_restante = (peso_soportado - p) / p
         #    peso += parte_restante * p
         #    valor += parte_restante * v
         #    candidatos.append(k)    
    return candidatos

# Ejemplo solución con un monticulo
def algoritmo_mochila_voraz_con_monticulo(objetos, peso_soportado):
    """
    Se recibe un diccionario de objetos, cada elemento del diccionario es una tupla (peso, valor)
    y una variable numérica, peso_soportado.
    Seleccionar las claves de los objetos cuya suma del peso no sea mayor que el peso soportado y se 
    maximice el valor usando un algoritmo voraz. Los objetos no pueden partirse.
    """
    #Nota del profe : Probar a que los objetos puedan partirse
    # Con el objeto.items(), nos devuelve los datos de un diccionario como una lista de tuplas (clave,valor)
    # entonces x[1] es la tupla (k,v)
    import heapq
    queue = []
    for o in objetos:
        heapq.heappush(queue,(-objetos[o][1]/objetos[o][0], o))
    peso = 0
    valor = 0
    candidatos = []
    #for k, (p,v) in objetos:
    _, candidato = heapq.heappop(queue)
    p,v = objetos[candidato]
    if peso + p <= peso_soportado:
        candidatos.append(k)
        peso+= p
        valor += v # error, esta variable no se usa
        # Esta parte del else es en el caso de que se pudieras partir los objetos
    #else:
        # parte_restante = (peso_soportado - p) / p
        # peso += parte_restante * p
        # valor += parte_restante * v
        # candidatos.append(k)    
    return candidatos

# Solucion de partiendo los objetos
def algoritmo_mochila_voraz_partida(objetos, peso_soportado):
    """
    Se recibe un diccionario de objetos, cada elemento del diccionario es una tupla (peso, valor)
    y una variable numérica, peso_soportado.
    Seleccionar las claves de los objetos cuya suma del peso no sea mayor que el peso soportado y se 
    maximice el valor usando un algoritmo voraz. Los objetos no pueden partirse.
    """
    #Nota del profe : Probar a que los objetos puedan partirse
    # Con el objeto.items(), nos devuelve los datos de un diccionario como una lista de tuplas (clave,valor)
    # entonces x[1] es la tupla (k,v)
    objetos = sorted(objetos.items(),key=lambda x : x[1][1] /x[1][0], reverse= True)
    peso = 0
    candidatos = {}
    for k, (p,v) in objetos:
        if peso + p <= peso_soportado:
            candidatos[k] = 1
            peso+= p
        else:
            parte_restante = (peso_soportado - peso) / p
            peso+= parte_restante * p
            candidatos[k] = parte_restante
    return candidatos  
 
 # El algoritmo de la mochila siempre ha entrado en el examen
 # nos lo puede pedir implementarlo pero utilizando un monticulo por ejemplo