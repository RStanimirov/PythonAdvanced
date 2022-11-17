# RS solution after the exam; could not submit it during the exam:
from collections import deque

vowels_que = deque(input().split())
consonants_stack = input().split()

model_list = ["rose", "tulip", "lotus", "daffodil"]
found_dict = {"rose": '', "tulip": '', "lotus": '', "daffodil": ''}
word_found = ''
is_found = False

while vowels_que and consonants_stack and not is_found:
    current_vowel = vowels_que[0]
    current_consonant = consonants_stack[-1]

    for x in model_list:
        if current_vowel in x:
            found_dict[x] += current_vowel
        if current_consonant in x:
            found_dict[x] += current_consonant

    if vowels_que:
        vowels_que.popleft()
    if consonants_stack:
        consonants_stack.pop()

    for k, v in found_dict.items():
        if set(k) == set(v):
            word_found = k
            is_found = True
            break

if is_found:
    print(f"Word found: {word_found}")
else:
    print("Cannot find any word!")
if vowels_que:
    print(f"Vowels left: {' '.join(x for x in vowels_que)}")
if consonants_stack:
    print(f"Consonants left: {' '.join(x for x in consonants_stack)}")


