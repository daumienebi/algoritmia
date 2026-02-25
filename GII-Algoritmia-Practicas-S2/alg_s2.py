# ## Algoritmia
# ### Práctica 2
# El objetivo de esta práctica es trabajar con recurrencias


# Se pide la implementación de las funciones que aparecen a continuación. 
#
# En el cuerpo de cada función hay una instrucción "pass", se debe sustituir por la implementación adecuada. 
#
# Para cada clase o función que se pide se proporcionan algunos tests. Las implementaciones deberían superar estos tests.

# Importaciones
from math import log

def generador_recurrencia_mine(coeficientes, funcion_adicional, iniciales):
    """
    Generador de valores de acuerdo a una recurrencia:
    F(n) = coeficientes[0]*F(n-1) + coeficientes[1]*F(n-2) + ...
         + funcion_adicional(n)
    Los valores iniciales son F(0) = iniciales[0], F(1) = iniciales[1],...
    Los valores que se generan son F(0), F(1), F(2),...
    Se deben generar los valores de uno en uno, no hay que devolver varios.
    Debe generar valores indefinidamente, no hay que poner límites.
    Aunque sea una recurrencia, los valores *no* deben calcularse recursivamente.
    """
    tamanho = len(iniciales) # tambien se podria obtener el tamanho con coeficientes  
    for n in range(tamanho):
        if(tamanho == 1 or tamanho == 2):
            fn = iniciales[n]
            yield fn
        else:
            fn = coeficientes[0] * iniciales[n-1] + coeficientes[1] * iniciales[n-2] + funcion_adicional(n)
            yield fn

def generador_recurrencia(coeficientes, funcion_adicional, iniciales):
    """
    Generador de valores de acuerdo a una recurrencia:
    F(n) = coeficientes[0]*F(n-1) + coeficientes[1]*F(n-2) + ...
         + funcion_adicional(n)
    Los valores iniciales son F(0) = iniciales[0], F(1) = iniciales[1],...
    Los valores que se generan son F(0), F(1), F(2),...
    Se deben generar los valores de uno en uno, no hay que devolver varios.
    Debe generar valores indefinidamente, no hay que poner límites.
    Aunque sea una recurrencia, los valores *no* deben calcularse recursivamente.
    """
    yield from iniciales
    # Le damos la vuelta a la lista de coeficientes por la formula que hay que aplicar
    coeficientes = coeficientes[::-1]
    lista_recurrencia = collections.deque(iniciales)
    indice = len(iniciales)
    while True:
        valor_adicional = funcion_adicional(indice)
        indice += 1
        valor = valor_adicional
        for in in range(len(coeficientes)):
            valor+= coeficientes[i] + lista_recurrencia[i]      
        # Otra forma de poner la linea anterior
        # valor = sum(coeficientes[i] * lista_recurrencia[i] for in in range(len(coeficientes))) + valor_adicional
        yield valor
        
        lista_recurrencia.append(valor)
        lista_recurrencia.popleft()
                 

class RecurrenciaMaestra: 
    """
    Clase que representa una recurrencia de las que se consideran en el 
    teorema maestro, de la forma T(n)=aT(n/b)+n^k. Se interpreta que en n/b
    la división es entera.
    Además de los métodos que aparecen a continuación, tienen que funcionar 
    los siguientes operadores: 
        ==, !=,
        str(): la representación como cadena debe ser 'aT(n/b)+n^k'
        []: el parámetro entre corchetes es el valor de n para calcular T(n).
    """
    
    def __init__(self, a, b, k, inicial = 0):
        """
        Constructor de la clase, los parámetros a, b, y k son los que
        aparecen en la fórmula aT(n/b)+n^k. El parámetro inicial es el valor
        para T(0).
        """
        self.a = a
        self.b = b
        self.k = k
        self.inicial = inicial
     
    def __str__(self):
          return f'{self.a}T(n/{self.b}) + n^{self.k}'
    
    def __getitem__(self,n):
        if n == 0:
            return self.inicial
        # Al utilizar los corchetes aqui con self []...es como si estuvieramos 
        # llamando al metodo __getitem__ dado que ese metodo corresponde a los corchetes
        #return self.a * self.__getitem__(n // self.b) + n ** self.k
        return self.a * self[n // self.b] + n ** self.k
        
    def __eq__(self,other):
        return self.a == other.a and self.b == other.b and self.k == other.k
                and self.inicial = other.inicial
    
    def metodo_maestro(self):
        """
        Devuelve una cadena con el tiempo de la recurrencia de acuerdo al 
        método maestro. La salida está en el formato "O(n^x)" o "O(n^x*log(n))",
        siendo x un número.
        """
        if log(self.a,self.b) == self.k:
            return f'O(n^{self.k} * log(n))'
        elif log(self.a,self.b) > self.k:
            return f'O{n^{self.k})'
    
    def __ne__(self):
        return not self == other
    
    def __iter__(self):
        """
        Generador de valores de la recurrencia: T(0), T(1), T(2), T(3)..., 
        indefinidamente.
        Aunque sea una recurrencia, los valores *no* deben calcularse 
        recursivamente.
        """
        lista_recurrencia = collections.deque([self.inicial])
        indice = 1
        yield self.inicial
        while True:
            valor = self.a * lista_recurrencia[0] + indice ** self.k
            yield valor
            lista_recurrencia.append(valor)
            
            indice+= 1
            # Esta siguiente linea es debido a encontrar el patron del crecimiento 
            if indice % self.b == 0:
                # Borramos el mas antiguo
                lista_recurrencia.popleft()    