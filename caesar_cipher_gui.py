# caesar_cipher_gui.py

import tkinter as tk
from tkinter import ttk, messagebox

def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def encrypt_action():
    text = entry_text.get()
    try:
        shift = int(entry_shift.get())
        encrypted = caesar_cipher_encrypt(text, shift)
        output_result.set(f"Encrypted: {encrypted}")
    except ValueError:
        messagebox.showerror("Input Error", "Shift must be an integer.")

def decrypt_action():
    text = entry_text.get()
    try:
        shift = int(entry_shift.get())
        decrypted = caesar_cipher_encrypt(text, -shift)
        output_result.set(f"Decrypted: {decrypted}")
    except ValueError:
        messagebox.showerror("Input Error", "Shift must be an integer.")

# Setup GUI window
window = tk.Tk()
window.title("Caesar Cipher Tool")
window.geometry("400x250")
window.resizable(False, False)

# Text input
ttk.Label(window, text="Enter Text:").pack(pady=5)
entry_text = ttk.Entry(window, width=50)
entry_text.pack()

# Shift input
ttk.Label(window, text="Enter Shift:").pack(pady=5)
entry_shift = ttk.Entry(window, width=20)
entry_shift.pack()

# Buttons
btn_frame = ttk.Frame(window)
btn_frame.pack(pady=10)

ttk.Button(btn_frame, text="Encrypt", command=encrypt_action).grid(row=0, column=0, padx=10)
ttk.Button(btn_frame, text="Decrypt", command=decrypt_action).grid(row=0, column=1, padx=10)

# Output
output_result = tk.StringVar()
ttk.Label(window, textvariable=output_result, foreground="blue", wraplength=380).pack(pady=10)

# Start GUI loop
window.mainloop()
