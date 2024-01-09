
#Elabore un algorirmo que sea capaz de calcular la cantidad total a pagar de salario. Teniendo
#en cuenta que el precio de la hora regular trabajada es de 5.25 $, y el precio de la hora extra
#es de 7.25 $. El algoritmo debera de solicitar el nombre del empleado, el numero de empleado
#y consultar al empleado tanto las horas regulares trabajadas y las horas extras trabajadas, y
#dentro del algoritmo calcular cuanto se debera de pagar de horas regulares y horas extras, y
#y al finalizar decir cuanto es el total del salario. 

#Entrada de datos
nombre_del_empleado = input("Ingrese su nombre: ")
numero_del_empleado = int(input("Ingrese su ID de empleado:")) #definir las variables segun sus tipos int = numeros enteros 
numero_de_horas_trabajadas = int(input("Ingrese su cantidad de horas trabajadas: "))
numero_de_horas_trabajadas_extra = float(input("Ingrese su cantidad de horas extras trabajadas")) #float = numeros reales es decir puede tener decimales

#Proceso de Datos
salario_de_horas_trabajadas= (numero_de_horas_trabajadas_extra * 5.25)
salario_de_horas_trabajadas_extra= (numero_de_horas_trabajadas_extra * 7.50)
salario_general=(salario_de_horas_trabajadas + salario_de_horas_trabajadas_extra)

#Salida de Datos
print("Sistema de calculo de salario")
print("Nombre del empleado:", nombre_del_empleado)
print("Numero de empleado:", numero_del_empleado)
print("Cantidad de horas trabajadas:", numero_de_horas_trabajadas, "Valor de las horas trabajadas:", "$", salario_de_horas_trabajadas)
print("Cantidad de horas trabajadas extras:", numero_de_horas_trabajadas_extra, "Valor de las horas extras", "$", salario_de_horas_trabajadas_extra)
print("Salario a recibir del empleado es:", "$", salario_general)