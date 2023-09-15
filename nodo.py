class Grafo: 
    def __init__(self):
        self.nodos = []
        self.aristas = []
        self.mostrar = []
        self.texto= ""
        
    def teorema(self, grados: list) -> bool:
        #Ordena la lista de mayor a menor
        lista_ord = sorted(grados, reverse=True)
        self.mostrar.append(lista_ord.copy())
        #Sale si se queda sin lista, o si hay un -1, o si todos son 0
        while len(lista_ord) > 0 and lista_ord.count(-1) == 0 and lista_ord.count(0) != len(lista_ord):
            print(lista_ord)
            to_remove = lista_ord.pop(0)
            for i in range(to_remove):
                lista_ord[i] -= 1
                
            lista_ord.sort(reverse=True)
            self.mostrar.append(lista_ord.copy())
            print(lista_ord)
        print(lista_ord)
        
        if lista_ord.count(-1) > 0:
            self.texto = "El grafo simple no existe"
            return False
        else:
            self.texto = "El grafo simple sí existe"
            return True
