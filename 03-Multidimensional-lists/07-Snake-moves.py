from math import ceil
# RS solution, initially 60/100 in judge, 100/100 with the help of below multiplication of the input word by ceil():
entries, sub_entries = [int(x) for x in input().split()]
word = input()
raw_string = word * ceil(entries * sub_entries / len(word))
snake_matrix = []
matrix_length = entries * sub_entries

while len(raw_string) > matrix_length:
    raw_string = raw_string[:-1]

chunks = [raw_string[i:i+sub_entries] for i in range(0, len(raw_string), sub_entries)]

for idx in range(len(chunks)):
    if idx % 2 != 0:
        chunk = list(chunks[idx])
        chunk.reverse()
    else:
        chunk = list(chunks[idx])

    snake_matrix.append(chunk)

for x in snake_matrix:
    print(''.join(x))
