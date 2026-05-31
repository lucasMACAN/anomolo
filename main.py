import os

local = "quarto"

while True:
    os.system("clear")

    if local == "quarto":
        print("Você acorda em um quarto desconhecido.")
        print("\n1 - Abrir a porta")
        print("2 - Olhar o espelho")

        escolha = input("> ")

        if escolha == "1":
            local = "corredor"

        elif escolha == "2":
            print("\nSeu reflexo sorri.")
            input("\nENTER para continuar.")

    elif local == "corredor":
        print("Um corredor longo e silencioso.")

        print("\n1 - Voltar ao quarto")
        print("2 - Ir para a cozinha")

        escolha = input("> ")

        if escolha == "1":
            local = "quarto"

        elif escolha == "2":
            local = "cozinha"

    elif local == "cozinha":
        print("A cozinha está vazia.")

        print("\n1 - Voltar")
        print("2 - Abrir a geladeira")

        escolha = input("> ")

        if escolha == "1":
            local = "corredor"

        elif escolha == "2":
            print("\nHá apenas um bilhete:")
            print('"Você já esteve aqui antes."')
            input("\nENTER para continuar.")