def criar_lista(tamanho):
  lista = []
  for _ in range(tamanho):
    numero = int(input("Digite um número: "))
    lista.append(numero)
  return lista
tamanho_lista1 = int(input("Digite o tamanho da primeira lista: "))
tamanho_lista2 = int(input("Digite o tamanho da segunda lista: "))
lista1 = criar_lista(tamanho_lista1)
lista2 = criar_lista(tamanho_lista2)
elementos_em_comum = []
for elemento in lista2:
  if elemento in lista1:
    elementos_em_comum.append(elemento)
if elementos_em_comum:
  print("Os elementos em comum são:", elementos_em_comum)
else:
  print("Não há elementos em comum entre as duas listas.")
print("Lista 1:", lista1)
print("Lista 2:", lista2)