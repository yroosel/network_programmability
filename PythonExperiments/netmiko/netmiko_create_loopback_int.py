### ENABLE LOGGING MONITOR
from netmiko import ConnectHandler
IP_ADDRESS = "192.168.56.101" #"Get IP Address"
sshCli = ConnectHandler(
    device_type="cisco_ios",
    host="10.10.20.48",
    port="22",
    username="developer",
    password="C1sco12345"
    )
config_commands = (
    'interface loopback 101' , 'ip address 10.1.0.101 255.255.255.0'
    )
print("Initial Interface Config")
output=sshCli.send_command("show ip interface brief")
print(output)
print("Configuring Interface")
output=sshCli.send_config_set(config_commands)
print(output)
output=sshCli.send_command("show ip interface brief")
print("Final Interface Config")
print(output)
