import socket
from PIL import Image
import io

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('192.168.1.5', 8222))

print("Port 8222 is activated")
while True:
    try:
        data, addr = s.recvfrom(100000)
        # print(data)
        video = Image.open(io.BytesIO(data))
        video.save("../captureVideoFromPi.mp4")
        video.show()
    except KeyboardInterrupt:
        print("Exiting")
        s.close()
        exit()