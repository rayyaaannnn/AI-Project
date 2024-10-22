cp = float(input("Enter the cost price: "))
sp = float(input("Enter the selling price: "))
    
if sp > cp:
        profit = sp - cp
        print("Profit: Rs.",profit)
elif sp < cp:
        loss = cp - sp
        print("Loss: Rs.",loss)
else:
        print("No profit, no loss.")