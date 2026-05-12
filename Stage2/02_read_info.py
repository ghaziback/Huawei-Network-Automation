# stage2/02_read_info.py

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from device_config import DEVICE  # now it works from anywhere
from netmiko import ConnectHandler


print("Connecting to Router ... ")
connection = ConnectHandler(**DEVICE)
print("Connected !\n")

# --- Pull raw output ---
vlan_output = connection.send_command('dis vla summ')
info_output = connection.send_command('dis ip interf brie')

print("=== VLAN SUMMARY ===")
print(vlan_output)

print("\n === IP INTERFACES === ")
print(info_output)

connection.disconnect()
print("\n Disconnect Done !!!")