numbers = [int(x) for x in input().split()]

positive_nums = []
negative_nums = []

for x in numbers:
    if x > 0:
        positive_nums.append(x)
    elif x < 0:
        negative_nums.append(x)

print(sum(negative_nums))
print(sum(positive_nums))

negative_strength = abs(sum(negative_nums))

if sum(positive_nums) > negative_strength:
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")