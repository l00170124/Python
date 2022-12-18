scan = {"192.168.3.10": "80", "192.168.3.11": "443", "192.168.3.55": "22"}
#Using code for the key in the scan: print(key) will 
#return a list of all keys in the dictionary but not the values.
for key in scan:
    print(key)
#Will return all keys and values
for key in scan.items():
    print(key)

for ipv4, port in scan.items(): 
    print(f"Found a service on {ipv4} at {port}")