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



numMovies = 1936
numUsuarios = 10
numRatings = numMovies*numUsuarios

cerosND = np.zeros(numRatings)

moviesND = np.arange(numMovies)
moviesND = moviesND+1
movies2ND = np.arange(numMovies)
movies2ND = movies2ND +1
for n in range(2, numUsuarios+1):
    movies2ND = np.append(movies2ND, moviesND)




usuariosND = np.zeros(numMovies, np.int64)
usuariosND.fill(1)
for n in range (2,numUsuarios+1):
    usuarioND = np.zeros(numMovies, np.int64)
    usuarioND.fill(n)
    usuariosND = np.append(usuariosND, usuarioND)




zerosDict = {'userId': usuariosND, 'movieId':movies2ND}

zerosDF=pd.DataFrame(zerosDict)
zerosDF['rating'] = np.nan
#zerosDF = zerosDF.fillna(0)
print(zerosDF)

print('$$$$$$$$$$      NEW      #########')
      
      


for i in range(1, 2):
    temp =ratingsDF[ ratingsDF.userId == i ]
    for j in range (1, numMovies):
        
        temp2 = temp[temp.movieId==j]
        if not temp2.empty:
            #print (i)
            #print(j)
            #print ([ (i-1)*numMovies + j])
            #print(zerosDF.values[(i-1)*numMovies + j, 2])
            zerosDF.at[(i-1)*numMovies + j, 'rating']= temp2.rating
            #print(zerosDF.values[(i-1)*numMovies + j, 2])
zerosDF = zerosDF.fillna(0)
print (zerosDF)
print ('hola')
