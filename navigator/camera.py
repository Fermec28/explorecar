import base64
import cv2
from threading import Thread

def thread1(threadname, instance):
    while instance._FINISH:
        rabbed, frame = instance.camera.read()  # grab the current frame
        encoded, buffer = cv2.imencode('.jpg', frame)
        instance.image = base64.b64encode(buffer)


class Camera:
    def __init__(self, camera_id):
        self.camera = cv2.VideoCapture(camera_id)
        self.camera.set(3 ,640)
        self.camera.set(3 ,480)
        self.image = ""
        self._FINISH = True
        self.thread = Thread( target=thread1, args=("Thread",self) )
        self.thread.start()

    def delete_camera(self):
        self._FINISH = False
        self.camera.release()

    def get_image(self):
        return self.image
