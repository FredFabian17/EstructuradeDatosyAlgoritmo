#Implementaremos una clase llamada Persona que tendrá como atributo (variable) su nombre
#y dos metodos (funiones), uno de dichos metodos inicializará
#el atributo nombre y el siguiente metodo mostrará en pantalla el contenido del mismo

class Persona:
    def inicializar (self, nomb):
        self.nombre = nomb
    
    def imprimir (self):
        print("Nombre:", self.nombre)
        
#bloque de codigos para probar la clase

print ("Ingresa un Nombre:")
print ("yo ingresare Maria y tu ingresaras el tuyo")
print ("Presiona Enter cuando hayas terminado")
#imprimimos un mensaje para que el usuario ingrese su nombre
persona1 = Persona() #instanciamos la clase
persona1.inicializar(input()) #inicializamos el atributo nombre
persona1.imprimir() #imprimimos el atributo nombre


persona2 = Persona() #instanciamos la clase
persona2.inicializar("Maria") #inicializamos el atributo nombre
persona2.imprimir() #imprimimos el atributo nombre
