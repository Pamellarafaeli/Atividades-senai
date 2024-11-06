class Animal:
    def __init__(self, nome, idade, especie):
        self._nome = nome
        self._idade = idade
        self._especie = especie

    def calcular_preco_servico(self):
        pass

class Cachorro(Animal):
    def calcular_preco_servico(self):
        return 50

class Gato(Animal):
    def calcular_preco_servico(self):
        return 40

class Passaro(Animal):
    def calcular_preco_servico(self):
        return 30

def menu():
    animais = []
    while True: 
        print("\nMenu:")
        print("1. Cadastrar animal")
        print("2. Consultar animal")
        print("3. Calcular preço de serviço")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            tipo_animal = input("Tipo de animal (cachorro/gato/passaro): ").strip().lower()
            nome = input("Nome do animal: ")
            idade = input("Idade do animal: ")

            if tipo_animal == 'cachorro':
                animal = Cachorro(nome, idade, tipo_animal)
            elif tipo_animal == 'gato':
                animal = Gato(nome, idade, tipo_animal)
            elif tipo_animal == 'passaro':
                animal = Passaro(nome, idade, tipo_animal)
            else:
                print("Animal inválido.")
                continue
            
            animais.append(animal)
            print("Animal cadastrado com sucesso!")

        elif opcao == '2':
            if not animais:
                print("Nenhum animal cadastrado.")
                continue
            
            for i, animal in enumerate(animais):
                print(f"{i + 1}. {animal._nome}, Idade: {animal._idade}, Espécie: {animal._especie}")

        elif opcao == '3':
            if not animais:
                print("Nenhum animal cadastrado.")
                continue

            indice = int(input("Digite o número do animal para calcular o preço do serviço: ")) - 1
            if 0 <= indice < len(animais):
                preco = animais[indice].calcular_preco_servico()
                print(f"O preço do serviço para '{animais[indice]._nome}' é R${preco:.2f}")
            else:
                print("Índice inválido.")

        elif opcao == '4':
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
