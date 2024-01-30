import json
import os
import tkinter as tk
from tkinter import filedialog

def sort_json_keys(json_data, specific_principal_email=None):
    try:
        # Parse JSON data
        data = json.loads(json_data)

        if isinstance(data, list):
            # If it's a list, sort the items based on their string representation
            sorted_data = sorted(map(str, data))
            output_file_path = os.path.join(os.path.dirname(file_path), 'sorted_output.txt')
            write_to_file(output_file_path, sorted_data)
            print(f"Sorted items written to '{output_file_path}'.")
        elif isinstance(data, dict):
            # If it's a dictionary, extract key-value pairs
            key_value_pairs = [(str(key), str(value)) for key, value in data.items()]

            # Filter key-value pairs based on specific_principal_email if provided
            if specific_principal_email:
                key_value_pairs = [(key, value) for key, value in key_value_pairs if key == 'principalEmail' and value == specific_principal_email]

            # Identify the key containing the timestamp (replace 'timestamp' with the actual key)
            timestamp_key = 'timestamp'

            # Sort key-value pairs based on the timestamp key (if present)
            sorted_key_value_pairs = sorted(key_value_pairs, key=lambda x: x[0] if x[0] != timestamp_key else x[1])

            output_file_path = os.path.join(os.path.dirname(file_path), 'sorted_output.txt')
            write_to_file(output_file_path, sorted_key_value_pairs)
            print(f"Sorted key-value pairs written to '{output_file_path}'.")
        else:
            print("Unsupported JSON structure. Please provide a JSON list or dictionary.")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")

def write_to_file(file_path, data):
    with open(file_path, 'w') as output_file:
        for item in data:
            output_file.write(f"{item}\n")

def upload_file():
    global file_path
    file_path = filedialog.askopenfilename(title="Select a JSON file", filetypes=[("JSON files", "*.json")])

    if file_path:
        specific_principal_email = input("Enter specific principalEmail to filter (or press Enter to skip): ")
        with open(file_path, 'r') as file:
            json_data = file.read()
            sort_json_keys(json_data, specific_principal_email)
    else:
        print("No file selected.")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    try:
        upload_file()
    except Exception as e:
        print(f"An error occurred: {e}")
