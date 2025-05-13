import matplotlib.pyplot as plt
import pandas as pd
import numpy as pn
from openpyxl import Workbook
from openpyxl.drawing.image import Image

arquivo_excel = 'FORMULÁRIO GERAL DE RESULTADOS DAS CAMPANHAS DO LIMPA BRASIL (respostas) (5) (1).xlsx'  
dados = pd.read_excel(arquivo_excel)



labels = ["Serviço de limpeza urbana", "Cooperativa de catadores", "Total"]
valores = ['3.905', '93.195', '97.100']


plt.pie(valores, labels=labels, autopct='%1.1f%%', startangle=90, colors=['red', 'yellow', 'pink', 'purple'])
plt.title('Quantidade de (KGs de lixo coletados) por Limpa Brasil')
plt.axis('equal')  
plt.show()








