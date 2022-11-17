from collections import deque

colour_substrings = deque(input().split())

main_colours = {"red", "yellow", "blue"}
secondary_colours = {"orange", "purple", "green"}
collected_colours = []

while colour_substrings:
    first_substring = colour_substrings.popleft()
    # if only one el has remained, we must pop empty string:
    second_substring = colour_substrings.pop() if colour_substrings else ''

    result = first_substring + second_substring
    if result in main_colours or result in secondary_colours:
        collected_colours.append(result)
        continue
    result = second_substring + first_substring
    if result in main_colours or result in secondary_colours:
        collected_colours.append(result)
        continue

    first_substring = first_substring[:-1]
    second_substring = second_substring[:-1]
    # tackle the cases where empty string might remain:
    if first_substring:
        colour_substrings.insert(len(colour_substrings)//2, first_substring)
    if second_substring:
        colour_substrings.insert(len(colour_substrings)//2, second_substring)

# Now, blend the colours:
result = []
required_colours = {'orange': ['red', 'yellow'], 'purple': ['red', 'blue'], 'green': ['yellow', 'blue']}
for x in collected_colours:
    if x in main_colours:
        result.append(x)
    else:
        is_valid = True
        for y in required_colours[x]:
            if y not in collected_colours:
                is_valid = False
                break
        if is_valid:
            result.append(x)

print(result)