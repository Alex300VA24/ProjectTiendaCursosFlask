import datetime

class Compra:
    
    def __init__(self, codigo, curso, usuario, fecha=None):
        self.codigo = codigo
        self.curso = curso
        self.usuario = usuario
        self.fecha = fecha
    
    def formatted_date(self):
        return datetime.datetime.strftime(self.fecha, "%d/%m/%Y - %H:%M:%S")
        