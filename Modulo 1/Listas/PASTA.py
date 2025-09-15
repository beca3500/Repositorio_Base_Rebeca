texto_pasta = ""  # variável para armazenar o nome da pasta

# Campo de entrada
texto_recebido = ft.TextField(label="Digite o nome da pasta ou arquivo...", width=300)
informativo = ft.Text("", size=16, color="white")

# Função para criar pasta
def criar_pasta(e):
    nonlocal texto_pasta
    texto_pasta = texto_recebido.value.strip()
    if texto_pasta:
        if not os.path.exists(texto_pasta):
            os.mkdir(texto_pasta)
            informativo.value = f"📁 Pasta criada: '{texto_pasta}'"
        else:
            informativo.value = f"⚠️ A pasta '{texto_pasta}' já existe."
    else:
        informativo.value = "⚠️ Digite um nome de pasta válido."
    page.update()

# Função para criar arquivo dentro da pasta
def criar_arquivo(e):
    nome_arquivo = texto_recebido.value.strip()
    if texto_pasta == "":
        informativo.value = "⚠️ Primeiro crie ou selecione uma pasta!"
    elif nome_arquivo:
        caminho_arquivo = os.path.join(texto_pasta, f"{nome_arquivo}.txt")
        try:
            with open(caminho_arquivo, "w") as f:
                f.write("")  # cria arquivo vazio
            informativo.value = f"📄 Arquivo '{nome_arquivo}.txt' criado em '{texto_pasta}'"
        except Exception as err:
            informativo.value = f"❌ Erro ao criar arquivo: {err}"
    else:
        informativo.value = "⚠️ Digite um nome de arquivo válido."
    page.update()

# Botões
botao_criar_pasta = ft.ElevatedButton("Criar Pasta", on_click=criar_pasta)
botao_criar_arquivo = ft.ElevatedButton("Criar Arquivo", on_click=criar_arquivo)

# Layout
page.add(
    texto_recebido,
    botao_criar_pasta,
    botao_criar_arquivo,
    informativo
)
ft.app(target=main)
