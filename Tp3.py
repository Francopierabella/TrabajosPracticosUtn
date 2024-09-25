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
        

def menuDeLogueo() -> None:
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
    print('2. Registro (Estudiantes unicamente) ')
    print()
    print('0. Salir')
    
def busquedaSecuencialDeId(vfa,vla,id) -> int:
    tamañoArchivo = os.path.getsize(vfa)
    pos = 0
    vla.seek(0,0)
    variableDeRegistro = pickle.load(vla)
    while vla.tell() < tamañoArchivo and variableDeRegistro.id != id:
        pos = vla.tell()
        variableDeRegistro = pickle.load(vla)
    if variableDeRegistro.id == id:
        return pos
    return -1

def contarRegistros(vfE,vlE) -> int:
    
    tamArchivo = os.path.getsize(vfE)
    if tamArchivo == 0: 
        return 0
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
        while variableLogicaArchivo.tell() < tamañoArchivo and variableDeRegistro.email != email:
            pos = variableLogicaArchivo.tell()
            variableDeRegistro = pickle.load(variableLogicaArchivo)
        if variableDeRegistro.email == email:
            return pos
        return -1


def formatearEstudiantes(variableDeRegistro) -> None:
    variableDeRegistro.id = str(variableDeRegistro.id).ljust(5,'')
    variableDeRegistro.email = str(variableDeRegistro.email).ljust(32,'')
    variableDeRegistro.nombre = str(variableDeRegistro.nombre).ljust(32,'')
    variableDeRegistro.contraseña = str(variableDeRegistro.contraseña).ljust(32,'')
    variableDeRegistro.estado = str(variableDeRegistro.estado).ljust(5,'')
    variableDeRegistro.datosPersonales[0] = str(variableDeRegistro.datosPersonales[0]).ljust(255,'') 
    variableDeRegistro.datosPersonales[1] = str(variableDeRegistro.datosPersonales[1]).ljust(16,'')
    variableDeRegistro.datosPersonales[2] = str(variableDeRegistro.datosPersonales[2]).ljust(16,'')
    variableDeRegistro.datosPersonales[3] = str(variableDeRegistro.datosPersonales[3]).ljust(16,'')
    variableDeRegistro.datosPersonales[4] = str(variableDeRegistro.datosPersonales[4]).ljust(16,'')
    variableDeRegistro.datosPersonales[5] = str(variableDeRegistro.datosPersonales[5]).ljust(255,'')
    variableDeRegistro.datosPersonales[6] = str(variableDeRegistro.datosPersonales[6]).ljust(32,'')
    variableDeRegistro.datosPersonales[7] = str(variableDeRegistro.datosPersonales[7]).ljust(32,'')
    
def formatearMods(variableDeRegistro) -> None:
    variableDeRegistro.id = str(variableDeRegistro.id).ljust(3,'')
    variableDeRegistro.email = str(variableDeRegistro.email).ljust(32,'')
    variableDeRegistro.contraseña = str(variableDeRegistro.contraseña).ljust(32,'')
    variableDeRegistro.estado = str(variableDeRegistro.estado).ljust(5,'')

def formatearAdmins(variableDeRegistro) -> None:
    variableDeRegistro.id = str(variableDeRegistro.id).ljust(3,'')
    variableDeRegistro.email = str(variableDeRegistro.email).ljust(32,'')
    variableDeRegistro.contraseña = str(variableDeRegistro.contraseña).ljust(32,'')

def altaAdmins(varFisicaAdmi,varLogicaAdmi,varFisicaMods,varLogicaMods,varFisicaEst,varLogicaEst) -> None:
    os.system('cls')
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
    

def altaModerador(varFisicaAdmi,varLogicaAdmi,varFisicaMods,varLogicaMods,varFisicaEst,varLogicaEst) -> None: 
    varLogicaMods.seek(0,2)
    variableDeRegistroMods = moderador()
    variableDeRegistroMods.id = contarRegistros(varFisicaMods,varLogicaMods)
    variableDeRegistroMods.email = input('Ingrese su email: ')
    while busquedaSecuencialDeEmail(varFisicaAdmi,varLogicaAdmi,variableDeRegistroMods.email) != 1 and \
            busquedaSecuencialDeEmail(varFisicaEst,varLogicaEst,variableDeRegistroMods.email) != 1 and \
                busquedaSecuencialDeEmail(varFisicaMods,varLogicaMods,variableDeRegistroMods.email) != 1 :
                    print('Ese email ya esta en uso! Intenta de nuevo. ')
                    variableDeRegistroMods.email = input('Ingrese su email: ')
    variableDeRegistroMods.contraseña = getpass_custom('Ingrese su contraseña: ')
    variableDeRegistroMods.estado = False if varLogicaMods.tell() == 0 else True
    formatearMods(variableDeRegistroMods)
    pickle.dump(variableDeRegistroMods,varLogicaMods)
    varLogicaMods.flush()
    
def altaEstudiantes(varFisicaAdmi,varLogicaAdmi,varFisicaMods,varLogicaMods,varFisicaEst,varLogicaEst) -> None:
    varLogicaEst.seek(0,2)
    variableDeRegistroEstuditante = estudiante()
    variableDeRegistroEstuditante.id = contarRegistros(varFisicaEst,varLogicaEst)
    variableDeRegistroEstuditante.nombre = input('Ingresa tu Nombre: ')
    variableDeRegistroEstuditante.email = input('Ingrese su email: ')
    while busquedaSecuencialDeEmail(varFisicaAdmi,varLogicaAdmi,variableDeRegistroEstuditante.email) != 1 and \
            busquedaSecuencialDeEmail(varFisicaEst,varLogicaEst,variableDeRegistroEstuditante.email) != 1 and \
                busquedaSecuencialDeEmail(varFisicaMods,varLogicaMods,variableDeRegistroEstuditante.email) != 1 :
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

def chequearEmail_contraseña(varLogicaArchivo,contraseña) -> int:
    variableDeRegistro = pickle.load(varLogicaArchivo)
    if variableDeRegistro.contraseña == contraseña:
        return 1
    return 0

def logueo(varFisicaAdmi,varLogicaAdmi,varFisicaMods,varLogicaMods,varFisicaEst,varLogicaEst) -> str:
    print('---------- LOG IN -----------')
    print()
    intentos = 2
    emailIngresado = input('Ingresa tu email: ')
    contraseñaIngresada = getpass_custom('Ingresa tu contrasaña: ')
    tipo = ''
    while  ((busquedaSecuencialDeEmail(varFisicaEst,varLogicaEst,emailIngresado) == -1 and chequearEmail_contraseña(varLogicaEst,contraseñaIngresada) == 0) or \
            (busquedaSecuencialDeEmail(varFisicaMods,varLogicaMods,emailIngresado) == -1 and chequearEmail_contraseña(varLogicaMods,contraseñaIngresada) == 0) or \
                (busquedaSecuencialDeEmail(varFisicaAdmi,varLogicaAdmi,emailIngresado) == -1 and chequearEmail_contraseña(varLogicaAdmi,contraseñaIngresada == 0))) \
                and intentos > 0:
                    print('Email y/o contraseña Incorrectas. Intenta de nuevo: \n')
                    varLogicaAdmi.seek(0,0)
                    varLogicaMods.seek(0,0)
                    varLogicaEst.seek(0,0)
                    intentos -= 1
                    emailIngresado = input('Ingresa tu email: ')
                    contraseñaIngresada = getpass_custom('Ingresa tu contrasaña: ')
    if intentos == 0:
        print('Te has quedado sin intentos. Vuelve mas tarde! ')
    else:
        if busquedaSecuencialDeEmail(varFisicaEst,varLogicaEst,emailIngresado) == 1:
            tipo = 'e'
        elif busquedaSecuencialDeEmail(varFisicaMods,varLogicaMods,emailIngresado) == 1:
            tipo = 'm'
        else:
            tipo = 'a'
    return tipo
                
def menuEstudiantes() -> None:
    ...
    
def main():
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
    # Antes de entrar al menu de logueo, debemos pre cargar un admi y un mod.
    # El usuario no va a poder loguearse hasta que no halla 4 estudiantes.
    altaAdmins(variableDeArchivoFisicoAdministradores,variableDeArchivoLogicaAdministradores,variableDeArchivoFisicoModeradores,variableDeArchivoLogicaModeradores, \
                variableDeArchivoFisicoEstudiantes,variableDeArchivoLogicaEstudiantes)
    altaModerador(variableDeArchivoFisicoAdministradores,variableDeArchivoLogicaAdministradores,variableDeArchivoFisicoModeradores,variableDeArchivoLogicaModeradores, \
                variableDeArchivoFisicoEstudiantes,variableDeArchivoLogicaEstudiantes)
    logOReg = 1
    while logOReg != 0:
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
            else:
                tipoDeUsuarioLogueado = logueo()
                if tipoDeUsuarioLogueado == 'e': 
                    posDelRegistroDelEstudianteLogueado = variableDeArchivoLogicaEstudiantes.tell()
                    menuEstudiantes()
                ...
        elif logOReg == '2':
            altaEstudiantes(variableDeArchivoFisicoAdministradores,variableDeArchivoLogicaAdministradores,variableDeArchivoFisicoModeradores,variableDeArchivoLogicaModeradores, \
                variableDeArchivoFisicoEstudiantes,variableDeArchivoLogicaEstudiantes)
        else:
            print('Hasta Luego! ')
            
            
                
                
                
                

    variableDeArchivoLogicaAdministradores.close()
    variableDeArchivoLogicaEstudiantes.close()
    variableDeArchivoLogicaModeradores.close()

            
main()
