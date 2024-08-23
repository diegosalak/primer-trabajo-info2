class Paciente():
    def __init__(self):
        self.__nombre = ""
        self.__cedula = 0
        self.__genero = ""
        self.__servicio = ""

    def AsignarNombre(self, nombre):
        self.__nombre = nombre

    def AsignarCedula(self, cedula):
        self.__cedula = cedula

    def AsignarGenero(self, genero):
        self.__genero = genero

    def AsignarServicio(self, servicio):
        self.__servicio = servicio

    def VerNombre(self):
        return self.__nombre

    def VerCedula(self):
        return self.__cedula

    def VerGenero(self):
        return self.__genero

    def VerServicio(self):
        return self.__servicio


class Sistema:
    def __init__(self):
        self.__listaPacientes = []
        self.__numPacientes = len(self.__listaPacientes)

    def IngresarPac(self):
        nombre = input("Ingrese el nombre: ")
        cedula = int(input("Ingrese la cedula: "))
        genero = input("Ingrese el genero ")
        servicio = input("Ingrese el servicio: ")

        p = Paciente()
        p.AsignarNombre(nombre)
        p.AsignarCedula(cedula)
        p.AsignarGenero(genero)
        p.AsignarServicio(servicio)

        self.__listaPacientes.append(p)
        self.__numPacientes = len(self.__listaPacientes)

    def VerNumPac(self):
        return self.__numPacientes

    def VerDataPac(self):
        cedula = int(input("Ingrese la cedula a buscar: "))
        for paciente in self.__listaPacientes:
            if cedula == paciente.VerCedula():
                print("Nombre:" + paciente.VerNombre())
                print("Cedula:" + str(paciente.VerCedula()))
                print("Genero:" + paciente.VerGenero())
                print("Servicio:" + paciente.VerServicio())
            else:
                print("no existe el paciente")


miSistema = Sistema()

while True:
    opcion = int(input(
        "1. Nuevo Paciente - 2. Numero de pacientes - 3. Datos de paciente - 4. Salir "))
    if opcion == 1:
        miSistema.IngresarPac()
    elif opcion == 2:
        print("Ahora hay: " + str(miSistema.VerNumPac()))
    elif opcion == 3:
        miSistema.VerDataPac()
    elif opcion == 4:
        break
    else:
        print("Opcion no valida")
