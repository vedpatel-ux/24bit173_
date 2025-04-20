def is_dict_empty(d):
    if not d:
        print("The dictionary is empty.")
    else:
        print("The dictionary is not empty.")

dict1 = {}
dict2 = {"Apple": 60, "mango": 30, "graps": 100}

is_dict_empty(dict1)
is_dict_empty(dict2)