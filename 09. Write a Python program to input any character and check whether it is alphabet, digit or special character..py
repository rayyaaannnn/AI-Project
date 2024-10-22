alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
numbers = '1234567890'
symbols = '!@#$%^&*()_+-={}:<>?'

a =  input("Enter any Character: ")

if a in alphabets:
    print(a,"is an Alphabet.")
elif a in numbers:
    print(a,"is a Number.")
elif a in symbols:
    print(a,"is a Symbol.")
    