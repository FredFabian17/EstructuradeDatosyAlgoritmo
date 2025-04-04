#Confeccionar una clas que represente un empleado. Definir como atributos su nombre y su sueldo.
#en el metodo __init__ cargar los atributos por teclado y luego en otro metodo imprimir sus datos
#y por ultimo uno que imprima un mensaje si debe pagar impuesto (si el sueldo supera los $3000).ad

class Empleado:
    def __init__(self):
        self.nombre = input("Ingrese el nombre del empleado: ")
        self.sueldo = float(input("Ingrese el sueldo del empleado: "))

    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Sueldo:", self.sueldo)

    def pagar_impuesto(self):
        if self.sueldo > 3000:
            print("El empleado debe pagar impuesto.")
        else:
            print("El empleado no debe pagar impuesto.")
            
#bloque de codigos para probar la clase
empleado1 = Empleado() #instanciamos la clase
empleado1.imprimir() #inicializamos los atributos nombre y sueldo
empleado1.pagar_impuesto() #mostramos el estado del empleado
