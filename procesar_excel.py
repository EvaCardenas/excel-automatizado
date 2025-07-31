import pandas as pd

# Cargar ambos archivos Excel
archivo_excel_1 = pd.ExcelFile('C:\\Users\\PC\\Downloads\\df_merged_motorizado02.xlsx')
archivo_excel_2 = pd.ExcelFile('C:\\Users\PC\\Downloads\\30df_final_actualizado.xlsx')


print("Hojas disponibles en el archivo:", archivo_excel_2.sheet_names)

# Cargar una hoja específica como DataFrame (por ejemplo, la primera)
df_excel = archivo_excel_2.parse(archivo_excel_2.sheet_names[0])

# Mostrar cantidad de filas y columnas
print(f"\n✅ El DataFrame resultante tiene {df_excel.shape[0]} filas y {df_excel.shape[1]} columnas.")
print("Primeras filas del DataFrame resultante:")
print(df_excel.head())

# Mostrar los nombres de las hojas de ambos archivos
print("Hojas en el primer archivo:")
print(archivo_excel_1.sheet_names)

print("\nHojas en el segundo archivo:")
print(archivo_excel_2.sheet_names)
