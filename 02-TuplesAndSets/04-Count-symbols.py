text = input()

text_diction = {}

for x in text:
    if x not in text_diction:
        text_diction[x] = 0
    text_diction[x] += 1

# print(text_diction)
# Lexicigraphical sorting using.sort()
# sorted_text_diction = text_diction.sort()
# Standard dictionary sorting:
sorted_text_diction = dict(sorted(text_diction.items(), key=lambda x: x[0]))
for key, value in sorted_text_diction.items():
    print(f"{key}: {value} time/s")
