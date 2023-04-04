from xmlrpc.server import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
import base64


class machine:
    def __init__(self, port) -> None:
        self.port = port
        with SimpleXMLRPCServer(('192.168.137.128', self.port), requestHandler = SimpleXMLRPCRequestHandler) as server:
            print(f"Activated port {self.port}")


            @server.register_function # DECORATOR FOR REGISTERING PROCEDURES THAT CAN BE CALLED BY CLIENTS
            def saveImage(file):
                image = base64.b64decode(file.encode())
                with open('../captureFromPi.jpg', 'wb') as f:
                    f.write(image)
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