# Осуществить перемещение файла. Начальную и конечную папку выбрать,
# не используя клавиатуру.

from tkinter import filedialog
import shutil

def move_file():
    print('Выберите начальную папку')
    initial_dir = filedialog.askdirectory(title="Выберите начальную папку")
    if (initial_dir == ''):
        print('Начальная папка не выбрана')
        return 0
    print('Выберите конечную папку')
    final_dir = filedialog.askdirectory(title="Выберите конечную папку")
    if initial_dir and final_dir:
        file_path = filedialog.askopenfilename(initialdir=initial_dir, title="Выберите файл для перемещения")

        if file_path:
            shutil.move(file_path, final_dir)
            print("Файл успешно перемещен.")
            final = filedialog.askopenfilename(initialdir=final_dir, title="Содержимое конечной папки")

move_file();