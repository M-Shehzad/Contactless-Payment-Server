import socket
from PIL import Image
import io
import numpy as np
import cv2
import base64

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('192.168.137.128', 8222))

print("Port 8222 is activated")
while True:
    try:
        data, addr = s.recvfrom(10000)
        # print(data)
        # video = Image.open(io.BytesIO(data))
        # video.save("../captureVideoFromPi.mp4")
        # video.show().
        # data = base64.b64decode(data)
        np_arr = np.frombuffer(data, np.uint8)
        # img_np = cv2.imdecode(np_arr, 1)
        print(np_arr.shape)
        # cv2.imshow('Live feedback', img_np)
    except KeyboardInterrupt:
        print("Exiting")
        s.close()
        exit()