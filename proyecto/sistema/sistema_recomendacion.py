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
                SistemaRecomendacion.MSG_MENU, 1, 3, "La opción es inválida")
            if opcion == 3:
                print("Vuelva pronto")
                break

    def __init__(self):
        SistemaRecomendacion.menu()
