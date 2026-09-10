# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

## 1. Grupo y tema

- Tema: Biblioteca musical
- Por qué lo eligieron (5–8 líneas): Elegimos desarrollar una biblioteca musical porque nos permite trabajar con un conjunto de datos real almacenado en un archivo CSV.
Creemos que es un tema sencillo de entender y fácil de aplicar en la materia.
Nos permite practicar el uso de listas, diccionarios y funciones en Python.
También facilita organizar la información de manera clara y ordenada.
 

## 2. Modelo

Qué es un ítem del catálogo. Qué es mutable y qué no (E1). Cómo se relacionan catálogo, colección principal, pila y cola.

Cada item del catálogo es una canción y cada una contiene como atibutos: "id","titulo","artista","album","genero","anio" y "duracion_seg". Por un lado la ID se utiliza tanto para identificar cada canción dentro de la biblioteca de canciones, como también para relacionarlas con sus versiones alternativas (remix, live, cover), por lo que cambiarlas ocasionaría errores. 
Los demás atributos son características propias de cada canción y no deberían cambiar nunca. Por ejemplo: El año de publicación es un dato que permanece en el tiempo y no se debe modificar. La totalidad de sus atributos son por lo tanto inmutables.
Las estructuras mutables son el catálogo (Biblioteca) y la colección principal (Playlist), ya que permiten modificar el orden de los items, y agregar/quitar canciones sin alterar sus atributos.

```text
<u>Relaciónes entre catálogo, colección principal, pila y cola</u>

                    Biblioteca (todos los ítems)
                                  │
                                  ▼
                Playlist (ítems activos/gestionados)
                                  │
              ┌───────────────────┴───────────────────┐
              ▼                                       ▼
            Pila                                    Cola
(Historial de reproducción)                 (Cola de reproducción)
```

## 3. Recursión (E2)

- Función:
- Caso base:
- Caso recursivo:
- Traza de un ejemplo real del dataset:

## 4. TADs (E3)

| TAD | Operaciones | Invariante |
| --- | --- | --- |
| ListaEnlazada |  |  |
| Pila |  |  |
| Cola |  |  |

Dónde se usa cada uno en el dominio.

## 5. Complejidad (E4)

| Operación | Tiempo | Espacio | Por qué |
| --- | --- | --- | --- |
|  |  |  |  |

Mediciones (`time.perf_counter`):

| Operación | n | segundos |
| --- | --- | --- |
|  |  |  |

## 6. Persistencia (E5)

- Layout del registro binario (campos, `struct`, anchos):
- Header:
- Cómo se actualiza un registro por posición:

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |
