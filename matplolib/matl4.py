import matplotlib.pyplot as plt

# Paso 1: Crear una figura y un eje
plt.figure(figsize=(8, 8))  # Tamaño más grande para mejor visualización

# Paso 2: Definir los puntos para la línea discontinua
x2 = [1,4,5,6,7]  # Coordenadas X para la línea discontinua
y2 = [2,6,3,6,3]  # Coordenadas Y para la línea discontinua

# Paso 3: Crear el gráfico de la línea discontinua
plt.plot(x2, y2, marker='s', color='red', linestyle=':', linewidth=2, markersize=8, label='Línea Discontinua')


# Paso 5: Añadir etiquetas, título y leyenda
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Gráfico con Línea Discontinua y Ticks Personalizados')
plt.legend()

# Mostrar el gráfico
plt.grid(True)
plt.show()
