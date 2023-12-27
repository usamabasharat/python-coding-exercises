# Write a Python program to swap first and last element of the list.

def swap_first_and_last(n_list):
    n_list[0], n_list[-1] = n_list[-1], n_list[0]

    return n_list


n_list = [1, 3, 4, 5, 7]

print(swap_first_and_last(n_list))
