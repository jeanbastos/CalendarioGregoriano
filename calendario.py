#Este diccionario se usa para saber cuandos días tiene cada mes del año
diasXMes =  {'1' : 31, '2' : 28, '3'  : 31 , '4'  : 30 , '5' : 31 , '6' : 30 , '7' : 31 , '8' : 31 , '9' : 30 , '10' : 31 , '11' : 30 , '12' : 31}


def menu():
    print("1: fecha_es_tupla")
    print("2: bisiesto")
    print("7: salir")
    opcion = input('Seleccione una opción: ')

    if(opcion == '1'):
        opcion = input('Ingrese la fecha en formato yyyy,mm,dd: ')
        valores = opcion.split(',')
        print(fecha_es_tupla(int(valores[0]),int(valores[1]),int(valores[2])))
        menu()
    elif(opcion == '2'):
        opcion = input('Ingrese el año en formato yyyy: ')
        print(bisiesto(int(opcion)))
        menu()
    
    elif(opcion == '7'):
        print("Fin del programa")
    else:
        menu()

#Recibe un año en el formato yyyy y retorna si es bisiesto o no
#El algoritmo utiliza el módulo para comprobar si es divisible entre 400
#Sino comprueba si es divisible entre 4 y no entre 100
def bisiesto(anho):
    if(anho%400 == 0):
        return(True)
    elif(anho%4 == 0 and anho%100 != 0):
        return(True)
    return(False)

#La siguiente función comprueba que el año sea igual o superior a la entrada en vigencia del calendario gregoriano
#Comprueba que el mes se encuentre entre 1 y 12
#Posteriormente con un diccionario comprueba si el día se encuentra entre la cantidad de días de cada mes
def fecha_es_tupla(anho, mes, dia):
    if(anho < 1582):
        return(False)
    elif(mes < 1 or mes > 12):
        return(False)
    elif(bisiesto(anho) and mes == 2):
        if(dia < 1 or dia > diasXMes[str(mes)]+1):
            return False
    elif(dia < 1 or dia > diasXMes[str(mes)]):
        return(False)        
    return(True)

menu()