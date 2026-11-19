# Parcial final: Estructuras de datos - Árboles - willian pantoja

Solución del parcial sobre representación, clasificación y recorridos de árboles. El programa `arbol.py` presenta los resultados en la terminal y dibuja el árbol con Matplotlib.

## Solución

El árbol tiene 12 nodos, numerados del 1 al 12, y estas 11 conexiones padre-hijo:

```text
1 -> 2, 3
2 -> 4, 5
3 -> 6, 7
4 -> 8
5 -> 9, 10
6 -> 11
7 -> 12
```

- **Raíz:** 1.
- **Nodos hoja:** 8, 9, 10, 11 y 12.
- **Nodos internos:** 1, 2, 3, 4, 5, 6 y 7.

### Recorridos

El programa muestra los nodos en estos órdenes:

- **Preorden (raíz, izquierda, derecha):** `1, 2, 4, 8, 5, 9, 10, 3, 6, 11, 7, 12`
- **Inorden (izquierda, raíz, derecha):** `8, 4, 2, 9, 5, 10, 1, 11, 6, 3, 12, 7`
- **Postorden (izquierda, derecha, raíz):** `8, 4, 9, 10, 5, 2, 11, 6, 12, 7, 3, 1`

### Aplicación propuesta

El árbol representa la organización de un proyecto de software: el nodo 1 es el proyecto completo, los nodos 2 y 3 son etapas principales, los nodos 4 a 7 son subtareas y los nodos 8 a 12 son actividades específicas. Cada conexión indica que una tarea depende de la etapa o tarea de la que es hija.

Para este ejemplo se selecciona el **postorden**, porque permite procesar primero las actividades y subtareas, y después sus etapas superiores. Así, los resultados de las tareas hijas están disponibles antes de dar por terminada una etapa o el proyecto.

## Resultados esperados

En la terminal se verán, entre otros, estos resultados:

```text
Cantidad de nodos: 12
Cantidad de aristas: 11
Raiz: 1
Nodos hoja: [8, 9, 10, 11, 12]
Nodos internos: [1, 2, 3, 4, 5, 6, 7]

RECORRIDO PREORDEN:
1 2 4 8 5 9 10 3 6 11 7 12

RECORRIDO INORDEN:
8 4 2 9 5 10 1 11 6 3 12 7

RECORRIDO POSTORDEN:
8 4 9 10 5 2 11 6 12 7 3 1

RECORRIDO SELECCIONADO: POSTORDEN
```

Además, se abrirá la representación gráfica con el nodo raíz arriba, los hijos debajo y flechas desde cada padre hacia sus hijos.
