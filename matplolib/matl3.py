import matplotlib.pyplot as plt

# Paso 1: Crear una figura y un eje
plt.figure(figsize=(8, 8))  # Tamaño más grande para mejor visualización

# Paso 2: Definir los puntos para la primera línea
x1 = [10, 20, 30]  # Coordenadas X para la primera línea
y1 = [20, 40, 10]  # Coordenadas Y para la primera línea

# Paso 3: Definir los puntos para la segunda línea
x2 = [10, 20, 30]  # Coordenadas X para la segunda línea
y2 = [40, 10, 30]  # Coordenadas Y para la segunda línea

# Paso 4: Crear el gráfico de las líneas
plt.plot(x1, y1, marker='o', color='blue', linestyle='-', linewidth=2, markersize=8, label='Línea 1')
plt.plot(x2, y2, marker='s', color='red', linestyle='--', linewidth=2, markersize=8, label='Línea 2')



# Paso 6: Añadir etiquetas, título y leyenda
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Gráfico con Dos Líneas')
plt.legend()

# Mostrar el gráfico
plt.grid(True)
plt.show()
