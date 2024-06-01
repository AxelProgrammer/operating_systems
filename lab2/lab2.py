import psutil
import tkinter as tk

def get_disk_info():
    disk_info = []
    for partition in psutil.disk_partitions():
        disk = psutil.disk_usage(partition.mountpoint)
        disk_info.append([partition.device, partition.fstype, disk.total, disk.free])
    return disk_info
def update_disk_info():
    disk_info = get_disk_info()
    for i, info in enumerate(disk_info):
        disk_label = f"{info[0]} {info[1]} {info[2]} {info[3]}"
        disk_labels[i].config(text=disk_label)

window = tk.Tk()

disk_labels = []
disk_info = get_disk_info()
for info in disk_info:
    disk_label = f"{info[0]} {info[1]} {info[2]} {info[3]}"
    label = tk.Label(window, text=disk_label)
    label.pack()
    disk_labels.append(label)

update_button = tk.Button(window, text="Обновить информацию о дисках", command=update_disk_info)
update_button.pack()

def get_usb_info():
    usb_info = []
    for partition in psutil.disk_partitions():
        if 'removable' in partition.opts or 'usb' in partition.opts:
            usb = psutil.disk_usage(partition.mountpoint)
            usb_info.append([partition.device, partition.fstype, usb.total, usb.free])
    return usb_info

def show_usb_info():
    usb_info = get_usb_info()
    if len(usb_info) > 0:
        usb_label = f"Флешка: {usb_info[0][0]} {usb_info[0][1]} {usb_info[0][2]} {usb_info[0][3]}"
        usb_info_label.config(text=usb_label)
    else:
        usb_info_label.config(text="Флешка не подключена")

usb_info_label = tk.Label(window, text="")
usb_info_label.pack()

show_usb_button = tk.Button(window, text="Показать информацию о флешке", command=show_usb_info)
show_usb_button.pack()

window.mainloop()