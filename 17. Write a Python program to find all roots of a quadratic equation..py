a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

if a == 0:
    print("Coefficient 'a' cannot be zero.")
else:
    d = b**2 - 4*a*c
    if d > 0:
        print(f"Roots are real and distinct: {(-b + d**0.5) / (2*a)} and {(-b - d**0.5) / (2*a)}")
    elif d == 0:
        print(f"Root is real and repeated: {-b / (2*a)}")
    else:
        print(f"Roots are complex: {-b / (2*a)} + {(-d)**0.5 / (2*a)}i and {-b / (2*a)} - {(-d)**0.5 / (2*a)}i")