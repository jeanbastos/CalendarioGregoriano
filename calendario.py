from datetime import date

#Este diccionario se usa para saber cuandos días tiene cada mes del año
diasXMes =  {'1' : 31, '2' : 28, '3'  : 31 , '4'  : 30 , '5' : 31 , '6' : 30 , '7' : 31 , '8' : 31 , '9' : 30 , '10' : 31 , '11' : 30 , '12' : 31}
#Este diccionario tiene el nombre asociado a un numero de mes
nombre_Mes = {1:'Enero', 2:'Febrero', 3:'Marzo', 4:'Abril', 5:'Mayo',6:'Junio',7:'Julio',8:'Agosto',9:'Setiembre',10:'Octubre',11:'Noviembre',12:'Diciembre'}

nombre_Dia = {0:'Domingo', 1:'Lunes', 2:'Martes', 3:'Miércoles', 4:'Jueves', 5:'Viernes', 6:'Sábado'}


#Esta función permite verificar que un valor ingresado corresponde a un integer.
def esEntero(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

#Recibe una fecha en formato (yyyy,mm,dd)
#Y la convierte a una tupla de 3 valores enteros
def parseDate(fecha):
    valores = fecha[1:][:-1]
    valores = valores.split(',')
    if(esEntero(valores[0]) and esEntero(valores[1]) and esEntero(valores[2])):
        return((int(valores[0]),int(valores[1]),int(valores[2])))
    else:
        return (False)

def menu():
    print("0: fecha_es_tupla")
    print("1: bisiesto")
    print("2: fecha_es_valida")
    print("3: dia_siguiente")
    print("4: dias_transcurridos")
    print("5: fecha_hoy")
    print("6: edad_hoy")
    print("7: dia_semana")
    print("8: imprimir_3x4")
    print("9: fecha_futura")
    print("10: dias_entre")
    print("11: salir")

    opcion = input('Seleccione una opción: ')
    
    #Fecha_es_tupla
    if(opcion == '0'):
        opcion = input('Ingrese la fecha en formato (yyyy,mm,dd): ')
        print("\n",fecha_es_tupla(parseDate(opcion)),"\n")
        menu()
    
    #Bisiesto
    elif(opcion == '1'):
        opcion = input('Ingrese el año en formato (yyyy): ')
        valores = opcion[1:][:-1]
        print("\n",bisiesto((int(valores))),"\n")
        menu()

    #Fecha_es_valida
    if(opcion == '2'):
        opcion = input('Ingrese la fecha en formato (yyyy,mm,dd): ')
        print("\n",fecha_es_valida(parseDate(opcion)),"\n")
        menu()

    #Dia_siguente
    elif(opcion == '3'):
        opcion = input('Ingrese la fecha en formato (yyyy,mm,dd): ')
        print("\n",dia_siguiente(parseDate(opcion)),"\n")        
        menu()
    
    #Dias_desde_primero_enero
    elif(opcion == '4'):
        opcion = input('Ingrese la fecha en formato (yyyy,mm,dd): ')
        if(parseDate(opcion)):
            print(dias_transcurridos(parseDate(opcion)),"\n") 
        else:
            print("\nDebe ingresar una fecha válida\n") 
        menu()

    #Fecha_hoy    
    elif(opcion == '5'):
        anho = int(date.today().strftime("%Y")) #Obtiene el anho de la fecha actual y lo castea a entero para futuros usos
        mes = int(date.today().strftime("%m"))#Obtiene el mes de la fecha actual y lo castea a entero para futuros usos
        dia = int(date.today().strftime("%d"))#Obtiene el dia de la fecha actual y lo castea a entero para futuros usos
        hoy = (anho,mes,dia)                    #tupla con la fecha completa
        print("\n",hoy,"\n")
        menu()

    elif(opcion == '6'):
        opcion = input('Ingrese la fecha en formato (yyyy,mm,dd): ')
        edad_hoy(parseDate(opcion))
        menu()

    elif(opcion == '7'):
        opcion = input('Ingrese la fecha en formato (yyyy,mm,dd): ')
        result = dia_semana(parseDate(opcion))
        if(result == False):
            print("\n La fecha ingresada es inválida\n")
        else:  
            print("\n",nombre_Dia[dia_semana(parseDate(opcion))],"\n")
        menu()

    elif(opcion == '8'):

        opcion = input('Ingrese el año en formato (yyyy): ')
        valores = opcion[1:][:-1]
        imprimir_3x4(int(valores))

        menu()

    elif(opcion == '9'):
        opcion = input('Ingrese la fecha en formato (yyyy,mm,dd): ')
        cantidad_dias = input('Ingrese un número entero positivo: ')
        if(esEntero(cantidad_dias)):
            fecha_futura(parseDate(opcion), int(cantidad_dias))
        else:
            print("Debe ingresar un número entero positivo.")
        menu()

    elif(opcion == '10'):
         f1 = input('Ingrese la primera fecha en formato (yyyy,mm,dd): ')
         f2 = input('Ingrese la segunda fecha en formato (yyyy,mm,dd): ')
         dias_entre(parseDate(f1), parseDate(f2))
         menu()

    elif(opcion == '11'):
        print("\nFin del programa")
        exit(0)
    else:
        print("\nOpcion Invalida\n")
        menu()

def fecha_es_tupla(fecha):
    if(fecha == False):
        return(False)
    if(fecha[0]<0):
        return(False)
    elif(fecha[1]<1 or fecha[1]>12):
        return(False)
    elif(fecha[2]<1 or fecha[2]>31):
        return(False)
    return(True)
    

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
def fecha_es_valida(fecha):
    if(fecha_es_tupla(fecha) == False):
        return(False)
    if(fecha[0] < 1582):
        return(False)
    elif(fecha[1] < 1 or fecha[1] > 12):
        return(False)
    elif(bisiesto(fecha[0]) and fecha[1] == 2):
        if(fecha[2] < 1 or fecha[2] > diasXMes[str(fecha[1])]+1):
            return False
    elif(fecha[2] < 1 or fecha[2] > diasXMes[str(fecha[1])]):
        return(False)        
    return(True)

#Esta funcion se encarga de agregar un dia mas a la fecha de entrada.
def dia_siguiente(fecha):

    #Valida si la fecha es correcta
    if(fecha_es_tupla(fecha)):
        anho = fecha[0]
        mes = fecha[1]
        dia = fecha[2]

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
        return("\nFecha Incorrecta\n")
    
# Esta funcion determina la cantidad de días que han pasado desde el primero de enero del año ingresado.
# Es necesario saber el año ya que puede influir el hecho de que sea bisiesto o no.
def dias_transcurridos(fecha):
    if(fecha_es_valida(fecha)):                                     ## Primero es necesario verificar que la fecha ingresada sea válida en el calendario gregoriano.
        anho = fecha[0]
        mes = fecha[1]
        dia = fecha[2]
        diasTranscurridos = dia - 1                                 ## Debido a que los días comienzan a contar a partir del 2 de enero (el 1 de enero da resultado 0), se le resta uno a la cantidad de días transcurridos.
        if(bisiesto(anho) and mes > 2):                             ## Luego se debe revisar si el año es bisiesto y el mes ingresado es mayor a 2 para sumar un día.
            diasTranscurridos += 1
        mes -= 1                                                    ## Como los días del mes ingresado ya se han contado, se le resta uno a la cantidad de meses.
        while(mes >= 1):                                            ## Finalmente, este while comenzará a sumar la cantidad de días de cada mes transcurrido.
            diasTranscurridos += diasXMes[str(mes)]
            mes -= 1
        print("\n Han pasado ", diasTranscurridos, " dias.\n")
        return diasTranscurridos
    else:
        print("\n Debe ingresar una fecha válida para el calendario gregoriano.\n")
        return

# Esta funcion va a retornar como resultado la cantidad de años, meses y días cumplidos al día de hoy, desde una fecha válida ingresada.
def edad_hoy(fecha):
    if(fecha_es_valida(fecha)):                                 ## En primer lugar se debe validar la fecha ingresada, luego, en caso de serlo, se obtiene la fecha actual.     
        anho = fecha[0]
        mes = fecha[1]
        dia = fecha[2]
        hoy = (int(date.today().strftime("%Y")),int(date.today().strftime("%m")),int(date.today().strftime("%d")))
        if(mes < hoy[1]):                                       ## Para obtener el tiempo de forma acertada, se optó por validar si el mes ingresado es mayor, menor o igual al mes actual.
            anhos = hoy[0] - anho
            if(dia <= hoy[2]):                                  ## Luego de realizar esa validación, se debe validar si el día es mayor, menor o igual al actual.
                meses = hoy[1] - mes
                dias = hoy[2] - dia
                print("\n Han pasado ", anhos, " años, ", meses, " meses y ", dias, " dias desde la fecha ingresada.\n")
                edad =(anhos, meses, dias)
                return edad
            else:
                meses = hoy[1] - mes - 1
                dias = hoy[2] + diasXMes[str(mes)] - dia
                print("\n Han pasado ", anhos, " años, ", meses, " meses y ", dias, " dias desde la fecha ingresada.\n")
                edad =(anhos, meses, dias)
                return edad
        elif(mes> hoy[1]):
            anhos = hoy[0] - anho - 1
            if(dia <= hoy[2]):
                meses = 12 - (mes - hoy[1])
                dias = hoy[2] - dia
                print("\n Han pasado ", anhos, " años, ", meses, " meses y ", dias, " dias desde la fecha ingresada.\n")
                edad =(anhos, meses, dias)
                return edad
            else:
                meses = 12 - (mes - hoy[1]) - 1
                dias = hoy[2] + diasXMes[str(mes)] - dia
                print("\n Han pasado ", anhos, " años, ", meses, " meses y ", dias, " dias desde la fecha ingresada.\n")
                edad =(anhos, meses, dias)
                return edad
        else:
            if(dia <= hoy[2]):
                anhos = hoy[0] - anho
                meses = hoy[1] - mes
                dias = hoy[2] - dia
                print("\n Han pasado ", anhos, " años, ", meses, " meses y ", dias, " dias desde la fecha ingresada.\n")
                edad =(anhos, meses, dias)
                return edad
            else:
                anhos = hoy[0] - anho - 1
                meses = 12 - (mes - hoy[1]) - 1
                dias = hoy[2] + diasXMes[str(mes)] - dia
                print("\n Han pasado ", anhos, " años, ", meses, " meses y ", dias, " dias desde la fecha ingresada.\n")
                edad =(anhos, meses, dias)
                return edad
    else:
        print("\n Debe ingresar una fecha válida para el calendario gregoriano.\n")

#Retorna el numero de día de la semana, tomando 0 como domingo
#El algoritmo utilizado es el siguiente:
#d=((A-1)%7+((A-1)/4-(3*((A-1)/100+1)/4))%7+DM%7+D%7)%7
#donde A = año, DM = días transcurridos antes del primer día del mes
#D = día
def dia_semana(fecha):
    if(fecha_es_valida(fecha)):
        a = fecha[0]
        m = fecha[1]
        d = fecha[2]
        #Módulos acumulados por mes para años regulares y años bisiestos
        constanteMes = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]
        constanteMesBisiesto = [0, 3, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6]
        if(bisiesto(a)): #
            m = constanteMesBisiesto[m-1]
        else:
            m = constanteMes[m-1]
        return int(((a-1)%7 + round(((a-1)/4-(3*((a-1)/100+1)/4))%7,0) + m + d%7)%7)
    else:
        return(False)

#Imprime el anno completo
def imprimir_3x4(anho):

    if(anho < 1582):
        print("\nAño incorrecto\n")
    else:
        print("\nCalendario del año %s D.C." % anho)
        fila(1,5,anho)
        fila(5,9,anho)
        fila(9,13,anho)

    return    


# Imprime las filas del calendario
def fila(i,f,anho):
    calendario =""
    for x in range (0,8):  #Filas del mes
        for j in range (i,f): #Columnas del calendario
            dia = dia_semana((anho,j,1))
            calendario += get_mes(dia, j, anho)[x] + "\t"
        calendario += "\n"
    print (calendario)
    return

# Esta funcion retorna el calendario de una fecha dada
def get_mes(dia,num_mes,anho):

    mes = ""
    contador = 1
    dia_inicio = dia #Es el dia en el que inicia el mes
    dia2 = 1
    mes += nombre_Mes[num_mes].center(28," ") + "|#"
    mes += ( ' D   L   K   M   J   V   S  |#')
    dia_mes = diasXMes[str(num_mes)]
    if(bisiesto(anho) and num_mes == 2):
        dia_mes = 29

    for dia in range(1,dia_mes+1+dia_inicio):
        
        if(dia2 > 7):
            mes += "|#"
            dia2 = 1
        dia2 += 1

        if(dia > dia_inicio):
            if(contador < 10):
                mes += " "+str(contador) + "  "
            else:
                mes += str(contador) + "  "
            contador += 1
        else:
            mes += '  ' + "  "
    result = mes.split('#')

    if (len(result) < 8):
        result.append('                            |')

    for j in range (0,8):
        
        for x in range (0,28):
            if (len(result[j]) < 28):
                result[j] += " "

        if '|' not in result[j]:
            result[j] += '|'
       
    return result


## La siguiente funcion determina una fecha a partir de una fecha y un número entero dados.
def fecha_futura(fecha, dias):
    if(fecha_es_valida(fecha) and dias >= 0):                               ## En primer lugar se debe validar la fecha ingresada y que el número sea entero mayor o igual a cero.
        anho = fecha[0]
        mes = fecha[1]
        dia = fecha[2]
        while(dias > 0):                                                    ## Se inicia un ciclo para realizar la suma de los días.
            if(bisiesto(anho) and mes == 2 and dia < 29):                   ## Se debe revisar si el año actual es bisiesto, para asegurarnos de que llegue a 29 días.
                dia += 1
            elif(dia < diasXMes[str(mes)]):                                 ## Si el día actual no es el último del mes, se suma uno al dia.
                dia += 1
            elif(bisiesto(anho) and mes == 2 and dia == 29):                ## Se debe revisar si el año actual es bisiesto, para realizar la suma correspondiente en el mes de febrero.
                mes = 3
                dia = 1
            elif(dia == diasXMes[str(mes)] and mes < 12):                   ## Si el día es el último del mes y no es Diciembre, se suma uno al mes y se devuelve la cantidad de días a 1.
                mes += 1
                dia = 1
            elif(dia == diasXMes[str(mes)] and mes == 12):                  ## Si el día es el último del mes y es Diciembre, se devuelve el mes y día a 1 y se aumenta el año en 1.
                anho += 1
                mes = 1
                dia = 1
            dias -= 1
        print("\n La fecha final es ", anho, "/", mes, "/", dia, ".\n")
        fecha = (anho, mes, dia)
        return fecha
    else:
        print("\n Debe ingresar una fecha válida.\n")
        return

## La siguiente es una funcion complementaria para saber cual, de dos fechas válidas ingresadas, es la "menor".

def fecha_menor(f1,f2):
    if(f1[0] < f2[0]):
        return(f1,f2)
    elif(f1[0] > f2[0]):
        return(f2,f1)
    elif(f1[1] < f2[1]):
        return(f1,f2)
    elif(f1[1] > f2[1]):
        return(f2,f1)
    elif(f1[2] < f2[2]):
        return(f1,f2)
    else:
        return(f2,f1)

## Esta funcion va a determinar la cantidad de días naturales entre las dos fechas ingresadas.
def dias_entre(f1, f2):
    if(fecha_es_valida(f1) and fecha_es_valida(f2)):                                ## Primero se verifica que ambas fechas sean válidas.
        cantidad_dias = 0
        fechas_ordenadas = fecha_menor(f1,f2)                                       ## Luego se utiliza una funcion complementaria para saber cual fecha es la menor y comenzar desde ahí el conteo.
        anho1 = fechas_ordenadas[0][0]
        anho2 = fechas_ordenadas[1][0]
        mes1 = fechas_ordenadas[0][1]
        mes2 = fechas_ordenadas[1][1]
        dia1 = fechas_ordenadas[0][2]
        dia2 = fechas_ordenadas[1][2]
        while(anho1 <= anho2):                                                      ## Mientras el año1 sea menor o igual al año2, se seguirá la suma de días.
            if(anho1 == anho2 and mes1 == mes2 and dia1 == dia2):                   ## Una vez ambos años, meses y días sean iguales, se cierra el while.
                break
            elif(bisiesto(anho1) and mes1 == 2 and dia1 < 29):                      ## Se debe revisar si el año actual es bisiesto, para asegurarnos de que llegue a 29 días.
                dia1 += 1
                cantidad_dias += 1
            elif(dia1 < diasXMes[str(mes1)]):                                       ## Si el día actual no es el último del mes, se suma uno al dia.
                dia1 += 1
                cantidad_dias += 1
            elif(bisiesto(anho1) and mes1 == 2 and dia1 == 29):                     ## Se debe revisar si el año actual es bisiesto, para realizar la suma correspondiente en el mes de febrero.
                mes1 = 3
                dia1 = 1
                cantidad_dias += 1
            elif(dia1 == diasXMes[str(mes1)] and mes1 < 12):                        ## Si el día es el último del mes y no es Diciembre, se suma uno al mes y se devuelve la cantidad de días a 1.
                mes1 += 1
                dia1 = 1
                cantidad_dias += 1
            elif(dia1 == diasXMes[str(mes1)] and mes1 == 12):                       ## Si el día es el último del mes y es Diciembre, se devuelve el mes y día a 1 y se aumenta el año en 1.
                anho1 += 1
                mes1 = 1
                dia1 = 1
                cantidad_dias += 1
        print("\nHay ", cantidad_dias, " dias entre las dos fechas ingresadas.\n")
        return cantidad_dias
    else:
        print("\n Debe ingresar dos fechas válidas.\n")
        return

menu()
































