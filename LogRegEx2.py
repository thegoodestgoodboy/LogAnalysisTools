import re
import os
import tkinter as tk
from tkinter import filedialog

def process_file(file_path):
    # Define the regular expression pattern
    pattern = re.compile(r'projects/.*\b\d{10}-\d{8}\b.*')

    # Output file path
    output_file_path = os.path.join(os.path.dirname(file_path), 'Regex Output.txt')

    with open(file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        for line_number, line in enumerate(input_file, start=1):
            # Find matches in each line
            matches = pattern.findall(line)
            for match in matches:
                output_file.write(match + '\n')
                print(f"Match found in line {line_number}: {match}")

    print(f"Output saved to: {output_file_path}")

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Prompt the user to select a .txt file
    file_path = filedialog.askopenfilename(title="Select a .txt file", filetypes=[("Text files", "*.txt")])

    if file_path:
        process_file(file_path)
    else:
        print("No file selected. Exiting.")

if __name__ == "__main__":
    main()
