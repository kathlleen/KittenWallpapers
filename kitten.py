from tkinter import *
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
import sys
import ctypes
import os
import time
import random
import tkinter as tk
from tkinter import ttk

def fake_delete():
    fake_window = tk.Toplevel(wnd)
    fake_window.title("Выполнено 0%")
    fake_window.geometry("420x240")
    fake_window.iconbitmap(resource_path('pictures/icon-explorer.ico'))
    fake_window.resizable(False, False)
    fake_window.config(bg="#F0F0F0")

    fake_window.bind("<Enter>", lambda event: move_window(fake_window))
    # Заголовок: процесс удаления
    title_label = tk.Label(
        fake_window,
        text="Перемещение элементов (717) из Системный(С:)",
        font=("Segoe UI", 10),
        anchor="w",
        justify="left"
    )
    title_label.pack(fill="x", padx=10, pady=(10, 0))

    # Текст "Выполнено X%"
    progress_label = tk.Label(
        fake_window,
        text="Выполнено 0%",
        font=("Segoe UI", 10),
        anchor="w"
    )
    progress_label.pack(fill="x", padx=10, pady=5)

    # Прогресс-бар
    progress_bar = ttk.Progressbar(
        fake_window,
        orient="horizontal",
        length=380,
        mode="determinate",
        maximum=100
    )
    progress_bar.pack(pady=5, padx=20)

    # Статус деталей
    details_label = tk.Label(
        fake_window,
        text="Имя: Windows\nОставшееся время: Оценивается...\nОсталось элементов: 717 (0 байт)",
        font=("Segoe UI", 9),
        anchor="w",
        justify="left"
    )
    details_label.pack(fill="x", padx=10, pady=(10, 0))

    # Кнопка "Меньше сведений"
    less_info_button = tk.Button(
        fake_window,
        text="Меньше сведений",
        font=("Segoe UI", 9),
        relief="flat",
        command=fake_window.destroy  # Просто закрывает окно
    )
    less_info_button.pack(anchor="w", padx=10, pady=5)

    # Симуляция процесса удаления
    total_files = 717
    total_size = 0  # Размер в байтах
    remaining_files = total_files

    while remaining_files > 0:
        # Симуляция размера файла (случайный размер)
        file_size = random.randint(90, 1000)  # Размер от 100 до 1000 байт
        total_size += file_size  # Добавляем размер для текущего удаляемого файла

        # Случайное уменьшение оставшихся файлов (от 1 до 20 файлов)
        files_to_remove = random.randint(10, 60)
        remaining_files -= files_to_remove

        # Обновляем прогресс
        progress = int(((total_files - remaining_files) / total_files) * 100)
        progress_bar['value'] = progress
        progress_label.config(text=f"Выполнено {progress}%")
        fake_window.title(f"Выполнено {progress}%")

        # Оставшиеся элементы и байты
        remaining_size = total_size  # Уменьшаем оставшийся размер
        details_label.config(
            text=f"Имя: Windows\nОставшееся время: Оценивается...\nОсталось элементов: {remaining_files} ({remaining_size} байт)")

        # Обновляем интерфейс
        fake_window.update_idletasks()
        time.sleep(0.3)  # Задержка для эффекта скачков

    # Финализация
    details_label.config(text="Имя: Windows\nУдаление завершено.")
    fake_window.update_idletasks()
    minimize_all_windows()
    fake_window.destroy()
    wnd.destroy()

def move_window(window):
    # Получаем текущие координаты окна
    x = window.winfo_x()
    y = window.winfo_y()

    # Генерируем случайные смещения
    dx = random.randint(-100, 100)
    dy = random.randint(-100, 100)

    # Вычисляем новые координаты
    new_x = x + dx
    new_y = y + dy

    # Перемещаем окно на новые координаты
    window.geometry(f"+{new_x}+{new_y}")

def minimize_all_windows():

    # Код клавиши Win (0x5B) и клавиши D (0x44)
    vk_lwin = 0x5B
    vk_d = 0x44

    # Нажимаем Win + D
    ctypes.windll.user32.keybd_event(vk_lwin, 0, 0, 0)  # Нажатие клавиши Win
    ctypes.windll.user32.keybd_event(vk_d, 0, 0, 0)     # Нажатие клавиши D
    ctypes.windll.user32.keybd_event(vk_d, 0, 2, 0)     # Отпускание клавиши D
    ctypes.windll.user32.keybd_event(vk_lwin, 0, 2, 0)  # Отпускание клавиши Win


def set_wallpaper(image_path):
    # Преобразуем путь к изображению в абсолютный
    image_path = os.path.abspath(image_path)
    # Устанавливаем обои через WinAPI
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)

def change(evt):
    global current_index
    t = cb.get()
    for k in range(len(names)):
        if t==names[k]:
            lbl.configure(image=imgs[k])
            lbl.image = imgs[k]  # Сохраняем ссылку на изображение
            current_index = k  # Сохраняем текущий индекс
            break

def on_select_button():
    selected_image_path = resource_path(path + files[current_index])
    set_wallpaper(selected_image_path)
    minimize_all_windows()
    wnd.destroy()

def resource_path(relative_path):
    """Возвращает абсолютный путь к ресурсу (для работы в .exe)"""
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller создаёт временную директорию _MEIPASS
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)



wnd = Tk()
wnd.title('Окошко')
wnd.iconbitmap(resource_path('pictures/2.ico'))
wnd_width=700
wnd_height=550

wnd.geometry(f"{wnd_width}x{wnd_height}")
wnd.resizable(False, False)


lbl = Label(wnd, text='Выбери котика :3', font=("Comic Sans MS", 18))
lbl.place(x=(wnd_width/2-120),y=7)

path = "pictures\\"
names = ["Чиловый", "Рыженький", "Невдупленыш", "Шмыгля", "Эстет", "Пухляш"]
files = ['chill.jpg', 'ginger.webp', 'small.jpg', 'шмыгля.webp', 'эстет.jpg', 'пухляш.webp']

imgs = []
for file in files:
    img = Image.open(resource_path(path + file))
    img = img.resize((600, 350), Image.Resampling.LANCZOS)  # Масштабируем до 600x300
    imgs.append(ImageTk.PhotoImage(img))

current_index = 0

lbl = Label(wnd, image=imgs[current_index])
lbl.configure(relief=GROOVE)
lbl.place(x=50, y=50, width=600, height=350)

cb = Combobox(wnd, state='readonly')
cb.configure(values=names)
cb.current(current_index)
cb.configure(font=("Comic Sans MS", 16))

cb.bind("<<ComboboxSelected>>", change)
cb.place(x=(wnd_width/2-100), y=410, width=200, height=30)

btn = Button(wnd, text="Выбрать", font=("Comic Sans MS", 12), command=on_select_button, bg='#c9c0bb')
btn.place(x=(wnd_width/3-85), y=460, width=170, height=60)

btn = Button(wnd, text="Мне не нравятся \n твои обои", font=("Comic Sans MS", 12), bg='#CD5C5C', command=fake_delete)
btn.place(x=(wnd_width/3*2-85), y=460, width=170, height=60)

wnd.mainloop()



