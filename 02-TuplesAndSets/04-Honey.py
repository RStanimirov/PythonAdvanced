from collections import deque
from math import floor

# import sys
# from io import StringIO
#
# input_1 = """0 62 99 35 0 150
# 120 60 10 1 70 0
# / + - + + / * - - /
# """
# input_2 = """30
# 15 9 5 150 8
# * + + * -
# """
#
# sys.stdin = StringIO(input_1)


def calculate_the_honey(honey: int, the_bees: int, the_nectar: int, the_symbol: str):
    if the_symbol == '+':
        honey += the_bees + the_nectar
    elif the_symbol == '-':
        honey += abs(the_bees - the_nectar)
    elif the_symbol == '*':
        honey += the_bees * the_nectar
    elif the_symbol == '/':
        honey += the_bees / the_nectar
    return honey


bees = deque(int(x) for x in input().split())
nectar = deque(int(x) for x in input().split())
symbols = deque(input().split())

total_honey = 0

while True:
    if not bees or not nectar:
        break
    if bees[0] > nectar[-1]:
        nectar.pop()
        continue
    else:
        current_bees = bees.popleft()
        current_nectar = nectar.pop()
        current_symbol = symbols.popleft()
        if current_bees == 0 and current_nectar == 0:
            continue
        total_honey = calculate_the_honey(total_honey, current_bees, current_nectar, current_symbol)

print(f"Total honey made: {total_honey}")
if bees:
    bees = ', '.join(str(x) for x in bees)
    print(f"Bees left: {bees}")
if nectar:
    nectar = ', '.join(str(x) for x in nectar)
    print(f"Nectar left: {nectar}")