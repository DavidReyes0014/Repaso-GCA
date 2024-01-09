
#Trabaja en el departamento de IT de una tienda de botellones de agua que se especializa en la venta de 
#botellones de agua de 5 galones. Le solicitan que haga un algoritmo que sea capaz de consultar al cliente 
#sus datos personales y consultar cuantos botellones desea compra y proveer el total a pagar (considerando 
#que el precio unitario de los botellones es de 38 Lps.). Los datos que debe de solicitar al cliente son 
#los siguientes: Nombre, Apellido, Genero, Lugar de Residencia, Cantidad de Botellones, y Total a Pagar 
#(El cual debe de ser calculado mediante la solicitud de la cantidad de botellones que desea ).  Debe 
#reflejar la información al final del algoritmo.

# Obtener entrada del usuario
Nombre = input("Escriba su nombre: ")
Apellido = input("Escriba su apellido: ")
Genero = input("Escriba su género: ")
Lugar_de_Residencia = input("Escriba su lugar de residencia: ")
Cantidad_de_Botellones = int(input("¿Cuántos botellones de agua desea?"))

# Realizar cálculos
multiplicacion = Cantidad_de_Botellones * 38

# Mostrar la información del usuario
print("Su nombre es", Nombre)
print("Su apellido es", Apellido)
print("Su género es", Genero)
print("Su lugar de residencia es", Lugar_de_Residencia)
print("Cantidad de botellones:", Cantidad_de_Botellones)
print("El total a pagar es: Lps.", multiplicacion)