from netmiko import ConnectHandler

# Detalles del dispositivo
device = {
    "device_type": "cisco_ios",
    "host": "192.168.101.2",  # Cambia por la IP de tu dispositivo
    "username": "ramesh",     # Cambia por tu usuario
    "password": "mypassword", # Cambia por tu contraseña
    "secret": "myenablepassword",  # Cambia por tu contraseña enable
}

# Conexión al dispositivo
net_connect = ConnectHandler(**device)
net_connect.enable()

# Comandos de configuración
config_commands = [
    "hostname myswitch",
    "ip domain-name thegeekstuff.com",
    "crypto key generate rsa modulus 1024",
    "ip default-gateway 192.168.101.1",
    "interface vlan 101",
    "ip address 192.168.101.2 255.255.255.0",
    "no shutdown",
    "line vty 0 4",
    "transport input ssh",
    "login local",
    "password 7",
    "line console 0",
    "logging synchronous",
    "login local",
    "username ramesh password mypassword",
    "enable secret myenablepassword",
    "service password-encryption",
]

# Enviar comandos al dispositivo
output = net_connect.send_config_set(config_commands)
print(output)

# Guardar la configuración
save_output = net_connect.save_config()
print(save_output)

# Cerrar la conexión
net_connect.disconnect()