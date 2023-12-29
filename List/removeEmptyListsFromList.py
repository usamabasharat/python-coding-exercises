# Remove empty lists from list

e_list = [1, 4, [1, 6, 1], [], [90, 12, 342], []]

# First Approach

for item in e_list:
    if not item:
        e_list.remove(item)

print(e_list)

# Second Approach

e_list = [1, 4, [1, 6, 1], [], [90, 12, 342], []]

print(list(filter(None, e_list)))
