import pandas as pd
import numpy as np

arr = np.random.randint(10,55,size=(4,4))
print(arr)

df1 = pd.DataFrame(data=arr,index=['A','B','C','D'],columns=['W','X','Y','Z'])
print(df1)

lista = [[1,2,3,4,5],[6,7,8,9,10]]
df2 = pd.DataFrame(data=lista)
print(df2)

dados = {'produtos':['videogame','PC','teclado'],'preço':[2000,3000,100]}
df3 = pd.DataFrame(data=dados)
print(df3)
df3['custo'] = [1800,2400,50]
print(df3)
df3['lucro'] = df3['preço'] - df3['custo']
print(df3)
