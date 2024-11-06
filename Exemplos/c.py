def reverso():
    """Solicita um número inteiro do usuário e retorna seu reverso."""
    
    # Solicita ao usuário que digite um número
    numero = int(input("Digite um número inteiro: "))
    
    # Inicializa a variável para o número invertido
    numero_invertido = 0

    # Enquanto o número não for zero
    while numero > 0:
        # Obtém o último dígito do número
        digito = numero % 10
        # Adiciona o dígito ao número invertido
        numero_invertido = numero_invertido * 10 + digito
        # Remove o último dígito do número
        numero //= 10

    return numero_invertido

# Chama a função e imprime o resultado
resultado = reverso()
print("O reverso do número é:", resultado)
