from sistema.utils import getIntegerFromInterval


class SistemaRecomendacion():

    MSG_BIENVENIDA = "¡Bienvenido al sistema de recomendaciones!"

    MSG_MENU = """
Digite una opción:

1) Iniciar sesión
2) Dar de alta nuevo usuario
3) Salir
                """

    @staticmethod
    def menu():
        print(SistemaRecomendacion.MSG_BIENVENIDA)
        while True:
            opcion = getIntegerFromInterval(
                SistemaRecomendacion.MSG_MENU, 1, 2, "La opción es inválida")
            if opcion == 3:
                print("Vuelva pronto")
                break
            elif opcion == 1:
                SistemaRecomendacion.buscarSugerencia(
                    getIntegerFromInterval(
                        "Digite el número de usuario a buscar", 1, nUsuarios,
                        "El usuario que intenta buscar no existe"))
            elif opcion == 2:
                SistemaRecomendacion.agregarUsuario()

    @staticmethod
    def buscarSugerencia(idUsuario):
        return

    def __init__(self):
        SistemaRecomendacion.menu()
