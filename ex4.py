#Crie uma funcao que receba duas listas de numeros inteiros e retorne um conjunto com os numeros que aparecem em ambas as listas.
def uniao_listas(lista1, lista2):
  uniao = []

  for elemento in lista1:
    if elemento in lista2 and elemento in uniao:
     uniao.append(elemento)
  return set (lista1) | set (lista2)
lista1 = [43,45,56,9,4,5]
lista2 = [43,45,56,87,1,2,9,4,5]
print(set(interseccao_listas(lista1, lista2)))
      