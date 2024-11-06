# Faça um programa, com uma função que leia um número.
# A função retorna ‘P’, se seu número for positivo, ‘N’, se seu
# número for negativo, e ‘Z’ se seu número for zero

def PNZ (numero):
    if (numero > 0):
     return 'P'
    elif (numero < 0):
        return 'N'
    else:
        return 'Z'
numero = int(input("Digite um número: "))
resultado = PNZ(numero)
print ("O resultado é", resultado)