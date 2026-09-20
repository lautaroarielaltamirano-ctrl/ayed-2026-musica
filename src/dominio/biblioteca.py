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
        for directas in VERSIONES:
            self.versiones.append(
                Version(
                directas['cancion_id'],
                directas['version_de_id'],
                directas['tipo']
                )
            )

