import pandas as pd

data = pd.read_csv(r'https://raw.githubusercontent.com/alura-cursos/alura_classificacao_multilabel/master/dataset/stackoverflow_perguntas.csv')
data.to_csv('dados.csv', index = False)