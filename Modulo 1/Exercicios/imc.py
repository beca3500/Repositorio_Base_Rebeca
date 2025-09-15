Nome_do_paciente = input("Digite o nome do paciente: ")
peso = float(input("Digite o peso do paciente: "))
altura = float(input("Digite a altura do paciente: "))
imc = peso / (altura * altura)

if imc < 18.5:
    print(f"Abaixo do peso:")
elif 18.5 <= imc < 24.9:
    print(f"Peso normal:")
elif 25 <= imc < 29.9:
    print(f"Sobrecarga:")
elif 30 <= imc < 34.9:
    print(f"Obesidade grau I:")
elif 35 <= imc < 39.9:
    print(f"Obesidade grau II:")
else:
    print(f"Obesidade grau III:")
