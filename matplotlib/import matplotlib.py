import matplotlib.pyplot as plt
import pandas as pd
import numpy as pn

arquivo_excel = 'FORMULÁRIO GERAL DE RESULTADOS DAS CAMPANHAS DO LIMPA BRASIL (respostas) (5) (1).xlsx'  
dados = pd.read_excel(arquivo_excel)

x = ["Serviço de limpeza urbana", "Cooperativa de catadores", "Total"]
y = ['3.905', '93.195', '97.100']

plt.plot(x, y, marker='o', linestyle='-', color='b', label='Linha Exemplo')


plt.title('Gráfico de total de kgs de lixo coletado do Limpa Brasil')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.legend()  
plt.grid(True)  


plt.show()
