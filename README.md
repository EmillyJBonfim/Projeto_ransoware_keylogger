# Projeto_ransoware_keylogger
Projeto educativo como fazer um ransoware e keylogger 
markdown

# 🛡️ Malware Simulation Lab: Ransomware & Keylogger

**Foco:** Cibersegurança, Infraestrutura de TI e Resposta a Incidentes.

---

## Sobre o Projeto
Este projeto demonstra na prática como ameaças digitais operam no sistema operacional, desde a captura de entradas do usuário até a manipulação direta de arquivos via criptografia. O objetivo é entender o ataque para construir defesas mais robustas.

### Ambiente de Teste
* **OS:** Kali Linux / Windows (Virtualizado)
* **Rede:** Isolada (Host-Only)
* **Linguagem:** Python 3.x
* **Bibliotecas:** `cryptography` (Fernet), `pynput`

---

## Estrutura Técnica

### 1. Ransomware (Criptografia Simétrica)
O script utiliza a classe **Fernet** da biblioteca `cryptography`. 
- **O Ataque:** Gera uma chave única de 128 bits, lê o arquivo alvo em modo binário, aplica a criptografia e sobrescreve o arquivo original.
- **A Recuperação:** O script `decryptor.py` realiza o processo inverso, exigindo a posse do arquivo `chave.key`.

### 2. Keylogger (Monitoramento de Eventos)
Utiliza a biblioteca `pynput` para "escutar" as interrupções do teclado.
- **Funcionamento:** O malware registra cada pressionamento de tecla e armazena em um arquivo de log local (`keylog.txt`).
- **Ponto de Atenção:** Em cenários reais, esses logs seriam exfiltrados via SMTP ou FTP.

---

## Como Executar (Laboratório)

1. **Instale as dependências:**
   bash
   pip install cryptography pynput
   
2. **Execute o Keylogger:**
   bash
   python keylogger_sim.py
   
3. **Simule o Ransomware:**
   - Crie um arquivo `alvo.txt`.
   - Rode `python ransomware.py`.
   - Tente abrir o arquivo e veja o conteúdo cifrado.
4. **Restaure os dados:**
   - Rode `python decryptor.py`.

---
