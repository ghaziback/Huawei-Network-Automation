from netmiko import ConnectHandler
from secrets import DEVICE

print("connecting to router...")
connection = ConnectHandler(**DEVICE)

print("Connected! Sending Commands")
output = connection.send_command('display version')
print(output)

connection.disconnect()
print("Disconnect")