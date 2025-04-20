def create_list(list1, list2):
    intersection = [item for item in list1 if item in list2]
    return intersection

list_x= [1, 2, 3, 4, 5]
list_y = [3, 4, 5, 6, 7]
result = create_list(list_x, list_y)
print("Intersection of lists:", result)