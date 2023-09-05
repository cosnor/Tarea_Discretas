class Grafo: 
    def __init__(self):
        self.nodos = []
        self.aristas = []
        
    def teorema(self, grados: list) -> bool:
        #TAM
        if sum(grados) % 2 == 0:
            lista_ord = sorted(grados, reverse=True)
            #Sale si se queda sin lista, o si hay un -1, o si todos son 0
            while len(lista_ord) > 0 and lista_ord.count(-1) == 0 and lista_ord.count(0) != len(lista_ord):
                print(lista_ord)
                to_remove = lista_ord.pop(0)
                for i in range(to_remove):
                    lista_ord[i] -= 1
                lista_ord.sort(reverse=True)
            print(lista_ord)
            #Despues reviso si quedó con un negativo, si quedó con un negativo es porque no es grafo
            if lista_ord.count(-1) > 0:
                return False
            else:
                return True
        else:
            return False
        
    def crear_matriz_adyacencia(self, grados: list) -> list:
        if self.teorema(grados):
            matriz = []
            for i in range(len(grados)):
                matriz.append([])
            #Debo conectar los nodos de tal forma que al conectar uno, se le reste 1 al grado de los dos
            vertices = [i for i in range(len(grados))]
            
            return matriz
        else:
            return False
        
    def agregar_arista(self, arista):
        self.aristas.append(arista)
    def agregar_nodo(self, nodo):
        self.nodos.append(nodo)
    

class Nodo:
    pass