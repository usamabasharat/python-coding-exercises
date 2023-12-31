# Multiple of number digits in List

list = [12, 4, 51, 10, 98]

# First Approach

new_list1 = []
el_mul = 1

for item in list:
    item_str = str(item)
    for str_index in range(len(item_str)):
        el_mul *= int(item_str[str_index])
    new_list1.append(el_mul)
    el_mul = 1

print(new_list1)

# Second Approach

new_list = [eval('*'.join(str(digit) for digit in map(int, str(item)))) for item in list]
print(new_list)
