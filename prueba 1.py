#>>>>> Ejercicio muestra

#               Escenario 
#>>> Recientemente has sido contratado para administrar museos de la ciudad de los Angeles
# tu primer proyecto se centra en los 4 museos que se temuestran a continuacion...
# para ello se aprovechara los datos que se proporcionan en el portal de los datos abiertos 
# que tiene la ciudad de los Angeles

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Cargamos los datos, en este caso tomamos el archivo de datos de visitantes de museo de los Angeles en 
# museum_data teniendo en cuenta que  la ruta del archivo en conjunto de datos se almacena como museum_filepath
# el nombre de la columna que se ultilizara como etiqueta es 'Fecha'

dataset_filepath = './dataset.csv'  # Ruta de archivo/dataseth
dataset_data = pd.read_csv(dataset_filepath, index_col='Date',parse_date='True') #leemos y almacenamos el archivo de un dataframe

# Ruta del archivo/dataset a utilizar
museum_filepath = './museum_visitors.csv'  #se ingresa la direccion del archivo, este es solo de ejemplo
museum_data = pd.read_csv(museum_filepath,index_col='Date', parse_dates=True)

# Revisamos datos con tail() que nos permite imprimir las ultimas 5 filas de datos en el dataset
museum_data.tail() 

# Utilizaremos las 5 filas para responder las siguientes preguntas
# ¿Cuantos visitantes recibio el Museo Chino Americano en Julio  de 2018
ca_museum_jul18 = 2620  # En base a la tabla anterior
# En octubre del 2018 ¿Cuantos visitantes mas recibio Avila Adobe que el museo Firehouse?
avila_oct18 = 14658

#>>>> Analizando los datos graficamente
sns.lineplot(data=museum_data)

#>>>> Evaluando la estacionalidad
# Se listan columnas
list(museum_data.columns)
# Grafico de lines que muestre el numero de visitantes 
plt.figure(figsize=(12.6))
plt.title('Numero de visitantes de Avila Adobea lo largo de tiempo')
sns.lineplot(data=museum_data['Avila Adobe'], label='Avila Adobe')
plt.xlabel("Date")

# ¿En que temporada Avila Adobe tiene mas visitantes?



