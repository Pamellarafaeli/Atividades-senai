def inicio():
    while True:
        print("\nBem-vindo ao painel de controle da nossa empresa!")
        print("---------------------------------------------------")
        print("Funcionário, por favor digite abaixo as informações!")
        
        nome = input("Digite seu nome: ")
        
        print("Qual o seu cargo: ")
        print("1) Produção")
        print("2) Administração")
        print("3) Controle de Estoque")
        
        try:
            opcao = int(input("Escolha uma opção (1/2/3): "))
        except ValueError:
            print("Opção inválida. Digite um número entre 1 e 3.")
            continue
        
        if opcao == 1:
            try:
                qnt_pecas = int(input("Digite a quantidade de peças: "))
            except ValueError:
                print("Quantidade inválida. Digite um número inteiro.")
                continue

            if qnt_pecas > 50:
                print("Você ultrapassou o limite de 50 peças. Volte as peças restantes ao armazém da empresa e assim seja dispensado.\n")
            else:
                print("-------------------------------")
                print("PAINEL DE CONTROLE DA PRODUÇÃO")
                print("-------------------------------\n")
                print("Checagem de peças concluída.")
                if qnt_pecas < 50:
                    print(f"Faltam {50 - qnt_pecas} peças para atingir a meta.\n")
                for i in range(1, qnt_pecas + 1):
                    print(f"[{i}] ", end='')
                print()

        elif opcao == 2:
            try:
                qnt_funcionarios = int(input("▪️ Digite o número de funcionários que chegaram hoje: "))
            except ValueError:
                print("Número inválido. Digite um número inteiro.")
                continue

            if qnt_funcionarios == 120:
                print("-----------------------")
                print(" PAINEL DE CONTROLE ")
                print("-----------------------")
                print(f"Quantidade de funcionários: {qnt_funcionarios}")
                print("Checagem de funcionários concluída. Todos presentes.")
            elif qnt_funcionarios > 120:
                print("-----------------------")
                print(" PAINEL DE CONTROLE ")
                print("-----------------------")
                print(f"Quantidade de funcionários: {qnt_funcionarios}")
                print("O número de funcionários ultrapassa o limite de 120.")
            else:
                print("-----------------------")
                print(" PAINEL DE CONTROLE ")
                print("-----------------------")
                print(f"Quantidade de funcionários: {qnt_funcionarios}")
                print("Faltam funcionários na empresa. Faça um relatório sobre a falta deles.")
                mensagem = input("▪️ Digite uma mensagem para o relatório de falta de funcionários: ")
                print(f"▪️ Relatório enviado. Aos funcionários faltantes ({120 - qnt_funcionarios}), será aplicada uma penalidade.\n")

        elif opcao == 3:
            try:
                qnt_pecas_semana = int(input("▪️ Quantas peças chegaram nesta semana: "))
                qnt_funcionarios_novos = int(input("▪️ Quantos funcionários novos teve nos últimos 7 dias: "))
            except ValueError:
                print("Número inválido. Digite números inteiros.")
                continue
            
            aumento_preco = input("▪️ O preço das peças aumentaram nos últimos 7 dias? (S/N): ").strip().upper()
            falta_funcionarios = input("▪️ Está ocorrendo muita falta de funcionários? (S/N): ").strip().upper()
            
            if falta_funcionarios == "S":
                print("-------------------------------")
                print("PAINEL DE CONTROLE DE ESTOQUE")
                print("-------------------------------\n")
                print("▫︎ Deverá ser avisado à DIRETORIA GERAL que está ocorrendo muita falta de funcionários.")
            
            if aumento_preco == "S":
                print("▫︎ Será necessário avisar à produção que o limite de peças será diminuído.")
            
            if aumento_preco == "S" and falta_funcionarios == "S":
                print("▫︎ Deverá ser avisado à diretoria da falta de funcionários e medidas serão tomadas.")

        else:
            print("Opção inválida. Escolha uma opção entre 1 e 3.")
        
        resposta = input("\nDeseja voltar ao início? (S/N): ").strip().upper()
        if resposta != "S":
            print("Saindo do sistema...\n")
            break

# Para rodar a função
inicio()
