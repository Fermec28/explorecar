import socket
import base64
import cv2
camera = cv2.VideoCapture(0)  # init the camera

s = socket.socket()
s.bind(("localhost", 3002))
s.listen(1)

sc, addr = s.accept()
print("server running")
while True:
    recibido = sc.recv(1024)
    print(recibido)
    if recibido == "image":
        grabbed, frame = camera.read()  # grab the current frame
        frame = cv2.resize(frame, (640, 480))  # resize the frame
        encoded, buffer = cv2.imencode('.jpg', frame)
        jpg_as_text = base64.b64encode(buffer)
        sc.send("blah")    
    elif recibido == "quit":
        break
print "adios"
    
sc.close()
s.close() 
