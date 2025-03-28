#Dados nao estruturado
#PSV
import pandas as pd

dados_csv = {
    "nome": ["Ana", "Luiz", "Rui", "Ian"],
    "idade": [23, 21, 25, 54],
    "cidade": ["Rio de Janeiro", "Curitiba", "Fortaleza", "Bahia"]
}
#criar dataframes - linhas e colunas
df_csv = pd.DataFrame(dados_csv)

#salvar em csv
df_csv.to_csv("Dadosnao.csv", index=False)


