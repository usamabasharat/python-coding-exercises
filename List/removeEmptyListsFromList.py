# Remove empty lists from list

e_list = [1, 4, [1, 6, 1], [], [90, 12, 342], []]
new_list = []

# First Approach

for item in e_list:
    if item:
        new_list.append(item)

print(new_list)

# Second Approach

print(list(filter(None, e_list)))
