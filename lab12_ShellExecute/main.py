import tkinter as tk
from tkinter import filedialog
import ctypes
from ctypes.wintypes import HWND, HINSTANCE, LPCWSTR, UINT

# Загрузка библиотеки shell32.dll
shell32 = ctypes.windll.shell32

# Определение функции ShellExecute
ShellExecute = shell32.ShellExecuteW
ShellExecute.argtypes = [HWND, LPCWSTR, LPCWSTR, LPCWSTR, LPCWSTR, UINT]
ShellExecute.restype = HINSTANCE

# Функция для открытия файла с использованием окна выбора
def open_file_dialog():
    root = tk.Tk()
    root.withdraw() 

    file_path = filedialog.askopenfilename()
    if file_path:
        file_path_str = str(file_path)
        # Вызов ShellExecute для открытия выбранного файла
        ShellExecute(None, "open", file_path_str, None, None, 5)

open_file_dialog()
