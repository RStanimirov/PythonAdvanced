# entries, sub_entries = [int(x) for x in input().split(', ')]
# company_matrix = []
#
# for i in range(entries):
#     employee_data = [x for x in input().split(', ')]
#     company_matrix.append(employee_data)
# # print(company_matrix)
#
# for sub_entry in range(sub_entries):
#     sum_of_columns = []
#     for entry in range(entries):
#         sum_of_columns.append(company_matrix[entry][sub_entry])
#     print(sum_of_columns)

rows, el_in_rows = [int(x) for x in input().split(', ')]
matrix = []

for i in range(rows):
    line = input().split(', ')
    matrix.append(line)

for x in matrix:
    print(*x, sep=' ')
