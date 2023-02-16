import random
import string
import tkinter as tk


def generate_password(length):
    # Define all possible characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password using the specified length and characters
    password = ''.join(random.choice(characters) for i in range(length))

    return password


def generate_and_show_password():
    # Get the length of the password from the input field
    length = int(length_entry.get())

    # Generate the password
    password = generate_password(length)

    # Update the label to display the generated password
    password_label.config(text="Your password is: " + password)


def copy_to_clipboard():
    # Get the generated password from the label
    password = password_label.cget("text")[16:]

    # Copy the password to the clipboard
    window.clipboard_clear()
    window.clipboard_append(password)
    window.update()


# Create the Tkinter window
window = tk.Tk()
window.title("Random Password Generator")
window.geometry("400x250")

# Create the input field for the password length
length_label = tk.Label(window, text="Password length:")
length_label.pack()
length_entry = tk.Entry(window)
length_entry.pack()

# Create the button to generate the password
generate_button = tk.Button(
    window, text="Generate password", command=generate_and_show_password)
generate_button.pack()

# Create the label to display the generated password
password_label = tk.Label(window, text="")
password_label.pack()

# Create the button to copy the password to the clipboard
copy_button = tk.Button(window, text="Copy to clipboard",
                        command=copy_to_clipboard)
copy_button.pack()

# Center the window on the screen
window.update_idletasks()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width // 2) - (window.winfo_width() // 2)
y = (screen_height // 2) - (window.winfo_height() // 2)
window.geometry("+{}+{}".format(x, y))

# Start the Tkinter event loop
window.mainloop()
