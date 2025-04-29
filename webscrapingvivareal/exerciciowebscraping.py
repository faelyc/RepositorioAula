import pandas as pd
import numpy as np

pd.read_excel("/content/casas.xlsx")

!pip install selenium
!apgt-get update
!apt install chromium-chromedriver

from selenium import webdriver

chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

wd_chrome = webdriver.Chrome(chrome_options)

wd_chrome.get('https://www.vivareal.com.br/venda/?transacao=venda&pagina=1')

from google.colab import drive

df = pd.read_excel("/content/casas.xlsx")

df_remove = df.dropna(subset=['quartos'])

print(df_remove)

df_remove = df.dropna(subset=['banheiros'])

print(df_remove)

df_remove = df.dropna(subset=['nomeRua'])

print(df_remove)

display(df.info())

df['metragem'] = df['metragem'].str.extract('(\d+)', expand=False)
print(df)

df['metragem'] = df['metragem'].astype(float)

print(df)
print(df.dtypes)

df['metragem'].mean()
print(df)

media_metragem = df['metragem'].mean()
print(f"A média da metragem é: {media_metragem}")

df['quartos'] = df['quartos'].str.extract('(\d+)', expand=False)
print(df)

df_sem_nan = df.dropna(subset=['quartos'])
print(df_sem_nan)

df['quartos'] = df['quartos'].astype(float)

print(df)
print(df.dtypes)
df_sem_nan = df.dropna(subset=['quartos'])
print(df_sem_nan)

media_quartos = df['quartos'].mean()
print(f"A média dos quartos é: {media_quartos}")

df['banheiros'] = df['banheiros'].str.extract('(\d+)', expand=False)
print(df)

df_sem_nan = df.dropna(subset=['banheiros'])
print(df_sem_nan)

df['banheiros'] = df['banheiros'].astype(float)

print(df)
print(df.dtypes)
df_sem_nan = df.dropna(subset=['banheiros'])
print(df_sem_nan)

media_banheiros = df['banheiros'].mean()
print(f"A média dos banheiros é: {media_banheiros}")

df['vagas'] = df['vagas'].str.extract('(\d+)', expand=False)
print(df)

df['vagas'] = df['vagas'].astype(float)

print(df)
print(df.dtypes)
df_sem_nan = df.dropna(subset=['vagas'])
print(df_sem_nan)

media_vagas = df['vagas'].mean()
print(f"A média dos vagas é: {media_vagas}")