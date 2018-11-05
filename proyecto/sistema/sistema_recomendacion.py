from sistema.utils import getIntegerFromInterval
from sistema.csv.abre_csv import calcularRecomendaciones, getNumUsers, searchMovieById, searchMovies, saveInRankigs, getNumMovies


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
            elif opcion == 1:
                nUsuarios = getNumUsers()
                recomendaciones = calcularRecomendaciones(
                    getIntegerFromInterval(
                        ("Digite el número de usuario a buscar, del 1 al %d:\n" %
                         nUsuarios),
                        1, nUsuarios,
                        "El usuario que intenta buscar no existe"))
                print("Las recomendaciones son las siguientes:\n")
                numP = 1
                for i in reversed(recomendaciones.index):
                    print("%d: %s (recomendacion %s)" % (
                        numP, searchMovieById(
                            recomendaciones.loc[i, "pelicula"]),
                        recomendaciones.loc[i, "recomendacion"]))
                    numP += 1
            elif opcion == 2:
                SistemaRecomendacion.agregarUsuario()

    @staticmethod
    def agregarUsuario():
        nUsuarios = getNumUsers()
        print("De las siguientes películas ingrese los rankigs de 10 películas:\nID:NOMBRE_PELÍCULA (GÉNERO)")
        peliculas = searchMovies()
        for i in peliculas.index:
            print("%d: %s (%s)" %
                  (peliculas.loc[i, "movieId"], peliculas.loc[i, "title"], peliculas.loc[i, "genres"]))
        while True:
            peliculasRankeadas = input(
                "El formato debe ser el siguiente: idPelicula,ranking,idPelicula2,ranking2...\nEl ranking debe ser del 1 al 5 [1-5]\nSe le recuerda que no puede dar diferentes rankigs a la misma película.\n").strip()
            peliculasRankeadas = SistemaRecomendacion.formateaArregloDePeliculasYRankings(
                peliculasRankeadas)
            if not peliculasRankeadas:
                print("El formato es inválido")
                continue
            saveInRankigs(nUsuarios + 1, peliculasRankeadas)
            break
        print("Se han guardado su registro, el número de usuario que tiene es el número %d" % (
            nUsuarios + 1))

    @staticmethod
    def formateaArregloDePeliculasYRankings(cadenaDeEntrada):
        arregloDeEntrada = cadenaDeEntrada.split(",")
        if len(arregloDeEntrada) != 20:
            return None
        try:
            maxMovie = getNumMovies()
            maxRanking = 5
            result = []
            peliculasReportadas = set()
            for i in range(0, len(arregloDeEntrada), 2):
                tmp = [int(arregloDeEntrada[i]),
                       float(arregloDeEntrada[i + 1])]
                peliculasReportadas.add(tmp[0])
                if tmp[0] < 1 or tmp[1] < 1 or tmp[0] > maxMovie or tmp[1] > maxRanking:
                    return None
                result.append(tmp)
            if len(peliculasReportadas) != 10:
                return None
            return result
        except Exception:
            return None

    def __init__(self):
        SistemaRecomendacion.menu()
