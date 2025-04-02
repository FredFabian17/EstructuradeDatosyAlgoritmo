# Configuración básica de un router Cisco
# Importar librerías
import paramiko
import time
import getpass

def configurar_router(ip, usuario, password, segmentos):
    """
    Configura un router Cisco con una configuración básica.

    :param ip: Dirección IP del router
    :param usuario: Usuario para la conexión SSH
    :param password: Contraseña para la conexión SSH
    :param segmentos: Diccionario con los segmentos de red para las interfaces
    """
    try:
        # Establecer la conexión SSH con el router
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Configurar los algoritmos de MAC compatibles
        ssh_transport = paramiko.Transport((ip, 22))
        ssh_transport.get_security_options().macs = [
            "hmac-sha1",
            "hmac-sha1-96",
            "hmac-md5",
            "hmac-md5-96"
        ]
        ssh_transport.connect(username=usuario, password=password)

        # Abrir un canal de shell
        shell = ssh_transport.open_session()
        shell.invoke_shell()
        time.sleep(1)

        # Entrar al modo de configuración global
        shell.send("enable\n")
        time.sleep(1)
        shell.send("configure terminal\n")
        time.sleep(1)

        # Configurar Ethernet 0/0 como DHCP
        shell.send("interface Ethernet0/0\n")
        time.sleep(1)
        shell.send("ip address dhcp\n")
        time.sleep(1)
        shell.send("no shutdown\n")
        time.sleep(1)
        shell.send("exit\n")
        time.sleep(1)

        # Configurar las otras interfaces con los segmentos proporcionados
        for interfaz, segmento in segmentos.items():
            shell.send(f"interface {interfaz}\n")
            time.sleep(1)
            shell.send(f"ip address {segmento['ip']} {segmento['mascara']}\n")
            time.sleep(1)
            shell.send("no shutdown\n")
            time.sleep(1)
            shell.send("exit\n")
            time.sleep(1)

        # Salir de la configuración
        shell.send("end\n")
        time.sleep(1)
        shell.send("write memory\n")
        time.sleep(2)

        # Leer la salida del comando
        salida = shell.recv(65535).decode("utf-8")
        print(salida)

        # Cerrar la conexión SSH
        shell.close()
        ssh_transport.close()

        print("Configuración básica del router completada exitosamente.")

    except paramiko.AuthenticationException:
        print("Error: Fallo en la autenticación. Verifique el usuario y la contraseña.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Solicitar datos al usuario
    ip = input("Ingrese la dirección IP del router: ")
    usuario = input("Ingrese el usuario para la conexión SSH: ")
    password = getpass.getpass("Ingrese la contraseña para la conexión SSH: ")

    # Solicitar los segmentos de red para las interfaces
    segmentos = {}
    for i in range(1, 4):  # Ethernet 0/1, 0/2, 0/3
        interfaz = f"Ethernet0/{i}"
        print(f"Configuración para {interfaz}:")
        ip_segmento = input(f"Ingrese la dirección IP para {interfaz} (por ejemplo, 192.168.{i}.1): ")
        mascara_segmento = input(f"Ingrese la máscara de subred para {interfaz} (por ejemplo, 255.255.255.0): ")
        segmentos[interfaz] = {"ip": ip_segmento, "mascara": mascara_segmento}

    # Llamar a la función con los datos proporcionados
    configurar_router(ip, usuario, password, segmentos)