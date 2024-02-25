from time import sleep

# Dicionário para armazenar as informações da ficha
ficha = {}

# Loop infinito para manter o menu em execução até que o usuário escolha sair
while True:
    try:
        # Exibe o menu
        print("\nFICHA CADASTRAL")
        print("1 - Incluir informações na ficha")
        print("2 - Obter informação da ficha")
        print("3 - Exibir a ficha completa")
        print("4 - Sair")
        op = int(input("Informe a opção desejada: "))

        if op == 1:
            # Incluir na ficha
            campo = str(input("Informe o campo que deseja cadastrar na ficha: "))
            valor = str(input(f"Informe o dado que deseja cadastrar a {campo}: "))

            if campo in ficha:
                # Verifica se o campo já existe na ficha e pergunta se deseja atualizá-lo
                atualizar = input("Campo já existente, deseja atualizá-lo? Sim/Não: ").title()
                if atualizar == "Sim":
                    # Atualiza o valor do campo
                    ficha[campo] = valor
                    print("Atualizando....")
                    sleep(1)
                    print("Campos atualizados")
                else:
                    # Mantém o valor atual do campo
                    print(f"Ok, o campo {campo} continua com o valor {ficha[campo]}!")
            else:
                # Adiciona o novo campo na ficha
                ficha[campo] = valor 
                print("Cadastrando....")
                sleep(1)
                print(f"Campo {campo} cadastrado!")
            
        elif op == 2:
            # Obter dados na ficha
            if len(ficha) == 0:
                print("Sem dados na ficha!")
            else:
                # Exibe os campos disponíveis na ficha
                for campos in ficha:
                    print(campos)
                chave = str(input("Informe qual campo deseja exibir: "))
                print("Procurando....")
                sleep(1)
                if chave in ficha:
                    # Exibe o valor do campo desejado
                    print(ficha[chave])
                else:
                    print("Campo não encontrado!")
        
        elif op == 3:
            # Exibir a ficha completa
            if len(ficha) == 0:
                print("Sem campos adicionados na ficha")
            else:
                for i, campo in enumerate(ficha):
                    print(f"{i+1}. {campo} -> {ficha[campo]}")
                    input("Aperte ENTER para continuar")
            
        elif op == 4:
            # Encerra o programa
            print("Saindo do sistema de ficha cadastral....")
            sleep(1)
            print("Finalizado!")
            break

        else: 
            print("Por favor, insira uma opção válida")
    except ValueError:
        # Trata erros de entrada inválida
        print("Inserção de dados inválida, digite de acordo com o informado!")
