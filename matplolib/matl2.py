import matplotlib.pyplot as plt

# Paso 1: Crear una figura y un eje
plt.figure(figsize=(8, 8))  # Tamaño más grande para mejor visualización

# Paso 2: Definir los puntos para la línea
x = [1, 2, 3]  # Coordenadas X
y = [2, 4, 1]  # Coordenadas Y

# Paso 3: Crear el gráfico de la línea
plt.plot(x, y, marker='o', color='blue', linestyle='-', linewidth=2, markersize=8)

# Paso 4: Ajustar los límites del gráfico para que la línea ocupe toda la pantalla

# Paso 5: Añadir etiquetas y título
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Mostrar el gráfico
plt.grid(True)
plt.show()
