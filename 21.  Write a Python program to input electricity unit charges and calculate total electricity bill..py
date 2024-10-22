a = int(input("Enter Electricity Units: "))

if a <=50:
    Base_Amount = a*0.50
    Additional_Surcharge = (Base_Amount*20/100)
    print("Base Amount: Rs.",Base_Amount)
    print("Additional Surcharge: Rs.",Additional_Surcharge)
    print("Total Electricity Bill: Rs.",Base_Amount+Additional_Surcharge)
elif a >50 and  a <=150:
    Base_Amount = (25)+(a-50)*0.75
    Additional_Surcharge = (Base_Amount*20/100)
    print("Base Amount: Rs.",Base_Amount)
    print("Additional Surcharge: Rs.",Additional_Surcharge)
    print("Total Electricity Bill: Rs.",Base_Amount+Additional_Surcharge)
elif a >150 and a <=250:
    Base_Amount = (100)+(a-150)*1.20
    Additional_Surcharge = (Base_Amount*20/100)
    print("Base Amount: Rs.",Base_Amount)
    print("Additional Surcharge: Rs.",Additional_Surcharge)
    print("Total Electricity Bill: Rs.",Base_Amount+Additional_Surcharge)
elif a >250:
    Base_Amount = (220)+(a-250)*1.50
    Additional_Surcharge = (Base_Amount*20/100)
    print("Base Amount: Rs.",Base_Amount)
    print("Additional Surcharge: Rs.",Additional_Surcharge)
    print("Total Electricity Bill: Rs.",Base_Amount+Additional_Surcharge)