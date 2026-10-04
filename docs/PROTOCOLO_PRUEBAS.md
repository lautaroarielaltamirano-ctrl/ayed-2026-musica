# Protocolo de pruebas

Pruebas **manuales**. Cada fila es un caso. Ejecutar sobre el tag que entregan.

Leyenda de resultado: `pasa` / `no pasa` / `no corrido`.

Mínimos: 8 casos escritos en E2; ejecutados en E3; 15 de regresión en E6 (pila, cola, archivos, recursión, búsquedas).

| ID | Entrega | Acción (pasos en el CLI) | Datos | Resultado esperado | Resultado | Notas |
| --- | --- | --- | --- | --- | --- | --- |
| P01 | E1 | Arrancar el programa y listar catálogo | dataset de la cátedra | lista no vacía, sin traceback | pasa |  |
| P02 | E1 | Elegir un ítem inexistente | id = -1 | mensaje claro, el menú sigue | pasa |  |
| P03 | E2 | Operación recursiva sobre un ítem con cadena | ver consigna §3.3 | imprime la cadena completa | pasa |  |
| P04 | E2 | Operación recursiva sobre un ítem sin derivados |  | imprime solo el ítem ingresado (caso base) | pasa |  |
| P05 | E2 | Evaluar la función recursiva con una canción no existente (ej:100) | La función devuelve un mensaje de error claro (ItemNoEncontradoError), el menú sigue | pasa |  |
| P06 | E2 | Evaluar la función recursiva con valor que no sea int (ej:abc) |  | La función devuelve un mensaje de error (ValueError), el menú sigue | pasa |  | 
| P07 | E1 | Pasar enter vacío en el menú |  | El menú continúa | pasa |  |
| P08 | E1 | Elegir una opción de menú inválida (ej. “abc”) |  | La función devuelve un mensaje de error claro, el menú sigue | pasa |  |
| P09 | E3 | Agregar a la colección principal hasta el tope | equipo de 6 / equivalente | el decimoquinto falla con excepción propia | pasa |  |
| P10 | E3 | Desapilar historial vacío | pila vacía | excepción propia, menú sigue | pasa |  |
| P11 | E3 | Desencolar cola vacía | cola vacía | excepción propia, menú sigue | pasa |  |
| P12 | E3 | Listar colección con el iterador | 2+ ítems | el orden coincide con las inserciones | pasa |  |
| P13 | E4 | Búsqueda lineal de un nombre que existe |  | lo encuentra |  |  |
| P14 | E4 | Búsqueda lineal de un nombre que no existe |  | no encontrado, sin traceback |  |  |
| P15 | E4 | Búsqueda binaria con catálogo desordenado |  | avisa o reordena; no da un falso hit |  |  |
| P16 | E4 | Ordenar por un criterio y después por otro |  | el orden cambia |  |  |
| P17 | E5 | Guardar CSV, salir, volver a entrar |  | los datos siguen |  |  |
| P18 | E5 | Guardar binario y modificar un registro por id |  | al recargar, ese campo cambió |  |  |
| P19 | E5 | Abrir un binario truncado o con magia mala | archivo basura | excepción de archivo inválido |  |  |
