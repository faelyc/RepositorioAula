#Crie una funcao que receba duas listas de numeros inteiros e retorne uma nova lista contendo os elementos que aparecem em ambas as listas (interseccao).
def interseccao_listas(lista1, lista2):
  interseccao = []

  for elemento in lista1:
    if elemento in lista2:
     interseccao.append(elemento)
  return interseccao
l1 = [12,43,67,32]
l2 = [43,45,56,87,1,2,9,4,5]
interseccao_listas(l1, l2) 