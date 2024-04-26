import matplotlib.pyplot as plt

# Datos de ejemplo
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Graficar x vs y
plt.plot(x, y)
plt.xlabel('Eje X')  # Etiqueta del eje X
plt.ylabel('Eje Y')  # Etiqueta del eje Y
plt.title('Gráfico de Y vs X')  # Título del gráfico
plt.grid(True)  # Mostrar cuadrícula
plt.show()  # Mostrar la gráfica
