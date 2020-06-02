from datetime import datetime

#Este diccionario se usa para saber cuandos días tiene cada mes del año
diasXMes =  {'1' : 31, '2' : 28, '3'  : 31 , '4'  : 30 , '5' : 31 , '6' : 30 , '7' : 31 , '8' : 31 , '9' : 30 , '10' : 31 , '11' : 30 , '12' : 31}


def menu():
    print("0: fecha_es_tupla")
    print("1: bisiesto")
    print("3: dia_siguiente")
    print("4: dias_transcurridos")
    print("5: fecha_hoy")
    print("7: salir")

    opcion = input('Seleccione una opción: ')
    
    #Fecha_es_tupla
    if(opcion == '0'):
        opcion = input('Ingrese la fecha en formato yyyy,mm,dd: ')
        valores = opcion.split(',')
        print(fecha_es_tupla(int(valores[0]),int(valores[1]),int(valores[2])))
        menu()
    
    #Bisiesto
    elif(opcion == '1'):
        opcion = input('Ingrese el año en formato yyyy: ')
        print(bisiesto(int(opcion)))
        menu()

    #Dia_siguente
    elif(opcion == '3'):
        opcion = input('Ingrese la fecha en formato yyyy,mm,dd: ')
        valores = opcion.split(',')
        print("\n",dia_siguiente(int(valores[0]),int(valores[1]),int(valores[2])),"\n")
        
        menu()
    
    #Dias_desde_primero_enero
    elif(opcion == '4'):
        opcion = input('Ingrese la fecha en formato yyy,mm,dd: ')
        valores = opcion.split(',')
        dias_transcurridos(int(valores[0]),int(valores[1]),int(valores[2]))
        menu()

    #Fecha_hoy    
    elif(opcion == '5'):
        anho = int(datetime.now().strftime("%Y")) #Obtiene el anho de la fecha actual y lo castea a entero para futuros usos
        mes = int(datetime.now().strftime("%m"))#Obtiene el mes de la fecha actual y lo castea a entero para futuros usos
        dia = int(datetime.now().strftime("%d"))#Obtiene el dia de la fecha actual y lo castea a entero para futuros usos
        hoy = (anho,mes,dia)                    #tupla con la fecha completa
        print("\n",hoy,"\n")
        menu()




##    elif(opcion == '6'):
##        opcion = input('Ingrese la fecha en formato yyy,mm,dd: ')
##        valores = opcion.split(',')
##        edad_hoy(anho, mes, dia)
##        menu()
    elif(opcion == '7'):
        print("Fin del programa")
    else:
        print("\nOpcion Invalida\n")
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

#Esta funcion se encarga de agregar un dia mas a la fecha de entrada.
def dia_siguiente(anho, mes, dia):
    
    #Valida si la fecha es correcta
    if(fecha_es_tupla(anho,mes,dia)):

        if(dia + 1 == 29 and bisiesto(anho) and mes == 2): #Caso especial del anno bisiesto y mes febrero
            return(anho, mes,dia+1)

        elif(dia + 1 > diasXMes[str(mes)]):
            dia = 1
            mes = mes + 1
            if(mes + 1 > 12):
                mes = 1
                anho = anho + 1

        else:
            dia = dia + 1
        return(anho,mes,dia)

    else:
        return("Fecha Incorrecta")







# Esta funcion determina la cantidad de días que han pasado desde el primero de enero del año ingresado.
# Es necesario saber el año ya que puede influir el hecho de que sea bisiesto o no.
def dias_transcurridos(anho, mes, dia):
    if(fecha_es_tupla(anho, mes, dia)):                             ## Primero es necesario verificar que la fecha ingresada sea válida en el calendario gregoriano.
        diasTranscurridos = dia - 1                                 ## Debido a que los días comienzan a contar a partir del 2 de enero (el 1 de enero da resultado 0), se le resta uno a la cantidad de días transcurridos.
        if(bisiesto(anho) and mes > 2):                             ## Luego se debe revisar si el año es bisiesto y el mes ingresado es mayor a 2 para sumar un día.
            diasTranscurridos += 1
        mes -= 1                                                    ## Como los días del mes ingresado ya se han contado, se le resta uno a la cantidad de meses.
        while(mes >= 1):                                            ## Finalmente, este while comenzará a sumar la cantidad de días de cada mes transcurrido.
            diasTranscurridos += diasXMes[str(mes)]
            mes -= 1
        print("\n Han pasado ", diasTranscurridos, " dias.\n")
    else:
        print("\n Debe ingresar una fecha válida para el calendario gregoriano.\n")

# Esta funcion va a retornar como resultado la cantidad de años, meses y días cumplidos al día de hoy, desde una fecha válida ingresada.
#def edad_hoy(anho, mes, dia):


menu()



































