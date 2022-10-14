#Modelagem de dados
import pandas as pd
import numpy as np

#Gráficas
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

#avisos
import warnings
warnings.filterwarnings('ignore')

#pré-configurações
pd.set_option('display.max_rows', 200)
pd.set_option('display.max_columns', 100)
plt.rcParams['figure.figsize'] = (12,6)
plt.style.use('seaborn-darkgrid')

#Libs
import re #regex
import nltk #NLP
from dateutil.parser import parse 



#Funcoes utilizadas
def ajustaData(Data):
    dataAux = Data
    dataTransformada = parse(dataAux).date()
    return dataTransformada





#Lendo base de dados
df = pd.read_csv('C:\\xampp\\htdocs\\sentiment_analyse\\tweets.csv')

# analisando a qualidade dos dados
#print(df.shape)
#print(df.head(5))
#print(df.isnull())
#print(df.isnull().sum())
#nulos = df.isnull()

#criando graficos com dados nulos para analise
#plt.title('Total de campos nulos',loc='right')
#sns.heatmap(nulos,cbar=False)
#plt.show()

remover_colunas = df.columns[10:]
#print('\n\n Colunas removidas: \n\n',remover_colunas)
df.drop(columns=remover_colunas, inplace=True)

#verifica a quantidade de campos com dados únicos
#print(df.nunique())

#remover uma coluna unica com drop
#print(df.columns)
df.drop(columns='Unnamed: 0', inplace=True)
#print(df.columns)
#print(df.shape)

#ajustando a coluna de datas
#print(df['Created At'].head(1))
#teste = df['Created At'][0]
#print(parse(teste).date())

#aplicando a funcao que ajusta o formato da data
#result = ajustaData(df['Created At'][3])
#print(result)

#tansformando os dados da coluna Created At para o formato correto
#print(df['Created At'].head(6).apply(ajustaData))
df['Created At'] = df['Created At'].apply(ajustaData)
#print(df['Created At'].head(5))

#Utilizando o pandas para separa o ANO, MÊS e DIA da data
df['Created At'] =  pd.to_datetime(df['Created At'])
df['Ano'] = df['Created At'].dt.year
df['Mes'] = df['Created At'].dt.month
df['Dia'] = df['Created At'].dt.day

print(df.iloc[0:3,5:])










