import pandas as pd
from datetime import date
import matplotlib.pyplot as plt

def over_25_years():
    # Cargar edades desde el archivo CSV
    edades = pd.read_csv('edades.csv', encoding="utf-8", header=None)
    
    # Obtener la fecha de hoy
    hoy = date.today()
    año_actual = hoy.year
    mes_actual = hoy.month
    día_actual = hoy.day
    
    # Función para calcular la edad a partir de la fecha de nacimiento
    def calcular_edad(fecha_nacimiento):
        año_nac, mes_nac, día_nac = map(int, fecha_nacimiento.split('/'))
        edad = año_actual - año_nac - ((mes_actual, día_actual) < (mes_nac, día_nac))
        return edad
    
    # Filtrar las edades para encontrar personas mayores de 25 años
    mayores_de_25 = []
    for índice, fila in edades.iterrows():
        if índice == 0:
            continue  # Saltar la fila de encabezado si está presente
        
        fecha_nacimiento = fila[0]
        edad = calcular_edad(fecha_nacimiento)
        
        if edad > 25:
            mayores_de_25.append(edad)
    
    # Crear un DataFrame con las edades filtradas
    df_edades = pd.DataFrame(mayores_de_25, columns=['Edad'])
    
    # Contar la frecuencia de cada edad
    frecuencia_edades = df_edades['Edad'].value_counts().sort_index()
    
    # Crear el gráfico de líneas
    plt.figure(figsize=(10, 6))
    plt.plot(frecuencia_edades.index, frecuencia_edades.values, marker='o', linestyle='-', color='b')
    
    # Configuración del gráfico
    plt.title('Frecuencia de Edades Mayores de 25 años')
    plt.xlabel('Edad')
    plt.ylabel('Frecuencia')
    plt.grid(True)
    
    # Mostrar el gráfico
    plt.show()

over_25_years()
