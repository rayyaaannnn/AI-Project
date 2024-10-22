basic_salary = float(input("Enter Basic Salary: "))

if basic_salary <= 10000:
    HRA = basic_salary*(20/100)
    DA = basic_salary*(80/100)
    print("Basic Salary is: ",basic_salary)
    print("House Rental Allowance: ",HRA)
    print("Dearness Allowance: ",DA)
    print("Total Salary: ",basic_salary+HRA+DA)

elif basic_salary <= 20000:
    HRA = basic_salary*(25/100)
    DA = basic_salary*(90/100)
    print("Basic Salary is: ",basic_salary)
    print("House Rental Allowance: ",HRA)
    print("Dearness Allowance: ",DA)
    print("Total Salary: ",basic_salary+HRA+DA)

elif basic_salary > 20000:
    HRA = basic_salary*(30/100)
    DA = basic_salary*(95/100)
    print("Basic Salary is: ",basic_salary)
    print("House Rental Allowance: ",HRA)
    print("Dearness Allowance: ",DA)
    print("Total Salary: ",basic_salary+HRA+DA)
