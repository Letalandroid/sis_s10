import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable
import networkx as nx
import math
import sympy as sp

x = sp.symbols('x')
funcion = x**2 - 4*x + 3
print("Función cuadrática:", funcion)

raices = sp.solve(funcion, x)
print("Raíces de la función:", raices)

derivada = sp.diff(funcion, x)
print("Derivada de la función:", derivada)

funcion_numerica = sp.lambdify(x, funcion, 'numpy')
derivada_numerica = sp.lambdify(x, derivada, 'numpy')

tabla = PrettyTable()
tabla.field_names = ["Función", "Raíces", "Derivada"]
tabla.add_row([str(funcion), [float(r) for r in raices], str(derivada)])
print("\nTabla de la función cuadrática:")
print(tabla)

x_vals = np.linspace(-2, 6, 400)
y_vals = funcion_numerica(x_vals)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label=f'f(x) = {funcion}', color='blue')
plt.axhline(0, color='black', linewidth=0.5)

for r in raices:
    plt.plot(float(r), funcion_numerica(float(r)), 'ro')
    plt.text(float(r), 0, f'  Raíz: {float(r):.2f}', color='red')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfica de la función cuadrática y sus raíces')
plt.legend()
plt.grid(True)
plt.show()

G = nx.DiGraph()
G.add_node("Función", label=f'f(x) = {funcion}')
G.add_node("Raíces", label="Raíces")
G.add_node("Derivada", label=f"f'(x) = {derivada}")

G.add_edge("Función", "Raíces")
G.add_edge("Función", "Derivada")

pos = nx.spring_layout(G)
labels = nx.get_node_attributes(G, 'label')
nx.draw(G, pos, with_labels=True, labels=labels, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold')
plt.title("Relación entre Función, Raíces y Derivada en un Grafo")
plt.show()