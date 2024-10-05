import pandas as pd

datos = {"Nombres": ["Alex", "Valeria", "Sara"],
         "Edad": [34, 33, 15],
         "RH": ["O", "B", "AB"]}

df= pd.DataFrame(datos)
print(df)
