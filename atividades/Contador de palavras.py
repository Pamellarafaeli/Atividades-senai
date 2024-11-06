# Contador de palavras #
texto_usuario = input("Digite um texto: ")

# Remove espaços extras e divide o texto em palavras
palavras = texto_usuario.split()

# Conta o número de palavras
numero_palavras = len(palavras)

print(f"O número de palavras no texto é: {numero_palavras}")
