import pandas as pd
import numpy as np

data = {'Sede':['SP','SP','MG','MG','RJ','RJ','ES','ES'],
       'Vendedor':['Jorge','Ana','Tiago','Pedro','Raphaela','Guto','Maria','Carolina'],
       'Vendas':[2000,2500,3100,1200,1500,3900,2900,3900]}
df = pd.DataFrame(data)

by_sede = df.groupby('Sede')
by_sedemax = by_sede.max()
print(by_sedemax)
#by_sede.mean (média) - by_sede.describe (tudo)
#by_sede.describe().transpose()  ---> o que é linha vira coluna



arrays = [['São Paulo', 'São Paulo', 'Rio de Janeiro', 'Rio de Janeiro','Minas Gerais','Minas Gerais'],
['Garrafas','Copos','Garrafas','Copos','Garrafas','Copos' ]]
index = pd.MultiIndex.from_arrays(arrays, names=('Estado', 'Produto'))
df1 = pd.DataFrame({'Total Vendido R$': [10000, 35000, 22400, 12890,10880,13900]},index=index)

multi_byestado = df1.groupby('Estado',level=0)
