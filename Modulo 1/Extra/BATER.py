def bater_no_ezequiel(): print("Com o quê você quer bater no Ezequiel? 👊😳") arma = input("Digite o nome do objeto (ex: chinelo, travesseiro, carinho): ") print(f"Você escolheu bater no Ezequiel com {arma}! 😱")

def dancinha_tiktok(): print("Qual dancinha do TikTok você vai arrasar hoje? 💃✨") danca = input("Digite o nome da dança (ex: Desenrola, Dança do Quadrado): ") print(f"Uau! Quero ver você dançando {danca} agora mesmo! 😍🎶")

def cantor_favorito(): print("Me conta, qual seu cantor ou cantora favorita? 🎤🎶") cantor = input("Digite o nome do seu cantor ou cantora preferida: ") print(f"Aaaah, eu também adoro {cantor}! Que bom gosto você tem, docinho! 💕")

while True: print("\nO que você deseja fazer?") print("1 - Bater no Ezequiel") print("2 - Fazer dancinha do TikTok") print("3 - Falar seu cantor favorito") print("4 - Sair do programa 💔")

try:
    opcao = int(input("➡️ Digite o número da opção: "))

    if opcao == 1:
        bater_no_ezequiel()
    elif opcao == 2:
        dancinha_tiktok()
    elif opcao == 3:
        cantor_favorito()
    elif opcao == 4:
        print("Aaah, já vai? Vou sentir saudade! Volta logo! 😢💖")
        break
    else:
        print("Opção inválida! 😢 Escolha 1, 2, 3 ou 4.")
except ValueError:
    print("Por favor, digite um número válido. 🧠💡")
