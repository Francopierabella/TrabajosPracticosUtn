import os 
import os.path
import pickle
import io
import msvcrt
import sys
from datetime import datetime
from datetime import date



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


class estudiante:
    def __init__(self):
        self.id = 0
        self.nombre = ''
        self.email = ''
        self.contraseña = ''
        self.sexo = ''
        self.estado = False
        self.datosPersonales = [''] * 9 #0 hobbies, 1 materiaFav, 2 deporteFav, 3 materiaFuerte, 4 materiaDebil, 5 bio, 6 pais, 7 ciudad, 8 fechaDeNacimiento. VALIDAR TODO!!!  

class moderador:
    def __init__(self):
        self.id = 0
        self.email = ''
        self.contraseña = ''
        self.estado = False
        
class administrador:
    def __init__(self):
        self.id = 0
        self.email = ''
        self.contraseña = ''
        

    
def busquedaSecuencialDeId(vfa,vla,id) -> int:
    tamañoArchivo = os.path.getsize(vfa)
    pos = 0
    vla.seek(0,0)
    variableDeRegistro = pickle.load(vla)
    while vla.tell() < tamañoArchivo and variableDeRegistro.id != id:
        pos = vla.tell()
        variableDeRegistro = pickle.load(vla)
    if variableDeRegistro.id.strip() == id.strip():
        return pos
    return -1

def contarRegistros(vfE,vlE) -> int:
    vlE.seek(0,0)
    tamArchivo = os.path.getsize(vfE)
    if tamArchivo == 0: 
        return 0
    vr = pickle.load(vlE)
    tamRegistro = vlE.tell()
    cantRegistros = tamArchivo // tamRegistro
    return cantRegistros

def busquedaSecuencialDeEmail(variableFisicaArchivo,variableLogicaArchivo,email) -> int:
    tamañoArchivo = os.path.getsize(variableFisicaArchivo)
    if tamañoArchivo == 0:
        return -1
    else:
        pos = 0
        variableLogicaArchivo.seek(0,0)
        variableDeRegistro = pickle.load(variableLogicaArchivo)
        while (variableLogicaArchivo.tell() < tamañoArchivo) and (variableDeRegistro.email.strip() != email.strip()):
            pos = variableLogicaArchivo.tell()
            variableDeRegistro = pickle.load(variableLogicaArchivo)
        if variableDeRegistro.email.strip() == email.strip():
            return pos
        return -1


def formatearEstudiantes(variableDeRegistro) -> None:
    variableDeRegistro.id = str(variableDeRegistro.id).ljust(5,' ')
    variableDeRegistro.email = str(variableDeRegistro.email).ljust(32,' ')
    variableDeRegistro.nombre = str(variableDeRegistro.nombre).ljust(32,' ')
    variableDeRegistro.contraseña = str(variableDeRegistro.contraseña).ljust(32,' ')
    variableDeRegistro.estado = str(variableDeRegistro.estado).ljust(5,' ') 
    variableDeRegistro.datosPersonales[0] = str(variableDeRegistro.datosPersonales[0]).ljust(255,' ') 
    variableDeRegistro.datosPersonales[1] = str(variableDeRegistro.datosPersonales[1]).ljust(16,' ')
    variableDeRegistro.datosPersonales[2] = str(variableDeRegistro.datosPersonales[2]).ljust(16,' ')
    variableDeRegistro.datosPersonales[3] = str(variableDeRegistro.datosPersonales[3]).ljust(16,' ')
    variableDeRegistro.datosPersonales[4] = str(variableDeRegistro.datosPersonales[4]).ljust(16,' ')
    variableDeRegistro.datosPersonales[5] = str(variableDeRegistro.datosPersonales[5]).ljust(255,' ')
    variableDeRegistro.datosPersonales[6] = str(variableDeRegistro.datosPersonales[6]).ljust(32,' ')
    variableDeRegistro.datosPersonales[7] = str(variableDeRegistro.datosPersonales[7]).ljust(32,' ')
    
def formatearMods(variableDeRegistro) -> None:
    variableDeRegistro.id = str(variableDeRegistro.id).ljust(3,' ')
    variableDeRegistro.email = str(variableDeRegistro.email).ljust(32,' ')
    variableDeRegistro.contraseña = str(variableDeRegistro.contraseña).ljust(32,' ')
    variableDeRegistro.estado = str(variableDeRegistro.estado).ljust(5,' ')

def formatearAdmins(variableDeRegistro) -> None:
    variableDeRegistro.id = str(variableDeRegistro.id).ljust(3,' ')
    variableDeRegistro.email = str(variableDeRegistro.email).ljust(32,' ')
    variableDeRegistro.contraseña = str(variableDeRegistro.contraseña).ljust(32,' ')

def altaAdmins(varFisicaAdmi,varLogicaAdmi,varFisicaMods,varLogicaMods,varFisicaEst,varLogicaEst) -> None:
    # os.system('cls')
    print('Hola Administrador! ')
    print('')
    print('Carga aqui tus datos! ')
    print('')
    varLogicaAdmi.seek(0,2)
    variableDeRegistroAdmins = administrador()
    variableDeRegistroAdmins.id = contarRegistros(varFisicaAdmi,varLogicaAdmi)
    variableDeRegistroAdmins.email = input('Ingresa tu email: ')
    while busquedaSecuencialDeEmail(varFisicaAdmi,varLogicaAdmi,variableDeRegistroAdmins.email) != -1 or \
            busquedaSecuencialDeEmail(varFisicaEst,varLogicaEst,variableDeRegistroAdmins.email) != -1 or \
                busquedaSecuencialDeEmail(varFisicaMods,varLogicaMods,variableDeRegistroAdmins.email) != -1 :
                    print('Ese email ya esta en uso! Intenta de nuevo. ')
                    variableDeRegistroAdmins.email = input('Ingrese su email: ')
    variableDeRegistroAdmins.contraseña = getpass_custom('Ingrese su contraseña: ')
    formatearAdmins(variableDeRegistroAdmins)
    pickle.dump(variableDeRegistroAdmins,varLogicaAdmi)
    varLogicaAdmi.flush()
    os.system('pause')
    
    

def altaModerador(varFisicaAdmi,varLogicaAdmi,varFisicaMods,varLogicaMods,varFisicaEst,varLogicaEst) -> None: 
    # os.system('cls')
    print('Hola Moderador!')
    print()
    print('Carga aqui tus datos !')
    print()
    varLogicaMods.seek(0,2)
    variableDeRegistroMods = moderador()
    variableDeRegistroMods.id = contarRegistros(varFisicaMods,varLogicaMods)
    variableDeRegistroMods.email = input('Ingrese su email: ')
    while (busquedaSecuencialDeEmail(varFisicaAdmi,varLogicaAdmi,variableDeRegistroMods.email) != -1 or \
            busquedaSecuencialDeEmail(varFisicaEst,varLogicaEst,variableDeRegistroMods.email) != -1 or \
                busquedaSecuencialDeEmail(varFisicaMods,varLogicaMods,variableDeRegistroMods.email) != -1 ):
                    print('Ese email ya esta en uso! Intenta de nuevo. ')
                    variableDeRegistroMods.email = input('Ingrese su email: ')
    variableDeRegistroMods.contraseña = getpass_custom('Ingrese su contraseña: ')
    variableDeRegistroMods.estado = True if varLogicaMods.tell() == 0 else False
    formatearMods(variableDeRegistroMods)
    pickle.dump(variableDeRegistroMods,varLogicaMods)
    varLogicaMods.flush()
    os.system('pause')
    
    
def altaEstudiantes(varFisicaAdmi,varLogicaAdmi,varFisicaMods,varLogicaMods,varFisicaEst,varLogicaEst) -> None:
    # os.system('cls')
    print('Hola Estudiante!')
    print()
    print('Carga aqui tus datos! ')
    print()
    varLogicaEst.seek(0,2)
    print(varLogicaEst.tell(), '.tell() alta estudiantes: ')
    variableDeRegistroEstuditante = estudiante()
    variableDeRegistroEstuditante.id = contarRegistros(varFisicaEst,varLogicaEst)
    variableDeRegistroEstuditante.nombre = input('Ingresa tu Nombre: ')
    variableDeRegistroEstuditante.email = input('Ingrese su email: ')
    while (busquedaSecuencialDeEmail(varFisicaAdmi,varLogicaAdmi,variableDeRegistroEstuditante.email) != -1) or \
            (busquedaSecuencialDeEmail(varFisicaEst,varLogicaEst,variableDeRegistroEstuditante.email) != -1) or \
                (busquedaSecuencialDeEmail(varFisicaMods,varLogicaMods,variableDeRegistroEstuditante.email) != -1) :
                    print('Ese email ya esta en uso! Intenta de nuevo. ')
                    variableDeRegistroEstuditante.email = input('Ingrese su email: ')
    variableDeRegistroEstuditante.contraseña = getpass_custom('Ingrese su contraseña: ')
    variableDeRegistroEstuditante.sexo = input('Sexo: (F o M)').upper()
    while variableDeRegistroEstuditante.sexo != 'M' and variableDeRegistroEstuditante.sexo != 'F': 
        print('Sexo Invalido. Intenta de nuevo.')
        variableDeRegistroEstuditante.sexo = input('Sexo: (F o M)').upper()
    estado = input('Ingresa tu estado, 1 (Activo) 0 (Inactivo): ')
    while estado != '1' and estado != '0':
        print('Estado Incorrecto! ingresa 0 o 1 por favor!')
        estado = input('Ingresa tu estado, 1 (Activo) 0 (Inactivo): ')
    variableDeRegistroEstuditante.estado = True if estado == '1' else False
    variableDeRegistroEstuditante.datosPersonales[0] = input('Ingresa tus hobbies: ')
    variableDeRegistroEstuditante.datosPersonales[1] = input('Ingresa tu materia favorita: ')
    variableDeRegistroEstuditante.datosPersonales[2] = input('Ingresa tu deporte favorito: ')
    variableDeRegistroEstuditante.datosPersonales[3] = input('Ingresa tu materia fuerte: ')
    variableDeRegistroEstuditante.datosPersonales[4] = input('Ingresa tu materia debil: ')
    variableDeRegistroEstuditante.datosPersonales[5] = input('Ingresa tu biografia: ')
    variableDeRegistroEstuditante.datosPersonales[6] = input('Ingresa tu pais: ')
    variableDeRegistroEstuditante.datosPersonales[7] = input('Ingresa tu ciudad: ')
    ok = False
    while not ok:
        try:
            fecha = input('Ingresa su fecha de nacimiento (aaaa/mm/dd): ')
            datetime.strptime(fecha,'%Y/%m/%d')
            variableDeRegistroEstuditante.datosPersonales[8] = fecha
            ok = True
        except: 
            print('Fecha invalida. Intenta de nuevo!')
    formatearEstudiantes(variableDeRegistroEstuditante)
    pickle.dump(variableDeRegistroEstuditante,varLogicaEst)
    varLogicaEst.flush()
    os.system('pause')

def chequearEmail_contraseña(varFisicaArchivo,varLogicaArchivo,contraseña,pos) -> int:
    if pos != -1:
        varLogicaArchivo.seek(pos,0)
        variableDeRegistro = pickle.load(varLogicaArchivo)
        if variableDeRegistro.contraseña.strip() == contraseña.strip():
            if varFisicaArchivo != variableDeArchivoFisicoAdministradores:
                if variableDeRegistro.estado.strip() == 'True': 
                    return 1
                else:
                    print('Usuario INACTIVO => Logueo Invalido ')
            else: 
                return 1
    return 0

def devolvertamañoDeRegistro(vfa,vla):
    if os.path.getsize(vfa) == 0:
        return 0
    aux = vla.tell()
    vla.seek(0,0)
    vr = pickle.load(vla)
    tamaño = vla.tell()
    vla.seek(aux,0)
    return tamaño

def logueo(varFisicaAdmi,varLogicaAdmi,varFisicaMods,varLogicaMods,varFisicaEst,varLogicaEst) -> str:
    print('---------- LOG IN -----------')
    print()
    intentos = 2
    emailIngresado = input('Ingresa tu email: ')
    contraseñaIngresada = getpass_custom('Ingresa tu contrasaña: ')
    tipo = ''
    posEstudiante = busquedaSecuencialDeEmail(varFisicaEst,varLogicaEst,emailIngresado)
    posModeradores = busquedaSecuencialDeEmail(varFisicaMods,varLogicaMods,emailIngresado)
    posAdministradores = busquedaSecuencialDeEmail(varFisicaAdmi,varLogicaAdmi,emailIngresado)
    # print('=> busqueda secuencial estudiantes = ',busquedaSecuencialDeEmail(varFisicaEst,varLogicaEst,emailIngresado), ' Cheq = ',chequearEmail_contraseña(varLogicaEst,contraseñaIngresada,posEstudiante))
    # print('=> busqueda secuencial mods = ',busquedaSecuencialDeEmail(varFisicaMods,varLogicaMods,emailIngresado),' Cheq = ',chequearEmail_contraseña(varFisicaMods,varLogicaMods,emailIngresado,contraseñaIngresada))
    # print('=> busqueda secuencial admis = ',busquedaSecuencialDeEmail(varFisicaAdmi,varLogicaAdmi,emailIngresado),' Cheq = ',chequearEmail_contraseña(varFisicaAdmi,varLogicaAdmi,emailIngresado,contraseñaIngresada))
    
    while  (posEstudiante == -1 or chequearEmail_contraseña(varFisicaEst,varLogicaEst,contraseñaIngresada,posEstudiante) == 0) and \
            (posModeradores == -1 or chequearEmail_contraseña(varFisicaMods,varLogicaMods,contraseñaIngresada,posModeradores) == 0) and \
                (posAdministradores == -1 or chequearEmail_contraseña(varFisicaAdmi,varLogicaAdmi,contraseñaIngresada,posAdministradores) == 0) \
                and intentos > 0:
                    print('Logueo INCORRECTO. Intenta de nuevo: \n')
                    varLogicaAdmi.seek(0,0)
                    varLogicaMods.seek(0,0)
                    varLogicaEst.seek(0,0)
                    emailIngresado = input('Ingresa tu email: ')
                    contraseñaIngresada = getpass_custom('Ingresa tu contrasaña: ')
                    intentos -= 1
                    posEstudiante = busquedaSecuencialDeEmail(varFisicaEst,varLogicaEst,emailIngresado)
                    posModeradores = busquedaSecuencialDeEmail(varFisicaMods,varLogicaMods,emailIngresado)
                    posAdministradores = busquedaSecuencialDeEmail(varFisicaAdmi,varLogicaAdmi,emailIngresado)
    if intentos == 0:
        print('Te has quedado sin intentos. Vuelve mas tarde! ')
    else:
        if posEstudiante != -1:
            tipo = 'e'
        elif posModeradores != -1:
            tipo = 'm'
        else:
            tipo = 'a'
    return tipo
            

def mostrarRegistros (vla,vfa) -> None:
    tam = os.path.getsize(vfa)
    if tam != 0:
        vla.seek(0,0)
        while vla.tell() < tam :
            reg = pickle.load(vla)
            print('ID: ',reg.id.strip(), 'Nombre: ',reg.nombre.strip(),' Email: ',reg.email.strip(), ' Contraseña: ',reg.contraseña.strip())
    os.system('pause')
    

def menuDeLogueo() -> None:
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
    print('2. Registro (Estudiantes unicamente) ')
    print()
    print('0. Salir')
# --------------------------------------------------------------------
# MENUS ESTUDIANTE 

def menuPrincipalEstudiante() -> None:
    os.system('cls')
    print()
    print()
    print()
    print('------------------------------')
    print()
    print('MENU PRINCIPAL')
    print()
    print('1. Gestionar mi perfil: ')
    print()
    print('2. Gestionar candidatos: ')
    print()
    print('3. Matcheos: ')
    print()
    print('4. Reportes estadisticos ')
    print()
    print('0. Salir:')  
    os.system('pause')
    

def MostrarOpcionesDeGestionarMiperfil():
    os.system('cls')
    print('                     GESTIONAR MI PERFIL ')
    print()
    print('------------------------------')
    print()
    print('a. Editar mis datos personales. ')
    print()
    print('b. Eliminar mi perfil. ')
    print()
    print('c. Volver')
    print()
    
def mostrarOpcionesDeGestionarCandidatos():
    os.system('cls') 
    print('                     GESTIONAR CANDIDATOS')
    print()
    print('------------------------------')
    print()
    print('a. Ver candidatos ')
    print()
    print('b. Reportar un candidato. ')
    print()
    print('c. Volver') 
    print()
    
def mostrarOpcionesDeMatcheos():
    os.system('cls')
    print('                       MATCHEOS ') 
    print()
    print('a. Ver matcheos')
    print()
    print('b. Eliminar un matcheo')
    print()
    print('c. Volver')   
    
# --------------------------------------------------------------------

# --------------------------------------------------------------------
# Menus MODERADORES

def menuPrincipalModeradores():
    os.system('cls')
    print()
    print('------------------------------')
    print()
    print('MENU PRINCIPAL')
    print()
    print('1. Gestionar Usuarios')
    print()
    print('2. Gestionar Reportes')
    print()
    print('3. Reportes Estadisticos')
    print()
    print('0. Volver')
    
def mostrarOpcionesDeGestionarUsuarios():
    os.system('cls') 
    print()
    print('                       GESTIONAR USUARIOS')
    print()
    print('a. Desactivar usuario')
       
    
def main():
    # Antes de entrar al menu de logueo, debemos pre cargar un admi y un mod.
    # El usuario no va a poder loguearse hasta que no halla 4 estudiantes.
    os.system('cls')
    print('Pre-Carga de administrador y De moderador.')
    os.system('pause')
    if os.path.getsize(variableDeArchivoFisicoAdministradores) == 0:
        altaAdmins(variableDeArchivoFisicoAdministradores,variableDeArchivoLogicaAdministradores,variableDeArchivoFisicoModeradores,variableDeArchivoLogicaModeradores, \
                variableDeArchivoFisicoEstudiantes,variableDeArchivoLogicaEstudiantes)
    if os.path.getsize(variableDeArchivoFisicoModeradores) == 0:
        altaModerador(variableDeArchivoFisicoAdministradores,variableDeArchivoLogicaAdministradores,variableDeArchivoFisicoModeradores,variableDeArchivoLogicaModeradores, \
                variableDeArchivoFisicoEstudiantes,variableDeArchivoLogicaEstudiantes)
    logOReg = '1'
    while logOReg != '0':
        variableDeArchivoLogicaAdministradores.seek(0,0)
        variableDeArchivoLogicaEstudiantes.seek(0,0)
        variableDeArchivoLogicaModeradores.seek(0,0)
        menuDeLogueo()
        logOReg = input('Elige una opcion: ')
        while logOReg != '0' and logOReg != '1' and logOReg != '2':
            print('Opcion Invalida! Intenta de nuevo. ')
            logOReg = input('Elige una opcion: ')
        if logOReg == '1':
            cantEstudiantes = contarRegistros(variableDeArchivoFisicoEstudiantes,variableDeArchivoLogicaEstudiantes)
            # cantMods = contarRegistros(variableDeArchivoFisicoModeradores,variableDeArchivoLogicaModeradores)
            # cantAdmins = contarRegistros(variableDeArchivoFisicoAdministradores,variableDeArchivoLogicaAdministradores)
            if cantEstudiantes < 4 :
                print('No puedes loguearte! Tiene que haber minimo 4. En este momento existen ',cantEstudiantes,' estudiantes')
                os.system('pause')
            else:
                print('REGISTROS: ')
                mostrarRegistros(variableDeArchivoLogicaEstudiantes,variableDeArchivoFisicoEstudiantes)
                tipoDeUsuarioLogueado = logueo(variableDeArchivoFisicoAdministradores,variableDeArchivoLogicaAdministradores,variableDeArchivoFisicoModeradores,variableDeArchivoLogicaModeradores , \
                    variableDeArchivoFisicoEstudiantes,variableDeArchivoLogicaEstudiantes)
                if tipoDeUsuarioLogueado == 'e': 
                    posDelRegistroDelEstudianteLogueado = variableDeArchivoLogicaEstudiantes.tell() - devolvertamañoDeRegistro(variableDeArchivoFisicoEstudiantes,variableDeArchivoLogicaEstudiantes)
                    print('Se logueo un estudiante! Su posicion en el archivo es: ',posDelRegistroDelEstudianteLogueado)
                    input()
                    # menuPrincipalEstudiante()
                elif tipoDeUsuarioLogueado == 'm':
                    posDelRegistroDelModeradorLogueado = variableDeArchivoLogicaModeradores.tell() - devolvertamañoDeRegistro(variableDeArchivoFisicoModeradores,variableDeArchivoLogicaModeradores)
                    print('Se logueo un Moderador! Su posicion en el registro es: ',posDelRegistroDelModeradorLogueado)

                    input()
                elif tipoDeUsuarioLogueado == 'a':
                    posDelRegistroDelAdmintradorLogueado = variableDeArchivoLogicaAdministradores.tell() - devolvertamañoDeRegistro(variableDeArchivoFisicoAdministradores,variableDeArchivoLogicaAdministradores)
                    print('Se logueo el adminsitrador! Su posicion en el registro es: ',posDelRegistroDelAdmintradorLogueado)
                    input()
                else:
                    print('No se logueo nadie. Vuelve mas tarde')
                    logOReg = '0'
                
                
        elif logOReg == '2':
            altaEstudiantes(variableDeArchivoFisicoAdministradores,variableDeArchivoLogicaAdministradores,variableDeArchivoFisicoModeradores,variableDeArchivoLogicaModeradores, \
                variableDeArchivoFisicoEstudiantes,variableDeArchivoLogicaEstudiantes)
        else:
            print('Hasta Luego! ')

    variableDeArchivoLogicaAdministradores.close()
    variableDeArchivoLogicaEstudiantes.close()
    variableDeArchivoLogicaModeradores.close()
    
    
variableDeArchivoFisicoEstudiantes = 'C:\\ayed\\Estudiantes.dat'
variableDeArchivoFisicoModeradores = 'C:\\ayed\\Moderadores.dat'
variableDeArchivoFisicoAdministradores = 'C:\\ayed\\Administradores.dat'

if not os.path.exists(variableDeArchivoFisicoAdministradores):
    variableDeArchivoLogicaAdministradores = open (variableDeArchivoFisicoAdministradores,'w+b')
else: 
    variableDeArchivoLogicaAdministradores = open (variableDeArchivoFisicoAdministradores,'r+b')
if not os.path.exists(variableDeArchivoFisicoModeradores):
    variableDeArchivoLogicaModeradores = open (variableDeArchivoFisicoModeradores,'w+b')
else:
    variableDeArchivoLogicaModeradores = open (variableDeArchivoFisicoModeradores,'r+b')
if not os.path.exists(variableDeArchivoFisicoEstudiantes):
    variableDeArchivoLogicaEstudiantes = open (variableDeArchivoFisicoEstudiantes,'w+b')
else:
    variableDeArchivoLogicaEstudiantes = open (variableDeArchivoFisicoEstudiantes,'r+b')
       
main()