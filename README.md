# SOKOBAN - INTELIGENCIA ARTIFICIAL
Proyecto de implementación de algortimos de busqueda por profundidad, amplitud e iterativo por profundidad para la materia Inteligencia Artificial. Tiene como objetivo solucionar tableros del juego Sokoban que son dados como input mediante archivos .txt

Adolfo León Maya García - 202025159

Jhon Freddy Popo Moreno - 202010003 

Herson Stiven Tangarife Davila - 202010007

# ¿Cómo Ejecutar?
Clonar el repositorio en su maquina local, agregar los niveles de prueba ocultos (O usar los aquí definidos) y desde la carpeta raíz ejecutar:

```bash
./run.sh ${NOMBRE_ARCHIVO1} ${NOMBRE_ARCHIVO2} ... ${N_NOMBRE_ARCHIVO}
```

De esta forma podrá ejecutar en una misma línea 1 o varios niveles uno tras otro formateado tal que:
```bash
"Cadena del DFS"
"Cadena del BFS"
"Cadena del IFS"

//En caso de error:
"No fue posible solucionar el mapa"
```
