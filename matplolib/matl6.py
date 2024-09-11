import matplotlib.pyplot as plt
from datetime import datetime

# Paso 1: Definir las fechas en el eje X y los valores del eje Y
fechas = ['2016-10-03', '2016-10-04', '2016-10-05', '2016-10-06', '2016-10-07']
fechas = [datetime.strptime(fecha, '%Y-%m-%d') for fecha in fechas]
valores = [772.5, 776.5, 776.6, 777.0, 774.5]

# Paso 2: Crear la figura y el gráfico
plt.figure(figsize=(10, 6))  # Tamaño de la figura

# Paso 3: Graficar los datos
plt.plot(fechas, valores, marker='o', color='red', linestyle='-', linewidth=2, markersize=8)

# Paso 4: Añadir etiquetas y título
plt.xlabel('Fecha', fontsize=12)
plt.ylabel('Valor', fontsize=12)
plt.title('Gráfico de valores entre 2016-10-03 y 2016-10-07', fontsize=14)

# Paso 5: Ajustar los límites del eje Y
plt.ylim(772, 778)

# Paso 6: Mostrar la cuadrícula
plt.grid(True)

# Mostrar el gráfico
plt.show()