import csv

Nome do arquivo CSV
arquivo = "alunos.csv"

Dados iniciais
dados = [ {"nome": "Alice", "idade": "17", "nota": "8.5"}, {"nome": "Bruno", "idade": "18", "nota": "7.0"}, {"nome": "Carla", "idade": "17", "nota": "9.2"}, {"nome": "Diego", "idade": "19", "nota": "6.8"}, {"nome": "Elisa", "idade": "18", "nota": "8.0"}, {"nome": "Felipe", "idade": "17", "nota": "7.5"}, {"nome": "Gabriela", "idade": "18", "nota": "9.0"}, {"nome": "Henrique", "idade": "19", "nota": "5.9"}, {"nome": "Isabela", "idade": "17", "nota": "8.7"}, {"nome": "João", "idade": "18", "nota": "6.5"}, {"nome": "Larissa", "idade": "17", "nota": "9.5"}, {"nome": "Marcos", "idade": "19", "nota": "7.8"}, {"nome": "Natália", "idade": "18", "nota": "8.3"}, {"nome": "Otávio", "idade": "17", "nota": "6.9"}, {"nome": "Patrícia", "idade": "18", "nota": "7.7"}, {"nome": "Rafael", "idade": "19", "nota": "8.9"}, {"nome": "Sofia", "idade": "17", "nota": "9.1"}, {"nome": "Tiago", "idade": "18", "nota": "6.2"}, {"nome": "Vitória", "idade": "19", "nota": "8.4"} ]

Salvar os dados iniciais no CSV
with open(arquivo, mode="w", newline="", encoding="utf-8") as f: escritor = csv.DictWriter(f, fieldnames=["nome", "idade", "nota"]) escritor.writeheader() escritor.writerows(dados)

=== Lendo os dados do CSV ===
with open(arquivo, mode="r", encoding="utf-8") as f: leitor = csv.DictReader(f) alunos = list(leitor)

1. Mostrar apenas os nomes dos alunos
print("=== Nomes dos alunos ===") for i, aluno in enumerate(alunos, start=1): print(f"{i}. {aluno['nome']}")

print("\n---\n")

2. Nome de todos os alunos com nota >= 7
print("=== Alunos com nota >= 7 ===") aprovados = [aluno for aluno in alunos if float(aluno["nota"]) >= 7] for i, aluno in enumerate(aprovados, start=1): print(f"{i}. {aluno['nome']} (nota: {aluno['nota']})")

print("\n---\n")

3. Média da turma
notas = [float(aluno["nota"]) for aluno in alunos] media = sum(notas) / len(notas) print(f"=== Média da turma ===\n{media:.2f}")

print("\n---\n")

4. Adicionar um novo aluno no final do CSV
novo_aluno = {"nome": "Elisa", "idade": "18", "nota": "8.0"} with open(arquivo, mode="a", newline="", encoding="utf-8") as f: escritor = csv.DictWriter(f, fieldnames=["nome", "idade", "nota"]) escritor.writerow(novo_aluno)

print("✅ Aluno Elisa adicionado com sucesso ao CSV!")
