expression = input()

opening_brackets = []
balanced = True

for ch in expression:
    if ch in '({[':
        opening_brackets.append(ch)
    elif not opening_brackets:
        balanced = False
        break
    else:
        last_opening_bracket = opening_brackets.pop()
        if f'{last_opening_bracket}{ch}' not in '(){}[]':
            balanced = False
            break

if balanced:
# correct should be if balanced and not opening_brackets: because input ({[ should be NO, not YES.
    print("YES")
else:
    print("NO")
