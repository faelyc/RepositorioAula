#Estruturado
import pandas as pd
df_excel = pd.read_excel("DadosEstruturados.xlsx", sheet_name=["planilha1"])
#df_aba1 = df_excel["planilha1"]
#df_aba2 = df_excel["planilha2"]
print(df_excel)