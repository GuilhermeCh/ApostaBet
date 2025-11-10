class Jogador:
    def __init__(self, nome, idade, carteira):
        self.nome = nome
        self.idade = idade
        self.carteira = carteira

def cadastro(): 
    while True:
        print("Bem-vindo ao ApostaBet!\n")
        print("> 1 - Cadastro")
        print("> 2 - Sair")
        
        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            nome = input("\nQual seu nome? ")
            
            # --- Verificação da idade do jogador ---
            try:
                idade = int(input("Qual sua idade? "))
            except ValueError:
                print("Idade inválida! Digite apenas números.")
                continue
            
            if idade < 18:
                print("\nIdade menor que 18! Apenas maiores de idade são permitidos!\n")
                return None  # Encerra o cadastro

            # --- Verificação do valor depositado ---
            try:
                valor = float(input("Quanto vai depositar? R$ "))
            except ValueError:
                print("\nValor inválido! Digite apenas números.\n")
                continue

            print(f"\nCadastro realizado!\n\n-- Bem-vindo, {nome} --\nIdade: {idade}\nSaldo: R$ {valor:.2f}\n")
            return nome, idade, valor

        elif escolha == "2":
            print("Saindo...")
            return None

        else:
            print("Opção inválida! Tente novamente.\n")