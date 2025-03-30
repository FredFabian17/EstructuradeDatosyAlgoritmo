import os

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
print(f"Su Ingreso mensual es de: RD$ {income_monthly:,.2f}")
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
print("Como indicaste que tienes", years, "años en la empresa")
print("-----------------------------------------------------------------------------------------------------------")
# calcular el Bono Vacacional
# si tienes menos de 1 año, el bono es de 0%
# si tienes entre 1 y 5 años, el bono es de 15%
# si tienes mas de 5 años, el bono es de 50%
# si tienes mas de 10 años, el bono es de 100%
def calculate_bono_vacacional(income_monthly, years):
    if years < 1:
        bono_vacacional = 0
    elif years <= 5:   
        bono_vacacional = (income_monthly * 15) / 100
    elif years <= 10:
        bono_vacacional = (income_monthly * 50) / 100
    else:
        bono_vacacional = (income_monthly * 100) / 100
    return bono_vacacional

bono_vacacional = calculate_bono_vacacional(income_monthly, years)
print(f"Tu bono vacacional es: RD$ {bono_vacacional:,.2f}")
print("-----------------------------------")


# Solicitar el bono de desempeño
bono_desempeno = float(input("Ingrese el monto del bono de desempeño en RD$: "))

# Calcular el ingreso total anual incluyendo todos los bonos
ingreso_total_anual = salario_cotizable_anual + bono + bono_vacacional + bono_desempeno
print("-----------------------------------")
print(f"El ingreso total anual (incluyendo bonos) es: RD$ {ingreso_total_anual:,.2f}")

# Recalcular el impuesto anual considerando el ingreso total
if ingreso_total_anual <= 416220:
    tax_total = 0  # Exento
elif ingreso_total_anual <= 624329:
    excedente = ingreso_total_anual - 416220
    tax_total = excedente * 0.15
elif ingreso_total_anual <= 867123:
    excedente = ingreso_total_anual - 624329
    tax_total = 31216 + (excedente * 0.20)
else:
    excedente = ingreso_total_anual - 867123
    tax_total = 79776 + (excedente * 0.25)

# Calcular el impuesto adicional pendiente por pagar debido a los bonos
impuesto_adicional = tax_total - tax

print("-----------------------------------")
print(f"El impuesto total anual (incluyendo bonos) es: RD$ {tax_total:,.2f}")
print(f"El impuesto adicional por los bonos es: RD$ {impuesto_adicional:,.2f}")
print("-----------------------------------")

# Dividir el impuesto adicional entre 12 para obtener el monto mensual adicional
impuesto_adicional_mensual = impuesto_adicional / 12
print(f"El impuesto adicional mensual por los bonos es: RD$ {impuesto_adicional_mensual:,.2f}")
print("-----------------------------------")
print("Resumen de Impuestos y Bonos")
from tabulate import tabulate

# Datos para la tabla
tabla_datos = [
    ["Salario Cotizable Anual", f"RD$ {salario_cotizable_anual:,.2f}"],
    ["Bono de Ley 87", f"RD$ {bono:,.2f}"],
    ["Bono Vacacional", f"RD$ {bono_vacacional:,.2f}"],
    ["Bono de Desempeño", f"RD$ {bono_desempeno:,.2f}"],
    ["Ingreso Total Anual (incluyendo bonos)", f"RD$ {ingreso_total_anual:,.2f}"],
    ["Impuesto Total Anual (sin bonos)", f"RD$ {tax:,.2f}"],
    ["Impuesto Total Anual (con bonos)", f"RD$ {tax_total:,.2f}"],
    ["Impuesto Adicional por Bonos", f"RD$ {impuesto_adicional:,.2f}"],
    ["Impuesto Adicional Mensual", f"RD$ {impuesto_adicional_mensual:,.2f}"]
]

# Imprimir la tabla
print(tabulate(tabla_datos, headers=["Concepto", "Monto"], tablefmt="grid"))
print("-----------------------------------")
print("-----------------------------------------------------------------------------------------------------------")
print("Gracias por usar el programa de cálculo de impuestos y bonos.")

os.system("pause")

