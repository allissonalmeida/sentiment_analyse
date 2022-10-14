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