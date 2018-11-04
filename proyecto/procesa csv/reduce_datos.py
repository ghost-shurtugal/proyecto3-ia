import numpy as np 
import pandas as pd 


numPeliculas= 14
numUsuarios=20



moviesDf = pd.read_csv('movies.csv')
nFilas = len(moviesDf.index)
moviesDf = moviesDf.drop(index=range(numPeliculas,nFilas))
print("movies")
#print(moviesDf)
moviesDf.to_csv(r'movies_reducido.csv')


ratingsDf = pd.read_csv('ratings.csv')
ratingsDf = ratingsDf.drop(columns=['timestamp'])

ratingsDf = ratingsDf[ratingsDf['movieId'] < numPeliculas]  

ratingsDf = ratingsDf[ratingsDf['userId'] < numUsuarios]  




print("ratings")
print(ratingsDf)

ratingsDf.to_csv(r'ratings_reducido.csv', index=False)