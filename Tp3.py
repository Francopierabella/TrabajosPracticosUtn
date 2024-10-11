import os # para usar os.system('cls' / 'pause')
import os.path # para poder acceder a las rutas de los arrchivos, osea a sus variables fisicas
import pickle # para usar el load y el dump
import msvcrt # para usar el getpass
import sys # Tambien para el getpass
from datetime import datetime #  para las fechas

'''

 TRABAJO PRACTICO 3 ' ALGORITMOS Y ESTRUCTURAS DE DATOS '
 INTEGRANTES: Franco Pierabella, Alejo Scarpetta, Matias Villalba y Manuel Real
 COM 101
 
'''
fecha_actual = datetime.now()   # Aqui calculamos la fecha de hoy con uso de la libreria Datetime
año_actual = fecha_actual.year  # Aqui calculamos el año actual con uso de la libreria Datetime
mes_actual = fecha_actual.month # Aqui calculamos el mes actual con uso de la libreria Datetime   
dia_actual = fecha_actual.day   # Aqui calculamos el dia actual con uso de la libreria Datetime

# FUNCION QUE NOS OCULTA LA CONTRASEÑA
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
 
# calcularEdad: str -> int
# Recibe la fecha en formato string,la convierte en tipo datetime, la procesa y nos calcula la edad.               
def calcularEdad(fecha : str) -> int:
    fechaAux = datetime.strptime(fecha.strip(),'%Y/%m/%d')
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
#------------------------------------------------------
# DECLARACION DE REGISTROS:  
 
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
        self.cantReportesIgnorados = 0
        self.cantReportesBloqueados = 0
        
class administrador:
    def __init__(self):
        self.id = 0
        self.email = ''
        self.contraseña = ''
        
class likes:
    def __init__ (self):
        self.remitente = 0
        self.destinatario = 0

class reportes:
    def __init__ (self):
        self.id_reportante = 0
        self.id_reportado = 0
        self.razon_reporte = ''
        self.estado = 0
  
#------------------------------------------------------
# FUNCIONES RELACIONADAS A BUSQUEDAS     

def busquedaSecuencialDeIdEstudiantes(id : str) -> int:
    
    # Var
    # tamañoArchivo,pos : int
    # variableDeRegistro : estudiante()
    tamañoArchivo = os.path.getsize(variableDeArchivoFisicoEstudiantes)
    pos = 0
    variableDeArchivoLogicaEstudiantes.seek(0,0)
    variableDeRegistro = pickle.load(variableDeArchivoLogicaEstudiantes)
    while variableDeArchivoLogicaEstudiantes.tell() < tamañoArchivo and variableDeRegistro.id.strip() != id:
        pos = variableDeArchivoLogicaEstudiantes.tell()
        variableDeRegistro = pickle.load(variableDeArchivoLogicaEstudiantes)
    if variableDeRegistro.id.strip() == id:
        return pos
    return -1
def busquedaSecuencialDeIdModeradores(id : str) -> int:
    
    
    # Var
    # tamañoArchivo,pos : int
    # variableDeRegistro : moderador()
    tamañoArchivo = os.path.getsize(variableDeArchivoFisicoModeradores)
    pos = 0
    variableDeArchivoLogicaModeradores.seek(0,0)
    variableDeRegistro = pickle.load(variableDeArchivoLogicaModeradores)
    while variableDeArchivoLogicaModeradores.tell() < tamañoArchivo and variableDeRegistro.id.strip() != id:
        pos = variableDeArchivoLogicaModeradores.tell()
        variableDeRegistro = pickle.load(variableDeArchivoLogicaModeradores)
    if variableDeRegistro.id.strip() == id.strip():
        return pos
    return -1
def busquedaSecuencialDeNombre(nombre: str,pos: int) -> int:
    
    # Var
    # tamArchivoEstudiantes, aux : int
    # r : estudiante()
    tamArchivoEstudiantes = os.path.getsize(variableDeArchivoFisicoEstudiantes)
    variableDeArchivoLogicaEstudiantes.seek(0,0)
    aux = 0 
    r = pickle.load(variableDeArchivoLogicaEstudiantes)
    while variableDeArchivoLogicaEstudiantes.tell() < tamArchivoEstudiantes and r.nombre.strip() != nombre:
            aux = variableDeArchivoLogicaEstudiantes.tell()
            r = pickle.load(variableDeArchivoLogicaEstudiantes)
    if r.nombre.strip() == nombre and aux != pos:
        return aux
    return -1  
def busquedaSecuencialDeEmailEnArchivoEstudiantes(email : str) -> int:
    # Var
    # tamañoArchivo,pos : int
    # variableDeRegistro : estudiante()
    tamañoArchivo = os.path.getsize(variableDeArchivoFisicoEstudiantes)
    if tamañoArchivo == 0:
        return -1
    else:
        pos = 0
        variableDeArchivoLogicaEstudiantes.seek(0,0)
        variableDeRegistro = pickle.load(variableDeArchivoLogicaEstudiantes)
        while (variableDeArchivoLogicaEstudiantes.tell() < tamañoArchivo) and (variableDeRegistro.email.strip() != email.strip()):
            pos = variableDeArchivoLogicaEstudiantes.tell()
            variableDeRegistro = pickle.load(variableDeArchivoLogicaEstudiantes)
        if variableDeRegistro.email.strip() == email.strip():
            return pos
        return -1

def busquedaSecuencialDeEmailEnArchivoModeradores(email : str) -> int:
    # Var
    # tamañoArchivo, pos : int
    # variableDeRegistro : moderador()
    tamañoArchivo = os.path.getsize(variableDeArchivoFisicoModeradores)
    if tamañoArchivo == 0:
        return -1
    else:
        pos = 0
        variableDeArchivoLogicaModeradores.seek(0,0)
        variableDeRegistro = pickle.load(variableDeArchivoLogicaModeradores)
        while (variableDeArchivoLogicaModeradores.tell() < tamañoArchivo) and (variableDeRegistro.email.strip() != email.strip()):
            pos = variableDeArchivoLogicaModeradores.tell()
            variableDeRegistro = pickle.load(variableDeArchivoLogicaModeradores)
        if variableDeRegistro.email.strip() == email.strip():
            return pos
        return -1

def busquedaSecuencialDeEmailEnArchivoAdministradores(email : str) -> int:
    # Var
    # tamañoArchivo, pos : int
    # variableDeRegistro : administrador()
    tamañoArchivo = os.path.getsize(variableDeArchivoFisicoAdministradores)
    if tamañoArchivo == 0:
        return -1
    else:
        pos = 0
        variableDeArchivoLogicaAdministradores.seek(0,0)
        variableDeRegistro = pickle.load(variableDeArchivoLogicaAdministradores)
        while (variableDeArchivoLogicaAdministradores.tell() < tamañoArchivo) and (variableDeRegistro.email.strip() != email.strip()):
            pos = variableDeArchivoLogicaAdministradores.tell()
            variableDeRegistro = pickle.load(variableDeArchivoLogicaAdministradores)
        if variableDeRegistro.email.strip() == email.strip():
            return pos
        return -1
#------------------------------------------------------
# FUNCIONES RELACIONADAS A CONTAR REGISTROS
def contarEstudiantes() -> int:
    # tamArchivo,tamRegistro,canRegistros : int
    # vr : estudiante()
    variableDeArchivoLogicaEstudiantes.seek(0,0)
    tamArchivo = os.path.getsize(variableDeArchivoFisicoEstudiantes)
    if tamArchivo == 0: 
        return 0
    vr = pickle.load(variableDeArchivoLogicaEstudiantes)
    tamRegistro = variableDeArchivoLogicaEstudiantes.tell()
    cantRegistros = tamArchivo // tamRegistro
    return cantRegistros

def contarModeradores() -> int:
    # tamArchivo,tamRegistro,canRegistros : int
    # vr : moderador()
    variableDeArchivoLogicaModeradores.seek(0,0)
    tamArchivo = os.path.getsize(variableDeArchivoFisicoModeradores)
    if tamArchivo == 0: 
        return 0
    vr = pickle.load(variableDeArchivoLogicaModeradores)
    tamRegistro = variableDeArchivoLogicaModeradores.tell()
    cantRegistros = tamArchivo // tamRegistro
    return cantRegistros

def contarAdministradores() -> int:
    # tamArchivo,tamRegistro,canRegistros : int
    # vr : administrador()
    variableDeArchivoLogicaAdministradores.seek(0,0)
    tamArchivo = os.path.getsize(variableDeArchivoFisicoAdministradores)
    if tamArchivo == 0: 
        return 0
    vr = pickle.load(variableDeArchivoLogicaAdministradores)
    tamRegistro = variableDeArchivoLogicaAdministradores.tell()
    cantRegistros = tamArchivo // tamRegistro
    return cantRegistros

def contarReportes():
    # Var
    # t,cont : int
    # r: reporte()
    t = os.path.getsize(variableDeArchivoFisicoReportes)
    cont = 0
    variableLogicaDeArchivoReportes.seek(0,0)
    while variableLogicaDeArchivoReportes.tell() < t:
        cont += 1
        r = pickle.load(variableLogicaDeArchivoReportes)
    return cont
#------------------------------------------------------
# FUNCIONES PARA FORMATEAR LOS REGISTROS

def formatearEstudiantes(variableDeRegistro : estudiante):
    variableDeRegistro.id = str(variableDeRegistro.id).ljust(5,' ')
    variableDeRegistro.email = str(variableDeRegistro.email).ljust(32,' ')
    variableDeRegistro.nombre = str(variableDeRegistro.nombre).ljust(32,' ')
    variableDeRegistro.contraseña = str(variableDeRegistro.contraseña).ljust(32,' ')
    variableDeRegistro.sexo = str(variableDeRegistro.sexo).ljust(1,' ')
    variableDeRegistro.estado = str(variableDeRegistro.estado).ljust(5,' ') 
    variableDeRegistro.datosPersonales[0] = str(variableDeRegistro.datosPersonales[0]).ljust(255,' ') 
    variableDeRegistro.datosPersonales[1] = str(variableDeRegistro.datosPersonales[1]).ljust(16,' ')
    variableDeRegistro.datosPersonales[2] = str(variableDeRegistro.datosPersonales[2]).ljust(16,' ')
    variableDeRegistro.datosPersonales[3] = str(variableDeRegistro.datosPersonales[3]).ljust(16,' ')
    variableDeRegistro.datosPersonales[4] = str(variableDeRegistro.datosPersonales[4]).ljust(16,' ')
    variableDeRegistro.datosPersonales[5] = str(variableDeRegistro.datosPersonales[5]).ljust(255,' ')
    variableDeRegistro.datosPersonales[6] = str(variableDeRegistro.datosPersonales[6]).ljust(32,' ')
    variableDeRegistro.datosPersonales[7] = str(variableDeRegistro.datosPersonales[7]).ljust(32,' ')
    variableDeRegistro.datosPersonales[8] = str(variableDeRegistro.datosPersonales[8]).ljust(10,' ')
    
def formatearMods(variableDeRegistro : moderador):
    variableDeRegistro.id = str(variableDeRegistro.id).ljust(3,' ')
    variableDeRegistro.email = str(variableDeRegistro.email).ljust(32,' ')
    variableDeRegistro.contraseña = str(variableDeRegistro.contraseña).ljust(32,' ')
    variableDeRegistro.estado = str(variableDeRegistro.estado).ljust(5,' ')
    variableDeRegistro.cantReportesIgnorados = str(variableDeRegistro.cantReportesIgnorados).ljust(2,' ')
    variableDeRegistro.cantReportesBloqueados = str(variableDeRegistro.cantReportesBloqueados).ljust(2,' ')

def formatearAdmins(variableDeRegistro : administrador):
    variableDeRegistro.id = str(variableDeRegistro.id).ljust(3,' ')
    variableDeRegistro.email = str(variableDeRegistro.email).ljust(32,' ')
    variableDeRegistro.contraseña = str(variableDeRegistro.contraseña).ljust(32,' ')

def formatearLikes(variableDeRegistro : likes):
    variableDeRegistro.remitente = str(variableDeRegistro.remitente).ljust(3,' ')
    variableDeRegistro.destinatario = str(variableDeRegistro.destinatario).ljust(3,' ')
    
def formatearReportes(variableDeRegistro : reportes):
    variableDeRegistro.id_reportante = str (variableDeRegistro.id_reportante).ljust(3,' ')
    variableDeRegistro.id_reportado = str (variableDeRegistro.id_reportado).ljust(3,' ')   
    variableDeRegistro.razon_reporte = str(variableDeRegistro.razon_reporte).ljust(255,' ')
#------------------------------------------------------
# FUNCIONES PARA DAR DE ALTA EL TIPO DE USUARIO O LOS LIKES O REPORTES     

def altaAdmins() -> None:
    # os.system('cls')
    print('Hola Administrador! ')
    print('')
    print('Carga aqui tus datos! ')
    print('')
    variableDeArchivoLogicaAdministradores.seek(0,2)
    variableDeRegistroAdmins = administrador()
    variableDeRegistroAdmins.id = contarAdministradores()
    variableDeRegistroAdmins.email = input('Ingresa tu email: ')
    while busquedaSecuencialDeEmailEnArchivoAdministradores(variableDeRegistroAdmins.email) != -1 or \
            busquedaSecuencialDeEmailEnArchivoEstudiantes(variableDeRegistroAdmins.email) != -1 or \
                busquedaSecuencialDeEmailEnArchivoModeradores(variableDeRegistroAdmins.email) != -1 :
                    print('Ese email ya esta en uso! Intenta de nuevo. ')
                    variableDeRegistroAdmins.email = input('Ingrese su email: ')
    variableDeRegistroAdmins.contraseña = getpass_custom('Ingrese su contraseña: ')
    formatearAdmins(variableDeRegistroAdmins)
    pickle.dump(variableDeRegistroAdmins,variableDeArchivoLogicaAdministradores)
    variableDeArchivoLogicaAdministradores.flush()
    os.system('pause')  

def altaModerador() -> None: 
    os.system('cls')
    print('Hola Administrador!')
    print()
    print('Carga aqui los datos del moderador! Ten en cuenta que su id es un numero auto-Incremental')
    print()
    variableDeArchivoLogicaModeradores.seek(0,2)
    variableDeRegistroMods = moderador()
    variableDeRegistroMods.id = contarModeradores()
    variableDeRegistroMods.email = input('Ingrese su email: ')
    while (busquedaSecuencialDeEmailEnArchivoAdministradores(variableDeRegistroMods.email) != -1 or \
            busquedaSecuencialDeEmailEnArchivoEstudiantes(variableDeRegistroMods.email) != -1 or \
                busquedaSecuencialDeEmailEnArchivoModeradores(variableDeRegistroMods.email) != -1 ):
                    print('Ese email ya esta en uso! Intenta de nuevo. ')
                    variableDeRegistroMods.email = input('Ingrese su email: ')
    variableDeRegistroMods.contraseña = getpass_custom('Ingrese su contraseña: ')
    variableDeRegistroMods.estado = True
    variableDeRegistroMods.cantReportesIgnorados = 0
    variableDeRegistroMods.cantReportesBloqueados = 0
    formatearMods(variableDeRegistroMods)
    pickle.dump(variableDeRegistroMods,variableDeArchivoLogicaModeradores)
    variableDeArchivoLogicaModeradores.flush()
     
def altaEstudiantes() -> None:
    # os.system('cls')
    print('Hola Estudiante!')
    print()
    print('Carga aqui tus datos! ')
    print()
    variableDeArchivoLogicaEstudiantes.seek(0,2)
    print(variableDeArchivoLogicaEstudiantes.tell(), '.tell() alta estudiantes: ')
    variableDeRegistroEstuditante = estudiante()
    variableDeRegistroEstuditante.id = contarEstudiantes()
    variableDeRegistroEstuditante.nombre = input('Ingresa tu Nombre: ')
    variableDeRegistroEstuditante.email = input('Ingrese su email: ')
    while (busquedaSecuencialDeEmailEnArchivoAdministradores(variableDeRegistroEstuditante.email) != -1) or \
            (busquedaSecuencialDeEmailEnArchivoEstudiantes(variableDeRegistroEstuditante.email) != -1) or \
                (busquedaSecuencialDeEmailEnArchivoModeradores(variableDeRegistroEstuditante.email) != -1) :
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
    pickle.dump(variableDeRegistroEstuditante,variableDeArchivoLogicaEstudiantes)
    variableDeArchivoLogicaEstudiantes.flush()
    os.system('pause')


def altaReportes(idReportante : str,idReportado : str):
    variableLogicaDeArchivoReportes.seek(0,2)
    variableDeRegistro = reportes()
    variableDeRegistro.id_reportante = idReportante
    variableDeRegistro.id_reportado = idReportado
    variableDeRegistro.razon_reporte = input('Ingresa la razon de porque Reportas al estudiante de id ' +  str(idReportado) + ': ')
    variableDeRegistro.estado = 0
    formatearReportes(variableDeRegistro)
    pickle.dump(variableDeRegistro,variableLogicaDeArchivoReportes)
    variableLogicaDeArchivoReportes.flush()
    print('')
    print('REPORTE')
    print(' ')
    print('ID REPORTANTE: ',idReportante)
    print('ID REPORTADO: ', idReportado)
    print('MOTIVO DE REPORTE: ',variableDeRegistro.razon_reporte.strip())
    print('ESTADO DEL REPORTE: ',variableDeRegistro.estado)

#------------------------------------------------------
# FUNCIONES REFERIDAS A LOS LIKES    
# LO QUE HACE EL .strip() es sacar los espacios en blanco dados por el formateo   
    
def leDioLike(idRemitente : str,idDestinatario : str) -> int:
    tamArchivoLikes = os.path.getsize(variableDeArchivoFisicoLikes)
    variableDeArchivoLogicaLikes.seek(0,0)
    while variableDeArchivoLogicaLikes.tell() < tamArchivoLikes:
        vr = pickle.load(variableDeArchivoLogicaLikes)
        if vr.remitente.strip() == idRemitente and vr.destinatario.strip() == idDestinatario:
            return 1
    return 0
        
def likesCorrespondidos(idRemitente : str,idDestinatario : str) -> int:
    if leDioLike(idRemitente,idDestinatario) == 1 and leDioLike(idDestinatario,idRemitente) == 1:
        return 1
    return 0

def porcentajeDeLikesDadosYRecibidos(idRemitente : str) -> int:
    tamArchivoLikes = os.path.getsize(variableDeArchivoFisicoLikes)
    variableDeArchivoLogicaLikes.seek(0,0)
    vr = pickle.load(variableDeArchivoLogicaLikes)
    tamañoRegistroLikes = variableDeArchivoLogicaLikes.tell()
    cantDeRegistroLikes = tamArchivoLikes // tamañoRegistroLikes
    cantDeLikesDadosYRecibidos = 0
    for i in range(cantDeRegistroLikes + 1):
        if i != int(idRemitente):
            if leDioLike(idRemitente,str(i)) and leDioLike(str(i),idRemitente):
                cantDeLikesDadosYRecibidos += 1
    porcentajeDeLikesDadosYRecibidos = cantDeLikesDadosYRecibidos * 100 // contarEstudiantes()
    return porcentajeDeLikesDadosYRecibidos

def likeDadoYNoRecibido(idRemitente : str)-> int:
    tamArchivoLikes = os.path.getsize(variableDeArchivoFisicoLikes)
    variableDeArchivoLogicaLikes.seek(0,0)
    vr = pickle.load(variableDeArchivoLogicaLikes)
    tamañoRegistroLikes = variableDeArchivoLogicaLikes.tell()
    cantDeRegistroLikes = tamArchivoLikes // tamañoRegistroLikes
    cantDeLikesDadosYNoRecibidos = 0
    for i in range(cantDeRegistroLikes + 1):
        if int(idRemitente) != i:
            if leDioLike(idRemitente,str(i)) == 1 and leDioLike(str(i),idRemitente) == 0:
                cantDeLikesDadosYNoRecibidos += 1
    return cantDeLikesDadosYNoRecibidos
    
def likeRecibidioYNoRespondido(idRemitente : str)-> int:
    tamArchivoLikes = os.path.getsize(variableDeArchivoFisicoLikes)
    variableDeArchivoLogicaLikes.seek(0,0)
    vr = pickle.load(variableDeArchivoLogicaLikes)
    tamañoRegistroLikes = variableDeArchivoLogicaLikes.tell()
    cantDeRegistroLikes = tamArchivoLikes // tamañoRegistroLikes
    cantDeLikesRecibidosYNoRespondidos = 0 
    for k in range (cantDeRegistroLikes + 1):
        if k != int(idRemitente):
            if leDioLike(str(k),idRemitente) == 1 and leDioLike(idRemitente,str(k)) == 0:
                cantDeLikesRecibidosYNoRespondidos += 1
    return cantDeLikesRecibidosYNoRespondidos
        
def altaLikes(idRemitente : str,idDestinatario : str):
        variableDeArchivoLogicaLikes.seek(0,2)
        variableDeRegistroLikes = likes()
        variableDeRegistroLikes.remitente = idRemitente
        variableDeRegistroLikes.destinatario = idDestinatario
        formatearLikes(variableDeRegistroLikes)
        pickle.dump(variableDeRegistroLikes,variableDeArchivoLogicaLikes)
        variableDeArchivoLogicaLikes.flush()
        print('Like dado de alta correctamente. ')
#------------------------------------------------------
# FUNCIONES PARA CHEQUEAR LOGUEO CORRECTO    
    
def chequearContraseñaDeEmailIngresadoEnArchivoEstudiantes(contraseña : str,pos : int) -> int:
    if pos != -1:
        variableDeArchivoLogicaEstudiantes.seek(pos,0)
        variableDeRegistro = pickle.load(variableDeArchivoLogicaEstudiantes)
        if variableDeRegistro.contraseña.strip() == contraseña.strip():
                if variableDeRegistro.estado.strip() == 'True': 
                    return 1
                else:
                    print('Usuario INACTIVO => Logueo Invalido ')
    return 0

def chequearContraseñaDeEmailIngresadoEnArchivoModeradores(contraseña : str,pos : int) -> int:
    if pos != -1:
        variableDeArchivoLogicaModeradores.seek(pos,0)
        variableDeRegistro = pickle.load(variableDeArchivoLogicaModeradores)
        if variableDeRegistro.contraseña.strip() == contraseña.strip():
                if variableDeRegistro.estado.strip() == 'True': 
                    return 1
                else:
                    print('Usuario INACTIVO => Logueo Invalido ')
    return 0

def chequearContraseñaDeEmailIngresadoEnArchivoAdministradores(contraseña : str,pos : int) -> int:
    if pos != -1:
        variableDeArchivoLogicaAdministradores.seek(pos,0)
        variableDeRegistro = pickle.load(variableDeArchivoLogicaAdministradores)
        if variableDeRegistro.contraseña.strip() == contraseña.strip():
            return 1
    return 0

def logueo() -> str:
    print('---------- LOG IN -----------')
    print()
    intentos = 3
    emailIngresado = input('Ingresa tu email: ')
    contraseñaIngresada = getpass_custom('Ingresa tu contraseña: ')
    tipo = ''
    posEstudiante = busquedaSecuencialDeEmailEnArchivoEstudiantes(emailIngresado)
    posModeradores = busquedaSecuencialDeEmailEnArchivoModeradores(emailIngresado)
    posAdministradores = busquedaSecuencialDeEmailEnArchivoAdministradores(emailIngresado)    
    while  (posEstudiante == -1 or chequearContraseñaDeEmailIngresadoEnArchivoEstudiantes(contraseñaIngresada,posEstudiante) == 0) and \
            (posModeradores == -1 or chequearContraseñaDeEmailIngresadoEnArchivoModeradores(contraseñaIngresada,posModeradores) == 0) and \
                (posAdministradores == -1 or chequearContraseñaDeEmailIngresadoEnArchivoAdministradores(contraseñaIngresada,posAdministradores) == 0) \
                and intentos > 0:
                    print('Logueo INCORRECTO. Intenta de nuevo: \n')
                    variableDeArchivoLogicaAdministradores.seek(0,0)
                    variableDeArchivoLogicaModeradores.seek(0,0)
                    variableDeArchivoLogicaEstudiantes.seek(0,0)
                    intentos -= 1
                    if intentos > 0: 
                        # Hacemos esto porque sino al ingresar correctamente en el 3er intento
                        # Toma como que intentos es == 0 entonces seria un logueo incorrectamente invalido
                        emailIngresado = input('Ingresa tu email: ')
                        contraseñaIngresada = getpass_custom('Ingresa tu contrasaña: ')
                        posEstudiante = busquedaSecuencialDeEmailEnArchivoEstudiantes(emailIngresado)
                        posModeradores = busquedaSecuencialDeEmailEnArchivoModeradores(emailIngresado)
                        posAdministradores = busquedaSecuencialDeEmailEnArchivoAdministradores(emailIngresado)
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
#------------------------------------------------------
# FUNCIONES PARA SABER EL TAMÑAÑO DE LOS REGISTROS
def devolvertamañoDeRegistroDeArchivoEstudiantes() -> int:
    if os.path.getsize(variableDeArchivoFisicoEstudiantes) == 0:
        return 0
    aux = variableDeArchivoLogicaEstudiantes.tell()
    variableDeArchivoLogicaEstudiantes.seek(0,0)
    vr = pickle.load(variableDeArchivoLogicaEstudiantes)
    tamaño = variableDeArchivoLogicaEstudiantes.tell()
    variableDeArchivoLogicaEstudiantes.seek(aux,0)
    return tamaño

def devolvertamañoDeRegistroDeArchivoModeradores() -> int:
    if os.path.getsize(variableDeArchivoFisicoModeradores) == 0:
        return 0
    aux = variableDeArchivoLogicaModeradores.tell()
    variableDeArchivoLogicaModeradores.seek(0,0)
    vr = pickle.load(variableDeArchivoLogicaModeradores)
    tamaño = variableDeArchivoLogicaModeradores.tell()
    variableDeArchivoLogicaModeradores.seek(aux,0)
    return tamaño

def devolvertamañoDeRegistroDeArchivoAdministradores() -> int:
    if os.path.getsize(variableDeArchivoFisicoAdministradores) == 0:
        return 0
    aux = variableDeArchivoLogicaAdministradores.tell()
    variableDeArchivoLogicaAdministradores.seek(0,0)
    vr = pickle.load(variableDeArchivoLogicaAdministradores)
    tamaño = variableDeArchivoLogicaAdministradores.tell()
    variableDeArchivoLogicaAdministradores.seek(aux,0)
    return tamaño

def devolverTamañoDeRegistroDeArchivoReportes() -> int:
    if os.path.getsize(variableDeArchivoFisicoReportes) == 0:
        return 0
    aux = variableLogicaDeArchivoReportes.tell()
    variableLogicaDeArchivoReportes.seek(0,0)
    vr = pickle.load(variableLogicaDeArchivoReportes)
    tamaño = variableLogicaDeArchivoReportes.tell()
    variableLogicaDeArchivoReportes.seek(aux,0)
    return tamaño
#------------------------------------------------------
# FUNCIONES PARA MOSTRAR ESTUDIANTES O REPORTES (PUEDEN SER BORRADAS SI SE QUIERE)
def mostrarRegistros ():
    tamEst = os.path.getsize(variableDeArchivoFisicoEstudiantes)
    if tamEst != 0:
        variableDeArchivoLogicaEstudiantes.seek(0,0)
        while variableDeArchivoLogicaEstudiantes.tell() < tamEst :
            reg = pickle.load(variableDeArchivoLogicaEstudiantes)
            print('ID: ',reg.id.strip(), 'Nombre: ',reg.nombre.strip(),' Email: ',reg.email.strip(), ' Contraseña: ',reg.contraseña.strip(),'Estado: ',reg.estado.strip())
    os.system('pause')

def mostrarReportes():
    tam = os.path.getsize(variableDeArchivoFisicoReportes)
    if tam != 0:
        variableLogicaDeArchivoReportes.seek(0,0)
        while variableLogicaDeArchivoReportes.tell() < tam:
            r = pickle.load(variableLogicaDeArchivoReportes)
            print('ID REPORTANTE: ',r.id_reportante, 'ID REPORTADO: ', r.id_reportado, 'RAZON REPORTE: ',r.razon_reporte.strip(),'ESTADO REPORTE: ',r.estado)
#------------------------------------------------------
#                                         FUNCIONES REFERIDAS A MENUS    
# MENU PRINCIPAL DE LOGUEO
def menuDeLogueo():
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
# TODO LO DE ESTUDIANTES, INCLUYENDO MENUS Y FUNCIONES 
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
    print()
    print('2. Gestionar candidatos: ')
    print()
    print('3. Matcheos: ')
    print()
    print('4. Reportes estadisticos ')
    print()
    print('0. Salir:')  
    
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
    
def imprimirOpcionesACambiar(registro : estudiante):
    os.system('cls')
    print('Estos son tus datos Actuales: \n')
    print('Tus hobbies: ',registro.datosPersonales[0])
    print('Tu fecha de nacimiento: ',registro.datosPersonales[8])
    print('Tu biografia: ',registro.datosPersonales[5])
    print('Tu ciudad: ',registro.datosPersonales[7])
    print('')
    print('Que datos deseas editar ? \n')
    print('1. Hobbies ')
    print('2. Fecha de nacimiento ')
    print('3. Biografia ')
    print('4. Ciudad ')
    print('0. Volver')
    
def eliminarPerfilEstudiantes(id : str):
    pos = busquedaSecuencialDeIdEstudiantes(id)
    variableDeArchivoLogicaEstudiantes.seek(pos,0)
    registro = pickle.load(variableDeArchivoLogicaEstudiantes)
    print('ATENCION')
    eliminar = input('Estas seguro que deseas eliminar el perfil? Responde si ó no: ').lower()
    while eliminar != 'si' and eliminar != 'no':
        print('Opcion invalida! Intenta de nuevo. ')
        eliminar = input('Estas seguro que deseas eliminar el perfil? Responde si ó no: ').lower()
    if eliminar == 'si':
        registro.estado = 'False'
        variableDeArchivoLogicaEstudiantes.seek(pos,0)
        pickle.dump(registro,variableDeArchivoLogicaEstudiantes)
        variableDeArchivoLogicaEstudiantes.flush()
    else:
        print('Decidiste no eliminar el perfil! ')
   
def gestionarMiPerfil(pos : int):
    os.system('cls')
    MostrarOpcionesDeGestionarMiperfil()
    op = input('Elige una opcion: ')
    while op != 'a' and op != 'b' and op != 'c':
        print('Opcion Invalida! Intenta de nuevo.')
        op = input('Elige una opcion: ')
    variableDeArchivoLogicaEstudiantes.seek(pos,0)
    registro = pickle.load(variableDeArchivoLogicaEstudiantes)
    if op == 'a':
        hobbieActual = registro.datosPersonales[0]
        fechaActual = registro.datosPersonales[8]
        bioActual = registro.datosPersonales[5]
        ciudadActual = registro.datosPersonales[7]
        aux = '1'
        actualizoAlgunDato = False
        while aux != '0':
            imprimirOpcionesACambiar(registro)
            aux = input('Elige una opcion: ')
            while aux != '0' and aux != '1' and aux != '2' and aux != '3' and aux != '4':
                print('Opcion invalida! Intenta de nuevo.')
                aux = input('Elige una opcion: ')
            match aux:
                case '1': 
                    nuevoHobbie = input('Ingresa tus nuevos hobbies: ')
                    registro.datosPersonales[0] = nuevoHobbie
                    actualizoAlgunDato = True
                case '2': 
                    ok = False
                    while not ok:
                        try:
                            fecha = input('Ingresa su fecha de nacimiento (aaaa/mm/dd): ')
                            datetime.strptime(fecha,'%Y/%m/%d')
                            registro.datosPersonales[8] = fecha
                            ok = True
                            actualizoAlgunDato = True
                            
                        except: 
                            print('Fecha invalida. Intenta de nuevo!')
                case '3': 
                    bioNueva = input('Ingresa tu nueva Biografia: ')
                    registro.datosPersonales[5] = bioNueva
                    actualizoAlgunDato = True
                    
                case '4':
                    ciudadNueva = input('Ingresa tu nueva ciudad: ')
                    registro.datosPersonales[7] = ciudadNueva
                    actualizoAlgunDato = True
            formatearEstudiantes(registro)
            pickle.dump(registro,variableDeArchivoLogicaEstudiantes)
            variableDeArchivoLogicaEstudiantes.flush()
        if actualizoAlgunDato:
            # SI TENGO TIEMPO AGREGAR MAS DATOS TODO
            print('Datos actualizados!  Aqui tienes los resultados: ')
            print('Tu nuevo hobbie: ',registro.datosPersonales[0]) if hobbieActual != registro.datosPersonales[0] else print('Hobbie: ',registro.datosPersonales[0])
            print('Tu nueva fecha de nacimiento: ',registro.datosPersonales[8]) if fechaActual != registro.datosPersonales[8] else print('Fecha de nacimiento: ',registro.datosPersonales[8])
            print('tu nueva Biografia: ',registro.datosPersonales[5]) if bioActual != registro.datosPersonales[5] else print('Biografia: ',registro.datosPersonales[5])
            print('Tu nueva ciudad: ',registro.datosPersonales[7]) if ciudadActual != registro.datosPersonales[7] else print('Ciudad: ',registro.datosPersonales[7])
        else:
            print('No actualizaste datos. ')
            print('Volviendo al menu anterior...')
        os.system('pause') 

    elif op == 'b':
        eliminarPerfilEstudiantes(pos)
    else:
        print('Volviendo al menu anterior...')
        os.system('pause')
        
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
    
def verCandidatos(pos : int):
    tamArchivoEstudiantes = os.path.getsize(variableDeArchivoFisicoEstudiantes)
    print('VER CANDIDATOS')
    print()
    print('Aqui tienes los datos de los estudiantes: ')
    variableDeArchivoLogicaEstudiantes.seek(0,0)
    while variableDeArchivoLogicaEstudiantes.tell() < tamArchivoEstudiantes:
        if variableDeArchivoLogicaEstudiantes.tell() != pos:
            vr = pickle.load(variableDeArchivoLogicaEstudiantes)
            print('--------------------')
            print('ESTUDIANTE CON ID: ',vr.id)
            print('NOMBRE: ',vr.nombre)
            print('FECHA DE NACIMIENTO: ',vr.datosPersonales[8])
            print('EDAD: ',calcularEdad(vr.datosPersonales[8]))
            print('BIOGRAFIA: ',vr.datosPersonales[5].strip())
            print('HOBBIES: ',vr.datosPersonales[0].strip())
            print('--------------------')
        else:
            vr = pickle.load(variableDeArchivoLogicaEstudiantes)
    variableDeArchivoLogicaEstudiantes.seek(pos,0)
    vrRemitente = pickle.load(variableDeArchivoLogicaEstudiantes)
    variableDeArchivoLogicaEstudiantes.seek(0,0)
    nombreDelQueTeGusta = input('Ingresa el nombre del estudiante que te gusta: ')
    while busquedaSecuencialDeNombre(nombreDelQueTeGusta,pos) == -1:
        print('Nombre incorrecto. Intenta de nuevo')
        nombreDelQueTeGusta = input('Ingresa el nombre del estudiante que te gusta: ')
    variableDeArchivoLogicaEstudiantes.seek(busquedaSecuencialDeNombre(nombreDelQueTeGusta,pos),0)
    vrDestinatario = pickle.load(variableDeArchivoLogicaEstudiantes)
    altaLikes(vrRemitente.id,vrDestinatario.id)

def reportarUnCandidato(pos : int):
    variableDeArchivoLogicaEstudiantes.seek(pos,0)
    vr = pickle.load(variableDeArchivoLogicaEstudiantes)
    idReportante = vr.id
    print('A continuacion, deberas ingresar el id del estudiante que quieras reportar. ')
    idReportado = input('Ingresa el id del estudiante a reportar: ')
    while idReportado == idReportante.strip():
        print('No puedes reportarte a ti mismo! Intenta de nuevo. ')
        idReportado = input('Ingresa el id del estudiante a reportar: ')  
    posDelIdReportado = busquedaSecuencialDeIdEstudiantes(idReportado)
    while posDelIdReportado == -1 :
        print('El id ingresado no esta en el sistema. Intenta de nuevo. ')
        idReportado = input('Ingresa el id del estudiante a reportar: ')
        posDelIdReportado = busquedaSecuencialDeIdEstudiantes(idReportado)
    altaReportes(idReportante,idReportado)
                 
def gestionarCandidatos(pos : int):
    mostrarOpcionesDeGestionarCandidatos()
    op = input('Elige una opcion: ').lower()
    while op != 'a' and op != 'b' and op != 'c':
        print('Opcion invalida! Intenta de nuevo. ')
        op = input('Elige una opcion: ').lower()
    if op == 'a':
        verCandidatos(pos)
    elif op == 'b':
        reportarUnCandidato(pos)
    else:
        print('Volviendo al menu anterior... ')
    os.system('pause')

def matcheos():
    os.system('cls')
    print('MATCHEOS')
    print()
    print('a. Ver matcheos ')
    print()
    print('b. Eliminar un matcheo ')
    print()
    print('c. Volver ')
    op = input('Elige una opcion: ')
    while op != 'a' and op != 'b' and op != 'c':
        print('Opcion Invalida. Intenta de nuevo.')
        op = input('Elige una opcion: ')
    if op == 'a':
        print('En contruccion! Vuelve Mas tarde. Disculpa las molestias.')
    elif op == 'b':
        print('En contruccion! Vuelve Mas tarde. Disculpa las molestias.')
    else:
        print('Volviendo al menu anterior...')
    os.system('pause')
                 
def reportesEstadisticos(pos : int):
    os.system('cls')
    tam = os.path.getsize(variableDeArchivoFisicoLikes)
    variableDeArchivoLogicaLikes.seek(0,0)
    while variableDeArchivoLogicaLikes.tell() < tam:
        vr = pickle.load(variableDeArchivoLogicaLikes) 
        print(vr.remitente,vr.destinatario)
    variableDeArchivoLogicaEstudiantes.seek(pos,0)
    vr = pickle.load(variableDeArchivoLogicaEstudiantes)
    id = vr.id.strip()
    print('REPORTES ESTADISTICOS DE ESTUDIANTE DE ID: ',id)
    print()
    print('Matcheados sobre el % posible: ',str(porcentajeDeLikesDadosYRecibidos(id)) + '%')
    print()
    print('Likes dados y no recibidos: ',likeDadoYNoRecibido(id))
    print()
    print('Likes recibidos y no respondidos: ',likeRecibidioYNoRespondido(id))
    print()
    os.system('pause')
    
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

def gestionarUsuarios():
    os.system('cls')
    print()
    print('a. Desactivar un usuario ')
    print()
    print('b. Volver')
    print()
    op = input('Elige una opcion: ')
    while op != 'a' and op != 'b':
        print('Opcion invalida! Intenta de nuevo ')        
        op = input('Elige una opcion: ')
    if op == 'a':
        pos = input('Ingresa el id de usuario a descativar: ').strip()
        while busquedaSecuencialDeIdEstudiantes(pos) == -1:
            print('ID invalida. Intenta de nuevo')
            pos = input('Ingresa el id de usuario a descativar: ')   
        eliminarPerfilEstudiantes(pos)
    else:
        print('Volviendo al menu anterior...')
    os.system('pause')

    os.system('cls')
    print()
    print('                       GESTIONAR REPORTES')
    print()
    print('a. Ver reportes')
    print()
    print('b. Volver')    

# Esta funcion la ponemos aca y no arriba donde estan todas las de contar porque es una funcion especifica de verReportes
def contarReportesPosibles() -> int:
    t = os.path.getsize(variableDeArchivoFisicoReportes)
    variableLogicaDeArchivoReportes.seek(0,0)
    cont = 0
    while variableLogicaDeArchivoReportes.tell() < t:
        r = pickle.load(variableLogicaDeArchivoReportes)
        posReportante = busquedaSecuencialDeIdEstudiantes(r.id_reportante.strip())
        posReportado = busquedaSecuencialDeIdEstudiantes(r.id_reportado.strip())
        variableDeArchivoLogicaEstudiantes.seek(posReportante,0)
        r1 = pickle.load(variableDeArchivoLogicaEstudiantes)
        variableDeArchivoLogicaEstudiantes.seek(posReportado,0)
        r2 = pickle.load(variableDeArchivoLogicaEstudiantes)
        if r1.estado.strip() == 'True' and r2.estado.strip() == 'True' and r.estado == 0:
            cont += 1
    return cont
        
def verReportes(posMod  : int):
    os.system('cls')
    if contarReportesPosibles() == 0:
        print('No hay reportes posibles para proceder. ')
    else:        
        tamArchivoReportes = os.path.getsize(variableDeArchivoFisicoReportes)
        mostrarReportes()
        variableDeArchivoLogicaEstudiantes.seek(0,0)
        variableLogicaDeArchivoReportes.seek(0,0)
        sigueViendoReportes = True
        while variableLogicaDeArchivoReportes.tell() < tamArchivoReportes and sigueViendoReportes:
            i = variableLogicaDeArchivoReportes.tell()
            reporte = pickle.load(variableLogicaDeArchivoReportes)
            posRegistroReportante = busquedaSecuencialDeIdEstudiantes(reporte.id_reportante.strip())
            posRegistroReportado = busquedaSecuencialDeIdEstudiantes(reporte.id_reportado.strip())
            variableDeArchivoLogicaEstudiantes.seek(posRegistroReportante,0)
            registroReportante = pickle.load(variableDeArchivoLogicaEstudiantes)
            variableDeArchivoLogicaEstudiantes.seek(posRegistroReportado,0)
            registroReportado = pickle.load(variableDeArchivoLogicaEstudiantes)
            if registroReportante.estado.strip() == 'True' and registroReportado.estado.strip() == 'True' and reporte.estado == 0:
                print('REPORTE')
                print(' ')
                print('ID REPORTANTE: ',reporte.id_reportante.strip())
                print('ID REPORTADO: ', reporte.id_reportado.strip())
                print('MOTIVO DE REPORTE: ',reporte.razon_reporte.strip())
                print('ESTADO DEL REPORTE: ',reporte.estado)
                print()
                print('Como deseas proceder? ')
                print()
                print('1. Ignorar el reporte')
                print()
                print('2. Bloquear al reportante')
                print()
                print('0. Volver')
                op = input('Elige una opcion: ')
                while op != '1' and op != '2' and op != '0':
                    print('Opcion invalida! Intenta de nuevo ')
                    op = input('Elige una opcion: ')
                if op == '1':
                    reporte.estado = 2  
                    print('El estado del reporte ha sido actualizado a 2.')
                    if posMod % devolvertamañoDeRegistroDeArchivoModeradores() == 0:         
                        variableDeArchivoLogicaModeradores.seek(posMod,0)
                        r = pickle.load(variableDeArchivoLogicaModeradores)
                        r.cantReportesIgnorados = str(int(r.cantReportesIgnorados.strip()) + 1)
                        formatearMods(r)
                        pickle.dump(r,variableDeArchivoLogicaModeradores)
                        variableDeArchivoLogicaModeradores.flush()
                    print(variableLogicaDeArchivoReportes.tell())
                    formatearReportes(reporte)
                    variableLogicaDeArchivoReportes.seek(i,0)
                    pickle.dump(reporte,variableLogicaDeArchivoReportes)
                    print(variableLogicaDeArchivoReportes.tell())
                    variableLogicaDeArchivoReportes.flush()
                elif op == '2':
                    reporte.estado = 1
                    registroReportado.estado = 'False'
                    print('El reportado ha sido bloqueado. ')
                    if posMod % devolvertamañoDeRegistroDeArchivoModeradores() == 0: # Esto se aplica solo cuando los moderadores ingresan.          
                        variableDeArchivoLogicaModeradores.seek(posMod,0)
                        r = pickle.load(variableDeArchivoLogicaModeradores)
                        r.cantReportesBloqueados = str(int(r.cantReportesBloqueados.strip()) + 1)
                        formatearMods(r)
                        pickle.dump(r,variableDeArchivoLogicaModeradores)
                        variableDeArchivoLogicaModeradores.flush()
                    print(variableLogicaDeArchivoReportes.tell())
                    formatearReportes(reporte)
                    variableLogicaDeArchivoReportes.seek(i,0)
                    pickle.dump(reporte,variableLogicaDeArchivoReportes)
                    print(variableLogicaDeArchivoReportes.tell())
                    variableLogicaDeArchivoReportes.flush()
                else:
                    sigueViendoReportes = False 
                
    print('Volviendo al menu anterior ')
    os.system('pause')
    
def gestionarReportes(pos : int):
    os.system('cls')
    print() 
    print('a. Ver reportes ') 
    print()
    print('b. Volver ')  
    op = input('Elige una opcion: ')
    while op != 'a' and op != 'b':
        print('Opcion invalida! Intenta de nuevo')
        op = input('Elige una opcion: ')
    if op == 'a':
        verReportes(pos)
    else:
        print('Volviendo al menu anterior ')
        os.system('pause')   
 # --------------------------------------------------------------------
# --------------------------------------------------------------------
# Menus ADMINISTRADORES        

def menuPrincipalAdministradores():
    os.system('cls')
    print()
    print('------------------------------')
    print()
    print('MENU PRINCIPAL')
    print()
    print('1. Gestionar Usuarios ')
    print()
    print('2. Gestionar Reportes ')
    print()
    print('3. Reportes Estadisticos ')
    print()
    print('0. Salir')
    print()

def mostrarOpcionesGestionarUsuariosSiendoAdmi():
    os.system('cls')
    print('')
    print('                       GESTIONAR USUARIOS')
    print()
    print('a. Eliminar un usuario ')
    print()
    print('b. Dar de alta un moderador ')
    print()
    print('c. Desactivar usuario ')
    print()
    print('d. Volver')

def eliminarPerfilMods(pos : int):
    variableDeArchivoLogicaModeradores.seek(pos,0)
    registro = pickle.load(variableDeArchivoLogicaModeradores)
    print('ATENCION')
    eliminar = input('Estas seguro que deseas eliminar el perfil? Responde si ó no: ').lower()
    while eliminar != 'si' and eliminar != 'no':
        print('Opcion invalida! Intenta de nuevo. ')
        eliminar = input('Estas seguro que deseas eliminar el perfil? Responde si ó no: ').lower()
    if eliminar == 'si':
        registro.estado = 'False'
        variableDeArchivoLogicaModeradores.seek(pos,0)
        pickle.dump(registro,variableDeArchivoLogicaModeradores)
        variableDeArchivoLogicaModeradores.flush()
    else:
        print('Decidiste no eliminar el perfil! ') 
      
def eliminarUsuarioSiendoAdmi():
    os.system('cls')
    print('que tipo de usuario deseas eliminar? ')
    print()
    print('a. Estudiante')
    print()
    print('b. Moderador')
    print()
    op = input('Elige una opcion: ')
    while op != 'a' and op != 'b':
        print('Opcion invalida! Intenta de nuevo.') 
        op = input('Elige una opcion: ')
    if op == 'a':
        estudianteAEliminar = input('Ingresa el ID del estudiante a eliminar: ')
        posAEliminar = busquedaSecuencialDeIdEstudiantes(estudianteAEliminar)
        while posAEliminar == -1:
            print('ID invalida! Intenta de nuevo')
            estudianteAEliminar = input('Ingresa el ID del estudiante a eliminar: ')
            posAEliminar = busquedaSecuencialDeIdEstudiantes(estudianteAEliminar)
        eliminarPerfilEstudiantes(posAEliminar)
    else:
        moderadorAEliminar = input('Ingresa ID de moderador a eliminar: ')
        posAEliminar = busquedaSecuencialDeIdModeradores(moderadorAEliminar)
        while posAEliminar == -1:
            print('ID invalida! Intenta de nuevo ')
            moderadorAEliminar = input('Ingresa ID de moderador a eliminar: ')
            posAEliminar = busquedaSecuencialDeIdModeradores(moderadorAEliminar) 
        eliminarPerfilMods(moderadorAEliminar)
    
def gestionarUsuariosSiendoAdmi():
    mostrarOpcionesGestionarUsuariosSiendoAdmi()
    op = input('Elige una opcion: ')
    while op != 'a' and op != 'b' and op != 'c' :
        print('Opcion Invalida! Intenta de nuevo')
        op = input('Elige una opcion: ')
    if op == 'a':
        eliminarUsuarioSiendoAdmi()
    elif op == 'b':
        altaModerador()
    print()
    print('Volviendo al menu anterior')
    os.system('pause')
    
def reportesIgnorados() -> int:
    t = os.path.getsize(variableDeArchivoFisicoReportes)
    cont = 0
    variableLogicaDeArchivoReportes.seek(0,0)
    while variableLogicaDeArchivoReportes.tell() < t:
        r = pickle.load(variableLogicaDeArchivoReportes)
        if r.estado == 2:
            cont += 1
    return cont

def reportesAceptados() -> int:
    t = os.path.getsize(variableDeArchivoFisicoReportes)
    cont = 0
    variableLogicaDeArchivoReportes.seek(0,0)
    while variableLogicaDeArchivoReportes.tell() < t:
        r = pickle.load(variableLogicaDeArchivoReportes)
        if r.estado == 1:
            cont += 1
    return cont

def moderadorQueMasReportesIgnoro() -> int:
    t = os.path.getsize(variableDeArchivoFisicoModeradores)
    posDelQueMasIgnoro = 0
    cantDelQueMasIgnoro = 0
    variableDeArchivoLogicaModeradores.seek(0,0)
    while variableDeArchivoLogicaModeradores.tell() < t:
        r = pickle.load(variableDeArchivoLogicaModeradores)
        if int(r.cantReportesIgnorados.strip()) > cantDelQueMasIgnoro:
            posDelQueMasIgnoro = variableDeArchivoLogicaModeradores.tell()
            cantDelQueMasIgnoro = int(r.cantReportesIgnorados)
    return posDelQueMasIgnoro

def moderadorQueMasReportesBloqueo() -> int:
    t = os.path.getsize(variableDeArchivoFisicoModeradores)
    posDelQueMasBloqueo = 0
    cantDelQueMasBloqueo = 0
    variableDeArchivoLogicaModeradores.seek(0,0)
    while variableLogicaDeArchivoReportes.tell() < t:
        r = pickle.load(variableDeArchivoLogicaModeradores)
        if int(r.cantReportesBloqueados.strip()) > cantDelQueMasBloqueo:
            posDelQueMasBloqueo = variableDeArchivoLogicaModeradores.tell()
            cantDelQueMasBloqueo = int(r.cantReportesBloqueados.strip())
    return posDelQueMasBloqueo

def moderadorQueMasReportesProceso() -> int:
    t = os.path.getsize(variableDeArchivoFisicoModeradores)
    posDelQueMasProceso = 0
    cantDelQueMasProceso = 0
    variableDeArchivoLogicaModeradores.seek(0,0)
    while variableDeArchivoLogicaModeradores.tell() < t:
        r = pickle.load(variableDeArchivoLogicaModeradores)
        sumaDeReportesProcesados = int(r.cantReportesIgnorados.strip()) + int(r.cantReportesBloqueados.strip())
        if sumaDeReportesProcesados > cantDelQueMasProceso:
            posDelQueMasProceso = variableDeArchivoLogicaModeradores.tell()
            cantDelQueMasProceso = sumaDeReportesProcesados
    return posDelQueMasProceso
           
def reportesEstadisticosSiendoAdmi() -> int:
    os.system('cls')
    cantReportes = contarReportes()
    print('REPORTES ESTADISTICOS')
    print('CANTIDAD DE REPORTES REALIZADOS POR LOS ESTUDIANTES: ',contarReportes())
    print()
    print('PORCENTAJE DE REPORTES IGNORADOS: ',str(reportesIgnorados() * 100 // cantReportes) + '%') 
    print()
    print('PORCENTAJE DE REPORTES ACEPTADOS: ',str(reportesAceptados() * 100 // cantReportes) + '%')
    print()
    if reportesIgnorados() == 0:
        print('No hay reportes ignorados. ')
    else:
        variableDeArchivoLogicaModeradores.seek(moderadorQueMasReportesIgnoro(),0)
        r = pickle.load(variableDeArchivoLogicaModeradores)
        print('EL MODERADOR QUE MAS REPORTES IGNORO FUE EL DE ID: ',r.id)
        print()
    if reportesAceptados() == 0:
        print('No hay reportes bloqueados')
    else:
        variableDeArchivoLogicaModeradores.seek(moderadorQueMasReportesBloqueo(),0)
        r = pickle.load(variableDeArchivoLogicaModeradores)
        print('EL MODERADOR QUE MAS REPORTES BLOQUEO FUE EL DE ID: ',r.id)
        print()
    if reportesAceptados() + reportesIgnorados() == 0:
        print('No se han procesado Reportes todavia')
        print()
    else:
        variableDeArchivoLogicaModeradores.seek(moderadorQueMasReportesProceso(),0)
        r = pickle.load(variableDeArchivoLogicaModeradores)
        print('EL MODERADOR QUE MAS REPORTES PROCESO FUE EL DE ID: ',r.id)
        print()
    os.system('pause')
#------------------------------------------------------    

def cargaAdmi():
    vr = administrador()
    vr.id = 0
    vr.email = 'admi'
    vr.contraseña = 'admi'
    formatearAdmins(vr)
    pickle.dump(vr,variableDeArchivoLogicaAdministradores)
    variableDeArchivoLogicaAdministradores.flush()
    ...        

def cargarEstudiante0():
    vr = estudiante()
    variableDeArchivoLogicaEstudiantes.seek(0,0)
    vr.nombre = 'Franco'
    vr.id = 0
    vr.email = 'fran'
    vr.contraseña = 'fran'
    vr.estado = True
    vr.sexo = 'M'
    vr.datosPersonales[0] = 'Hobbies de Franco'
    vr.datosPersonales[1] = 'Matematica'
    vr.datosPersonales[2] = 'Futbol'
    vr.datosPersonales[3] = 'AyED'
    vr.datosPersonales[4] = 'Fisica'
    vr.datosPersonales[5] = 'Biografia de Franco'
    vr.datosPersonales[6] = 'Argentina'
    vr.datosPersonales[7] = 'Casilda'
    vr.datosPersonales[8] = '2004/01/12'
    formatearEstudiantes(vr)
    pickle.dump(vr,variableDeArchivoLogicaEstudiantes)
    variableDeArchivoLogicaEstudiantes.flush()
def cargarEstudiante1():
    vr = estudiante()
    variableDeArchivoLogicaEstudiantes.seek(0,2)
    vr.nombre = 'Matias'
    vr.id = 1
    vr.email = 'mati'
    vr.contraseña = 'mati'
    vr.estado = True
    vr.sexo = 'M'
    vr.datosPersonales[0] = 'Hobbies de Matias'
    vr.datosPersonales[1] = 'Matematica'
    vr.datosPersonales[2] = 'Futbol'
    vr.datosPersonales[3] = 'AyED'
    vr.datosPersonales[4] = 'Fisica'
    vr.datosPersonales[5] = 'Biografia de Matias'
    vr.datosPersonales[6] = 'Argentina'
    vr.datosPersonales[7] = 'Fisherton'
    vr.datosPersonales[8] = '2006/06/15'
    formatearEstudiantes(vr)
    pickle.dump(vr,variableDeArchivoLogicaEstudiantes)
    variableDeArchivoLogicaEstudiantes.flush()
def cargaEstudiante2(): 
    vr = estudiante()
    variableDeArchivoLogicaEstudiantes.seek(0,2)
    vr.nombre = 'Alejo'
    vr.id = 2
    vr.email = 'ale'
    vr.contraseña = 'ale'
    vr.estado = True
    vr.sexo = 'M'
    vr.datosPersonales[0] = 'Hobbies de Alejo'
    vr.datosPersonales[1] = 'Matematica'
    vr.datosPersonales[2] = 'Futbol'
    vr.datosPersonales[3] = 'AyED'
    vr.datosPersonales[4] = 'Fisica'
    vr.datosPersonales[5] = 'Biografia de Alejo'
    vr.datosPersonales[6] = 'Argentina'
    vr.datosPersonales[7] = 'Rosario'
    vr.datosPersonales[8] = '2003/07/11'
    formatearEstudiantes(vr)
    pickle.dump(vr,variableDeArchivoLogicaEstudiantes)
    variableDeArchivoLogicaEstudiantes.flush()
def cargaEstuiante3():
    vr = estudiante()
    variableDeArchivoLogicaEstudiantes.seek(0,2)
    vr.nombre = 'Manuel'
    vr.id = 3
    vr.email = 'manu'
    vr.contraseña = 'manu'
    vr.estado = True
    vr.sexo = 'M'
    vr.datosPersonales[0] = 'Hobbies de Manuel'
    vr.datosPersonales[1] = 'Matematica'
    vr.datosPersonales[2] = 'Futbol'
    vr.datosPersonales[3] = 'AyED'
    vr.datosPersonales[4] = 'Fisica'
    vr.datosPersonales[5] = 'Biografia de Manuel'
    vr.datosPersonales[6] = 'Argentina'
    vr.datosPersonales[7] = 'Firmat'
    vr.datosPersonales[8] = '2004/01/12'
    formatearEstudiantes(vr)
    pickle.dump(vr,variableDeArchivoLogicaEstudiantes)
    variableDeArchivoLogicaEstudiantes.flush()    

def cargar4Estudiantes():
    cargarEstudiante0()
    cargarEstudiante1()
    cargaEstudiante2()
    cargaEstuiante3()
def main():
    if os.path.getsize(variableDeArchivoFisicoAdministradores) == 0:
        cargaAdmi()
    if os.path.getsize(variableDeArchivoFisicoEstudiantes) == 0:
        cargar4Estudiantes()
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
            tipoDeUsuarioLogueado = logueo()
            if tipoDeUsuarioLogueado == 'a':
                    posDelAdmiLogueado = variableDeArchivoLogicaAdministradores.tell() - devolvertamañoDeRegistroDeArchivoAdministradores()
                    op = '1'
                    while op != '0':
                        menuPrincipalAdministradores()
                        op = input('Elige una opcion: ')
                        while op != '0' and op != '1' and op != '2' and op != '3':
                            print('Opcion invalida! Intenta de nuevo. ')
                            op = input('Elige una opcion: ')
                        match op:
                            case '1':
                                gestionarUsuariosSiendoAdmi()
                            case '2':
                                gestionarReportes(posDelAdmiLogueado)
                            case '3':
                                reportesEstadisticosSiendoAdmi()
                            case '0':
                                print('Volviendo a la seccion de logueo')
                                os.system('pause')
            elif tipoDeUsuarioLogueado == 'e': 
                    posDelRegistroDelEstudianteLogueado = variableDeArchivoLogicaEstudiantes.tell() - devolvertamañoDeRegistroDeArchivoEstudiantes()
                    op = '1'
                    while op != '0':
                        menuPrincipalEstudiante()
                        op = input('Elije una opcion: ')
                        while op != '0' and op != '1' and op != '2' and op != '3' and op != '4':
                            print('Opcion invalida! Intenta de nuevo. ')
                            op = input('Elije una opcion: ')
                        match op:
                            case '1': 
                                gestionarMiPerfil(posDelRegistroDelEstudianteLogueado)
                                variableDeArchivoLogicaEstudiantes.seek(posDelRegistroDelEstudianteLogueado,0)
                                vr = pickle.load(variableDeArchivoLogicaEstudiantes)
                                if vr.estado == 'False':
                                    op = '0'
                            case '2': 
                                gestionarCandidatos(posDelRegistroDelEstudianteLogueado)
                            case '3':
                                matcheos()
                            case '4':
                                reportesEstadisticos(posDelRegistroDelEstudianteLogueado)
                            case '0':
                                print('Volviendo a la seccion de logueo...')
                                os.system('pause')
                                
            elif tipoDeUsuarioLogueado == 'm':
                    posDelModLogueado = variableDeArchivoLogicaModeradores.tell() - devolvertamañoDeRegistroDeArchivoModeradores()
                    op = '1'
                    while op != '0':
                        menuPrincipalModeradores()
                        op = input('Elige una opcion: ')
                        while op != '1' and op != '2' and op != '3' and op != '0':
                            print('Opcion invalida! Intenta de nuevo ')
                            op = input('Elige una opcion: ')
                        match op:
                            case '1':
                                gestionarUsuarios()
                            case '2':
                                gestionarReportes(posDelModLogueado)
                            case '3':
                                print('En Contruccion! Disculpa las molestias.')
                                os.system('Pause')
                            case '0':
                                print('Volviendo a la seccion de logueo...')
                                print()
                                os.system('pause')                  
            else:
                    print('No se logueo nadie. Vuelve mas tarde')
                    logOReg = '0'
        elif logOReg == '2':
            altaEstudiantes()
        else:
            print('Hasta Luego! ')

    variableDeArchivoLogicaAdministradores.close()
    variableDeArchivoLogicaEstudiantes.close()
    variableDeArchivoLogicaModeradores.close()
    variableDeArchivoLogicaLikes.close()
    variableLogicaDeArchivoReportes.close()
    
    
variableDeArchivoFisicoEstudiantes = 'C:\\AYED\\Estudiantes.dat'
variableDeArchivoFisicoModeradores = 'C:\\AYED\\Moderadores.dat'
variableDeArchivoFisicoAdministradores = 'C:\\AYED\\Administradores.dat'
variableDeArchivoFisicoLikes = 'C:\\AYED\\Likes.dat'
variableDeArchivoFisicoReportes = 'C:\\AYED\\Reportes.dat'

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
if not os.path.exists(variableDeArchivoFisicoLikes):
    variableDeArchivoLogicaLikes = open (variableDeArchivoFisicoLikes,'w+b')
else:
    variableDeArchivoLogicaLikes = open(variableDeArchivoFisicoLikes,'r+b')
if not os.path.exists(variableDeArchivoFisicoReportes):
    variableLogicaDeArchivoReportes = open (variableDeArchivoFisicoReportes,'w+b')
else:
    variableLogicaDeArchivoReportes = open (variableDeArchivoFisicoReportes,'r+b')

main()