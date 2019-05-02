import socket

s = socket.socket()
s.connect(("localhost", 9999))

while True:
    mensaje = raw_input("> ")
    blah = s.send(mensaje)
    print(blah)
    if mensaje == "quit":
        break
    
print "adios"

s.close()  
