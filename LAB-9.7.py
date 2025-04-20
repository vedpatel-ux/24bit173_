def ispalindrome(str):
    x= str
    y = x[::-1]
    return str == y

n = input("Enter a name :")
print(ispalindrome(n))