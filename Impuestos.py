# Vamos a ingresar el ingreso anual y calcular el impuesto a pagar
# Según la escala anual proporcionada

income = float(input("Introduce el ingreso mensual: ")) * 12  # Convertir ingreso mensual a anual

if income <= 416220:
    tax = 0  # Exento
elif income <= 624329:
    tax = (income - 416220) * 0.15
elif income <= 867123:
    tax = 31216 + (income - 624329) * 0.20
else:
    tax = 79776 + (income - 867123) * 0.25

monthly_tax = tax / 24  # Dividir el impuesto entre 24
annual_tax = monthly_tax * 12  # Calcular el impuesto total anual

print("El impuesto total anual es: ", round(annual_tax, 2))
print("El impuesto mensual es: ", round(monthly_tax, 2))