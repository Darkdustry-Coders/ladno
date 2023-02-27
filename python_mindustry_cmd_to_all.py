import socket

host = 'localhost'
port = 6859
num  = 9
command = input("Command: ")

print(f"The following command will be sent to ALL servers on socket ports {port}-{port+num}:")
print(f"    {command}")
print(f"If you are sure about this, type 'yes'")
if input(">").lower() != "yes":
    print("Aborted.")
    exit()

for i in range(num):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (host, port+i)
    sock.connect(server_address)
    sock.sendall(command.encode())
    print(f"Sent successfully to {port+i}")
    sock.close()
