class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f'Livro "{self.titulo}" emprestado com sucesso.')
        else:
            print(f'O livro "{self.titulo}" já está emprestado.')

    def devolver(self):
        self.disponivel = True
        print(f'Livro "{self.titulo}" devolvido com sucesso.')

    def exibir_informacoes(self):
        status = "Disponível" if self.disponivel else "Indisponível"
        print(f'Título: {self.titulo}, Autor: {self.autor}, Status: {status}')


class Biblioteca:
    def __init__(self):
        self.acervo = []

    def adicionar_livro(self, livro):
        self.acervo.append(livro)
        print(f'Livro "{livro.titulo}" adicionado ao acervo.')

    def buscar_livro(self, titulo):
        for livro in self.acervo:
            if livro.titulo.lower() == titulo.lower():
                return livro
        print(f'Livro "{titulo}" não encontrado.')
        return None


def main():
    biblioteca = Biblioteca()

    while True:
        print("\nMenu:")
        print("1. Adicionar livro")
        print("2. Emprestar livro")
        print("3. Devolver livro")
        print("4. Consultar livro")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            novo_livro = Livro(titulo, autor)
            biblioteca.adicionar_livro(novo_livro)

        elif opcao == '2':
            titulo = input("Título do livro a ser emprestado: ")
            livro = biblioteca.buscar_livro(titulo)
            if livro:
                livro.emprestar()

        elif opcao == '3':
            titulo = input("Título do livro a ser devolvido: ")
            livro = biblioteca.buscar_livro(titulo)
            if livro:
                livro.devolver()

        elif opcao == '4':
            titulo = input("Título do livro a ser consultado: ")
            livro = biblioteca.buscar_livro(titulo)
            if livro:
                livro.exibir_informacoes()

        elif opcao == '5':
            print("Saindo do sistema.")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
