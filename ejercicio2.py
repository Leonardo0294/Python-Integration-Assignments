import pandas as pd
from datetime import datetime

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('edades.csv')

# Convertir la columna 'fecha_nacimiento' a tipo datetime
df['fecha_nacimiento'] = pd.to_datetime(df['fecha_nacimiento'])

# Calcular la fecha actual
fecha_actual = datetime.now()

# Calcular la edad de cada persona en años
df['edad'] = (fecha_actual - df['fecha_nacimiento']).astype('<m8[Y]')

# Filtrar personas mayores de 25 años
df_filtrado = df[df['edad'] > 25]

# Ordenar las edades en forma ascendente
df_filtrado = df_filtrado.sort_values(by='edad')

# Contar las edades únicas y su frecuencia
edades_unicas = df_filtrado['edad'].value_counts().sort_index()

# Crear un DataFrame con las edades únicas y su frecuencia
df_edades = pd.DataFrame({'Edad': edades_unicas.index, 'Frecuencia': edades_unicas.values})

# Mostrar el DataFrame resultante
print(df_edades)
