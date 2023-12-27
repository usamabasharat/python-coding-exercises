# Sum of number digits in List

list = [12, 4, 51, 10, 98]

# First approach
new_list1 = []
el_sum = 0

for item in list:
    item_str = str(item)
    for str_index in range(len(item_str)):
        el_sum += int(item_str[str_index])
    new_list1.append(el_sum)
    el_sum = 0

print(new_list1)

# Second approach

new_list = [sum(map(int, str(item))) for item in list]
print(new_list)
