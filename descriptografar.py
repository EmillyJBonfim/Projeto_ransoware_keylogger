import os
from cryptography.fernet import Fernet

def carregar_chave():
    return open("chave.key", "rb").read()

def descriptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados_criptografados = file.read()
    
    dados_descriptografados = f.decrypt(dados_criptografados)
    
    with open(arquivo, "wb") as file:
        file.write(dados_descriptografados)

def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if not nome.endswith(".key") and nome != "ransomware_sim.py":
                lista.append(caminho)
    return lista

def main():
    try:
        chave = carregar_chave()
        arquivos = encontrar_arquivos("test_files")
        
        for arquivo in arquivos:
            descriptografar_arquivo(arquivo, chave)
        
        print(" Arquivos restaurados com sucesso!")
    except Exception as e:
        print(f" Erro na restauração: {e}")

if __name__ == "__main__":
    main()
