chars_to_replace = ["-", ",", ".", "!", "?"]

with open('text.txt', 'r') as file:
    for row_idx, line_str in enumerate(file):
        if row_idx % 2 == 0:
            result = ' '.join(reversed(line_str.strip().split()))
            for x in chars_to_replace:
                result = result.replace(x, '@')
            print(result)

