from itertools import permutations

digits = [1, 3, 4]

# First Approach

for x in digits:
    for y in digits:
        for z in digits:
            if x != y and x != z and y != z:
                print([x, y, z])

# Second Approach

print(list(permutations(digits, 3)))