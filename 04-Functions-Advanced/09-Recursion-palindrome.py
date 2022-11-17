def palindrome(text, idx):
    if idx == len(text) // 2:
        return f"{text} is a palindrome"
    left_char = text[idx]
    right_char = text[len(text) - 1 - idx]
    if left_char != right_char:
        return f"{text} is not a palindrome"

    return palindrome(text, idx+1)


print(palindrome("abcba", 0))