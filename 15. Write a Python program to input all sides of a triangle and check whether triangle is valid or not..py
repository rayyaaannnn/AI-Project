side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Check if sides are positive
if side1 <= 0 or side2 <= 0 or side3 <= 0:
    print("Sides must be positive numbers.")
else:
    if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
        print("The triangle is valid.")
    else:
        print("The triangle is not valid.")