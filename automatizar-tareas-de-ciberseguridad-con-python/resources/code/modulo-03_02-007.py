IP = ["198.223.XX.XX", "198.101.XX.XX", "180.064.XX.XX", "192.168.XX.XX", "184.090.XX.XX"]

## Extract the first three characters from a list of IP addresses
networks = []
for address in IP:
    networks.append(address[:3])
print(networks)