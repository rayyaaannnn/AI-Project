a = 500

q = int(input("Enter Marks Obtained in Physics: "))
w = int(input("Enter Marks Obtained in Chemistry: "))
e = int(input("Enter Marks Obtained in Biology: "))
r = int(input("Enter Marks Obtained in Mathamatics: "))
t = int(input("Enter Marks Obtained in Computer: "))

y = q+w+e+r+t

Percentage = y/a*100

print("Total Marks Obtained: ",y)
print ("Your Percentage is: ",Percentage,"%")

if  Percentage >= 90:
    print("Grade A")
elif Percentage >= 80:
    print("Grade B")
elif Percentage >= 70:
    print("Grade C")
elif Percentage >= 60:
    print("Grade D")
elif Percentage >= 40:
    print("Grade E")
elif Percentage < 40:
    print("Grade F")