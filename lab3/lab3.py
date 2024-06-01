import os.path
import shutil
from tkinter import *
from tkinter import messagebox

def get_path():
    global way
    way = path_entry.get()
    update_file_list()

def files(data):
    result = "Файлы находящиеся по заданному пути:\n"
    for elem in data:
        result += elem + "\n"
    return result

def remove_file():
    removed_file = removed_file_entry.get()
    if removed_file in datas:
        os.remove(way + "\\" + removed_file)
        messagebox.showinfo("Успех", "Файл успешно удален!")
    else:
        messagebox.showerror("Ошибка", "Такого файла нет в директории.")
    update_file_list()

def copy_file():
    copy_file = copy_file_entry.get()
    fin_way = fin_way_entry.get()
    if copy_file in datas:
        shutil.copy(way + "\\" + copy_file, fin_way)
        messagebox.showinfo("Успех", "Файл успешно скопирован в указанное место!")
    else:
        messagebox.showerror("Ошибка", "Такого файла не найдено или неверно указан конечный путь!")
    update_file_list()

def rename_file():
    rename_file = rename_file_entry.get()
    new_name = new_name_entry.get()
    if rename_file in datas:
        os.rename(way + "\\" + rename_file, way + "\\" + new_name)
        messagebox.showinfo("Успех", "Файл успешно переименован!")
    else:
        messagebox.showerror("Ошибка", "Такого файла не существует!")
    update_file_list()

def update_file_list():
    global datas
    datas = os.listdir(way)
    file_list_label["text"] = files(datas)

way = ""
datas = []

root = Tk()
root.title("Файловый менеджер")

path_label = Label(root, text="Введите путь до папки:")
path_label.pack()

path_entry = Entry(root)
path_entry.pack()

get_path_button = Button(root, text="Получить путь", command=get_path)
get_path_button.pack()

file_list_label = Label(root, text="")
file_list_label.pack()

removed_file_label = Label(root, text="Введите имя файла, который нужно удалить:")
removed_file_label.pack()

removed_file_entry = Entry(root)
removed_file_entry.pack()

remove_file_button = Button(root, text="Удалить файл", command=remove_file)
remove_file_button.pack()

copy_file_label = Label(root, text="Введите имя файла, который нужно скопировать:")
copy_file_label.pack()

copy_file_entry = Entry(root)
copy_file_entry.pack()

fin_way_label = Label(root, text="Введите путь, куда нужно скопировать файл:")
fin_way_label.pack()

fin_way_entry = Entry(root)
fin_way_entry.pack()

copy_file_button = Button(root, text="Скопировать файл", command=copy_file)
copy_file_button.pack()

rename_file_label = Label(root, text="Введите имя файла, который нужно переименовать:")
rename_file_label.pack()

rename_file_entry = Entry(root)
rename_file_entry.pack()

new_name_label = Label(root, text="Введите новое имя файла:")
new_name_label.pack()

new_name_entry = Entry(root)
new_name_entry.pack()

rename_file_button = Button(root, text="Переименовать файл", command=rename_file)
rename_file_button.pack()

root.mainloop()