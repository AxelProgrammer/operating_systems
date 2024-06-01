import tkinter as tk
import winreg


def create_registry_key():
    key_path = key_entry.get()
    value = value_entry.get()
    data = data_entry.get()

    try:
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)
        winreg.SetValueEx(key, value, 0, winreg.REG_SZ, data)
        result_label.config(text="Значение успешно создано в реестре.")
    except Exception as e:
        result_label.config(text="Ошибка при создании значения в реестре: " + str(e))


def read_registry_value():
    key_path = key_entry.get()
    value = value_entry.get()

    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path)
        data, _ = winreg.QueryValueEx(key, value)
        result_label.config(text=f"Значение: {data}")
    except Exception as e:
        result_label.config(text="Ошибка при чтении значения из реестра: " + str(e))


def delete_registry_value():
    key_path = key_entry.get()
    value = value_entry.get()

    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
        winreg.DeleteValue(key, value)
        result_label.config(text="Значение успешно удалено из реестра.")
    except Exception as e:
        result_label.config(text="Ошибка при удалении значения из реестра: " + str(e))


# Создание главного окна
root = tk.Tk()
root.title("Менеджер реестра")

# Создание виджетов
key_label = tk.Label(root, text="Путь к ключу:")
key_label.grid(row=0, column=0, padx=5, pady=5)

key_entry = tk.Entry(root)
key_entry.grid(row=0, column=1, padx=5, pady=5)

value_label = tk.Label(root, text="Имя значения:")
value_label.grid(row=1, column=0, padx=5, pady=5)

value_entry = tk.Entry(root)
value_entry.grid(row=1, column=1, padx=5, pady=5)

data_label = tk.Label(root, text="Данные:")
data_label.grid(row=2, column=0, padx=5, pady=5)

data_entry = tk.Entry(root)
data_entry.grid(row=2, column=1, padx=5, pady=5)

create_button = tk.Button(root, text="Создать значение", command=create_registry_key)
create_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="we")

read_button = tk.Button(root, text="Считать значение", command=read_registry_value)
read_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="we")

delete_button = tk.Button(root, text="Удалить значение", command=delete_registry_value)
delete_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="we")

result_label = tk.Label(root, text="")
result_label.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
