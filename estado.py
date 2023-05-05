class State():
    #Definición de Clase Estado
    #player: Una coordenada (x,y)
    #boxes: Diccionario de Coordenadas de cajas
    #movement: UP: (1,0), DOWN: (0,1), LEFT:(0,-1) o RIGHT: (0,1)
    
    #Constructor
    def __init__(self, player, boxes, movement, depth):
        self.player = player
        self.boxes = boxes
        self.movement = movement
        self.depth = depth

    #Igualdad para validar la función __hash__
    def __eq__(self, otherState):
        return self.player == otherState.player and self.boxes == otherState.boxes

    #Función Hash Python (Entre la posición del Jugador y de las cajas)
    def __hash__(self):
        return hash((self.player, tuple(self.boxes)))
    
    #Definición de Operadores
    def possibleMoves(self, storages, obstacles):
        possibleMoves = []
        
        #Orden: U, D, L, R
        for directions in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            newPlayerPos = (self.player[0]+directions[0], self.player[1]+directions[1])
            if (newPlayerPos in obstacles):
                continue
            
            #Copiar el Diccionario
            newBoxesPos = dict(self.boxes)
            if (newPlayerPos in self.boxes):
                newBoxPos = (newPlayerPos[0]+directions[0], newPlayerPos[1]+directions[1])
                #La caja no puede moverse en una dirección con obstaculos
                if(newBoxPos in obstacles):
                    continue
                #La caja no puede moverse en una dirección con otras cajas
                if(newBoxPos in self.boxes):
                    continue
                #Actualiza dado un índice el diccionario de las cajas
                i = newBoxesPos.pop(newPlayerPos)
                newBoxesPos[newBoxPos] = i
            
            newState = State(newPlayerPos, newBoxesPos, directions)
            possibleMoves.append(newState)

        return possibleMoves
    
    #Función de Meta: Valida que las cajas estén en la posición de los almacenes (storages)
    def isGoalState(self, storagesIn):
        for box in self.boxes:
            if box not in storagesIn:
                return False
        return True
    
    #Función para Imprimir cada Estado
    def getMap(self, obstaclesIn, storagesIn, heightIn, widthIn):
        matrix = [[' ' for col in range(widthIn)] for row in range(heightIn)]
        for obstacles in obstaclesIn:
            matrix[obstacles[0]][obstacles[1]] = 'W'
        for storages in storagesIn:
            matrix[storages[0]][storages[1]] = 'X'
        for box in self.boxes:
            matrix[box[0]][box[1]] = 'C'
        matrix[self.player[0]][self.player[1]] = 'I'

        return matrix