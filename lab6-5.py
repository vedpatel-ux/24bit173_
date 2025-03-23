tuple_list = [(2, 2), (), (7, 8, 9), (), (6, 7)]

filtered_list = [t for t in tuple_list if t]

print("List after removing empty tuples:", filtered_list)