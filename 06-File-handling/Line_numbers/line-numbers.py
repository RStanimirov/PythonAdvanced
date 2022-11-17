import re

with open('text.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    for r, l in enumerate(input_file):
        stripped_line = l.strip()
        pattern_letters = '[A-za-z]'
        pattern_marks = '[,.\\-\'":?!]'
        letters_count = len(re.findall(pattern_letters, stripped_line))
        marks_count = len(re.findall(pattern_marks, stripped_line))
        output_file.write(f"Line {r + 1}: {stripped_line} ({letters_count})({marks_count})\n")


