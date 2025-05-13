import matplotlib.pyplot as plt
import pandas as pd
import numpy as pn
from openpyxl import Workbook
from openpyxl.drawing.image import Image

arquivo_excel = 'FORMULÁRIO GERAL DE RESULTADOS DAS CAMPANHAS DO LIMPA BRASIL (respostas) (5) (1).xlsx'  
dados = pd.read_excel(arquivo_excel)

x = ["Fragmentos de Plástico", "Brinquedos", "Canudos", "Copos/talheres/pratos", "Embalagens de alimento", "Escovas de dente", "Esponja/espuma", "Garrafas PET", "Hastes de cotonete/pirulito", "Isqueiros", "Pedaços de isopor (maiores que 2,5cm)", "Pinos de plástico", "Sacos e sacolas", "Tampas/lacres/argolas de garrafa", "Outros", "Chinelos/Sandálias", "Luvas", "Preservativos (Camisinha)", "Fósforos", "Pedaços de madeira", "Roupas e pedaços de tecido", "Caixas de leite/suco, etc", "Embalagens de papel", "Papelão", "Pedaços de papel/guardanapos", "Anéis de lacre de latas de bebidas", "Pedaços de metal", "Tampas de metal (ex. garrafas, potes, etc)", "Garrafas", "Pedaços de cerâmica", "Pedaços de vidro", "Potes de vidro ou cerâmica", "Bitucas/guimbas/filtros de cigarro", "Cera de vela/parafina", "Eletroeletrônicos (TV, celular, computador, etc)"]
y = ['7.300', '1', '3', '14', '65', '1', '2', '2.508', '55', '9', '2.898', '23', '2.481', '54', '324', '1', '19', '5', '2', '64', '1', '20', '2.875', '60', '7', '11', '43', '23.202', '9', '2', '1', '460', '1', '1', '1']

plt.plot(x, y, marker='o', linestyle='-', color='b', label='Linha Exemplo')


plt.title('Total de CADA TIPO DE LIXO (Em KGs) por Ano')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.legend()  
plt.grid(True)  


plt.show()
