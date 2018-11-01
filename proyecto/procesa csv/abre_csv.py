import numpy as np 
import pandas as pd 
##
names = ['movieId','title', 'genres']
peliculasDF = pd.read_csv('movies.csv',
                  skiprows = 1,
                  index_col=False, 
                  names = names)
"""
peliculasDF = pd.read_csv('movies.csv')
"""
peliculasDF = peliculasDF.drop(columns="movieId")
#print(peliculasDF)

vectoresLista = []






ratingsDF = pd.read_csv('ratings.csv')
ratingsDF = ratingsDF.drop(columns=['timestamp'])

ratingsDF = ratingsDF.drop(index=range(1259,100836))

print(ratingsDF)

#print(ratingsDF.loc[0])

#print(ratingsDF[ratingsDF.userId==1])

numMovies = 193609
numUsuarios = 10
numRatings = numMovies*numUsuarios

cerosND = np.zeros(numRatings)

moviesND = np.arange(numMovies)
moviesND = moviesND+1
movies2ND = np.arange(numMovies)
movies2ND = movies2ND +1
for n in range(2, numUsuarios+1):
    movies2ND = np.append(movies2ND, moviesND)
#print(movies2ND)
#print(len(movies2ND))

usuariosND = np.zeros(numMovies, np.int8)
usuariosND.fill(1)
for n in range (2,numUsuarios+1):
    usuarioND = np.zeros(numMovies, np.int8)
    usuarioND.fill(n)
    usuariosND = np.append(usuariosND, usuarioND)
#print(usuariosND)
#print(len(usuariosND))


cerosDict = {'userId': usuariosND, 'movieId':movies2ND}

cerosDF=pd.DataFrame(cerosDict)
cerosDF['rating'] = np.nan
#cerosDF = cerosDF.fillna(0)
print(cerosDF)

print('$$$$$$$$$$      NEW      #########')
      
      
nueva = cerosDF.combine_first(ratingsDF)


#nueva = ratingsDF.merge(ratingsDF, how = 'left')
#nueva = cerosDF.fillna(ratingsDF)

print(nueva)