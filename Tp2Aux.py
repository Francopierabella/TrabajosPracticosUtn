import random
import sys
import os
import msvcrt
from datetime import datetime


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
            
'''
    Algoritmos y Estructuras de Datos

    Trabajo Practico 2
    Integrantes(Comision 101):
        Franco Pierabella
        Matias Villalba
        Alejo Scarpetta
        Manuel Real

'''

# Type
# ArregloModeradoresYEstudiantes: matriz [0 ... 11,0 .. 3]
# Datos: matriz[0 ... 7,0 ... 4]

# Var
# arrayUsuarios: ArregloModeradoresYEstudiantes
# arrayDatos : Datos

ejemplo = [['francopierabella10@gmaiil.com','1223','Activo','Moderador'], # Id 0
           ['alejoScarpe@gmail.com','1231','Activo','Estudiante'], # Id 1
           ['villalbamatias@gmail.com','1212','Activo','Estudiante'], # Id 2
           ['manuelreal@gmail.com','2121','Activo','Estudiante'], # Id 3
           ['carlos@gmail.com','3131','Inactivo','Estudiante']] # Id 4

            

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

            
          
    

def cargaDeUsuariosInicio(arrayUsuarios,arrayDatos):
    print('ENTRE A CARGA DE USUARIOS INICIO')
    if arrayUsuarios[0][0] == '':
        print('Carga de los primeros 4 estudiantes!')
        for i in range (4):
            print()
            print('Carga tu email,tu contraseña y tu estado')
            print()
            arrayUsuarios[i][0] = input('Ingrese su email: ')
            arrayUsuarios[i][1] = getpass_custom('Ingrese su contraseña')
            arrayUsuarios[i][2] = input('Ingrese su estado: ')
            arrayUsuarios[i][3] = 'Estudiante' 
            print()
            print('Carga ahora tus datos personales (nombre,fecha de nacimiento,sexo,biografia y hobbies): ')
            arrayDatos[i][0] = input('Ingresa tu nombre: ')
            fechaDeNacimiento = input('Ingresa tu fecha de nacimiento: ')
            while not ingresarFechaValida(fechaDeNacimiento):
                print('Fecha invalida. Por favor ingresa una fecha correcta')
                fechaDeNacimiento = input('Ingresa tu fecha de nacimientoi: ')
            arrayDatos[i][1] = fechaDeNacimiento       
            arrayDatos[i][2] = input('Ingrese su sexo(F, M o N): ')
            arrayDatos[i][3] = input('Ingrese su biografia: ')
            arrayDatos[i][4] = input('Ingresa tus hobbies: ')
            arrayDatos[i][5] = calcularEdad(fechaDeNacimiento)
            print('El estudiante ',i,' ha sido cargado correctamente')
            print()
        print('\n')
        print('Carga del primer moderador\n')
        arrayUsuarios[4][0] = input('Ingrese su Email: ')
        arrayUsuarios[4][1] = getpass_custom('Ingrese su contraseña')
        arrayUsuarios[4][2] = input('Ingrese su estado: ')
        arrayUsuarios[4][3] = 'Moderador'
        print('Carga Completa!')
    else: # Quiere decir que eligio primero registrarse antes que loguearse
        print('ENTRE AL ELSE DE CARGA DE USUARIOS')
        if arrayUsuarios[0][3] == 'Estudiante':
            print('Carga los 3 estudiantes faltantes')
            print('\n')
            for i in range(1,4):
                arrayUsuarios[i][0] = input('Ingrese su email: ')
                arrayUsuarios[i][1] = getpass_custom('Ingrese su contraseña')
                arrayUsuarios[i][2] = input('Ingrese su estado: ')
                arrayUsuarios[i][3] = 'Estudiante' 
                print()
                print('Carga ahora tus datos personales (nombre,fecha de nacimiento,sexo,biografia y hobbies): ')
                arrayDatos[i][0] = input('Ingresa tu nombre: ')
                fechaDeNacimiento = input('Ingresa tu fecha de nacimiento: ')
                while not ingresarFechaValida(fechaDeNacimiento):
                    print('Fecha invalida. Por favor ingresa una fecha correcta')
                    fechaDeNacimiento = input('Ingresa tu fecha de nacimiento: ')
                arrayDatos[i][1] = fechaDeNacimiento
                arrayDatos[i][2] = input('Ingrese su sexo(F, M o N): ')
                arrayDatos[i][3] = input('Ingrese su biografia: ')
                arrayDatos[i][4] = input('Ingresa tus hobbies: ')
                arrayDatos[i][5] = calcularEdad(fechaDeNacimiento)
                print()
                print('El estudiante ',i, ' ha sido cargado correctamente.')
                print()
            print()
            print('Carga el primer moderador \n')
            arrayUsuarios[4][0] = input('Ingrese su Email: ')
            arrayUsuarios[4][1] = getpass_custom('Ingrese su contraseña')
            arrayUsuarios[4][2] = input('Ingrese su estado: ')
            arrayUsuarios[4][3] = 'Moderador'
            print('El moderador ha sido cargado correctamente.')
            print()
        elif arrayUsuarios[0][3] == 'Moderador':
            print('Carga los 4 estudiantes faltantes')
            print('\n')
            for i in range(1,5):
                arrayUsuarios[i][0] = input('Ingrese su email: ')
                arrayUsuarios[i][1] = getpass_custom('Ingrese su contraseña')
                arrayUsuarios[i][2] = input('Ingrese su estado: ')
                arrayUsuarios[i][3] = 'Estudiante' 
                print()
                print('Carga ahora tus datos personales (nombre,fecha de nacimiento,sexo,biografia y hobbies): ')
                arrayDatos[i][0] = input('Ingresa tu nombre: ')
                fechaDeNacimiento = input('Ingresa tu fecha de nacimiento: ')
                while not ingresarFechaValida(fechaDeNacimiento):
                    print('Fecha invalida. Por favor ingresa una fecha correcta')
                    fechaDeNacimiento = input('Ingresa tu fecha de nacimiento: ')
                arrayDatos[i][1] = fechaDeNacimiento
                arrayDatos[i][2] = input('Ingrese su sexo(F, M o N): ')
                arrayDatos[i][3] = input('Ingrese su biografia: ')
                arrayDatos[i][4] = input('Ingresa tus hobbies: ')
                arrayDatos[i][5] = calcularEdad(fechaDeNacimiento)
                
                print()
                print('El estudiante ', i , ' ha sido cargado correctamente.') 
                print()    
            
            
def Registrarse(arrayUsuarios,arrayDatos):
    print('Bienvenido!')
    aux = input('Eres estudiante (e) o moderador (m)?: ')
    while aux != 'e' and aux != 'm':
        print('Error! Responde -e- o -m-')
        aux = input('Eres estudiante (e) o moderador (m)?: ')
    print('A continuacion, Carga tu Email, contraseña y estado')
    print('\n')
    arrayUsuarios[0][0] = input('ingresa tu email: ')
    arrayUsuarios[0][1] = getpass_custom('ingresa tu contraseña: ')
    arrayUsuarios[0][2] = input('Ingresa tu estado: ')
    if aux == 'm':
        arrayUsuarios[0][3] = 'Moderador'
    else:
        arrayUsuarios[0][3] = 'Estudiante'
        print( )
        print('Por ultimo, carga tu nombre, tu fecha de nacimiento,tu sexo,tu biografia y tus hobbies')
        print()
        arrayDatos[0][0] = input('Ingresa tu nombre: ')
        fechaDeNacimiento = input('Ingresa tu fecha de nacimiento: ')
        while not ingresarFechaValida(fechaDeNacimiento):
            print('Fecha invalida. Por favor ingresa una fecha correcta')
            fechaDeNacimiento = input('Ingresa tu fecha de nacimiento: ')
        arrayDatos[0][1] = fechaDeNacimiento    
        arrayDatos[0][2] = input('Ingresa tu sexo (F, M o N): ')
        arrayDatos[0][3] = input('Ingresa tu biografia: ')
        arrayDatos[0][4] = input('Ingresa tus hobbies: ')
        arrayDatos[0][5] = calcularEdad(fechaDeNacimiento)

def retornarPosicionEstudianteLogueado(array):
    emailIngresado = input('Ingresa tu email: ')
    contraseñaIngresada = getpass_custom('Ingresa tu contraseña')
    intentos = 2
    i = 0 # Es indirectamente la Id del usuario
    while(emailIngresado != array[i][0] or contraseñaIngresada != array[i][1] or array[i][2] != 'Activo') and intentos > 0:
        print('Email del usuario ',i,':',array[i][0])
        print('Contraseña del usuario ',i,': ', array[i][1])
        print('Error! Email y/o Contraseña incorrectos!')
        i = i + 1
        intentos = intentos - 1
        emailIngresado = input('Ingresa tu email: ')
        contraseñaIngresada = getpass_custom('Ingresa tu contraseña')
    if intentos == 0:
        return -1
    else:
        return i # Posicion del estudiante logueado

            
def contarEstudiantes(array):
    cont = 0
    for i in range(12):
        if array[i][3] == 'Estudiante':
            cont +=1
    return cont

def contarModeradores(array):
    cont = 0
    for i in range(12):
        if array[i][3] == 'Moderador':
            cont +=1
    return cont
            
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
    print('2. Registrarse')
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
    

def editarDatos(id,array):
    os.system('cls')
    fechaDeNacimiento = input('Ingresa tu fecha de nacimiento: ')
    while not ingresarFechaValida(fechaDeNacimiento):
        print('Fecha invalida. Por favor ingresa una fecha correcta')
        fechaDeNacimiento = input('Ingresa tu fecha de nacimiento: ')
    fechaAux = datetime.strptime(fechaDeNacimiento,'%Y/%m/%d')
    array[id][2] = input('Sexo (F, M o N): ') 
    array[id][3] = input('Biografia: ')
    array[id][4] = input('Hobbies: ')
    array[id][5] = calcularEdad(fechaAux)
    print()
    print('Datos Actualizados!')
    print()
    print()
    os.system('pause')
    

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
    for i in range(cantEstudiantes):
        if i != id:
            print('Aqui tienes tus candidatos. ')
            print()
            print('Estudiante numero ',i,'. Sus datos son: ')
            print('Su nombre: ',arrayDatos[i][0])
            print('Su fecha de nacimiento: ',arrayDatos[i][1])
            print('Su edad: ',arrayDatos[i][5])
            print('Su biografia: ',arrayDatos[i][3])
            print('Sus hobbies: ',arrayDatos[i][4])
            print()
            print('----------------------------')
            print()
    

def gestionarCandidatos(cantEstudiantesCargados,arrayDatos,arrayUsuarios,idDeEstudianteLogueado,arrayReporte):
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
        mostrarDatos(idDeEstudianteLogueado,arrayDatos,cantEstudiantesCargados)
        meGusta = input('Ingresa el nombre del Estudiante con el que quieres hacer un futuro Matcheo: ')
        while (meGusta != arrayDatos[0][0] and meGusta != arrayDatos[1][0] and meGusta != arrayDatos[2][0] and meGusta != arrayDatos[3][0]) or meGusta == arrayDatos[idDeEstudianteLogueado][0]:
            if meGusta == arrayDatos[idDeEstudianteLogueado][0]:
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
        while idDeEstudianteAreportar == idDeEstudianteLogueado or  arrayUsuarios[idDeEstudianteAreportar][0] == '':
            print('ID invalida. ')
            print()
            idDeEstudianteAreportar = int(input('Ingresa el ID del estudiante a reportar: '))
        motivo = input('ingresa el motivo por el cual lo reportas: ')
        p = 0
        while arrayReporte[p][0] != '':
            p += 1
        arrayReporte[p][0] = str(idDeEstudianteLogueado)
        arrayReporte[p][1] = str(idDeEstudianteAreportar)
        arrayReporte[p][2] = motivo
        arrayReporte[p][3] = str(0)
        print('')
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
        
    

def reportesEstadisticos(matrizLikes,idDeEstudianteLogueado,cantDeEstudiantes):
    matcheoAmbasVeces = 0
    yoSiPeroElNo = 0
    ElSiPeroYoNo = 0
    for i in range(cantDeEstudiantes):
        if idDeEstudianteLogueado != i:
            if matrizLikes[idDeEstudianteLogueado][i] == matrizLikes[i][idDeEstudianteLogueado]:
                matcheoAmbasVeces += 1
    for j in range(cantDeEstudiantes):
        if idDeEstudianteLogueado != j:
            if matrizLikes[idDeEstudianteLogueado][j] == 1 and matrizLikes[j][idDeEstudianteLogueado] == 0:
                yoSiPeroElNo += 1
    for k in range(cantDeEstudiantes):
        if idDeEstudianteLogueado != k:
            if matrizLikes[k][idDeEstudianteLogueado] == 1 and matrizLikes[idDeEstudianteLogueado][k] == 0:
                ElSiPeroYoNo += 1
    print('Porcentaje de matcheos mutuos: ',(matcheoAmbasVeces * 100 ) / cantDeEstudiantes,'%')
    print()
    print('Personas a las que le dimos like pero no nos lo devolvieron: ',yoSiPeroElNo)
    print()
    print('Personas que nos dieron like pero nosotros no respondimos: ',ElSiPeroYoNo)
    print()
    os.system('pause')
                
                
    
def gestionarUsuarios(arrayUsuarios): 
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
        idDeEstudianteADesactivar = int(input('Ingresa el ID del estudiante a desactivar: '))
        while arrayUsuarios[idDeEstudianteADesactivar][0] == '':
            print('No hay estudiantes con ese ID !')
            idDeEstudianteADesactivar = int(input('Ingresa el ID del estudiante a desactivar: '))
        opcAuxiliar = input('Estas seguro que quieres desactivar al usuario '+ str(idDeEstudianteADesactivar) + ' ? Ingresa Si o No').lower
        while opcAuxiliar != 'si' and opcAuxiliar != 'no':
            print('Opcion invalida! ')
            opcAuxiliar = input('Estas seguro que quieres desactivar al usuario '+ str(idDeEstudianteADesactivar) + ' ? Ingresa Si o No').lower
        if opcAuxiliar == 'si':
            arrayUsuarios[idDeEstudianteADesactivar][2] == 'Inactivo'
            print()
            print('El usuario ', idDeEstudianteADesactivar, ' ha sido eliminado.')
        else:
            print('No has decidido eliminar al usuario ',idDeEstudianteADesactivar)
        os.system('pause')
    else:
        print('Volviendo al menu Anterior...')
        print()
        os.system('pause')
            
            
def gestionarReportes(arrayUsuarios,arrayReporte):
    os.system('cls')
    cont = 0
    while arrayReporte[cont][0] != '':
        cont += 1
    for i in range(cont):
        if arrayUsuarios[arrayReporte[cont][0]][2] and arrayUsuarios[arrayReporte[cont][0]][2] == 'Activo' and arrayReporte[cont][3] == '0':
            print()
            print(arrayReporte[cont])
            print()
            print('Como quieres proceder? ')
            print()
            print('a. Ignorar Reporte')
            print()
            print('b. Bloquear al reportante')
            print()
            opc = input('Elige una opcion (a,b): ')
            while opc != 'a' and opc != 'b':
                print('Opcion Invalida')
                opc = input('Elige una opcion (a,b): ')
            if opc == 'a':
                arrayReporte[cont][3] == '2'
                print()
                print('El estado del reporte ',cont,' ha sido cambiado a 2.')
            else:
                arrayReporte[cont][3] == '1'
                print()
                print('El estado del reporte ',cont,' ha sido cambiado a 1.')
                print()
                arrayUsuarios[arrayReporte[cont][1]][3] = 'Inactivo'
                print('El Estado del usuario ',arrayReporte[cont][1],' ha sido cambiado a Inactivo.')
    print()
    print('Volviendo al menu anterior...')            
    os.system('pause')
   
 
#matrizLikes: matriz[0 ... 7,0 ... 7]

def cargaMatrizDeLikes(array):
    for i in range(8):
        for j in range(8):
            if i == j:
                array[i][j] == 0 # Esto es para que no matchee un estudiante con sigo mismo
            else:
                array[i][j] = random.randint(0,1)
            
    
        
def principal():
    arrayLikes = [[0]* 8 for k in range(8)]
    cargaMatrizDeLikes(arrayLikes)
    arrayUsuarios = [[''] * 4 for n in range(12)]
    arrayDatos = [[''] * 6 for j in range(8)]
    # Login 
    logOReg = 1
    while logOReg != 0:    
        menuPrincipal()
        logOReg = int(input('Elije una opcion: '))
        while logOReg != 0 and logOReg != 1 and logOReg != 2:
            print('Error! Opcion incorrecta. Elige 0, 1 ó 2')
            logOReg = int(input('Elije una opcion: '))
        if logOReg == 2:
            Registrarse(arrayUsuarios,arrayDatos)
        if logOReg != 0:    
            cargaDeUsuariosInicio(arrayUsuarios,arrayDatos)
            cantidadDeEstudiantesCargados = contarEstudiantes(arrayUsuarios)
            idDeEstudianteLogueado = retornarPosicionEstudianteLogueado(arrayUsuarios)
            print(arrayUsuarios[idDeEstudianteLogueado][2])      
            if idDeEstudianteLogueado == -1:
                print('Te has quedado sin intentos. Vuelve mas tarde! ')
                os.system('pause')
            else:
                arrayReporte = [[''] * 4 for n in range(cantidadDeEstudiantesCargados - 1)]
                if arrayUsuarios[idDeEstudianteLogueado][3] == 'Moderador':
                    menuPrincipalModeradores()
                    eleccion = int(input('Elige una opcion (0,1,2,3): '))
                    while eleccion not in range(4):
                        print('Opcion Invalida!')
                        eleccion = int(input('Elige una opcion (0,1,2,3): '))
                    match eleccion:
                        case 1: gestionarUsuarios(arrayUsuarios)
                        case 2: gestionarReportes(arrayReporte) 
                        case 3: enConstruccion()
                        case 0: print('Volviendo al menu de logueo')  
                else:
                    segundaOpcion = 1
                    while segundaOpcion != 0 and arrayUsuarios[idDeEstudianteLogueado][2] == 'Activo':  
                        print(arrayUsuarios[idDeEstudianteLogueado][2])      
                        menuPrincipalEstudiante()
                        segundaOpcion = int(input('Elige una opcion (0,1,2,3,4)'))
                        while segundaOpcion != 0 and segundaOpcion != 1 and segundaOpcion != 2 and segundaOpcion != 3 and segundaOpcion != 4:
                            print('Error! Opcion invalida. ')
                            segundaOpcion = int(input('Elige una opcion (0,1,2,3,4)'))
                        match segundaOpcion:
                            case 1: gestionarPerfil(idDeEstudianteLogueado,arrayDatos,arrayUsuarios)
                            case 2: gestionarCandidatos(cantidadDeEstudiantesCargados,arrayDatos,arrayUsuarios,idDeEstudianteLogueado,arrayReporte)
                            case 3: enConstruccion()
                            case 4: reportesEstadisticos(arrayLikes,idDeEstudianteLogueado)
                            case 0: print('Volviendo al menu de logueo')  
                            
                            
                        # mostramos menu para estudiantes
        else:
            print()
            print()
            print('Adios!')
principal()
            
   
   
        
        
     
        



