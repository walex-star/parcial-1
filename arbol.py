
# TALLER DE ALGORITMOS 2
# ESTRUCTURAS DE DATOS: ARBOLES

import matplotlib.pyplot as plt

# 1. REPRESENTACION DEL ARBOL

nodos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Cada pareja representa padre e hijo

aristas = [
    [1, 2], [1, 3],
    [2, 4], [2, 5],
    [3, 6], [3, 7],
    [4, 8],
    [5, 9], [5, 10],
    [6, 11],
    [7, 12]
]

print("\nPARTE 1: IDENTIFICACION DEL ARBOL")

print("\nNodos:")
print(nodos)

print("Cantidad de nodos:", len(nodos))

print("\nConexiones:")

for conexion in aristas:
    print(conexion[0], "->", conexion[1])

print("Cantidad de aristas:", len(aristas))


# 2. IDENTIFICACION DE LOS NODOS

raiz = 1
hojas = []
internos = []

for nodo in nodos:

    tiene_hijos = False

    for conexion in aristas:

        if conexion[0] == nodo:
            tiene_hijos = True

    if tiene_hijos == True:
        internos.append(nodo)
    else:
        hojas.append(nodo)

print("\nCLASIFICACION")

print("Raiz:", raiz)
print("Nodos hoja:", hojas)
print("Nodos internos:", internos)

# 4. RECORRIDOS

print("\nPARTE 1: RECORRIDOS")

# PREORDEN: RAIZ - IZQUIERDA - DERECHA

preorden = [1, 2, 4, 8, 5, 9, 10, 3, 6, 11, 7, 12]

print("\nRECORRIDO PREORDEN:")

for nodo in preorden:
    print(nodo, end=" ")

print()


# INORDEN: IZQUIERDA - RAIZ - DERECHA

inorden = [8, 4, 2, 9, 5, 10, 1, 11, 6, 3, 12, 7]

print("\nRECORRIDO INORDEN:")

for nodo in inorden:
    print(nodo, end=" ")

print()


# POSTORDEN: IZQUIERDA - DERECHA - RAIZ

postorden = [8, 4, 9, 10, 5, 2, 11, 6, 12, 7, 3, 1]

print("\nRECORRIDO POSTORDEN:")

for nodo in postorden:
    print(nodo, end=" ")

print()


# 5. APLICACION EN LA VIDA REAL

print("\nPARTE 2: APLICACION REAL")

print("\nOrganizacion de un proyecto de software")

print("Nodo 1: Proyecto completo.")
print("Nodos 2 y 3: Etapas principales.")
print("Nodos 4, 5, 6 y 7: Subtareas.")
print("Nodos 8, 9, 10, 11 y 12: Actividades especificas.")

print("\nLas conexiones representan la relacion")
print("entre las tareas principales y sus subtareas.")


# 6. ANALISIS DE RECORRIDOS

print("\nPARTE 3: ANALISIS")

print("\nRECORRIDO SELECCIONADO: POSTORDEN")

print("\nJustificacion:")

print("1. Orden de procesamiento:")
print("Primero se realizan las actividades pequenas")
print("y despues las etapas principales.")

print("\n2. Necesidad del problema:")
print("Una etapa no puede finalizar si sus tareas")
print("todavia estan pendientes.")

print("\n3. Flujo de informacion:")
print("Los resultados de las tareas hijas permiten")
print("determinar si se puede finalizar el nodo padre.")


# 7. RESUMEN FINAL

print("\n======================================")
print("             RESUMEN")
print("======================================")

print("Total de nodos:", len(nodos))
print("Total de conexiones:", len(aristas))

print("Raiz:", raiz)
print("Hojas:", hojas)
print("Nodos internos:", internos)

print("\nRecorrido seleccionado: POSTORDEN")

print("\nALGORITMO FINALIZADO")


# 8. REPRESENTACION GRAFICA DEL ARBOL

def dibujar_arbol(nodos, aristas, raiz):
    hijos = {nodo: [] for nodo in nodos}

    for padre, hijo in aristas:
        hijos[padre].append(hijo)

    posiciones = {}
    siguiente_x = 0

    def asignar_posiciones(nodo, nivel=0):
        nonlocal siguiente_x

        if hijos[nodo]:
            posiciones_hijos = [
                asignar_posiciones(hijo, nivel + 1)
                for hijo in hijos[nodo]
            ]
            x = sum(posicion[0] for posicion in posiciones_hijos) / len(posiciones_hijos)
        else:
            x = siguiente_x
            siguiente_x += 1

        posiciones[nodo] = (x, -nivel)
        return posiciones[nodo]

    asignar_posiciones(raiz)

    fig, ax = plt.subplots(figsize=(11, 7))

    for padre, hijo in aristas:
        ax.annotate(
            "",
            xy=posiciones[hijo],
            xytext=posiciones[padre],
            arrowprops={
                "arrowstyle": "->",
                "color": "#64748b",
                "linewidth": 1.8,
                "shrinkA": 18,
                "shrinkB": 18,
            },
        )

    x = [posiciones[nodo][0] for nodo in nodos]
    y = [posiciones[nodo][1] for nodo in nodos]
    ax.scatter(x, y, s=1100, color="#087e8b", edgecolors="white", linewidths=2, zorder=2)

    for nodo in nodos:
        ax.text(
            posiciones[nodo][0],
            posiciones[nodo][1],
            str(nodo),
            color="white",
            fontsize=14,
            fontweight="bold",
            ha="center",
            va="center",
            zorder=3,
        )

    ax.set_title("Representación gráfica del árbol", fontsize=16)
    ax.axis("off")
    ax.margins(x=0.1, y=0.15)
    fig.tight_layout()
    plt.show()


dibujar_arbol(nodos, aristas, raiz)
