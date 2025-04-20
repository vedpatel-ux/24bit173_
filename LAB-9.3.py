def create_array(a, b, c, value):
    return [[[value for _ in range(c)] for _ in range(b)] for _ in range(a)]

array = create_array(3, 4, 5, 1)
for layer in array:
    for row in layer:
        print(row)
    print()