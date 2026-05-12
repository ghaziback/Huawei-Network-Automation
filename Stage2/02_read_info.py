# stage2/02_read_info.py

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from netmiko import ConnectHandler
from device_config import DEVICE 

# ─── 1. Connect ───────────────────────────────────────────
print("Connecting to Router ... ")
connection = ConnectHandler(**DEVICE)
print("Connected !\n")


# ─── 2. Pull raw output ───────────────────────────────────
info_output = connection.send_command('dis ip interf brie')
connection.disconnect()

# ─── 3. Parse it ──────────────────────────────────────────
lines = info_output.splitlines()

# skip junk, keep data
skip_words = [
    '*down:', '!down:', '^down:',
    '(l):', '(s):', '(d):', '(E):',
    'The number', 'Interface',
    '---- More ----'
]

for i ,line in enumerate(lines):
    #skip emty lines
    if not line.strip():
        continue

    #skip header/legened lines
    if any(word in line for word in skip_words):
        continue

    # Split the line into parts
    parts = line.split()

    print(f"parts = {parts}")
    print(f"  [0] interface = {parts[0]}")
    print(f"  [1] ip        = {parts[1]}")
    print(f"  [2] physical  = {parts[2]}")
    print(f"  [3] protocol  = {parts[3]}")
    print(f"  [4] vpn       = {parts[4] if len(parts) >= 5 else '--'}")
    print()