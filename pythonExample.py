import socket
import json

def controllerGenerator():
    controller = {
        "steer": 0.0,
        "throttle": 0.0,
        "roll": 0.0,
        "pitch": 0.0,
        "yaw": 0.0,
        "jump": False,
        "boost": False,
        "use_item": False,
        "chat": 0
    }

    return controller

def createHeader(jString):
    length = len(jString.encode('utf-8'))
    header = str(length).encode('utf-8')
    header+= b' '*(16 - len(header))
    return header



class SocketBot():
    def __init__(self,):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = 8085
        self.socket.connect(("localhost",8085))

    def recievePacket(self,):
        recieved = self.socket.recv(1024)
        header = int(recieved[:16].decode('utf-8'))
        recieved = recieved[16:]

        while len(recieved) < header:
            recieved += self.socket.recv(1024)

        packet = json.loads(recieved,encoding='utf-8')
        return packet

    def sendControls(self,controler):
        c_string = json.dumps(controler)
        header = createHeader(c_string)
        controlerBytes = header + bytes(c_string.encode('utf-8'))
        self.socket.sendall(controlerBytes)



    def getOutput(self):
        packet = self.recievePacket()
        print(packet)
        blankControls = controllerGenerator()
        self.sendControls(blankControls)


if __name__ == "__main__":
    bot = SocketBot()
    while True:
        bot.getOutput()






