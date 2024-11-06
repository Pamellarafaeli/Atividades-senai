
entrada = input("Digite uma palavra ou frase: ")


entrada_limpa = entrada.replace(" ", "").lower()

# Verifica se a entrada é igual à sua reversa
if entrada_limpa == entrada_limpa[::-1]:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
