from netmiko import ConnectHandler
import datetime

# Configuración del dispositivo Fortinet
fw_01 = {
    'host': '192.168.126.130',
    'username': 'admin',
    'password': 'admin',
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
    nombre_archivo = f"backup_{fw_01['host']}_{fecha_actual}.conf"
    with open(nombre_archivo, "w") as backup_file:
        backup_file.write(full_config)
    print(f"Backup guardado en: {nombre_archivo}")

except Exception as e:
    print(f"Error: {e}")
finally:
    # Cerrar la conexión
    net_connect.disconnect()
    print("Conexión cerrada.")