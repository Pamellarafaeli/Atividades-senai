#Faça uma função que computa a potência ab para valores a e b (suponha números inteiros) passados por parâmetro (não use o operador **).
def potencia(base, expoente):
  resultado = 1
  for _ in range(expoente):
    resultado *= base
  return resultado
base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))
resultado = potencia(base, expoente)
print("O resultado de", base, "elevado á", expoente, "é", resultado)