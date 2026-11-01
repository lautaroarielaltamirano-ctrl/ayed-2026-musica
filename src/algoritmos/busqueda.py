def busqueda_lineal(coleccion, clave, obtener_clave=None):
    """Devuelve el ítem cuya clave coincide, o None."""
    for elemento in coleccion:
        if obtener_clave is None:
            if elemento == clave:
                return elemento
        
        elif obtener_clave(elemento) == clave:
            return elemento
        
    return None


def busqueda_binaria(coleccion, clave, obtener_clave):
    """La colección tiene que estar ordenada por obtener_clave."""
    izq = 0
    der = len(coleccion) - 1

    while izq <= der:
        medio = (izq + der) // 2
        valor = obtener_clave(coleccion[medio])

        if valor == clave:
            return coleccion[medio]

        if valor < clave:
            izq = medio + 1

        if valor > clave:
            der = medio - 1

    return None
