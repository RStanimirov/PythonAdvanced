# clothes_truck = [int(x) for x in input().split()]
# rack_capacity = int(input())
# used_racks = 1
# current_rack_capacity = rack_capacity
#
# while clothes_truck:
#     hangers = clothes_truck[-1]
#     if hangers <= current_rack_capacity:
#         clothes_truck.pop()
#         current_rack_capacity -= hangers
#     else:
#         used_racks += 1
#         current_rack_capacity = rack_capacity
#
# print(used_racks)
clothes = [int(x) for x in input().split()]
rack_capacity = int(input())
current_load_on_rack = 0
counter = 1

while clothes:
    if current_load_on_rack + clothes[-1] < rack_capacity:
        current_load_on_rack += clothes.pop()
    elif current_load_on_rack + clothes[-1] == rack_capacity:
        current_load_on_rack += clothes.pop()
        if counter == 1:
            pass
        else:
            counter += 1
            current_load_on_rack = 0
    else:
        counter += 1
        current_load_on_rack = 0

print(counter)
