import matplotlib.pyplot as plt
import numpy as np

# Crear datos similares a los que se muestran en la imagen
x = np.linspace(0, 5, 20)  # 20 puntos entre 0 y 5
y1 = x ** 2  # y1 es x al cuadrado
y2 = x ** 3  # y2 es x al cubo
x3 = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 5]  # Coordenadas X para el tercer conjunto
y3 = [0, 0, 0, 0, 0, 0, 0, 0, 0.20]            # Coordenadas Y para la línea en la parte inferior

# Crear el gráfico
plt.figure(figsize=(8, 6))  # Configuración del tamaño de la figura
plt.plot(x, y1, 's', color='b', label='Cuadrados')  # Marcadores cuadrados
plt.plot(x, y2, '^', color='brown', label='Cubos')  # Marcadores triangulares
plt.plot(x3, y3, marker='o', color='green', label='Línea Inferior', linestyle='--', linewidth=2)  # Círculos grises con línea discontinua

# Etiquetas y leyenda
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.legend()

# Mostrar el gráfico
plt.show()