archivoN = open("valores.txt") # Archivo valores txt
archivoS = open("valores_totales.txt", 'wt') # aquí crea el archivo valores totales, y pasamos la operacion deseada sobre el archivo.
print("Procesando entrada...")

suma = 0

for linea in archivoN:
    suma += int(linea) # tenemos que convertir las lineas a enteros para poder sumarlas.
    print(linea.rstrip(), file = archivoS) # rightStrip borra los espacios en blanco del archivo a la derecha.

print("\nTotal", suma, file = archivoS) # el resultado se imprime en el mismo archivo S ( valores_totales.txt ).

archivoS.close() # Cerramos el archivo.
print("Salida completada...")