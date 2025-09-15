opcao=0

while opcao==0: nome=(input("Digite seu nome: ")) numero = int(input("Digite um número: ")) opcao = input("Digite 's' para repetir a ação ou qualquer outra tecla para sair: ") if numero % 2 == 0: print(f"{nome}, {numero} é par") elif numero % 2 == 1: print(f"{nome}, {numero} é ímpar") elif opcao == 's': continue else: break print(f"Obrigado por usar o programa, {nome}!")
