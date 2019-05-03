import base64
import cv2
from threading import Thread



class Camera:
    def __init__(self, camera_id):
        self.camera = cv2.VideoCapture(camera_id)
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
        self.image = ""
        self._FINISH = True
        self.thread = Thread( target=self.update, args=() )
        self.thread.daemon = True
        self.thread.start()

    def delete_camera(self):
        self._FINISH = False
        self.camera.release()

    def get_image(self):
        return self.image

    def update(self):
        while self._FINISH:
            rabbed, frame = self.camera.read()  # grab the current frame
            encoded, buffer = cv2.imencode('.jpg', frame)
            self.image = base64.b64encode(buffer)
