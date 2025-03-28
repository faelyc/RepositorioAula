#Dados estruturados
#Excel
import pandas as pd

#Estrutura de dicionário
dados_planilha1 = {
    "nome": ["Ana", "Luiz", "Rui", "Ian"],
    "idade": [23, 21, 25, 54],
    "cidade": ["Rio de Janeiro", "Curitiba", "Fortaleza", "Bahia"]
}
#cria dataframe
df_planilha1 = pd.DataFrame(dados_planilha1)


#salvar no excel
with pd.ExcelWriter("DadosEstruturados.xlsx") as writer:
    df_planilha1.to_excel(writer, sheet_name="planilha1", index=False)

