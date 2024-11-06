from ast import AugStore


class livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.disponivel = True
        self.autor = autor
    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print ("O livro ", self.titulo, "foi entregue com sucesso!")
        else:
            print ("O livro já foi emprestado.")
    def devolver (self):
        self.disponivel = True 
        print ("O livro ",self.titulo, "foi devolvido com sucesso!")
    def exibir_informacoes (self):
        Livro = "Disponível" if self.disponivel else "Indisponível"
        print ("Livro:", self.titulo, "Autor:", self.autor, "Está:", Livro)

class Biblioteca:
    def __init__(self):
        self.biblioteca = []
    def adicionar (self, livro):
        self.biblioteca.append(livro)
        print ("Livro ", self.titulo, "adicionado na biblioteca com sucesso!")
    def buscar (self, titulo):
        for livro in self.biblioteca:
            if livro.titulo == titulo:
                return livro 
            else:
                print ("Livro não encontrado.")
                return None

def main():
  mano = Biblioteca()
  
  while True():
      print ("⊹ ࣪ ˖₊˚⊹⋆")
      print ("\nMenu: ")
      print ("1) Adicionar Livros")
      print ("2) Emprestar")
      print ("3) Devolver")
      print ("4) Consultar")
      opcao = input ("Digite a opção que você deseja!: ")
      if opcao == '1':
          titulo = input("Adicione o título do livro!: ")
          autor = input("Adicione o nome do autor!: ")
          novo = livro(titulo,autor)
          mano.adicionar_livro(novo)
      elif opcao == '2':
          titulo = input("Nome do livro que deseja?: ")
          livro = mano.buscar_livro(titulo)
          if livro:
            livro.emprestar()
      elif opcao == '3':
          titulo = input ("Qual livro deseja devolver?: ")
          livro = mano.buscar_livro(titulo)
          if livro:
            livro.devolver()
      elif opcao == '4':
          titulo = input ("Qual livro deseja consultar?: ")
          livro = mano.buscar_livro(titulo)
          if livro:
            livro.exibir_informacoes()
      else:
          print ("Opção inválida.")