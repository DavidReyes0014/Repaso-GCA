#Está trabajando en el departamento informática del Supermercado la Antorcha,  le solicitan que elabore el sistema de facturación de la caja rápida. En la cual 
#se puede facturar un máximo de 5 productos por cliente, y para todas aquellas compras superiores 500 Lps. se le aplicara un descuento del 10%, y aquellas 
#compras menores a 500 Lps. no recibirán ningún tipo de descuento. Al momento de facturar deberá de solicitar el Nombre del Cliente, el Numero de Identidad 
#del Cliente, solicitar el precio de cada uno de los cinco productos. A lo largo del proceso de los datos deberá calcular, el precio total, mediante sumar el impuesto
#(15%), el subtotal, y restando el descuento. 


#Solicitud de Datos
nombre = input("Ingrese su Nombre Completo: ")
dni = input("Ingrese su Numero de Identidad: ")

producto1 = float(input("Ingrese el costo del primer producto: "))
producto2 = float(input("Ingrese el costo del segundo producto: "))
producto3 = float(input("Ingrese el costo del tercer producto: "))
producto4 = float(input("Ingrese el costo del cuarto producto: "))
producto5 = float(input("Ingrese el costo del quinto producto:"))

#Proceso de Datos 
subtotal= float(producto1+producto2+producto3+producto4+producto5)
impuesto = float(subtotal * 0.15)

if subtotal >= 500: #Condicionante subtotal mayor a 500 Lps. 
    descuento = float(subtotal * 0.10)
else: #condicionante todas aquellos subtotales menores a 500 Lps. 
    descuento= float(0)

total_pagar = float(subtotal+impuesto-descuento)

#Salida de Datos
print("============================================")
print("Supermercados la Antorcha")
print("Nombre del Cliente: ", nombre)
print("Numero de Identidad del Cliente: ", dni)
print(f"Precio Producto 1 : ", producto1, " Lps.") # la funcion (f"texto", varaible "texto") se utiliza para transformar todas aquellas varibales int o float
print(f"Precio Producto 2 : ", producto2, " Lps.") # en str (strings) par poder realizar el print de forma correcta. 
print(f"Precio Producto 3 : ", producto3, " Lps.")
print(f"Precio Producto 4 : ", producto4, " Lps.")
print(f"Precio Producto 5 : ", producto5, " Lps.")
print(f"Subtotal : ", subtotal, " Lps.")
print(f"Impuesto: ", impuesto, " Lps.")
print(f"Descuento: ", descuento, " Lps.")
print(f"Total a Pagar: ", total_pagar, " Lps.")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")