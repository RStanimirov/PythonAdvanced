from collections import deque

words = ['rose', 'tulip', 'lotus', 'daffodil']

vowels = deque(v for v in input().split())
consonants = [c for c in input().split()]
my_letters = []
is_word = True
find_word = ''

while vowels and consonants:
    my_letters.append(vowels.popleft())
    my_letters.append(consonants.pop())

    for word in words:
        is_word = True
        for letter in word:
            if letter not in my_letters:
                is_word = False
                break
        if is_word:
            find_word = word
            break

    if is_word:
        break

if not is_word:
    print('Cannot find any word!')
else:
    print(f"Word found: {find_word}")

if vowels:
    print(f'Vowels left: {" ".join([str(v) for v in vowels])}')

if consonants:
    print(f'Consonants left: {" ".join(str(c) for c in consonants)}')