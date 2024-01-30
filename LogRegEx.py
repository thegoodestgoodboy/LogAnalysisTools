import tkinter as tk
from tkinter import filedialog
import re

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(tk.END, file_path)

def parse_text():
    file_path = file_entry.get()
    regex_pattern = regex_entry.get()

    try:
        with open(file_path, 'r') as file:
            text_content = file.read()
    except FileNotFoundError:
        result_label.config(text="File not found.")
        return

    result = re.findall(regex_pattern, text_content)

    output_file_path = "RegExOutput.txt"
    with open(output_file_path, 'w') as output_file:
        for match in result:
            output_file.write(f"{match}\n")

    result_label.config(text=f"Results saved to {output_file_path}")

# Create the main window
window = tk.Tk()
window.title("Text File Parser")

# File Entry
file_label = tk.Label(window, text="Select a text file:")
file_label.pack()

file_entry = tk.Entry(window, width=40)
file_entry.pack()

browse_button = tk.Button(window, text="Browse", command=browse_file)
browse_button.pack()

# Regular Expression Entry
regex_label = tk.Label(window, text="Enter a regular expression:")
regex_label.pack()

regex_entry = tk.Entry(window, width=40)
regex_entry.pack()

# Parse Button
parse_button = tk.Button(window, text="Parse", command=parse_text)
parse_button.pack()

# Result Label
result_label = tk.Label(window, text="")
result_label.pack()

# Run the main loop
window.mainloop()
