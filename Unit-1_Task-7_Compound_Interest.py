principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual rate of interest (%): "))
time = float(input("Enter time in years: "))

amount = principal * (1 + rate / 100) ** time
compound_interest = amount - principal

print("Total Amount =", amount)
print("Compound Interest =", compound_interest)
