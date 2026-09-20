class Cancion:
    def __init__(self,id,titulo,artista,album,genero,anio,duracion_segundos):
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.genero = genero
        self.anio = anio
        self.duracion_segundos = duracion_segundos

    def listar(self):
        print(f"{self.id:>3}  {self.artista} - {self.titulo}")
