import socket
import io
import numpy as np
import cv2
import base64

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('192.168.1.6', 8222))

print("Port 8222 is activated")
while True:
    try:
        data, addr = s.recvfrom(2**16)
        # print(data)
        # video = Image.open(io.BytesIO(data))
        # video.save("../captureVideoFromPi.mp4")
        # video.show().
        # data = io.BytesIO(data)
        # data = base64.b64decode(data)
        # np_arr = np.frombuffer(data, np.uint8)
        # img_np = cv2.imdecode(np_arr, 1)
        # print(np_arr)
        # cv2.imshow('Live feedback', img_np)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

        data = data.decode()
        print(data)
    except KeyboardInterrupt:
        print("Exiting")
        s.close()
        exit()