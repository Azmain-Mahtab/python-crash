import re

file_path = "/home/azmain/Desktop/xyz.log"
pattern = r"ERROR.*$"

try:
    with open(file_path, 'r') as file:
        content = file.read()
        matches = re.findall(pattern, content, re.MULTILINE)
        if matches: 
            print(f"Found {len(matches)} matches for the pattern '{pattern}':")
            for match in matches:
                print(match)
        else:
            print(f"No matches found for the pattern '{pattern}'.")
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
# This code reads a log file and searches for occurrences of the word "error" using regular expressions.