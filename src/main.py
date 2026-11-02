from src.config import TEMA
from src.dominio.biblioteca import biblioteca, versionario
from src.dominio.playlist import playlist
from src.dominio.historial import historial
from src.dominio.cola_reproduccion import cola_reproduccion
from src.excepciones import ItemNoEncontradoError, ColeccionLlenaError, PilaVaciaError, ColaVaciaError
from src.algoritmos.busqueda import busqueda_lineal, busqueda_binaria
from src.algoritmos.ordenamiento import ordenar_seleccion, ordenar_insercion
canciones = list(biblioteca.catalogo) #el documento de E4 dice que esta permitido si tenemos el catalogo en listaenlazada, como es nuestro caso

TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}



def pedir_id_cancion():
    id_cancion = int(input("Ingrese el ID de la canción: "))
    if id_cancion <= 0 or id_cancion >= 68:
        raise ItemNoEncontradoError("Canción no encontrada.")
    return id_cancion

def pedir_titulo():
    titulo = input("Ingrese el titulo de la cancion:" ).strip()
    if not titulo: 
        raise ValueError("Debe ingresar un titulo para iniciar la busqueda.")
    return titulo

def pendiente():
    print("Todavía no está implementado. Completar en la entrega que corresponde.")


def mostrar_menu():
    nombre = TEMAS.get(TEMA, TEMA or "(sin tema)")
    print()
    print(f"=== {nombre} — AyED C2 2026 ===")
    print("1. Listar catálogo")
    print("2. Ver detalle")
    print("3. Buscar")
    print("4. Ordenar")
    print("5. Mostrar versiones Alternativas")
    print("6. Colección principal (equipo / menú / playlist)")
    print("7. Historial (pila)")
    print("8. Cola")
    print("9. Guardar / cargar archivos")
    print("0. Salir")

def mostrar_menu_busqueda():
    print(f"=== Busqueda ===")
    print("1. Buscar por Titulo (lineal)")
    print("2. Buscar por Titulo (binaria) - Se reordenara la lista por titulo")
    print("0. Volver")

def mostrar_menu_ordenamiento():
    print(f"=== Ordenamiento ===")
    print("1. Ordenar por Titulo (insercion)")
    print("2. Ordenar por ID (seleccion)")
    print("0. Volver")

def mostrar_menu_playlist():
    print(f"=== Playlist ===")
    print("1. Agregar a la lista de reproduccion")
    print("2. Eliminar de la lista de reproduccion")
    print("3. Ver lista de reproduccion")
    print("0. Volver")

def mostrar_menu_pila():
    print("1. Agregar al historial")
    print("2. Eliminar del historial")
    print("3. Ver última canción")
    print("0. Volver")

def mostrar_menu_cola():
    print("1. Encolar")
    print("2. Desencolar")
    print("0. Volver")

def main():
    if TEMA not in TEMAS:
        print("Seteá TEMA en src/config.py: 'pokedex', 'recetario' o 'musica'.")
        return

    opcion = None
    while opcion != "0":
        mostrar_menu()
        opcion = input("> ").strip()
        if opcion == "0":
            print("Chau.")
        elif opcion == "1": #listado
            biblioteca.listar_canciones()

        elif opcion == "2": #detalles de una cancion
            try:
                id_cancion = pedir_id_cancion()
                biblioteca.mostrar_detalles(id_cancion)

            except ItemNoEncontradoError as e:
                print(e)
            except ValueError:
                print("Debe ingresar un número entero.")

        elif opcion == "3": #busqueda
            opcion_busqueda = None
            while opcion_busqueda != "0":
                mostrar_menu_busqueda()
                opcion_busqueda = input("> ").strip()
                if opcion_busqueda == "0":
                    break
                elif opcion_busqueda == "1":
                    try: 
                        titulo = pedir_titulo()
                        resultado = busqueda_lineal(canciones, titulo, lambda c: c._titulo)

                        if resultado is not None:
                            print(resultado)
                        
                        else: print("No se encontro en la biblioteca.")
                
                    except ValueError as e:
                        print(e)
                
                elif opcion_busqueda == "2":
                    ordenar_insercion(canciones, lambda c: c._titulo)
                    print("se reordeno la lista por titulo.")
                    try:
                        titulo = pedir_titulo()
                        resultado = busqueda_binaria(canciones, titulo, lambda c: c._titulo)

                        if resultado is not None:
                            print(resultado)

                        else: print("No se encontro en la biblioteca.")

                    except ValueError as e:
                        print(e)
                
                else:
                    print("Opción inválida.")

        elif opcion == "4": #ordenamiento
                opcion_ordenamiento = None
                while opcion_ordenamiento != "0":
                        mostrar_menu_ordenamiento()
                        opcion_ordenamiento = input("> ").strip()
                        if opcion_ordenamiento == "0":
                            break
                        elif opcion_ordenamiento == "1":
                            ordenar_insercion(canciones, lambda c: c._titulo)
                            print("Se ordeno por titulo.")
                            for c in canciones:
                                print(c)

                        elif opcion_ordenamiento == "2":
                            ordenar_seleccion(canciones, lambda c: c._id)
                            print("Se ordeno por id.")
                            for c in canciones:
                                print(c)

                        else:
                            print("Opción inválida.")

        elif opcion == "5": #recursiva
            try:
                id_cancion = pedir_id_cancion()
                resultado = versionario.versiones_de(id_cancion)
                biblioteca.mostrar_canciones(resultado)

            except ItemNoEncontradoError as e:
                print(e)
            except ValueError:
                print("Debe ingresar un número entero.")

        elif opcion == "6":
            opcion_playlist = None
            while opcion_playlist != "0":
                mostrar_menu_playlist()
                opcion_playlist = input("> ").strip()
                if opcion_playlist == "0":
                    break
                elif opcion_playlist == "1":
                    try: 
                        id_cancion = pedir_id_cancion()
                        playlist.agregar(biblioteca.buscar(id_cancion))

                    except ItemNoEncontradoError as e:
                        print(e)
                    except ColeccionLlenaError as e:
                        print(e)
                    except ValueError:
                        print("Debe ingresar un número entero.")

                elif opcion_playlist == "2":
                    try:
                        id_cancion = pedir_id_cancion()
                        playlist.eliminar(biblioteca.buscar(id_cancion))

                    except ItemNoEncontradoError as e:
                    
                        print(e)
                    except ValueError:
                        print("Debe ingresar un número entero.")

                elif opcion_playlist == "3":
                    playlist.listar()
                else:
                    print("Opción inválida.")
        
        elif opcion == "7":
            opcion_pila = None
            while opcion_pila != "0":
                mostrar_menu_pila()
                opcion_pila = input("> ").strip()
                if opcion_pila == "0":
                    break
                elif opcion_pila == "1":
                    try: 
                        id_cancion = pedir_id_cancion()
                        historial.apilar(biblioteca.buscar(id_cancion))

                    except ItemNoEncontradoError as e:
                        print(e)
                    except ValueError:
                        print("Debe ingresar un número entero.")

                elif opcion_pila == "2":
                    try:  
                        print(f'Eliminada del historial: {historial.desapilar()}')

                    except PilaVaciaError as e:
                        print(e)

                elif opcion_pila == "3":
                    try: print(historial.ver_tope())
                    except PilaVaciaError as e:
                        print(e)

                else:
                    print("Opción inválida.")

        elif opcion == "8":
            opcion_cola = None
            while opcion_cola != "0":
                mostrar_menu_cola()
                opcion_cola = input("> ").strip()
                if opcion_cola == "0":
                    break
                elif opcion_cola == "1":
                    try: 
                        id_cancion = pedir_id_cancion()
                        cola_reproduccion.encolar(biblioteca.buscar(id_cancion))
                    
                    except ItemNoEncontradoError as e:
                        print(e)
                    except ValueError:
                        print("Debe ingresar un número entero.")

                elif opcion_cola == "2":
                    try: 
                        print(f'Eliminada de la cola: {cola_reproduccion.desencolar()}')
                    except ColaVaciaError as e:
                        print(e)
                
                else:
                    print("Opción inválida.")

        elif opcion in {"9"}:
            pendiente()
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
