import pandas as pd
import numpy as np
np.random.seed(100)

indices = ['janeiro','marco','maio','julho','agosto','outubro','novembro']
colunas = np.arange(1,32)
dados = np.random.randint(492,2050,size=(7,31))

df = pd.DataFrame(data=dados,index=indices,columns=colunas)
print(df)

# df[coluna]
# df[[col1,col2,col3]]
# df[coluna][linha]
# df[linha1:linha2][2:][2:5]
# df.loc[indice linha, indice coluna] df.loc['julho',30]
# df.iloc[ind num linha, ind num coluna] df.iloc[3,30]
# df.loc[[ind1,ind2,ind3],[col1,col2,col3]

df1 = df[df>1000].fillna('-')
print(df1)

df2 = df[(df[10]>1000) & (df[15]>1500)]
print(df2)

df3 = df[(df[10]>1000) | (df[15]>1500)]
print(df3)
