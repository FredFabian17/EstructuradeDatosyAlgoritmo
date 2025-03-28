# Vamos a ingresar el ingreso anual y calcular el impuesto a pagar
# Según la escala anual proporcionada

income_monthly = float(input("Introduce el ingreso mensual en RD$: "))
income_annual = income_monthly * 12  # Convertir ingreso mensual a anual

if income_annual <= 416220:
    tax = 0  # Exento
elif income_annual <= 624329:
    tax = (income_annual - 416220) * 0.15
elif income_annual <= 867123:
    tax = 31216 + (income_annual - 624329) * 0.20
else:
    tax = 79776 + (income_annual - 867123) * 0.25

monthly_tax = tax / 12  # Dividir el impuesto anual entre 12 para obtener el mensual
SFS = income_annual * 0.0304  # Calcular el SFS (3% del ingreso anual)
AFP = income_annual * 0.0287  # Calcular el AFP (2.87% del ingreso anual)
monthly_tax2 = income_monthly * 0.0469409  # Calcular el impuesto mensual (4.69409% del ingreso mensual)
print("-----------------------------------")
print("Tus ingresos anuales son: RD$", "{:,.2f}".format(income_annual))
print("-----------------------------------")
print("Tu pago diario es de: RD$", "{:,.2f}".format(income_monthly / 23.83))  # Suponiendo 23.83 días al mes
print("-----------------------------------")
print ("tu descuento de SFS mensual de: RD$", "{:,.2f}".format(SFS / 12))  # Dividir el SFS anual entre 12 para obtener el mensual
print("lo que hace un total anual de: RD$", "{:,.2f}".format(SFS))
print("-----------------------------------")
print("tu descuento de AFP mensual de: RD$", "{:,.2f}".format(AFP / 12))  # Dividir el AFP anual entre 12 para obtener el mensual
print("lo que hace un total anual de: RD$", "{:,.2f}".format(AFP))
print("-----------------------------------")   
print("-----------------------------------")    
print("Tu pagas un impuesto mensual de: RD$", "{:,.2f}".format(monthly_tax2))  # Dividir el impuesto anual entre 12 para obtener el mensual
print("-----------------------------------")
print("-----------------------------------")
print("te van a pagar una bonificacion por 60 dias de: RD$", "{:,.2f}".format((income_monthly / 23.83) * 60))  # Dividir el impuesto anual entre 12 para obtener el mensual   
print("-----------------------------------")    
print("tomando en cuenta que a esto hay que cobrarle el 25% de impuestos")
print("lo que hace un total de: RD$", "{:,.2f}".format(((income_monthly / 23.83) * 60) * 0.25))  # Dividir el impuesto anual entre 12 para obtener el mensual
print("Te pagaran un total de: RD$", "{:,.2f}".format(((income_monthly / 23.83) * 60) - (((income_monthly / 23.83) * 60) * 0.25)))  # Dividir el impuesto anual entre 12 para obtener el mensual    
print("-----------------------------------")






#print("El impuesto mensual es: RD$", "{:,.2f}".format(monthly_tax))


#print("El impuesto total anual es: RD$", "{:,.2f}".format(tax))
#print("-----------------------------------")