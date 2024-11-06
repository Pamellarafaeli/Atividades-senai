# Média de notas #
notas = []
n = int(input( ))
for i in range (n):
    dado = float (input())
    notas.append(dado)
print (notas)

# Calcula a média #
soma = 0
for i in range (len(notas)):
    soma = soma + notas[i]
media = soma/n
print (format(media, ".1f"))