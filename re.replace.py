import re

file_path = "/home/azmain/Desktop/xyz.log"
pattern = r"error"

replacement = "ERROR"

try:
    with open(file_path, 'r') as file:
        content = file.read()
        new_content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
        
    with open(file_path, 'w') as file:
        file.write(new_content)
        
    print(f"Replaced occurrences of '{pattern}' with '{replacement}' in {file_path}.")
except FileNotFoundError:
    print(f"File not found: {file_path}")
