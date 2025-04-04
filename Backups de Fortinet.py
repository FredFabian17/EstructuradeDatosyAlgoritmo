import os
from netmiko import ConnectHandler
import datetime

# Solicitar datos al usuario
host = input("Ingrese la dirección IP del dispositivo Fortinet: ")
username = input("Ingrese el usuario para la conexión SSH: ")
password = input("Ingrese la contraseña para la conexión SSH: ")
nombre_archivo = input("Ingrese el nombre del archivo de backup (sin extensión): ")

# Configuración del dispositivo Fortinet
fw_01 = {
    'host': host,
    'username': username,
    'password': password,
    'device_type': 'fortinet',
    'port': 22,
}

try:
    print(f"{'#' * 20} Connecting to Fortinet Firewall {'#' * 20}")
    net_connect = ConnectHandler(**fw_01)
    print(f"Connected to {fw_01['host']}")

    # Deshabilitar la paginación para evitar problemas con '--more--'
    net_connect.send_command("config global")
    net_connect.send_command("set output standard")
    net_connect.send_command("end")

    # Obtener la configuración completa
    print(f"{'#' * 20} Getting Configuration {'#' * 20}")
    command = 'show full-configuration'
    full_config = net_connect.send_command(command)

    # Guardar la configuración en un archivo
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    archivo_completo = f"{nombre_archivo}_{fecha_actual}.conf"
    with open(archivo_completo, "w") as backup_file:
        backup_file.write(full_config)
    print(f"Backup guardado en: {archivo_completo}")

except Exception as e:
    print(f"Error: {e}")
finally:
    # Cerrar la conexión
    net_connect.disconnect()
    print("Conexión cerrada.")
os.system("pause")