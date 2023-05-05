from estado import *
from collections import deque

#Clase Nodo: Representación del Arbol de Busqueda
class Node():
    #Constructor
    def __init__(self, state, parent, depth):
        self.state = state
        self.parent = parent
        self.depth = depth

    #Devuelve la lista de movimientos (Coords) necesarios para llegar al nodo actual
    def getPath(self):
        path = [self.state.movement]
        actual = self.parent
        while actual:
            path.append(actual.state.movement)
            actual = actual.parent
        path.reverse()
        return path

    #Devuelve una cadena de caracteres, representando los movimientos necesarios para llegar al nodo actual
    def getMoves(self):
        path = self.getPath()
        nameOfMoves = {(0,0): '', (0,-1): 'L', (1,0): 'D', (0,1): 'R', (-1,0): 'U'}

        formatMoves = ''
        for moves in path:
            formatMoves += nameOfMoves[moves]
        
        return formatMoves

    #Devuelve una lista de matrices que representan los estados en cada paso para llegar al nodo actual
    def getPathMaps(self, obstaclesIn, storagesIn, highIn, widthIn):
        pathOfStates=[self.state.getMap(obstaclesIn, storagesIn, highIn, widthIn)]
        
        actual = self.parent
        while actual:
            pathOfStates.append(actual.state.getMap(obstaclesIn, storagesIn, highIn, widthIn))
            actual = actual.parent
        pathOfStates.reverse()
        return pathOfStates
    
#DFS (Profundidad - Max 64 Niveles, si no: "No se pudo encontrar solución")
def DFS(stateObj, obstacles, storages):
    #Inicializar el primer Nodo del Árbol con el estado dado (No tiene padre)
    startNode = Node(stateObj, None, 0)

    #Añadir el nuevo nodo a la pila del arbol
    tree = deque([startNode])

    #Repetido es un objeto conjunto de python para almacenar los estados ya visitados
    repetido = set()
    
    while tree:
        #Obtener el último nodo agregado y agregarlo como repetido
        currentNode = tree.pop()
        repetido.add(currentNode.state)

        #Validar si el estado es meta y retornar qué nodo fue
        if(currentNode.state.isGoalState(storages)):
            return currentNode
        
        #Validar si la solución exedió el límite de busqueda y retornar error
        if currentNode.depth >= 64:
            continue
        
        #Obtener los operadores (En un array) que permitirían la expansión del nodo padre
        validMovesStates = currentNode.state.possibleMoves(storages, obstacles)

        #Revertir el arreglo para validar el orden UDLR dispuesto en State
        validMovesStates.reverse()

        #Crea un nodo hijo nuevo por cada operador posible y lo valida en los estados repetidos
        for childState in validMovesStates:
            childNode = Node(childState, currentNode, currentNode.depth+1)
            if childNode.state in repetido:

                continue
            else:
                tree.append(childNode)
    return None

#Funcion Auxiliar para impresión de las matrices resultantes
def printMap(matrix):
    height = len(matrix[0])
    width = len(matrix[0][0])
    for i in range(len(matrix)):
        for j in range(height):
            for k in range(width):
                print (matrix[i][j][k], end='')
            print ()
        print()

#Función Auxiliar para leer el archivo .txt del tablero de sokoban y crear el estado inicial
def readBoard(lines, obstacles, storages, stateObj):
    agent = ()
    boxes = {}
    numline = 0
    numstorages= 0
    flag = True
    for line in lines:
        if line == "\n":
            break
        if line[0] == "W" or line[0] == "0":
            width = len(line)
            for i in range(0,len(line)):
                if line[i] == "W":
                    obstacles.append((numline,i))
                else :
                    if line[i] == "X":
                        storages[(numline,i)] = numstorages
                        numstorages = numstorages + 1
            numline = numline +1
        else:
            if flag:
                height = numline
                coords = line[0:len(line)].split(",")
                agent = (int(coords[0]),int(coords[1]))
                numstorages = 0
                flag = False
            else:
                coords = line[0:len(line)].split(",")
                boxes[(int(coords[0]),int(coords[1]))] = numstorages
                numstorages = numstorages + 1
            stateObj = State(agent,boxes,(0,0))
            numline = numline + 1
    stateObj = State(agent,boxes,(0,0))
    return obstacles, storages, stateObj, height, width


#Función Main: Principal de Ejecución
if __name__ == '__main__':
    #Lectura del texto
    import sys
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    
    lines = [line.strip() for line in lines if line.strip()]
    
    if lines:
        #obstacles: Lista de coordenadas de las paredes
        #storages: Diccionario de Metas    
        obstacles = []
        storages = {}

        #Estado Inicial Vacío y la posterior creación de Estado Inicial dado el input .txt
        stateObj = None
        obstacles, storages, state, height, width = readBoard(lines, obstacles, storages, stateObj)
        
        #Ejecución de la Busqueda por Profundidad
        result = DFS(state, obstacles, storages)
        if (result):
            #printMap (result.getPathMaps(obstacles, storages, height, width))
            print (result.getMoves()+"\n")
        else:
            print ('No fue posible solucionar el mapa')