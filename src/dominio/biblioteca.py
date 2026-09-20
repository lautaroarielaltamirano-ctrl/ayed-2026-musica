from .cancion import Cancion
from .version import Version
from .musica import CATALOGO, VERSIONES

class Biblioteca:
    def __init__(self):
        self.canciones = []
        for temas in  CATALOGO:
            self.canciones.append(
                Cancion(
                temas['id'],
                temas['titulo'],
                temas['artista'],
                temas['album'],
                temas['genero'],
                temas['anio'],
                temas['duracion_seg']
                )
            )

    def listar_canciones(self):
        for cancion in self.canciones:
            cancion.listar()

class Versionario:
    def __init__(self):
        self.versiones = []
        for versiones in VERSIONES:
            self.versiones.append(
                Version(
                versiones['cancion_id'],
                versiones['version_de_id'],
                versiones['tipo']
                )
            )

    def versiones_directas(self, id_cancion):
        directas = []
        for versiones in self.versiones:
            if versiones.version_de_id == id_cancion:
                directas.append(versiones.cancion_id)
        return directas

    def versiones_de(self, id_cancion):
        versiones = self.versiones_directas(id_cancion)
        if not versiones:
            return [id_cancion]
        
        resultado = [id_cancion]
        for v in versiones: resultado += self.versiones_de(v)
        return resultado