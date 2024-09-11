import matplotlib.pyplot as plt

# Paso 1: Crear una figura y un eje
plt.figure(figsize=(6, 6))

# Paso 2: Definir los puntos para la línea diagonal del 0.50 al 1.50
x = [0.00, 2.00]  # Coordenadas X
y = [0.00, 2.00]  # Coordenadas Y

# Paso 3: Crear el gráfico de la línea diagonal
plt.plot(x, y, marker='o', color='blue', linestyle='-', linewidth=2, markersize=5)

# Paso 5: Añadir etiquetas y título
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Mostrar el gráfico
plt.grid(True)
plt.show()
