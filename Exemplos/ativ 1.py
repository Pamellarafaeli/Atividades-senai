def inverte(num):
    sequência = 0
    while num > 0:
        digito_invertido = num % 10
        num //= 10
        sequência = sequência * 10 + digito_invertido
    return sequência

num = int(input("Digite um número: "))
resultado = inverte(num)
print("O número invertido é:", resultado)