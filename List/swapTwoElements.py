# Given a list and provided the positions of the elements, write a program to swap the two elements in the list.


def swap_elements(n_list, first_element, second_element):
    try:
        n_list[second_element - 1], n_list[first_element - 1] = n_list[first_element - 1],  n_list[second_element - 1]

        return n_list
    except Exception as e:
        print(f"Error: {e}")


n_list = [1, 3, 4, 5, 7]

print(swap_elements(n_list, 3, 5))
