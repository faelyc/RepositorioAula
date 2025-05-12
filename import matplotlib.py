import matplotlib.pyplot as plt
import pandas as pd
import numpy as pn

arquivo_excel = '2013_coleta_tipos_residuos.xlsx'  
dados = pd.read_excel(arquivo_excel)

x = ["Jan", "Fev", "Mar", "Abr", "Jun"]
y = ['10,87', '15,92', '31,89', '8,64', '9,34']

plt.plot(x, y, marker='o', linestyle='-', color='b', label='Linha Exemplo')


plt.title('Gráfico de 2013 do Entulho Apreendido com Matplotlib')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.legend()  
plt.grid(True)  


plt.show()
