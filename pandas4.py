import pandas as pd
import numpy as np

# MULTIINDEX DF

lista = [['brasil','brasil','brasil','argentina','argentina','argentina'],[2017,2018,2019,2017,2018,2019]]
tuplas = zip(*lista)
tuplas = list(tuplas)
print(tuplas)

multi = pd.MultiIndex.from_tuples(tuplas)

df1 = pd.DataFrame(data=np.random.randn(6,2),index=multi,columns=('EXP TRIGO','EXP ARROZ'))
df1.index.names = ['PAÍS','ANO']
print(df1)

df2 = df1.xs(2017,level=1)
print(df2)

# vendo o DF de outra maneira
df3 = df1.unstack()
print(df3)

df4 = df3.xs(2017,axis=1,level=1)
print(df4)