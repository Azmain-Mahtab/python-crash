import re

text = "apple,banana,orange,grape"
pattern = r","

split_result = re.split(pattern, text)
print("Split result:", split_result)
# This code splits a string of fruits separated by commas into a list of individual fruits using regular expressions.
# The output will be a list of fruits: ['apple', 'banana', 'orange', 'grape']

