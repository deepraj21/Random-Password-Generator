import random
import string
import tkinter as tk

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def generate_and_show_password():
    length = int(length_entry.get())
    password = generate_password(length)
    password_label.config(text="Your password is: " + password)


def copy_to_clipboard():
    password = password_label.cget("text")[16:]
    window.clipboard_clear()
    window.clipboard_append(password)
    window.update()

window = tk.Tk()
window.title("Random Password Generator")
window.geometry("400x250")
length_label = tk.Label(window, text="Password length:")
length_label.pack()
length_entry = tk.Entry(window)
length_entry.pack()
generate_button = tk.Button(window, text="Generate password", command=generate_and_show_password)
generate_button.pack()
password_label = tk.Label(window, text="")
password_label.pack()
copy_button = tk.Button(window, text="Copy to clipboard",command=copy_to_clipboard)
copy_button.pack()

window.update_idletasks()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width // 2) - (window.winfo_width() // 2)
y = (screen_height // 2) - (window.winfo_height() // 2)
window.geometry("+{}+{}".format(x, y))

window.mainloop()
