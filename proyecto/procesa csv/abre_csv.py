import numpy as np 
import pandas as pd 



def crea_cerosDf(numMovies, numUsuarios):
    
    #este vector se usará para la columna movies, son las peliculas
    #repetidas u veces donde u son los usuarios
    moviesND = np.arange(numMovies)
    moviesND = moviesND+1
    movies2ND = np.arange(numMovies)
    movies2ND = movies2ND +1
    for n in range(2, numUsuarios+1):
        movies2ND = np.append(movies2ND, moviesND)
    
    #esta es la columna de usuarios
    usuariosND = np.zeros(numMovies, np.int64)
    usuariosND.fill(1)
    for n in range (2,numUsuarios+1):
        usuarioND = np.zeros(numMovies, np.int64)
        usuarioND.fill(n)
        usuariosND = np.append(usuariosND, usuarioND)   

    #crea el Dataframe        
    zerosDict = {'userId': usuariosND, 'movieId':movies2ND}
    zerosDF=pd.DataFrame(zerosDict)
    zerosDF['rating'] = np.nan
    
    return zerosDF


def combinaDf(numMovies, numUsuarios, ratingsDF, zerosDf):
    for i in range(1, numUsuarios):
        temp =ratingsDF[ ratingsDF.userId == i ]
        for j in range (1, numMovies):
            
            temp2 = temp[temp.movieId==j]
            if not temp2.empty:
                #print (i)
                #print(j)
                #print ([ (i-1)*numMovies + j])
                #print(zerosDF.values[(i-1)*numMovies + j, 2])
                zerosDf.at[(i-1)*numMovies + j, 'rating']= temp2.rating
                #print(zerosDF.values[(i-1)*numMovies + j, 2])
    zerosDf = zerosDf.fillna(0)

    zerosDf.to_csv(r'zerosDf.csv')
    return zerosDf
    
    
def vectoriza(numMovies, numUsuarios, zerosDf):
    
    #crea un Df vacio con los indides de las peliculas como columnas
    peliculasND = np.arange(numMovies)
    vectorsDF = pd.DataFrame(columns = peliculasND)   
    
    for i in range(1, numUsuarios):
        vectUsuario = zerosDf.loc[zerosDf.userId == i]
        if (i <3):
            print("fd")
            #print(vectUsuario)
        vectUsuario = vectUsuario.drop(columns = ['userId', 'movieId'])
        #print(vectUsuario)
        vectUsuario = vectUsuario.stack()
        vectUsuario = vectUsuario.values
        seriesUsuario = pd.Series(vectUsuario)
        #print(vectUsuario)
        vectorsDF = vectorsDF.append(seriesUsuario, ignore_index=True)
    return vectorsDF


def obten_distancias(numUsuarios, vectorsDf, miVector):
    
    distancias = pd.DataFrame(columns =['i', 'd'])

    for i in range (1, numUsuarios-1):
        vectUs = vectorsDF.values[i]
        dist = np.linalg.norm(miVector- vectUs)
        nueva = pd.Series([i, dist])
        distancias = distancias.append(nueva, ignore_index = True)
    
    
    distancias = distancias.drop(columns= ['i', 'd'])
    distancias = distancias.rename(index=str, columns={0: "id", 1: "dist"})

    distancias = distancias.sort_values(by=['dist'])
    return distancias

    
def obten_rec(distancias):
    
    suma = np.zeros(numMovies, np.int64)
    
    for i in range (0,4):
        index = distancias.values[i,0]
        index_int = int(index)
        print(index)
        suma= np.add(suma, vectorsDF.values[index_int])
        print (vectorsDF.values[index_int])
    print (suma)
    recomendaciones = suma *(1/4)
    print(recomendaciones)
    
    
    recDF = pd.DataFrame(columns =['peli', 'rec'])
    for i in range (1, numMovies-1):
        nueva = pd.Series([i, recomendaciones[i]])
        recDF = recDF.append(nueva, ignore_index = True)
        
    
    print(recDF)
    recDf = recDF.sort_values(by=[1])
    return recDf




numMovies = 1936
numUsuarios = 10

ratingsDF = pd.read_csv('ratings.csv')
ratingsDF = ratingsDF.drop(columns=['timestamp'])
ratingsDF = ratingsDF.drop(index=range(1259,100836))
print(ratingsDF)



zerosDf = crea_cerosDf(numMovies, numUsuarios)
print(zerosDf)




zerosDf = combinaDf(numMovies, numUsuarios, ratingsDF, zerosDf)
print ("combinados")
print(zerosDf)
      

vectorsDf = vectoriza(numMovies, numUsuarios, zerosDf)
print ("vectors")
print(vectorsDf)



miVector = zerosDf.loc[zerosDf.userId == 1]
miVector = miVector.drop(columns = ['userId', 'movieId'])
    #print(vectUsuario)
miVector = miVector.stack()
miVector = miVector.values



distancias = obten_distancias(numUsuarios, vectorsDf, miVector)
print("distancias")
print(distancias)


recDf = obten_rec(distancias)
print("recomendaciones")
print(recDF)


