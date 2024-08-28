#data frame
import pandas as pd
data={
    'nombre' : ['Juan', 'Ana', 'Luis', 'Marta'],
    'edad' : [15, 14, 16, 15],
    'nota' : [8.5,9.0,7.5,8.0]
}
df = pd.DataFrame(data)
#agregar una nueva columna
df['Ciudad'] = ['madrid', 'barcelona', 'valencia','sevilla']
#mostrar los primeros datos de la fila
print(df.head(1))
