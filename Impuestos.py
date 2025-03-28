# Vamos a ingresar el ingreso mensual y calcular el ISR Anual y Mensual
# Según la escala anual proporcionada

income_monthly = float(input("Ingrese su ingreso mensual en RD$: "))

# Calcular AFP y SFS
AFP = income_monthly * 0.0287  # 2.87%
SFS = income_monthly * 0.0304  # 3.04%

# Calcular salario cotizable mensual y anual
salario_cotizable_mensual = income_monthly - AFP - SFS
salario_cotizable_anual = salario_cotizable_mensual * 12

print("-----------------------------------")
print(f"Su ingreso mensual es de: RD$ {income_monthly:,.2f}")
print(f"El descuento por AFP (2.87%) es: RD$ {AFP:,.2f}")
print(f"El descuento por SFS (3.04%) es: RD$ {SFS:,.2f}")
print(f"Su salario cotizable mensual es de: RD$ {salario_cotizable_mensual:,.2f}")
print(f"Su salario cotizable anual es de: RD$ {salario_cotizable_anual:,.2f}")
print("-----------------------------------")

# Definimos las escalas de ISR según la ley 253-12
print("Tabla de cálculo del ISR:")
print("Escala Anual (RD$)                     | Tasa (%) | Excedente (RD$) | Impuesto (RD$)")
print("------------------------------------------------------------------------------------")

if salario_cotizable_anual <= 416220:
    tax = 0  # Exento
    print(f"Hasta RD$416,220.00                   | Exento   | 0.00            | 0.00")
elif salario_cotizable_anual <= 624329:
    excedente = salario_cotizable_anual - 416220
    tax = excedente * 0.15
    print(f"De RD$416,221.00 a RD$624,329.00      | 15%      | {excedente:,.2f}      | {tax:,.2f}")
elif salario_cotizable_anual <= 867123:
    excedente = salario_cotizable_anual - 624329
    tax = 31216 + (excedente * 0.20)
    print(f"De RD$624,330.00 a RD$867,123.00      | 20%      | {excedente:,.2f}      | {tax:,.2f}")
else:
    excedente = salario_cotizable_anual - 867123
    tax = 79776 + (excedente * 0.25)
    print(f"De RD$867,124.00 en adelante          | 25%      | {excedente:,.2f}      | {tax:,.2f}")

# Dividir el impuesto anual entre 12 para obtener el mensual
monthly_tax = tax / 12

print("-----------------------------------")
print(f"El impuesto total anual es: RD$ {tax:,.2f}")
print(f"El impuesto mensual es: RD$ {monthly_tax:,.2f}")
print(f"El valor que pagas quincenal es: RD$ {monthly_tax / 2:,.2f}")


print("-----------------------------------------------------------------------------------------------------------")

# Calcular cuanto me saldra de bono de Ley 87
# ver cuantos años tienes en la empresa
# si tiene mas de 5 años, el bono es de 60 dias de salario
# si tiene entre 1 y 5 años, el bono es de 45 dias de salario

print("¿Cuantos años tienes en la empresa?")
years = int(input("Ingrese el número de años: "))
def calculate_bono(income_monthly, years):
    if years > 5:
        bono = (income_monthly * 60) / 23.83
    elif years >= 1:
        bono = (income_monthly * 45) / 23.83
    else:
        bono = 0
    return bono

# Calcular el bono
bono = calculate_bono(income_monthly, years)
print("-----------------------------------")
print(f"El bono de Ley 87 es: RD$ {bono:,.2f}")
print("-----------------------------------")
# Calcular el monto total que recibira el empleado
# El monto total es el ingreso mensual menos el impuesto mensual mas el bono
total = income_monthly - monthly_tax + bono
print(f"El monto total que recibira el empleado es: RD$ {total:,.2f}")
print("-----------------------------------")