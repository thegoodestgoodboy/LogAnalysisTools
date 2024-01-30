import json
import os
import tkinter as tk
from tkinter import filedialog

def extract_compute_engines(audit_logs):
    compute_engines = set()

    for log_entry in audit_logs:
        proto_payload = log_entry.get('protoPayload', {})
        resource_name = proto_payload.get('resourceName')
        
        if resource_name and resource_name.startswith('projects/'):
            compute_engines.add(resource_name)

    return compute_engines

def process_file(file_path):
    try:
        with open(file_path, 'r') as f:
            audit_logs = json.load(f)

        compute_engines = extract_compute_engines(audit_logs)

        output_file = os.path.join(os.path.dirname(file_path), "ComputeEngineAudit.txt")
        with open(output_file, 'w') as f:
            for engine in compute_engines:
                f.write(engine + '\n')

        print(f"Compute engines extracted and saved to {output_file}")
    except FileNotFoundError:
        print("Error: Input file not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in the input file.")
    except Exception as e:
        print(f"Error: {str(e)}")

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if file_path:
        process_file(file_path)

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Display file dialog and process selected file
    browse_file()

if __name__ == "__main__":
    main()
