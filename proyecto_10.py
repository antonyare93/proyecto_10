class Alumno():
    def __init__(self, nombre="Sin nombre", nota="Sin nota") -> None:
        self.nombre = nombre
        self.nota = nota
        if self.nota.isnumeric():
            if int(self.nota)>5:
                # self.aprueba = True
                self.aprueba = 'arpueba'
            else:
                # self.aprueba = False
                self.aprueba = 'reprueba'
        else:
            self.aprueba = 'Sin definir'


estudiante1 = Alumno('Jacobo', '6')

print(f'El estudiante {estudiante1.nombre} saca {estudiante1.nota} en su nota final, por lo tanto {estudiante1.aprueba}')