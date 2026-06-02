import customtkinter
import tkinter
import random

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

chars = 'qwertyuiopasdfghjklzxcvbnm'
symbols = '+-#&%#$@^*$'
numbers = '0123456789'

# Создаем единый список символов
chars_list = list(chars + chars.upper() + symbols + numbers)


def generate():
    # Очищаем поле перед генерацией новых паролей
    text_field.delete("1.0", tkinter.END)

    try:
        len_passwords = int(entry_len.get())
        count_passwords = int(entry_count.get())
    except ValueError:
        text_field.insert(tkinter.END, "Ошибка: введите целые числа!")
        return

    if len_passwords <= 0 or count_passwords <= 0:
        text_field.insert(tkinter.END, "Ошибка: числа должны быть больше 0!")
        return

    available_chars = ""

    if use_lower.get():
        available_chars += chars

    if use_upper.get():
        available_chars += chars.upper()

    if use_digits.get():
        available_chars += numbers

    if use_symbols.get():
        available_chars += symbols

    if not available_chars:
        text_field.insert(
            tkinter.END,
            "Ошибка: выберите хотя бы один тип символов!"
        )
        return

    for _ in range(count_passwords):
        password = ''.join(
            random.choice(available_chars)
            for _ in range(len_passwords)
        )
        text_field.insert(tkinter.END, password + '\n')

def clear():
    text_field.delete("1.0", tkinter.END)


def copy_password():
    # Получаем весь текст из текстового поля
    text_to_copy = text_field.get("1.0", tkinter.END).strip()
    if text_to_copy:
        window.clipboard_clear()
        window.clipboard_append(text_to_copy)
        window.update()  # Фиксируем буфер обмена


window = customtkinter.CTk()
window.title('Генератор паролей')
window.geometry('800x800')

use_lower = customtkinter.BooleanVar(value=True)
use_upper = customtkinter.BooleanVar(value=True)
use_digits = customtkinter.BooleanVar(value=True)
use_symbols = customtkinter.BooleanVar(value=True)

customtkinter.CTkCheckBox(
    window, text="Строчные буквы", variable=use_lower
).place(x=20, y=100)

customtkinter.CTkCheckBox(
    window, text="Заглавные буквы", variable=use_upper
).place(x=20, y=130)

customtkinter.CTkCheckBox(
    window, text="Цифры", variable=use_digits
).place(x=20, y=160)

customtkinter.CTkCheckBox(
    window, text="Спецсимволы", variable=use_symbols
).place(x=20, y=190)

customtkinter.CTkLabel(window, text='Кол-во паролей: ').place(x=220, y=30)
entry_count = customtkinter.CTkEntry(window, width=50)
entry_count.place(x=350, y=30)

customtkinter.CTkLabel(window, text='Длина паролей: ').place(x=220, y=60)
entry_len = customtkinter.CTkEntry(window, width=50)
entry_len.place(x=350, y=60)

btn_generate = customtkinter.CTkButton(window, text='Генерировать', command=generate)
btn_generate.place(x=150, y=220)

btn_clear = customtkinter.CTkButton(window, text='Очистить', command=clear)
btn_clear.place(x=350, y=220)

btn_copy = customtkinter.CTkButton(window, text='Скопировать пароли', command=copy_password)
btn_copy.place(x=550, y=220)

text_field = customtkinter.CTkTextbox(window, width=560, height=400)
text_field.place(x=100, y=290)

window.mainloop()
