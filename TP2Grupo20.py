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
          
    

def cargaDeUsuariosInicio(arrayUsuarios,arrayDatos,cantEst,cantMods):
    if contarEstudiantes(arrayUsuarios) >= 4 and contarModeradores(arrayUsuarios) >= 1:
        print('Puedes loguearte! ')
    else:
        print('Para poder loguearte necesitamos al menos 4 estudiantes y un moderador!')
        print()
        print('Cargalos aqui... ')
        print()
        if arrayUsuarios[0][0] == '':
            print('Carga de los estudiantes!')
            for i in range (cantEst):
                print()
                print('Carga tu email,tu contraseña y tu estado')
                print()
                arrayUsuarios[i][0] = input('Ingrese su email: ')
                arrayUsuarios[i][1] = getpass_custom('Ingrese su contraseña: ')
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
                print('El estudiante ',i,' ha sido cargado correctamente')
                print()
            print('\n')
            print('Carga el/los moderadores \n')
            for k in range(cantMods):
                arrayUsuarios[cantEst + k][0] = input('Ingrese su Email: ')
                arrayUsuarios[cantEst + k][1] = getpass_custom('Ingrese su contraseña: ')
                arrayUsuarios[cantEst + k][2] = input('Ingrese su estado: ')
                arrayUsuarios[cantEst + k][3] = 'Moderador'
            print('Carga Completa!')
        else: # Quiere decir que eligio primero registrarse antes que loguearse
            print('Para poder Loguearte necesitamos cargar los estudiantes y moderadores restantes! ')
            
            if arrayUsuarios[0][3] == 'Estudiante':
                for i in range(1,cantEst):
                    arrayUsuarios[i][0] = input('Ingrese su email: ')
                    arrayUsuarios[i][1] = getpass_custom('Ingrese su contraseña: ')
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
                print('Carga el/ los moderadores  \n')
                for l in range(cantMods):
                    print('Ingresa sus datos: \n')
                    arrayUsuarios[cantEst + l][0] = input('Ingrese su Email: ')
                    arrayUsuarios[cantEst + l][1] = getpass_custom('Ingrese su contraseña: ')
                    arrayUsuarios[cantEst + l][2] = input('Ingrese su estado: ')
                    arrayUsuarios[cantEst + l][3] = 'Moderador'
                    print('El moderador ha sido cargado correctamente.')
                print()
            elif arrayUsuarios[0][3] == 'Moderador':
                for o in range(1,cantMods):
                    print('Ingresa sus datos: \n')
                    arrayUsuarios[o][0] = input('Ingrese su Email: ')
                    arrayUsuarios[o][1] = getpass_custom('Ingrese su contraseña: ')
                    arrayUsuarios[o][2] = input('Ingrese su estado: ')
                    arrayUsuarios[o][3] = 'Moderador'
                    print('El moderador ha sido cargado correctamente.')
                    
                print('Carga los estudiantes faltantes')
                print('\n')
                for i in range(cantMods,cantMods + cantEst):
                    arrayUsuarios[i][0] = input('Ingrese su email: ')
                    arrayUsuarios[i][1] = getpass_custom('Ingrese su contraseña: ')
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
    i = 0
    while arrayUsuarios[i][0] != '':
        i += 1
    arrayUsuarios[i][0] = input('ingresa tu email: ')
    arrayUsuarios[i][1] = getpass_custom('ingresa tu contraseña: ')
    arrayUsuarios[i][2] = input('Ingresa tu estado: ')
    if aux == 'm':
        arrayUsuarios[i][3] = 'Moderador'
    else:
        arrayUsuarios[i][3] = 'Estudiante'
        print( )
        print('Por ultimo, carga tu nombre, tu fecha de nacimiento,tu sexo,tu biografia y tus hobbies')
        print()
        arrayDatos[i][0] = input('Ingresa tu nombre: ')
        fechaDeNacimiento = input('Ingresa tu fecha de nacimiento: ')
        while not ingresarFechaValida(fechaDeNacimiento):
            print('Fecha invalida. Por favor ingresa una fecha correcta')
            fechaDeNacimiento = input('Ingresa tu fecha de nacimiento: ')
        arrayDatos[i][1] = fechaDeNacimiento    
        arrayDatos[i][2] = input('Ingresa tu sexo (F, M o N): ')
        arrayDatos[i][3] = input('Ingresa tu biografia: ')
        arrayDatos[i][4] = input('Ingresa tus hobbies: ')
        arrayDatos[i][5] = calcularEdad(fechaDeNacimiento)


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
        emailIngresado = input('Ingresa tu email: ')
        contraseñaIngresada = getpass_custom('Ingresa tu contraseña: ')
        intentos -= 1
        print('Te quedan ',intentos,' intentos') 
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
            print('----------------------------')
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
        while idDeEstudianteAreportar == idDeEstudianteLogueado or  arrayUsuarios[idDeEstudianteAreportar][0] == '' or arrayUsuarios[idDeEstudianteAreportar][3] == 'Moderador':
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
        idDeUsuarioADesactivar = int(input('Ingresa el ID del usuario a desactivar: '))
        while arrayUsuarios[idDeUsuarioADesactivar][0] == '':
            print('No hay usuario con ese ID !')
            idDeUsuarioADesactivar = int(input('Ingresa el ID del estudiante a desactivar: '))
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
            
            
def gestionarReportes(arrayUsuarios,arrayReporte):
    os.system('cls')
    cont = 0
    while arrayReporte[cont][0] != '':
        cont += 1
    for i in range(cont):
        if arrayUsuarios[arrayReporte[cont][0]][2] == 'Activo' and arrayReporte[cont][3] == '0':
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
                arrayReporte[cont][3] = '2'
                print()
                print('El estado del reporte ',cont,' ha sido cambiado a 2.')
            else:
                arrayReporte[cont][3] = '1'
                print()
                print('El estado del reporte ',cont,' ha sido cambiado a 1.')
                print()
                arrayUsuarios[arrayReporte[cont][1]][3] = 'Inactivo'
                print('El Estado del usuario ',arrayReporte[cont][1],' ha sido cambiado a Inactivo.')
    print()
    print('Volviendo al menu anterior...')            
    os.system('pause')
   
 
#matrizLikes: matriz[0 ... 7,0 ... 7]

def cargaMatrizDeLikes(array,cantEst):
    for i in range(cantEst):
        for j in range(cantEst):
            if i == j:
                array[i][j] = 0 # Esto es para que no matchee un estudiante con sigo mismo
            else:
                array[i][j] = random.randint(0,1)
            
    
        
def principal():
    arrayUsuarios = [[''] * 4 for n in range(12)]
    arrayDatos = [[''] * 6 for j in range(8)]
    # Login 
    cantEstudiantes = int(input('Cuantos estudiantes vas a cargar? (minimo 4 y maximo 8): '))
    arrayLikes = [[0] * cantEstudiantes for k in range(cantEstudiantes)]
    cargaMatrizDeLikes(arrayLikes,cantEstudiantes)
    print()
    while cantEstudiantes < 4 and cantEstudiantes > 8:
        print('Error! Tiene que ser minimo 4 y maximo 8!')
        cantEstudiantes = int(input('Cuantos estudiantes vas a cargar? (minimo 4 y maximo 8): '))
        print()
    cantModeradores = int(input('Cuantos moderadores vas a cargar? (minimo 1 maximo 4): '))
    while cantModeradores < 1 and cantModeradores > 4:
        print('Error! Minimo 1 Maximo 4!')
        cantModeradores = int(input('Cuantos moderadores vas a cargar? (minimo 1 maximo 4): '))
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
        if logOReg != 0:    
            cargaDeUsuariosInicio(arrayUsuarios,arrayDatos,cantEstudiantes,cantModeradores)
            cantidadDeEstudiantesCargados = contarEstudiantes(arrayUsuarios)
            idDeEstudianteLogueado = logueo(arrayUsuarios)
            if idDeEstudianteLogueado != -1 :   
                arrayReporte = [[''] * 4 for n in range(cantidadDeEstudiantesCargados)]
                if arrayUsuarios[idDeEstudianteLogueado][3] == 'Moderador':
                    segundaOpcion = 1
                    while segundaOpcion != 0:
                        menuPrincipalModeradores()
                        eleccion = int(input('Elige una opcion (0,1,2,3): '))
                        while eleccion not in range(4):
                            print('Opcion Invalida!')
                            eleccion = int(input('Elige una opcion (0,1,2,3): '))
                        match eleccion:
                            case 1: gestionarUsuarios(arrayUsuarios)
                            case 2: gestionarReportes(arrayReporte) 
                            case 3: enConstruccion()
                            case 0: 
                                print('Volviendo al menu de logueo!')
                                os.system('pause')    
                else:
                    segundaOpcion = 1
                    while segundaOpcion != 0 and arrayUsuarios[idDeEstudianteLogueado][2] == 'Activo':       
                        menuPrincipalEstudiante()
                        segundaOpcion = int(input('Elige una opcion (0,1,2,3,4)'))
                        while segundaOpcion != 0 and segundaOpcion != 1 and segundaOpcion != 2 and segundaOpcion != 3 and segundaOpcion != 4:
                            print('Error! Opcion invalida. ')
                            segundaOpcion = int(input('Elige una opcion (0,1,2,3,4)'))
                        match segundaOpcion:
                            case 1: gestionarPerfil(idDeEstudianteLogueado,arrayDatos,arrayUsuarios)
                            case 2: gestionarCandidatos(cantidadDeEstudiantesCargados,arrayDatos,arrayUsuarios,idDeEstudianteLogueado,arrayReporte)
                            case 3: enConstruccion()
                            case 4: reportesEstadisticos(arrayLikes,idDeEstudianteLogueado,cantidadDeEstudiantesCargados)
                            case 0: 
                                print('Volviendo al menu de logueo')  
                                os.system('pause')
                            
                        # mostramos menu para estudiantes
            else:
                print('Te has quedado sin intetos! ')
                print('Vuelve mas tarde! ')
                print('Adios!')
principal()
            
   
   
        
        
     
        



