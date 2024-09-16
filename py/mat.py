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