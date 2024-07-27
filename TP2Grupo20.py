import random
import sys
import os
import msvcrt
from datetime import datetime

'''
    Algoritmos y Estructuras de Datos

    Trabajo Practico 2
    Integrantes(Comision 101):
        Franco Pierabella
        Matias Villalba
        Alejo Scarpetta
        Manuel Real

'''

fecha_actual = datetime.now()   # Aqui calculamos la fecha de hoy con uso de la libreria Datetime
año_actual = fecha_actual.year  # Aqui calculamos el año actual con uso de la libreria Datetime
mes_actual = fecha_actual.month # Aqui calculamos el mes actual con uso de la libreria Datetime   
dia_actual = fecha_actual.day   # Aqui calculamos el dia actual con uso de la libreria Datetime

def getpass_custom(prompt='Password: '):
    print(prompt, end='', flush=True)
    password = ''
    while True:
        key = msvcrt.getch()
        key = key.decode("utf-8")
        if key == '\r':
            print('')
            return password
        elif key == '\b':
            if password:
                password = password[:-1]
                sys.stdout.write('\b \b')
        else:
            password += key
            sys.stdout.write('*')
            sys.stdout.flush()
            

            

def calcularEdad(fecha):
    fechaAux = datetime.strptime(fecha,'%Y/%m/%d')
    año = fechaAux.year
    mes = fechaAux.month
    dia = fechaAux.day
    if mes > mes_actual:
        edad = (año_actual - año) - 1
    elif mes < mes_actual:
        edad = año_actual - año
    else:
        if dia > dia_actual:
            edad = (año_actual - año) - 1
        else:
            edad = año_actual - año
    return edad


def ingresarFechaValida(fecha):
    fechaAux = datetime.strptime(fecha,'%Y/%m/%d')
    año = fechaAux.year
    mes = fechaAux.month
    dia = fechaAux.day  
    if año > año_actual:
        return False
    if mes > 12:
        return False
    if dia > 31:
        return False
    if mes == 2 and dia > 28:
        return False
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia > 31:
            return False
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia > 30:
            return False
    return True



# contarEstudiantes recibe como parametro el array de los usuarios, y devuelve cuantos de ellos son estudiantes            
def contarEstudiantes(array):
    cont = 0
    for i in range(12):
        if array[i][3] == 'Estudiante':
            cont +=1
    return cont


# contarModeradores recibe como parametro el array de los usuarios, y devuelve cuantos de ellos son moderadores            
def contarModeradores(array):
    cont = 0
    for i in range(12):
        if array[i][3] == 'Moderador':
            cont +=1
    return cont
             
            
            
def Registrarse(arrayUsuarios,arrayDatos):
    print('Bienvenido!')
    aux = input('Eres estudiante (e) o moderador (m)?: ')
    while aux != 'e' and aux != 'm':
        print('Error! Responde -e- o -m-')
        aux = input('Eres estudiante (e) o moderador (m)?: ')
    if (aux == 'e' and contarEstudiantes(arrayUsuarios) > 8) or (aux == 'm' and contarModeradores(arrayUsuarios) > 4):
        if aux == 'e':
            print('Ya hemos llegado al maximo de Estudiantes! No puedes registrar mas!')
        else:
            print('Ya hemos llegado al maximo de Moderadores! No puedes registrar mas!')
    else:   
        print('A continuacion, Carga tu Email, contraseña y estado')
        print('\n')
        i = 0
        while arrayUsuarios[i][0] != '':
            i += 1
        arrayUsuarios[i][0] = input('ingresa tu email: ')
        arrayUsuarios[i][1] = getpass_custom('ingresa tu contraseña: ')
        arrayUsuarios[i][2] = input('Ingresa tu estado: ').capitalize()
        if aux == 'm':
            arrayUsuarios[i][3] = 'Moderador'
            print()
            print('Moderador Cargado correctamente!')
            input()
        else:
            arrayUsuarios[i][3] = 'Estudiante'
            j = 0
            while arrayDatos[j][0] != '':
                j += 1
            print()
            print('Por ultimo, carga tu nombre, tu fecha de nacimiento,tu sexo,tu biografia y tus hobbies')
            print()
            arrayDatos[j][0] = input('Ingresa tu nombre: ')
            fechaDeNacimiento = input('Ingresa tu fecha de nacimiento: ')
            while not ingresarFechaValida(fechaDeNacimiento):
                print('Fecha invalida. Por favor ingresa una fecha correcta')
                fechaDeNacimiento = input('Ingresa tu fecha de nacimiento: ')
            arrayDatos[j][1] = fechaDeNacimiento    
            arrayDatos[j][2] = input('Ingresa tu sexo (F, M o N): ')
            arrayDatos[j][3] = input('Ingresa tu biografia: ')
            arrayDatos[j][4] = input('Ingresa tus hobbies: ')
            arrayDatos[j][5] = calcularEdad(fechaDeNacimiento)
            print()
            print('Estudiante Cargado correctamente! ')
            input()


def logueo(arrayUsuarios):
    print('---------- LOG IN -----------')
    print()
    intentos = 2
    emailIngresado = input('Ingresa tu email: ')
    contraseñaIngresada = getpass_custom('Ingresa tu contraseña: ')
    while((emailIngresado != arrayUsuarios[0][0] or contraseñaIngresada != arrayUsuarios[0][1])\
        and (emailIngresado != arrayUsuarios[1][0] or contraseñaIngresada != arrayUsuarios[1][1])\
        and (emailIngresado != arrayUsuarios[2][0] or contraseñaIngresada != arrayUsuarios[2][1])\
        and (emailIngresado != arrayUsuarios[3][0] or contraseñaIngresada != arrayUsuarios[3][1])\
        and (emailIngresado != arrayUsuarios[4][0] or contraseñaIngresada != arrayUsuarios[4][1])\
        and (emailIngresado != arrayUsuarios[5][0] or contraseñaIngresada != arrayUsuarios[5][1])\
        and (emailIngresado != arrayUsuarios[6][0] or contraseñaIngresada != arrayUsuarios[6][1])\
        and (emailIngresado != arrayUsuarios[7][0] or contraseñaIngresada != arrayUsuarios[7][1])\
        and (emailIngresado != arrayUsuarios[8][0] or contraseñaIngresada != arrayUsuarios[8][1])\
        and (emailIngresado != arrayUsuarios[9][0] or contraseñaIngresada != arrayUsuarios[9][1])\
        and (emailIngresado != arrayUsuarios[10][0] or contraseñaIngresada != arrayUsuarios[10][1])\
        and (emailIngresado != arrayUsuarios[11][0] or contraseñaIngresada != arrayUsuarios[11][1])) and intentos > 0:
        print('Email y/o contraseña Incorrectas! ')
        print()
        print('Te quedan ',intentos, ' intentos') 
        emailIngresado = input('Ingresa tu email: ')
        contraseñaIngresada = getpass_custom('Ingresa tu contraseña: ')
        intentos -= 1
        print()
    if intentos == 0:
        return -1
    else:
        i = 0
        while(emailIngresado != arrayUsuarios[i][0] or contraseñaIngresada != arrayUsuarios[i][1]):
            i = i + 1
        return i # Posicion del estudiante logueado


            
            
def menuPrincipal():
    os.system("cls")
    print('Bienvenido!')
    print()
    print()
    print('------------------------------')
    print()
    print('MENU PRINCIPAL')
    print('Ya tienes una cuenta => Logueate respondiendo 1!')
    print('En caso contrario, creala respondiendo 2!')
    print()
    print('1. Log in')
    print()
    print('2. Registro')
    print()
    print('0. Salir')

def menuPrincipalModeradores():
    os.system("cls")
    print() 
    print()
    print()
    print('------------------------------')
    print()
    print('MENU PRINCIPAL')
    print()
    print('1. Gestionar Usuarios')
    print()
    print('2. Gestionar Reportes')
    print()
    print('3. Reportes Estadisiticos')
    print()
    print('0. Salir')
    

def menuPrincipalEstudiante():
    os.system('cls')
    print()
    print()
    print()
    print('------------------------------')
    print()
    print('MENU PRINCIPAL')
    print()
    print('1. Gestionar mi perfil: ')
    print('2. Gestionar candidatos: ')
    print('3. Matcheos: ')
    print('4. Reportes estadisticos ')
    print('0. Salir:')   
    

def editarDatos(id,arrayDatos):
    os.system('cls')
    print()
    print('Estos son tus datos actuales: ')
    print('Tu nombre: ',arrayDatos[id][0])
    print('')
    print('Tu fecha de nacimiento: ',arrayDatos[id][1])
    print('')
    print('Tu sexo: ',arrayDatos[id][2])
    print('')
    print('Tu biografia: ',arrayDatos[id][3])
    print('')
    print('Tus hobbies: ',arrayDatos[id][4])
    print('')
    print('Tu Edad: ',arrayDatos[id][5])
    print('')
    print('Aqui podras editar tu fecha de nacimiento,tu bio,tus hobbies y tu sexo ')
    print()
    fechaDeNacimiento = input('Ingresa tu fecha de nacimiento: ')
    while not ingresarFechaValida(fechaDeNacimiento):
        print('Fecha invalida. Por favor ingresa una fecha correcta')
        fechaDeNacimiento = input('Ingresa tu fecha de nacimiento: ')
    arrayDatos[id][1] = fechaDeNacimiento
    arrayDatos[id][2] = input('Sexo (F, M o N): ') 
    arrayDatos[id][3] = input('Biografia: ')
    arrayDatos[id][4] = input('Hobbies: ')
    arrayDatos[id][5] = calcularEdad(fechaDeNacimiento)
    print()
    print('Tu nueva fecha de nacimiento: ',arrayDatos[id][1])
    print()
    print('Tu nuevo sexo: ', arrayDatos[id][2])
    print()
    print('Tu nueva biografia: ',arrayDatos[id][3])
    print()
    print('Tus nuevos hobbies: ',arrayDatos[id][4])
    print()
    print('Tu nueva edad: ',arrayDatos[id][5])
    print()
    print('Datos Actualizados!')
    print()
    print()
    os.system('pause')
    

#           var 
# eleccion: int
# opcAuxiliar: string
def gestionarPerfil(id,arrayDatos,arrayUsuarios):
    os.system('cls')
    print()
    print()
    print()
    print('------------------------------')
    print()
    print('a. Editar mis datos personales. ')
    print('b. Eliminar mi perfil. ')
    print('c. Volver')
    eleccion = input('Elije una opcion (a , b , c): ')
    while eleccion != 'a' and eleccion != 'b' and eleccion != 'c':
        print('Error! opcion incorrecta. Elige a,b,c')
        eleccion = input('Elije una opcion (a , b , c): ')
    if eleccion == 'a':
        editarDatos(id,arrayDatos)
    elif eleccion == 'b':
        opcAuxiliar = input('Estas seguro que deseas eliminar tu perfil? (ingresa si o no): ')
        while opcAuxiliar != 'si' and opcAuxiliar != 'no':
            print('Opcion invalida! ')
            opcAuxiliar = input('Estas seguro que deseas eliminar tu perfil? (ingresa si o no): ')
        if opcAuxiliar == 'si':
            arrayUsuarios[id][2] = 'Inactivo' 
            print('El usuario ',id,' ha sido eliminado!')
        else:
            print('Tu usuario no ha sido eliminado.')
        print() 
        os.system('pause')
    else:
        print()
        print('Volviendo al menu anterior. ')
        os.system('pause')
   
def mostrarDatos(id,arrayDatos,cantEstudiantes):
    os.system('cls')
    print('Aqui tienes tus candidatos. ')
    print()
    for i in range(cantEstudiantes):
        if i != id:
            print('----------------------------')
            print()
            print('Estudiante numero ',i,'. Sus datos son: ')
            print('Su nombre: ',arrayDatos[i][0])
            print('Su fecha de nacimiento: ',arrayDatos[i][1])
            print('Su edad: ',arrayDatos[i][5])
            print('Su biografia: ',arrayDatos[i][3])
            print('Sus hobbies: ',arrayDatos[i][4])
            print()
            print()
    
    

def gestionarCandidatos(cantEstudiantesCargados,arrayDatos,arrayUsuarios,idDeUsuarioLogueado,arrayReporte,arrayMotivos):
    os.system('cls') 
    print()
    print()
    print()
    print('------------------------------')
    print()
    print('a. Ver candidatos ')
    print('b. Reportar un candidato. ')
    print('c. Volver') 
    eleccion = input('Elige una opcion (a,b,c): ')
    while eleccion != 'a' and eleccion != 'b' and eleccion != 'c':
        print('Opcion incorrecta! Por favor elige (a,b,c)')
        eleccion = input('Elige una opcion (a,b,c): ')
    if eleccion == 'a':
        mostrarDatos(idDeUsuarioLogueado,arrayDatos,cantEstudiantesCargados)
        meGusta = input('Ingresa el nombre del Estudiante con el que quieres hacer un futuro Matcheo: ')
        while (meGusta != arrayDatos[0][0] and meGusta != arrayDatos[1][0] and meGusta != arrayDatos[2][0] and meGusta != arrayDatos[3][0]) or meGusta == arrayDatos[idDeUsuarioLogueado][0]:
            if meGusta == arrayDatos[idDeUsuarioLogueado][0]:
                print('No puedes gustarte a ti mismo. ')
            else:
                print('Nombre incorrecto! Por favor ingresa un nombre de un estudiante')
            print()
            meGusta = input('Ingresa el nombre del Estudiante con el que quieres hacer un futuro Matcheo: ')
        print()
        print('Te gusta el estudiante: ',meGusta)
        print()
        print('Volviendo al menu anterior.')
        os.system('pause')
    elif eleccion == 'b':
        print()
        idDeEstudianteAreportar = int(input('Ingresa el ID del estudiante a reportar: '))
        while idDeEstudianteAreportar == idDeUsuarioLogueado or  arrayUsuarios[idDeEstudianteAreportar][0] == '' or arrayUsuarios[idDeEstudianteAreportar][3] == 'Moderador':
            print('ID invalida. ')
            print()
            idDeEstudianteAreportar = int(input('Ingresa el ID del estudiante a reportar: '))
        motivo = input('ingresa el motivo por el cual lo reportas: ')
        p = 0
        while arrayReporte[p][0] != '':
            p += 1
        arrayReporte[p][0] = idDeUsuarioLogueado
        arrayReporte[p][1] = idDeEstudianteAreportar
        arrayReporte[p][2] = 0
        arrayMotivos[p] = motivo
        print('')
        print('REPORTE')
        print()
        print('El usuario ',idDeUsuarioLogueado,' ha reportado al usuario',idDeEstudianteAreportar,' con el motivo: ',arrayMotivos[p])
        print()
        os.system('pause')
    else:
        print('Volviendo al menu anterior.')
        os.system('pause')
                    
                
                
def enConstruccion():
    os.system('cls')
    print('-----------------')
    print()
    print('En construccion! ')
    print()
    print('Vuelve dentro de unos meses! :)')
    print()
    print('-----------------')                
    print()
    os.system('pause')         
        
    

def reportesEstadisticos(matrizLikes,idDeUsuarioLogueado,cantDeEstudiantes):
    matcheoAmbasVeces = 0
    yoSiPeroElNo = 0
    ElSiPeroYoNo = 0
    for i in range(cantDeEstudiantes):
        if idDeUsuarioLogueado != i:
            if matrizLikes[idDeUsuarioLogueado][i] == matrizLikes[i][idDeUsuarioLogueado]:
                matcheoAmbasVeces += 1
    for j in range(cantDeEstudiantes):
        if idDeUsuarioLogueado != j:
            if matrizLikes[idDeUsuarioLogueado][j] == 1 and matrizLikes[j][idDeUsuarioLogueado] == 0:
                yoSiPeroElNo += 1
    for k in range(cantDeEstudiantes):
        if idDeUsuarioLogueado != k:
            if matrizLikes[k][idDeUsuarioLogueado] == 1 and matrizLikes[idDeUsuarioLogueado][k] == 0:
                ElSiPeroYoNo += 1
    print('Porcentaje de matcheos mutuos: ',int((matcheoAmbasVeces * 100 ) / cantDeEstudiantes),'%')
    print()
    print('Personas a las que le dimos like pero no nos lo devolvieron: ',yoSiPeroElNo)
    print()
    print('Personas que nos dieron like pero nosotros no respondimos: ',ElSiPeroYoNo)
    print()
    os.system('pause')
                
                
    
def gestionarUsuarios(arrayUsuarios,idDeUsuarioLogeuado): 
    os.system('cls')
    print()
    print('a. Desactivar Usuario.')
    print()
    print('b. Volver')
    opc = input('Elige una opcion (a,b,c): ')
    while opc != 'a' and opc != 'b' and opc != 'c':
        print('Opcion invalida! ')
        opc = input('Elige una opcion (a,b,c): ')
    if opc == 'a':
        idDeUsuarioADesactivar = int(input('Ingresa el ID del usuario a desactivar: '))
        while arrayUsuarios[idDeUsuarioADesactivar][0] == '' or idDeUsuarioADesactivar == idDeUsuarioLogeuado:
            print('ID invalida! Has ingresado una id inexistente o tu misma id!')
            idDeUsuarioADesactivar = int(input('Ingresa el ID del estudiante a desactivar: '))
        if arrayUsuarios[idDeUsuarioADesactivar][2] == 'Inactivo':
            print('Este usuario ya esta inactivo! ')
            print()
            print('Volviendo al menu anterior...',input())
        else:
            opcAuxiliar = input('Estas seguro que quieres desactivar al usuario '+ str(idDeUsuarioADesactivar) + ' ? Ingresa si o no')
            while opcAuxiliar != 'si' and opcAuxiliar != 'no':
                print('Opcion invalida! ')
                opcAuxiliar = input('Estas seguro que quieres desactivar al usuario '+ str(idDeUsuarioADesactivar) + ' ? Ingresa si o no')
            if opcAuxiliar == 'si':
                arrayUsuarios[idDeUsuarioADesactivar][2] = 'Inactivo'
                print()
                print('El usuario ', idDeUsuarioADesactivar, ' ha sido eliminado.')
            else:
                print('No has decidido eliminar al usuario ',idDeUsuarioADesactivar)
            os.system('pause')
    else:
        print('Volviendo al menu Anterior...')
        print()
        os.system('pause')
            
            
def gestionarReportes(arrayUsuarios,arrayReporte,arrayMotivos):
    os.system('cls')
    print()
    print('a. Ver Reportes')
    print()
    print('b. Volver')
    print()
    opc = input('Elige una opcion (a,b): ')
    while opc != 'a' and opc != 'b':
        print('Opcion invalida! Debe ser -a- o -b-')
        opc = input('Elige una opcion: (a,b)')
    if opc == 'a':
        cantidadDeReportes = 0
        while arrayReporte[cantidadDeReportes][0] != '':
            cantidadDeReportes += 1
        print('CANTIDAD DE REPORTES: ',cantidadDeReportes)
        if cantidadDeReportes == 0:
            print('No hay reportes cargados todavia!')
        else: 
            j = 0
            for p in range(cantidadDeReportes):
                if arrayReporte[p][2] == 0:
                    j += 1
            if j == 0:
                print('Los reportes ya han sido modificados por los moderadores!')
                print()
            else:
                for i in range(cantidadDeReportes):
                    if arrayUsuarios[arrayReporte[i][0]][2] == 'Activo' and arrayUsuarios[arrayReporte[i][1]][2] == 'Activo' and arrayReporte[i][2] == 0:
                        print()
                        print('REPORTE: ')
                        print()
                        print('El usuario ',arrayReporte[i][0],' ha reportado al usuario ',arrayReporte[i][1],' con el motivo: ',arrayMotivos[i])
                        print()
                        print('Como quieres proceder? ')
                        print()
                        print('a. Ignorar Reporte')
                        print()
                        print('b. Bloquear al reportante')
                        print()
                        print('c. Volver')
                        opc2 = input('Elige una opcion (a,b): ')
                        while opc2 != 'a' and opc2 != 'b':
                            print('Opcion Invalida')
                            opc2 = input('Elige una opcion (a,b): ')
                        if opc2 == 'a':
                            arrayReporte[i][2] = 2
                            print()
                            print('El estado del reporte ',i,' ha sido cambiado a 2.')
                        elif opc2 == 'b':
                            arrayReporte[i][2] = 1
                            print()
                            print('El estado del reporte ',i,' ha sido cambiado a 1.')
                            print()
                            arrayUsuarios[arrayReporte[i][1]][2] = 'Inactivo'
                            print('El Estado del usuario ',arrayReporte[i][1],' ha sido cambiado a Inactivo.')
                        else:
                            print('Volviendo al menu anterior...')
                            input()
    print()
    print('Volviendo al menu anterior...')            
    input()
   
 
# matrizLikes: matriz[0 ... 7,0 ... 7]

def cargaMatrizDeLikes(array,cantEst):
    for i in range(cantEst):
        for j in range(cantEst):
            if i == j:
                array[i][j] = 0 # Esto es para que no matchee un estudiante con sigo mismo
            else:
                array[i][j] = random.randint(0,1)
            
    
# Type
# ArregloModeradoresYEstudiantes: matriz [0 ... 11,0 .. 3] of strings
# Datos: matriz[0 ... 7,0 ... 4] of strings
# Reportes: matriz[0 ... 25,0 ... 2] or int
# Motivos: array[0...25] of strigs
# Likes: matriz[0... cantDeEstudiantes,0 ... cantDeEstudiantes] ?

# Var
# arrayUsuarios: ArregloModeradoresYEstudiantes
# arrayDatos : Datos
# arrayReportes : Reportes
# arrayMotivos : Motivos
# arrayLikes : Likes
# logOReg,cantidadDeEstudiantesCargados,cantidadDeModeradoresCargados,idDeUsuarioLogueado,segundaOpcion: int
        
def principal():
    arrayUsuarios = [[''] * 4 for n in range(12)]
    arrayDatos = [[''] * 6 for j in range(8)]
    arrayMotivos = [''] * 25 
    arrayReporte = [[''] * 3 for n in range(25)]
    # Login 
    print() 
    logOReg = 1
    while logOReg != 0:    
        menuPrincipal()
        logOReg = int(input('Elije una opcion: '))
        while logOReg != 0 and logOReg != 1 and logOReg != 2:
            print('Error! Opcion incorrecta. Elige 0, 1 ó 2')
            logOReg = int(input('Elije una opcion: '))
        if logOReg == 2:
            Registrarse(arrayUsuarios,arrayDatos)
        elif logOReg == 1:    
            cantidadDeEstudiantesCargados = contarEstudiantes(arrayUsuarios)
            cantidadDeModeradoresCargados = contarModeradores(arrayUsuarios)
            if cantidadDeEstudiantesCargados < 4 or cantidadDeModeradoresCargados < 1:
                print('Para poder loguearte, necesitamos como minimo 4 estudiantes y 1 moderador! ')
                print()
                print('Volviendo a la pantalla de Log in. ')
                os.system('pause')
            else:
                matrizLikes = [[0] * cantidadDeEstudiantesCargados for n in range(cantidadDeEstudiantesCargados)]
                cargaMatrizDeLikes(matrizLikes,cantidadDeEstudiantesCargados)
                print('')
                idDeUsuarioLogueado = logueo(arrayUsuarios)
                if arrayUsuarios[idDeUsuarioLogueado][2] == 'Inactivo':
                    print('Logueo invalido. Usuario Inactivo')
                    print('Volviendo al menu de Logueo...')
                    input()
                else:
                    if idDeUsuarioLogueado != -1 :   
                        if arrayUsuarios[idDeUsuarioLogueado][3] == 'Moderador':
                            segundaOpcion = 1
                            while segundaOpcion != 0:
                                menuPrincipalModeradores()
                                segundaOpcion = int(input('Elige una opcion (0,1,2,3): '))
                                while segundaOpcion not in range(4):
                                    print('Opcion Invalida!')
                                    segundaOpcion = int(input('Elige una opcion (0,1,2,3): '))
                                match segundaOpcion:
                                    case 1: gestionarUsuarios(arrayUsuarios,idDeUsuarioLogueado)
                                    case 2: gestionarReportes(arrayUsuarios,arrayReporte,arrayMotivos) 
                                    case 3: enConstruccion()
                                    case 0: 
                                        print('Volviendo al menu de logueo!')
                                        os.system('pause')    
                        else:
                            segundaOpcion = 1
                            while segundaOpcion != 0 and arrayUsuarios[idDeUsuarioLogueado][2] == 'Activo':       
                                menuPrincipalEstudiante()
                                segundaOpcion = int(input('Elige una opcion (0,1,2,3,4)'))
                                while segundaOpcion != 0 and segundaOpcion != 1 and segundaOpcion != 2 and segundaOpcion != 3 and segundaOpcion != 4:
                                    print('Error! Opcion invalida. ')
                                    segundaOpcion = int(input('Elige una opcion (0,1,2,3,4)'))
                                match segundaOpcion:
                                    case 1: gestionarPerfil(idDeUsuarioLogueado,arrayDatos,arrayUsuarios)
                                    case 2:
                                        gestionarCandidatos(cantidadDeEstudiantesCargados,arrayDatos,arrayUsuarios,idDeUsuarioLogueado,arrayReporte,arrayMotivos)
                                    case 3: enConstruccion()
                                    case 4: reportesEstadisticos(matrizLikes,idDeUsuarioLogueado,cantidadDeEstudiantesCargados)
                                    case 0: 
                                        print('Volviendo al menu de logueo')  
                                        os.system('pause')                
                    else:
                        print('Te has quedado sin intentos! ')
                        print('Vuelve mas tarde! ')
                        print('Adios!')
        else:
            print('Antes de terminar, Deseas hacer el BonusTrack 2? ')
            auxiliar = input('Responde si o no: ').lower()
            while auxiliar != 'si' and auxiliar != 'no':
                auxiliar = input('Responde si o no: ').lower()
            if auxiliar == 'si':
                cantidadDeMatcheosPosibles = cantidadDeEstudiantesCargados * (cantidadDeEstudiantesCargados - 1)
                print('La cantida de matcheos combinados, independientemente del sexo, es de: ',cantidadDeMatcheosPosibles)   
            print('Hasta aqui hemos llegado. Hasta la proxima!!!')
                             
                
            
principal()
            
   

def ordenarArray(array,longitudArray):
    for i in range(longitudArray - 1):
        for j in range(i + 1,longitudArray):
            if array[j] > array [i]:
                aux = array[i]
                array[i] = array[j]
                array[j] = aux


def busquedaDeHuecos(array,longitudDelArray):
    i = 0
    while array[i] - array[i + 1] == 1  or i == longitudDelArray:
        i += 1
    if array[i + 1] - array[i] != 1:
        print('Hay un hueco entre las edades ',array[i], ' y ',array[i + 1])
    else:
        print('no hay huecos! ')
        
def bonusTrack1():
    edades = [21,18,20,19,23,24]
    ordenarArray(edades,6)
    print(edades)
    busquedaDeHuecos(edades,6)

# bonusTrack1()

    
            
     
        



