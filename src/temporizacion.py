import time
from src.main import canciones
from src.algoritmos.busqueda import busqueda_lineal, busqueda_binaria
from src.algoritmos.ordenamiento import ordenar_insercion
canciones_grandes = canciones * 10

ordenar_insercion(canciones, lambda c: c._titulo)
ordenar_insercion(canciones_grandes, lambda c: c._titulo)
titulo = "hola123456789"

# Búsqueda lineal (67)
inicio = time.perf_counter()
resultado = busqueda_lineal(canciones, titulo, obtener_clave=lambda c: c._titulo)
fin = time.perf_counter()
print(f"Lineal (67): {fin - inicio:.6f} s")

# Búsqueda lineal (670)
inicio = time.perf_counter()
resultado = busqueda_lineal(canciones_grandes, titulo, obtener_clave=lambda c: c._titulo)
fin = time.perf_counter()
print(f"Lineal (670): {fin - inicio:.6f} s")

# Búsqueda binaria (67)
inicio = time.perf_counter()
resultado = busqueda_binaria(canciones, titulo, obtener_clave=lambda c: c._titulo)
fin = time.perf_counter()
print(f"Binaria (67): {fin - inicio:.6f} s")

# Búsqueda binaria (670)
inicio = time.perf_counter()
resultado = busqueda_binaria(canciones_grandes, titulo, obtener_clave=lambda c: c._titulo)
fin = time.perf_counter()
print(f"Binaria (670): {fin - inicio:.6f} s")

"python -m src.temporizacion"
