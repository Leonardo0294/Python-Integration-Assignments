import matplotlib.pyplot as plt
import pandas as pd

# Crear un DataFrame con datos de ejemplo
data = {
    'Año': [2010, 2011, 2012, 2013, 2014],
    'Ventas': [100, 150, 200, 180, 220]
}

df = pd.DataFrame(data)

# Graficar los datos usando matplotlib
plt.plot(df['Año'], df['Ventas'], marker='o', linestyle='-', color='b')
plt.xlabel('Año')
plt.ylabel('Ventas')
plt.title('Ventas anuales')
plt.grid(True)
plt.show()
