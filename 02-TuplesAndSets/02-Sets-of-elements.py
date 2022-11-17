numbers = input().split()

n = int(numbers[0])
m = int(numbers[1])

n_set = []
m_set = []
unique_set = set()

for i in range(n):
    n_num = int(input())
    n_set.append(n_num)

for j in range(m):
    m_num = int(input())
    m_set.append(m_num)

for k in n_set:
    for v in m_set:
        if k == v:
            unique_set.add(k)

print('\n'.join(str(x) for x in unique_set))    