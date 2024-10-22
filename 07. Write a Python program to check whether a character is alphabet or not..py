alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
char = input("Enter a character: ")

if char in alphabets:
    print(char,"is an alphabet.")
else:
    print(char,"is not an alphabet.")