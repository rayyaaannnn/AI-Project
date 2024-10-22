a = int(input("Enter any Number: "))
b = int(input("Enter any Number: "))
c = int(input("Enter any Number: "))

if a >= b and a >= c:
    print(a,"is the largest number.")
elif b >= a and b >= c:
    print(b,"is the largest number.")
elif  c >= a and c >= b:
    print(c,"is the largest number.")
