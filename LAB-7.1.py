dict1 = {"apple": 30, "banana": 60}
dict2 = {"watermelon": 30, "graps": 150}
dict3 = {"grapes": 60, "pineapple": 40}

dict4 = {**dict1, **dict2, **dict3}

print("Merged Dictionary 4:", dict4)