#compound intrest
principal=int(input("Enter the principal amount:"))
rate=int(input("Enter the rate of interest:"))
time=int(input("Enter the time period:"))
total=principal*(1+rate/100)**time
Compound_interest=total-principal
print("Compound interest:", Compound_interest)
