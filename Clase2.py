#Implementar una clase llamada ALumno que tenga como atributos su nombre y su nota.
#luego definir los metodos para inicializar sus atributos,
#imprimirlo y mostrar un mensaje si esta reglar (nota mayor o igual a 4)

class Alumno:
    def inicializar(self, nomb, nota):
        self.nombre = nomb
        self.nota = nota
    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Nota:", self.nota)
    def mostrar_estado(self):
        if self.nota >= 4:
            print("El alumno está regular.")
        else:
            print("El alumno no está regular.")
            
#bloque de codigos para probar la clase
alumno1 = Alumno() #instanciamos la clase
alumno1.inicializar("Juan", 5) #inicializamos los atributos nombre y nota
alumno1.imprimir() #imprimimos los atributos nombre y nota
alumno1.mostrar_estado() #mostramos el estado del alumno

alumno2 = Alumno() #instanciamos la clase
alumno2.inicializar("Maria", 3) #inicializamos los atributos nombre y nota
alumno2.imprimir() #imprimimos los atributos nombre y nota