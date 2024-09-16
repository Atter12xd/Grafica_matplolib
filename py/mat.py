# Paso 1 Importar las Librerías Necesarias
import matplotlib.pyplot as plt
import numpy as np


# paso 2 Crear los datos 
x = np.linspace(-10, 10, 200)  # 200 puntos entre -10 y 10
y1 = x**2  # y1 = x^2
y2 = 2 * x + 3  # y2 = 2x + 3


# paso 3 Crear la Gráfica con Múltiples Elementos
# Crear la figura y los ejes
plt.figure(figsize=(10, 6))  # Tamaño de la figura

# Graficar las funciones
plt.plot(x, y1, label='y = x^2', color='blue', linestyle='-', linewidth=2)  # Gráfica de y1
plt.plot(x, y2, label='y = 2x + 3', color='red', linestyle='--', linewidth=2)  # Gráfica de y2

#Paso 4
# Encontrar y marcar puntos de interés
intersecciones_x = np.array([-3, 1])  # Aprox donde se intersectan las funciones
intersecciones_y = 2 * intersecciones_x + 3  # Valores de y en las intersecciones

plt.scatter(intersecciones_x, intersecciones_y, color='green', zorder=5)  # Puntos de intersección

# Añadir anotaciones
for i in range(len(intersecciones_x)):
    plt.annotate(f'({intersecciones_x[i]}, {intersecciones_y[i]})', 
                 (intersecciones_x[i], intersecciones_y[i]), 
                 textcoords="offset points", 
                 xytext=(-10,10), 
                 ha='center',
                 fontsize=10,
                 color='green')
    
#paso 5
# Personalización
plt.title('Gráfica de Funciones Cuadrática y Lineal', fontsize=16)  # Título
plt.xlabel('Valores de x', fontsize=14)  # Etiqueta del eje x
plt.ylabel('Valores de y', fontsize=14)  # Etiqueta del eje y

# Líneas de cuadrícula
plt.grid(color='gray', linestyle='--', linewidth=0.5)

# Líneas de los ejes
plt.axhline(0, color='black', linewidth=0.8)  # Línea horizontal en y=0
plt.axvline(0, color='black', linewidth=0.8)  # Línea vertical en x=0

# Mostrar leyenda
plt.legend(fontsize=12)