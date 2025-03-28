#Dados semiestruturado
#Json
import pandas as pd

dados_json = {
    "nome": ["Ana", "Luiz", "Rui", "Ian"],
    "idade": [23, 21, 25, 54],
    "cidade": ["Rio de Janeiro", "Curitiba", "Fortaleza", "Bahia"]
}
#Criar dataframec- linhas e colunas
df_json = pd.DataFrame(dados_json)


#Salvar em json
df_json.to_json("DadosSemi.json", orient="records", lines=False)

