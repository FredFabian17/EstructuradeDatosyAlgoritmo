# Hacer backup por consola de Fortinet
# Importar librerías
import paramiko
import time  # Para manejar el tiempo de espera entre comandos
import os  # Para crear carpetas
import datetime  # Para obtener la fecha y hora actual para el nombre del archivo
import getpass  # Para ocultar la contraseña al escribirla en la consola

def realizar_backup(ip, usuario, password, nombre_dispositivo):
    """
    Realiza un backup de la configuración de un dispositivo Fortinet.
    
    :param ip: Dirección IP del dispositivo
    :param usuario: Usuario para la conexión SSH
    :param password: Contraseña para la conexión SSH
    :param nombre_dispositivo: Nombre del dispositivo para identificar el archivo de backup
    """
    # Crear una carpeta para almacenar los backups si no existe
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nombre_carpeta = f"Backups_{fecha_actual}"
    if not os.path.exists(nombre_carpeta):
        os.makedirs(nombre_carpeta)

    # Crear el nombre del archivo de backup
    nombre_archivo = f"{nombre_dispositivo}_{fecha_actual}.conf"
    ruta_archivo = os.path.join(nombre_carpeta, nombre_archivo)

    # Establecer la conexión SSH con el dispositivo Fortinet
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username=usuario, password=password)

    # Abrir un canal de shell
    shell = ssh.invoke_shell()
    time.sleep(1)  # Esperar a que se establezca la conexión

    # Ejecutar el comando para iniciar el backup
    shell.send("config system \n")
    time.sleep(1)
    shell.send("exec backup config flash\n")
    time.sleep(1)

    # Leer la salida del comando y guardarla en el archivo
    with open(ruta_archivo, "w") as archivo_backup:
        while True:
            salida = shell.recv(65535).decode("utf-8")
            archivo_backup.write(salida)
            if "Backup complete" in salida:  # Verificar si el backup se completó
                break

    # Cerrar la conexión SSH
    shell.close()
    ssh.close()

    print(f"Backup completado. Archivo guardado en: {ruta_archivo}")

if __name__ == "__main__":
    # Solicitar datos al usuario
    ip = input("Ingrese la dirección IP del dispositivo Fortinet: ")
    usuario = input("Ingrese el usuario para la conexión SSH: ")
    password = getpass.getpass("Ingrese la contraseña para la conexión SSH: ")
    nombre_dispositivo = input("Ingrese el nombre del dispositivo: ")

    # Llamar a la función con los datos proporcionados
    realizar_backup(ip, usuario, password, nombre_dispositivo)