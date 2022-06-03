#Importamos la líbreria Queue
from queue import Queue
#Creamos nueva clase
class Grafo:
    '''Constructor
    Con la funcion def se define la identificación'''
    def __init__(self, num_de_nodos, dirigido=True):
        '''Especifiar el atributo de la instancia'''
        self.m_num_de_nodos = num_de_nodos
        '''La función range es el ranfo qu eva a retorna'''
        self.m_nodos = range(self.m_num_de_nodos)
		
        ''' Diriguido  y no dirigido'''
        self.m_dirigido = dirigido
		
        ''' Representación gráfica- lista de adyacencia
         Usamos un diccionario para implementar una lista de adyacencia'''
        self.m_lista_calificativo = {nodo: set() for nodo in self.m_nodos}      
	
    # Agregar borde al gráfico
    def add_arista(self, nodo1, nodo2, peso=1):
        #Especifiar el atributo de la instancia de acuerdo a los nodos 
        self.m_lista_calificativo[nodo1].add((nodo2, peso))
        ''' Condicion para un nodo que no esta dirigido'''

        if not self.m_dirigido:
            self.m_lista_calificativo[nodo2].add((nodo1, peso))
    
    # Imprimir la representación gráfica y contiene el parámetro
    def print_lista_calificativo(self):
        '''Es para recorrer los elementos del objeto, para asi poder ejecutar un bloque de código
        y poder imprimir la lista de nodos especificados'''
        for key in self.m_lista_calificativo.keys():
            print("nodo", key, ": ", self.m_lista_calificativo[key])

    def dfs(self, inicio, objetivo, path = [], visit = set()):
        path.append(inicio)
        visit.add(inicio)
        if inicio == objetivo:
            return path
        for (neighbour, peso) in self.m_lista_calificativo[inicio]:
            if neighbour not in visit:
                result = self.dfs(neighbour, objetivo, path, visit)
                if result is not None:
                    return result
        path.pop()
        return None

#Para ejecutar un archivo
if __name__ == "__main__":
    #### EXAMPLE #####

    '''Crear una instancia de los Grafos clase
    Este grafo no está dirigido y tiene 5 nodos el cual realizara su respectiva recorrido'''
    graph = Grafo(5, dirigido=False)

    '''Agregue bordes al grafo con determinado  peso = 1 
    Estas lineas de codigo es para añadir los elementos de los nodos
    que tenemos que van recorriendo en cadena'''
    graph.add_arista(0, 1)
    graph.add_arista(0, 2)
    graph.add_arista(1, 3)
    graph.add_arista(2, 3)
    graph.add_arista(3, 4)
    # Print adjacency list in the form node n: {(node, weight)}
    graph.print_lista_calificativo()

    traversal_path = []
    traversal_path = graph.dfs(0, 3)
    print(f" The traversal path from node 0 to node 3 is {traversal_path}")




# Execution Steps
# Current Node	Path	Visited
# 0	[0]	{0}
# 1	[0, 1]	{0, 1}
# 3	[0, 1, 3]	{0, 1, 3}