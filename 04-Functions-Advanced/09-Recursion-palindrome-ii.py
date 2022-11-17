# def palindrome(text, idx):
#     if text[idx] == text[::-1][idx]:
#         if idx == len(text)-1:
#             return f"{text} is a palindrome"
#         return palindrome(text, idx+1)
#     else:
#         return f"{text} is not a palindrome"
#
#
# print(palindrome("abcba", 0))

#RS without recursion:
def palindrome(text, idx):
    reversed_text = ''
    for i in range(len(text)-1, -1, -1):
        reversed_text += text[i]
    if text == reversed_text:
        return f"{text} is a palindrome"
    else:
        return f"{text} is not a palindrome"


print(palindrome("abuycba", 0))