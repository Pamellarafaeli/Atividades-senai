def caracteres(num):
    return len((str(num)))

num = str(input('Digite um número: ')).strip()
print ("Este número tem", caracteres(num), "caracteres")