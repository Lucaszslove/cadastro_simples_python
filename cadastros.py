# Cadastro de pessoas simples em python
import os

cadastros = []
while True:
    print("----- Sistema de Cadastros de Pessoas -----")
    print()
    print("Escolha uma das opções:")
    print("[1] Efutuar Cadastro\n[2] Verificar cadastros\n[3] Sair\n")

    try:
        escolha_de_opcao = int(input("Digite uma opção: "))
        if escolha_de_opcao == 1:
            os.system("cls")
            print("---- Cadastro PF ----")
            print()
            nome = input("Digite seu nome: ")
            if nome == "":
                print("Digite um nome por favor")
                continue
            try:
                idade = int(input("Digite sua idade: "))
                if idade >=18:
                    pf = {
                        "nome": nome,
                        "idade": idade
                    }
        
                    cadastros.append(pf)
                    print("Cadastro Efetuado com Sucesso!")
                else:
                    print("Idade não permitida.")
            except:
                print("Digite uma idade, por favor")
        elif escolha_de_opcao == 2:
            os.system("cls")
            if len(cadastros) == 0:
                print("Nenhum cadastro encontrado")
            else:
                print("\nCadastros:")
                for pf in cadastros:
                    print(f'Nome: {pf["nome"]}\nIdade: {pf["idade"]}')
                    print("-------------------")
                print()
        elif escolha_de_opcao == 3:
            print("Você saiu")
            break
        else:
            print("Escolha uma das opções: [1], [2] ou [3]")
    except:
        print("Digite apenas uma opção em número inteiro")