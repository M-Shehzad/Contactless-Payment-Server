from xmlrpc.server import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
import base64
import numpy as np
import cv2


class machine:
    def __init__(self, port) -> None:
        self.port = port
        with SimpleXMLRPCServer(('192.168.1.6', self.port), requestHandler = SimpleXMLRPCRequestHandler) as server:
            print(f"Activated port {self.port}")


            @server.register_function # DECORATOR FOR REGISTERING PROCEDURES THAT CAN BE CALLED BY CLIENTS
            def saveImage(file):
                image = base64.b64decode(file.encode())
                with open('../captureFromPi.jpg', 'wb') as f:
                    f.write(image)
                return "Done"
            
            @server.register_function # DECORATOR FOR REGISTERING PROCEDURES THAT CAN BE CALLED BY CLIENTS to show image using opencv
            def showImage(file):
                image = base64.b64decode(file.encode())
                np_arr = np.frombuffer(image, np.uint8)
                img_np = cv2.imdecode(np_arr, 1)
                cv2.imshow('Live feedback', img_np)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    cv2.destroyAllWindows()
                return "Done"

            try:
                # server.handle_request() # HANDLE ONE REQUEST AND THEN SHUTDOWN THE SERVER
                server.serve_forever() # HANDLE ONE REQUEST AND THEN SHUTDOWN THE SERVER
            # ALTERNATIVELY WE CAN USE server.serve_forever() TO KEEP THE SERVER RUNNING IN INFINITE LOOP
            except KeyboardInterrupt:
                print("Exiting")
                server.server_close()
                exit()

# try:
#     machine(8111)
# except KeyboardInterrupt:
#     print("Exiting")

machine(8111)