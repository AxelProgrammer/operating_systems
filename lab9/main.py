
import tkinter as tk
import pygetwindow as gw

def get_windows():
    # Получаем список всех окон
    windows = gw.getAllTitles()
    return windows

def close_selected_window():
    # Получаем выбранное окно из списка
    selected_window = window_listbox.get(tk.ACTIVE)
    # Закрываем выбранное окно
    for window in gw.getAllWindows():
        if window.title == selected_window:
            window.close()
            break
    # Удаляем закрытое окно из списка
    update_window_list()

def update_window_list():
    # Получаем список всех окон
    windows = get_windows()
    # Очищаем список окон в приложении
    window_listbox.delete(0, tk.END)
    # Заполняем список обновленными данными
    for window in windows:
        window_listbox.insert(tk.END, window)

    # Перезапускаем эту функцию через 3 секунду(сделал так много,
    # чтобы пользователь успевал закрывать окна)
    app.after(5000, update_window_list)


app = tk.Tk()
app.title("Управление окнами")
app.geometry("500x300")

# Создаем список окон
window_listbox = tk.Listbox(app, selectmode=tk.SINGLE, width=60)
window_listbox.pack(pady=10)

close_button = tk.Button(app, text="Закрыть выбранное окно", command=close_selected_window)
close_button.pack(pady=5)

update_window_list()

app.mainloop()