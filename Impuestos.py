income = float (input("introduce el ingreso anual: "))
if income <= 85528:
    tax = income * 0.18 - 556.2
else:
    tax = 14839.02 + (income - 85528) * 0.32
if tax < 0:
    tax = 0
print("El impuesto es: ", tax)