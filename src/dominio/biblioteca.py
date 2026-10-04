from .cancion import Cancion
from .version import Version
from .musica import CANCIONES, VERSIONES
from src.tads.lista_enlazada import ListaEnlazada

Catalogo = ListaEnlazada()
for datos in CANCIONES:
    cancion = Cancion(**datos)
    Catalogo.insertar_al_final(cancion)

class Biblioteca:
    def __init__(self, catalogo):
        self.catalogo = catalogo

    def listar_canciones(self):
        for cancion in self.catalogo:
            print(cancion)

    def mostrar_canciones(self, ids):
        for id in ids:
            for cancion in self.catalogo:
                if cancion._id == id:
                    print(cancion)

    def mostrar_detalles(self, id):
        for cancion in self.catalogo:
            if cancion._id == id:
                cancion.mostrar_detalles()
                return
    
    def buscar(self, id):
        for cancion in self.catalogo:
            if cancion._id == id:
                return cancion
        return None
            
biblioteca = Biblioteca(Catalogo)





Catalogo_versiones = ListaEnlazada()
for datos in VERSIONES:
    versiones = Version(**datos)
    Catalogo_versiones.insertar_al_final(versiones)

class Biblioteca_versiones:
    def __init__(self, versionario):
            self.versionario = versionario

    def versiones_directas(self, id_cancion):
        directas = []

        for version in self.versionario:
            if version._version_id == id_cancion:
                directas.append(version._cancion_id)
        return directas

    def versiones_de(self, id_cancion):
        versiones = self.versiones_directas(id_cancion)

        if not versiones:
            return [id_cancion]
        
        resultado = [id_cancion]
        for v in versiones: resultado += self.versiones_de(v) #Funcion recursiva, devuelve lista con ids de las canciones
        return resultado


versionario = Biblioteca_versiones(Catalogo_versiones)