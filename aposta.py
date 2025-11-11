import random
from times import escolhe_time, define_resultado

def aposta(valor):
    escolha_menu = 1
    while escolha_menu == 1:
        # --- Menu do ApostaBet ---
        print("|| Menu do ApostaBet ||\n")
        print("1 - Apostar")
        print("2 - Sair")

        try:
            escolha_menu = int(input("\nEscolha uma opção: "))
        except ValueError:
            print("Entrada inválida! Digite 1 ou 2.")
            continue

        if escolha_menu == 2:
            print(f"\nSaindo... \nSaldo final: R${valor:.2f}")
            break

        # --- Escolha dos times e dos resultado ---
        time1, time2 = escolhe_time()
        placar1, placar2 = define_resultado()
        bet1 = round(random.uniform(0.1, 3.0), 2)
        bet2 = round(random.uniform(0.1, 3.0), 2)
        
        print("\n## Jogo para apostar ##\n")
        print(f">>    Time 1   [ODD]  |< >|    Time 2   [ODD] <<")
        print(f"1 - {time1} [{bet1}] |< >| 2 - {time2} [{bet2}]")
        print(f"Seu saldo atual: R$ {valor:.2f}\n")

        # --- Menu de aposta ---
        try:
            escolha = int(input("Qual time vai apostar? (1 ou 2): "))
            if escolha not in [1, 2]:
                print("Opção inválida! Escolha 1 ou 2.")
                continue
            valor_apostado = float(input("Quanto vai apostar? R$ "))
        except ValueError:
            print("Entrada inválida! Tente novamente.")
            continue

        if valor_apostado > valor:
            print("Saldo insuficiente!")
            continue

        # --- Resultado do jogo ---
        print(f"\n- Resultado do jogo: -")
        print(f"> {time1} [{placar1}] x [{placar2}] {time2} <\n")

        # --- Vitória do time 1 ---
        if escolha == 1 and placar1 > placar2:
            lucro = valor_apostado * bet1
            valor += lucro
            print(f"{time1} ganhou!\n+ R$ {lucro:.2f}\nSaldo: R$ {valor:.2f}\n")

        # --- Vitória do time 2 ---
        elif escolha == 2 and placar2 > placar1:
            lucro = valor_apostado * bet2
            valor += lucro
            print(f"{time2} ganhou!\n+ R$ {lucro:.2f}\nSaldo: R$ {valor:.2f}\n")

        # --- Derrota time 1 ---
        elif escolha == 1 and placar2 > placar1:
            valor -= valor_apostado
            print(f"{time1} perdeu!\n- R$ {valor_apostado:.2f}\nSaldo: R$ {valor:.2f}\n")

        # --- Derrota time 2 ---
        elif escolha == 2 and placar1 > placar2:
            valor -= valor_apostado
            print(f"{time2} perdeu!\n- R$ {valor_apostado:.2f}\nSaldo: R$ {valor:.2f}\n")

        # --- Empate ---
        else:
            print("Empate! Ninguém ganhou nem perdeu.\n")

        # --- Verifica se o saldo acabou ---
        if valor <= 0:
            print("Você ficou sem saldo! Fim das apostas.")
            break


    return valor
