import os

1️⃣ Criar pasta "Projetos"
pasta = "Projetos"
if not os.path.exists(pasta):
os.mkdir(pasta)
print(f"📁 Pasta '{pasta}' criada com sucesso!")
else:
print(f"📁 Pasta '{pasta}' já existe.")

2️⃣ Conteúdos dos arquivos com exercícios
arquivos_exercicios = {
"matematica.txt": [
"1. Resolva: 5 + 7 = ?",
"2. Resolva: 12 * 3 = ?",
"3. Resolva: 20 / 4 = ?"
],
"portugues.txt": [
"1. Escreva uma frase com sujeito e predicado.",
"2. Identifique o verbo nesta frase: 'O cachorro correu no parque.'",
"3. Substitua o substantivo 'cachorro' por um sinônimo."
],
"ciencias.txt": [
"1. Qual é o planeta mais próximo do Sol?",
"2. O que é fotossíntese?",
"3. Cite três estados físicos da água."
],
"historia.txt": [
"1. Quem foi Napoleão Bonaparte?",
"2. Em que ano ocorreu a Revolução Francesa?",
"3. Cite três grandes civilizações antigas."
]
}

3️⃣ Criar arquivos de Matemática, Português e Ciências
for arquivo in ["matematica.txt", "portugues.txt", "ciencias.txt"]:
caminho = os.path.join(pasta, arquivo)
if not os.path.exists(caminho):
with open(caminho, "w") as f:
f.write("\n".join(arquivos_exercicios[arquivo]))
print(f"📄 Arquivo '{arquivo}' criado com exercícios!")
else:
print(f"📄 Arquivo '{arquivo}' já existe!")

4️⃣ Listar arquivos atuais na pasta
print("\n🗂️ Arquivos atualmente na pasta:")
arquivos_atual = os.listdir(pasta)
for arq in arquivos_atual:
print(f"- {arq}")

5️⃣ Renomear ciencias.txt para historia.txt com exercícios de História
antigo = os.path.join(pasta, "ciencias.txt")
novo = os.path.join(pasta, "historia.txt")
if os.path.exists(antigo):
os.rename(antigo, novo)
with open(novo, "w") as f:
f.write("\n".join(arquivos_exercicios["historia.txt"]))
print("\n✏️ 'ciencias.txt' renomeado para 'historia.txt' com exercícios de História")
else:
print("\n⚠️ 'ciencias.txt' não existe para renomear.")

6️⃣ Remover portugues.txt
remover = os.path.join(pasta, "portugues.txt")
if os.path.exists(remover):
os.remove(remover)
print("🗑️ 'portugues.txt' removido com sucesso!")
else:
print("⚠️ 'portugues.txt' não encontrado para remover.")

7️⃣ Listar arquivos finais na pasta
print("\n🗂️ Arquivos finais na pasta:")
arquivos_finais = os.listdir(pasta)
for arq in arquivos_finais:
print(f"- {arq}")
