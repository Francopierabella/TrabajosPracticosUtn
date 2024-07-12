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

# Type
# Estudiantes: Array[0 ... 7] of strings
# Moderadores: Array[0 ... 3] of strings

# VAR
# ArrayEstudiantes: Estudiantes
# ArrayModeradores: Moderadores


# Constantes del programa
#-------------------------------


fecha_actual = datetime.now()   # Aqui calculamos la fecha de hoy con uso de la libreria Datetime
año_actual = fecha_actual.year  # Aqui calculamos el año actual con uso de la libreria Datetime
mes_actual = fecha_actual.month # Aqui calculamos el mes actual con uso de la libreria Datetime   
dia_actual = fecha_actual.day   # Aqui calculamos el dia actual con uso de la libreria Datetime

# Esto nos servirá para poder calcular la edad de los estudiantes dada su fecha de nacimiento

#-------------------------------

#Datos Moderador 1

moderador0_nombre = 'Luis'
moderador0_email = 'luis@gmail.com'
moderador0_contraseña = '12345'
moderador0_estado = 'Activo'
idDeUsuarioModerador0 = 0

#-------------------------------

#Datos Moderador 1

moderador1_nombre = 'Carlos'
moderador1_email = 'Carlos@gmail.com'
moderador1_contraseña = '1234'
moderador1_estado = 'Activo'
idDeUsuarioModerador1 = 1

#-------------------------------

#Datos de Moderador nuevo

moderadorNuevo_nombre = ''
moderadorNuevo_email = ''
moderadorNuevo_contraseña = ''
moderadorNuevo_estado = ''
#----------------------------------

#Datos estudiante 1
estudiante0_nombre = 'Matias'
estudiante0_email = "mati@gmail.com"
estudiante0_estado = 'Activo'
estudiante0_contraseña = '123456'
estudiante0_sexo = 'Masculino'
idDeUsuarioEst0 = 0
estudiante0_nacimiento = '2006/06/13'
estudiante0_biografia = 'soy de arg dhy me huas ndu ah dh i ejoc acnanc a'
estudiante0_hobbies = 'me gusta hace futbol'
fechaNacimientoEst0 = datetime.strptime(estudiante0_nacimiento,'%Y/%m/%d')
añoNacimientoEst0 = fechaNacimientoEst0.year # Si queremos podemos validar el ingreso de la fecha de nacimiento. 
mesNacimientoEst0 = fechaNacimientoEst0.month
diaNacimientoEst0 = fechaNacimientoEst0.day 

#-------------------------------

#Datos estudiante 2
estudiante1_nombre = 'Alejo'
estudiante1_email = "alejo@gmail.com"
estudiante1_estado = 'Activo'
idDeUsuarioEst1 = 1
estudiante1_sexo = 'Masculino'
estudiante1_contraseña = '123457'
estudiante1_nacimiento = '2003/07/11'
estudiante1_biografia = 'soy de arg dhy me huas ndu ah dh i ejoc acnanc a'
estudiante1_hobbies = 'me gusta hace futbol'
fechaNacimientoEst1 = datetime.strptime(estudiante1_nacimiento,'%Y/%m/%d')
añoNacimientoEst1 = fechaNacimientoEst1.year
mesNacimientoEst1 = fechaNacimientoEst1.month
diaNacimientoEst1 = fechaNacimientoEst1.day

#-------------------------------

#Datos estudiante 3
estudiante2_nombre = 'Franco'
estudiante2_email = "franco@gmail.com"
idDeUsuarioEst2 = 2
estudiante2_contraseña = '123458'
estudiante2_sexo = 'Masculino'
estudiante2_estado = 'Activo'
estudiante2_nacimiento = '2004/01/12'
estudiante2_biografia = 'Me llamo Franco tengo 20 años y soy de la ciudad de Casilda'
estudiante2_hobbies = 'me gusta hace futbol'
fechaNacimientoEst2 = datetime.strptime(estudiante2_nacimiento,'%Y/%m/%d')
añoNacimientoEst2 = fechaNacimientoEst2.year
mesNacimientoEst2 = fechaNacimientoEst2.month
diaNacimientoEst2 = fechaNacimientoEst2.day

#-------------------------------
#Datos estudiante 4
estudiante3_nombre = 'Manuel'
estudiante3_email = "Manuel@gmail.com"
estudiante3_contraseña = '123459'
idDeUsuarioEst3 = 3
estudiante3_sexo = 'Masculino'
estudiante3_estado = 'Activo'
estudiante3_nacimiento = '2001/06/26'
estudiante3_biografia = 'Me llamo manuel...'
estudiante3_hobbies = 'me gusta hace futbol'
fechaNacimientoEst3 = datetime.strptime(estudiante3_nacimiento,'%Y/%m/%d')
añoNacimientoEst3 = fechaNacimientoEst3.year
mesNacimientoEst3 = fechaNacimientoEst3.month
diaNacimientoEst3 = fechaNacimientoEst3.day

#--------------------------------
#Datos del estudiante que se registra. De no registrarse quedan en blanco
estudianteNuevo_nombre = ''
estudianteNuevo_email = ''
estudianteNuevo_contraseña = ''
estudianteNuevo_estado = ''
estudianteNuevo_sexo = ''
estudianteNuevo_hobbies = ''
estudianteNuevo_biografia = ''
estudianteNuevo_fechaDeNacimiento = ''
fechaNacimientoEstNuevo = datetime.strptime(estudiante3_nacimiento,'%Y/%m/%d')
añoNacimientoEstNuevo = fechaNacimientoEstNuevo.year
mesNacimientoEstNuevo = fechaNacimientoEstNuevo.month
diaNacimientoEstNuevo = fechaNacimientoEstNuevo.day
#--------------------------------------

# EDADES DE LOS ESTUDIANTES

# Calculamos la edad del estudiante 1:

edadEst0 = 0  # Variable de tipo entero que guarda la edad del estudiante 1

if mes_actual < mesNacimientoEst0:
    edadEst0 = (año_actual - añoNacimientoEst0) - 1
elif mes_actual > mesNacimientoEst0:
    edadEst0 = año_actual - añoNacimientoEst0
else:
    if dia_actual < diaNacimientoEst0:
        edadEst0 = (año_actual - añoNacimientoEst0) - 1
    elif dia_actual >= diaNacimientoEst0:
        edadEst0 = año_actual - añoNacimientoEst0

# Calculamos la edad del estudiante 2:

edadEst1 = 0  # Variable de tipo entero que guarda la edad del estudiante 2

if mes_actual < mesNacimientoEst1:
    edadEst1 = (año_actual - añoNacimientoEst1) - 1
elif mes_actual > mesNacimientoEst1:
    edadEst1 = año_actual - añoNacimientoEst1
else:
    if dia_actual < diaNacimientoEst1:
        edadEst1 = (año_actual - añoNacimientoEst1) - 1
    elif dia_actual >= diaNacimientoEst1:
        edadEst1 = año_actual - añoNacimientoEst1
        
# Calculamos la edad del estudiante 3:

edadEst2 = 0 # Variable de tipo entero que guarda la edad del estudiante 3

if mes_actual < mesNacimientoEst2:
    edadEst2 = (año_actual - añoNacimientoEst2) - 1
elif mes_actual > mesNacimientoEst2:
    edadEst2 = año_actual - añoNacimientoEst2
else:
    if dia_actual < diaNacimientoEst2:
        edadEst2 = (año_actual - añoNacimientoEst2) - 1
    elif dia_actual >= diaNacimientoEst2:
        edadEst2 = año_actual - añoNacimientoEst2
    
# Calculamos la edad del estudiante 4:

edadEst3 = 0 # Variable de tipo entero que guarda la edad del estudiante 3

if mes_actual < mesNacimientoEst3:
    edadEst3 = (año_actual - añoNacimientoEst3) - 1
elif mes_actual > mesNacimientoEst2:
    edadEst2 = año_actual - añoNacimientoEst3
else:
    if dia_actual < diaNacimientoEst3:
        edadEst3 = (año_actual - añoNacimientoEst3) - 1
    elif dia_actual >= diaNacimientoEst3:
        edadEst3 = año_actual - añoNacimientoEst3
    
# Constantes del Programa        
#--------------------------------- 
ArrayEstudiantes = [-1] * 8 # mails?
ArrayModeradores = [-1] * 4 # Mails?



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
          
def carga(array1,array2):
    for i in range(4):
        array1[i] = i # En la posicion i del arreglo de estudiantes, esta el estudiante i
    array2[0] = 0 #moderador 0
    array2[1] = 1 #moderador 1
    
def posicionAregistrarse(array:list,long):
    i = 0
    while array[i] != '' and i < long:
        i += 1
    if array[i] == '':
        return i

def busqueda(array,valor,long):
    inf = 0
    sup = long - 1
    med = (inf + sup) // 2
    while array [med] != valor and inf <= sup:
        if array[med] > valor:
            sup = med - 1
        else:
            inf = med + 1
    if array[med] == valor:
        return True
    else:
        return False
    

def registro(array,posicion,valor):
    array[posicion] = valor

def retornarEstadoDeEstudianteCargados(id):
    match id:
        case 0: return estudiante0_estado
        case 1: return estudiante1_estado
        case 2: return estudiante2_estado
        case 3: return estudiante3_estado
          
def logueoCorrecto(emailIngresado,contraseñaIngresada):
    if emailIngresado == estudiante0_email and contraseñaIngresada == estudiante0_contraseña and estudiante0_estado == 'Activo':
        return 0
    if emailIngresado == estudiante1_email and contraseñaIngresada == estudiante1_contraseña and estudiante1_estado == 'Activo':
        return 1
    if emailIngresado == estudiante2_email and contraseñaIngresada == estudiante2_contraseña and estudiante2_estado == 'Activo':
        return 2
    if emailIngresado == estudiante3_email and contraseñaIngresada == estudiante3_contraseña and estudiante3_estado == 'Activo':
        return 3
    if emailIngresado == estudianteNuevo_email and contraseñaIngresada == estudianteNuevo_contraseña and estudianteNuevo_estado == 'Activo':
        return 4
    if emailIngresado == moderador0_email and contraseñaIngresada == moderador0_contraseña and moderador0_estado == 'Activo':
        return 0
    if emailIngresado == moderador1_email and contraseñaIngresada == moderador1_contraseña and moderador1_estado == 'Activo':
        return 1
    if emailIngresado == moderadorNuevo_email and contraseñaIngresada == moderadorNuevo_contraseña and moderadorNuevo_estado == 'Activo':
        return 2
    return -1
                
        
        
        
        
        

carga(ArrayEstudiantes,ArrayModeradores)
#Cargo los 4 estudiantes en el arreglo([0,1,2,3] => ID) y el moderador en el arreglo([0])
print('Bienvenido! ')
opc = input('Desesa loguearte (Responde -l-) o Registrarte (Responde -r-) ?: ').lower
while opc != 'l' and opc != 'r':
    print('Error. Por favor Responde -l- o -r-')
    opc = input('Desesa loguearte (Responde -l-) o Registrarte (Responde -r-) ?: ').lower
if opc == 'r':
    print('Registrate aquí!')
    moderadorOEstudiante = input('Eres moderador (Responde -m-) o estudiante (Responde -e-)?: ').lower
    while moderadorOEstudiante != 'm' and moderadorOEstudiante != 'e':
        print('Error! Por favor responde -m- o -e-')
        moderadorOEstudiante = input('Eres moderador (Responde -m-) o estudiante (Responde -e-)?: ').lower
    if moderadorOEstudiante == 'm' and ArrayModeradores[3] == '':
        print('Dinos tus Datos! \n')    
        moderadorNuevo_nombre = input('Ingresa tu nombre: ')
        moderadorNuevo_email = input('Ingresa tu email: ')
        moderadorNuevo_contraseña = input('Ingresa tu contraseña: ')
        moderadorNuevo_estado = input('Ingresa tu estado: ')
        ArrayModeradores[posicionAregistrarse(ArrayModeradores,4)] = posicionAregistrarse(ArrayModeradores,4)
        idDeNuevoModerador = posicionAregistrarse(ArrayModeradores,4)
    if moderadorOEstudiante == 'e' and ArrayEstudiantes[7] == '':
        print('Dinos tus datos \n')
        estudianteNuevo_nombre = input('Ingresa tu nombre')
        estudianteNuevo_email = input('Ingresa tu email')
        estudianteNuevo_contraseña = input('Ingresa tu contraseña')
        estudianteNuevo_estado = input('Ingresa tu estado')
        estudianteNuevo_sexo = input('')
        estudianteNuevo_hobbies = input('Ingresa tus hobbies')
        estudianteNuevo_biografia = input('Ingresa tu biografia')
        estudianteNuevo_fechaDeNacimiento = input('Ingresa tu fecha de nacimiento (año/mes/dia)') #validar!
        # Sacar su edad
        ArrayEstudiantes[posicionAregistrarse(ArrayEstudiantes,8)] = posicionAregistrarse(ArrayEstudiantes,8)
        idDeNuevoEstudiante = posicionAregistrarse(ArrayEstudiantes,8)
    else:
        print('Ya no puedes registrarte como estudiante! ')
elif opc == 'l':
    print('Log in')
    emailIngresado = input('Ingrese su mail: ')
    contraseñaIngresada = getpass_custom('Ingrese su contraseña: ')
    intentos = 2
    while  (logueoCorrecto(emailIngresado,contraseñaIngresada) == -1) and intentos > 0:
        print('Email y/o contraseña incorrecta')
        emailIngresado = input('Ingrese su mail: ')
        contraseñaIngresada = getpass_custom('Ingrese su contraseña: ') 
        intentos -= 1
        
        
        
            
            
            

            
                
            
             
            
            
        
        
    



































# logOReg = input('log o reg (l 0 r): ')
# while logOReg != 'l' and logOReg != 'r':
#     print('Error! por favor elige -l- o -r- : ')
#     logOReg = input('log o reg (l 0 r): ')
# if logOReg == 'r':
#     print('Registrate')
#     modOEst = input('Mod o est: ')
#     if modOEst == 'e':
#         carga(ArrayEstudiantes,8)
#     else:
#         carga(ArrayModeradores,4)
# while logOReg == 'l' and ArrayEstudiantes[3] == '' and ArrayModeradores[0] == '':
#     if ArrayEstudiantes[3] == '':
#         print('No puedes loguearte ya que no hay 4 estudiantes')
#     elif ArrayModeradores[0] == '':
#         print('No puedes loguearte ya que no hay 1 moderador')
# if logOReg == 'l' and ArrayEstudiantes[3] != '' and ArrayModeradores[0] != '':
#     emailUsuario = input('Ingrese su Email: ')
#     contraseñaIngresada = getpass_custom('Ingrese su contraseña: ')
#     intentos = 2
#     if ((emailUsuario != Estudiante0[0] or contraseñaIngresada != Estudiante0[1] and Estudiante0[2] != 'Activo') \
#         and (emailUsuario != estudiante0[0] or contraseñaIngresada != estudiante0[1] and estudiante0[2] != 'Activo')\
#             and (emailUsuario != estudiante1[0] or contraseñaIngresada != estudiante1[1] and estudiante1[2] != 'Activo')\
#                 and (emailUsuario != estudiante2[0] or contraseñaIngresada != estudiante2[1] and estudiante2[2] != 'Activo')\
#                     and (emailUsuario != estudiante3[0] or contraseñaIngresada != estudiante3[1] and estudiante3[2] != 'Activo')\
#                         and (emailUsuario != Estudiante5[0] or contraseñaIngresada != Estudiante5[1] and Estudiante5[2] != 'Activo')\
#                             and (emailUsuario != Estudiante6[0] or contraseñaIngresada != Estudiante6[1] and Estudiante6[2] != 'Activo')\
#                                 and (emailUsuario != Estudiante7[0] or contraseñaIngresada != Estudiante7[1] and Estudiante7[2] != 'Activo')\
#                                     and (emailUsuario != Moderador0[0] or contraseñaIngresada != Moderador0[1] and Moderador0[2] != 'Activo')\
#                                         and (emailUsuario != Moderador1[0] or contraseñaIngresada != Moderador1[1] and Moderador1[2] != 'Activo')\
#                                             and (emailUsuario != Moderador2[0] or contraseñaIngresada != Moderador2[1] and Moderador2[2] != 'Activo')\
#                                                 and (emailUsuario != Moderador3[0] or contraseñaIngresada != Moderador3[1] and Moderador3[2] != 'Activo')):



#                     print()













