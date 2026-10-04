from src.config import TEMA
from src.dominio.biblioteca import biblioteca, versionario
from src.dominio.playlist import playlist
from src.dominio.historial import historial
from src.dominio.cola_reproduccion import cola_reproduccion
from src.excepciones import ItemNoEncontradoError, ColeccionLlenaError, PilaVaciaError, ColaVaciaError

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
        elif opcion == "1":
            biblioteca.listar_canciones()
        elif opcion == "2":
            try:
                id_cancion = pedir_id_cancion()
                biblioteca.mostrar_detalles(id_cancion)

            except ItemNoEncontradoError as e:
                print(e)
            except ValueError:
                print("Debe ingresar un número entero.")

        elif opcion == "5":
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

        elif opcion in {"3", "4", "9"}:
            pendiente()
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
