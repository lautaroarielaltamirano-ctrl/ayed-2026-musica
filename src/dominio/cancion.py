class Cancion:
    def __init__(self,id,titulo,artista,album,genero,anio,duracion_seg):
        self._id = id
        self._titulo = titulo
        self._artista = artista
        self._album = album
        self._genero = genero
        self._anio = anio
        self._duracion_seg = duracion_seg

    def __str__(self):
        return f"{self._id:>3}  {self._artista} - {self._titulo} - {self._album}"

    def mostrar_detalles(self):
        print(f"{self._id:>3}  {self._artista} - {self._titulo} - {self._album} - {self._genero} - {self._anio} - {self._duracion_seg//60:.0f} minutos y {self._duracion_seg%60} segundos")