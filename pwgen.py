import random
import string
import tkinter as tk
from tkinter import ttk
import sys

def generate_password(length):
    if length < 8 or length > 50:
        return "Length must be between 8 and 50"
    
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = ",\"#$%^&*!"

    required_chars = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

    remaining_length = length - len(required_chars)
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters
    random_chars = [random.choice(all_characters) for _ in range(remaining_length)]

    all_chars = required_chars + random_chars
    random.shuffle(all_chars)

    return ''.join(all_chars)

def generate_password_gui(event=None):
    length = int(length_entry.get())
    result_text.set(generate_password(length))


def copy_to_clipboard():
    pw = result_text.get()
    window.clipboard_clear()
    window.clipboard_append(pw)
    window.update()

    copy_button.config(bg="lime", text="Copied!")
    window.after(2000, revert_copy_button)

def revert_copy_button():
    copy_button.config(bg="SystemButtonFace", text="Copy to Clipboard")

# Check if a command-line argument is provided
if len(sys.argv) > 1:
    try:
        length_from_command_line = int(sys.argv[1])
        if 8 <= length_from_command_line <= 50:
            # Generate and print the random string
            random_string = generate_password(length_from_command_line)
            print(random_string)
            sys.exit(0)
        else:
            print("Length must be between 8 and 50.")
            sys.exit(1)
    except ValueError:
        print("Invalid length. Please provide an integer length.")
        sys.exit(1)


window = tk.Tk()
window.title("Password Generator")

length_label = tk.Label(window, text="Enter length (8-50):")
default_length = "12"
length_var = tk.StringVar(value=default_length)
length_entry = tk.Entry(window, textvariable=length_var)
length_entry.focus_set()
length_entry.icursor(tk.END)
generate_button = tk.Button(window, text="Generate", command=generate_password_gui)
result_text = tk.StringVar()
result_entry = tk.Entry(window, textvariable=result_text)
copy_button = tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard)

# Bind the Enter key to the generate_random_string_gui function
length_entry.bind("<Return>", generate_password_gui)

# Place widgets in the window with spacing
length_label.pack(pady=5)
length_entry.pack(pady=5)
generate_button.pack(pady=10)
result_entry.pack(pady=5)
copy_button.pack(pady=10)

# Start the GUI event loop
window.mainloop()
