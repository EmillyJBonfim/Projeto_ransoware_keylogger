import ctypes
import os

def ocultar_janela():
    # Verifica se o sistema é Windows e oculta o console
    if os.name == 'nt':
        kernel32 = ctypes.WinDLL('kernel32')
        user32 = ctypes.WinDLL('user32')
        hWnd = kernel32.GetConsoleWindow()
        if hWnd != 0:
            user32.ShowWindow(hWnd, 0) # 0 = SW_HIDE
