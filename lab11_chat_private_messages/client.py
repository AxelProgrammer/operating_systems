import socket
import tkinter as tk
from tkinter import messagebox
from threading import Thread


class ChatClient:
    def __init__(self, master):
        self.master = master
        self.master.title("Чат")

        self.message_listbox = tk.Listbox(master, width=50, height=20)
        self.message_listbox.pack(padx=10, pady=10)

        self.private_message_label_1 = tk.Label(master, text="Личное сообщение: '@имя_получателя' сообщение")
        self.private_message_label_1.pack(padx=10, pady=5)
        self.private_message_label_1 = tk.Label(master, text="Обычное сообщение: сообщение")
        self.private_message_label_1.pack(padx=10, pady=5)

        self.message_entry = tk.Entry(master, width=50)
        self.message_entry.pack(padx=10, pady=5)

        self.send_button = tk.Button(master, text="Отправить", command=self.send_message)
        self.send_button.pack(padx=10, pady=5)

        self.name_entry = tk.Entry(master, width=20)
        self.name_entry.pack(padx=10, pady=5)

        self.connect_button = tk.Button(master, text="Подключиться", command=self.connect_to_server)
        self.connect_button.pack(padx=10, pady=5)

        self.client_socket = None
        self.receive_thread = None

    def connect_to_server(self):
        name = self.name_entry.get()
        if not name:
            messagebox.showerror("Ошибка", "Введите ваше имя")
            return

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client_socket.connect(('127.0.0.1', 5555))
            self.client_socket.send(bytes(name, 'utf-8'))
            response = self.client_socket.recv(1024).decode('utf-8')
            if response == "Имя уже занято. Пожалуйста, выберите другое.":
                messagebox.showerror("Ошибка", response)
                self.client_socket.close()
                self.connect_button.config(state=tk.NORMAL)  # Enable the button
            else:
                self.receive_thread = Thread(target=self.receive_messages)
                self.receive_thread.start()
                self.connect_button.config(state=tk.DISABLED)
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось подключиться к серверу: {e}")

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                self.message_listbox.insert(tk.END, message)
            except:
                break

    def send_message(self):
        message = self.message_entry.get()
        if message:
            try:
                self.client_socket.send(bytes(message, 'utf-8'))
                self.message_entry.delete(0, tk.END)
            except:
                messagebox.showerror("Ошибка", "Не удалось отправить сообщение")


def main():
    root = tk.Tk()
    client_app = ChatClient(root)
    root.mainloop()


if __name__ == "__main__":
    main()
