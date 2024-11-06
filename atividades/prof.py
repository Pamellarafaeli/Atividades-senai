texto = input ('Digite um texto: ')
pontuacao = [".", ",", ":", ";", "!", "?"]

for p in pontuacao:
    texto = texto.replace(p, " ")

numero_palavras = len (texto.split())
print ("Números de palavras: ", numero_palavras)