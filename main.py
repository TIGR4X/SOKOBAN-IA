from estado import *

#Clase Nodo: Representación del Arbol de Busqueda
class Node():
    #Constructor
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent

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