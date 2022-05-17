import pandas as pd
import numpy as np
lista = [10,20,30,40,50]
serie = pd.Series(lista)
print(serie)

dicionario = {'telefone1':'123456','telefone2':'123457','telefone3':'987654'}
telefones = pd.Series(dicionario)
print(telefones)

arr = np.array([10,20,30,40,50])
print(arr)
series2 = pd.Series(arr)
print(series2)

series3 = pd.Series([1,2,3,4],index=['brasil','argentina','paraguai','uruguai'])
print(series3)

series4 = pd.Series([4,8,9,1],index=['brasil','usa','paraguai','uruguai'])
print(series4)

soma = series3+series4
print(soma)