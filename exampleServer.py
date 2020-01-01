import socket
import json
import struct

def packetGenerator():
    gamePacket ={
        "frame": 0,
        "score": [
            0,
            0
        ],
        "ball": {
            "position": [
                0.0,
                0.0,
                0.0
            ],
            "velocity": [
                0.0,
                0.0,
                0.0
            ],
            "euler_angles": [
                0.0,
                0.0,
                0.0
            ],
            "angular_velocity": [
                0.0,
                0.0,
                0.0
            ],
            "damage": 0.0,
            "shape": 0,
            "radius": -92.0,
            "height": -1.0
        },
        "cars": [
            {
                "position": [
                    0.0,
                    0.0,
                    0.0
                ],
                "velocity": [
                    0.0,
                    0.0,
                    0.0
                ],
                "euler_angles": [
                    0.0,
                    0.0,
                    0.0
                ],
                "angular_velocity": [
                    0.0,
                    0.0,
                    0.0
                ],
                "boost": 0.0,
                "on_ground": True,
                "jumped": False,
                "double_jumped": False,
                "demolished": False,
                "is_bot": True,
                "team": -1,
                "name": "",
                "body_type": 0,
                "hitbox_offset": [
                    0.0,
                    0.0,
                    0.0
                ],
                "hitbox_dimensions": [
                    0.0,
                    0.0,
                    0.0
                ]
            },
            {
                "position": [
                    0.0,
                    0.0,
                    0.0
                ],
                "velocity": [
                    0.0,
                    0.0,
                    0.0
                ],
                "euler_angles": [
                    0.0,
                    0.0,
                    0.0
                ],
                "angular_velocity": [
                    0.0,
                    0.0,
                    0.0
                ],
                "boost": 0.0,
                "on_ground": True,
                "jumped": False,
                "double_jumped": False,
                "demolished": False,
                "is_bot": True,
                "team": -1,
                "name": "",
                "body_type": 0,
                "hitbox_offset": [
                    0.0,
                    0.0,
                    0.0
                ],
                "hitbox_dimensions": [
                    0.0,
                    0.0,
                    0.0
                ]
            }
        ],
        "goals": [
            {
                "position": [
                    0.0,
                    0.0,
                    0.0
                ],
                "direction": [
                    0.0,
                    0.0,
                    0.0
                ],
                "width": 0.0,
                "height": 0.0,
                "team": 0,
                "state": 0
            },
            {
                "position": [
                    0.0,
                    0.0,
                    0.0
                ],
                "direction": [
                    0.0,
                    0.0,
                    0.0
                ],
                "width": 0.0,
                "height": 0.0,
                "team": 0,
                "state": 0
            }
        ],
        "pads": [
            {
                "position": [
                    0.0,
                    0.0,
                    0.0
                ],
                "type": 0,
                "available": False
            },
            {
                "position": [
                    0.0,
                    0.0,
                    0.0
                ],
                "type": 0,
                "available": False
            }
        ],
        "time_left": 0.0,
        "time_elapsed": 0.0,
        "is_overtime": True,
        "is_round_active": False,
        "is_kickoff_paused": False,
        "is_match_ended": False,
        "is_unlimited_time": False,
        "gravity": -0.0,
        "map": 32758,
        "type": 0
    }
    return gamePacket


def createHeader(jString):
    length = len(jString.encode('utf-8'))
    # header = str(length).encode('utf-8')
    # header+= b' '*(16 - len(header))
    header = struct.pack("H",length)
    return header

def sendPacket(jPacket,socket):
    header = createHeader(jPacket)
    packetBytes = header+bytes(jPacket.encode('utf-8'))
    socket.sendall(packetBytes)

def recieveController(socket):
    recieved = socket.recv(1024)
    header = struct.unpack("H", recieved[:2])[0]
    recieved = recieved[2:]

    while len(recieved) < header:
        recieved += socket.recv(1024)

    controler = json.loads(recieved,encoding='utf-8')
    print(controler)


def server():
    print("server loaded")
    _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _socket.bind(("localhost", 8085))
    _socket.listen(1)  # set how many connections to accept
    print("server awaiting connections")
    client, address = _socket.accept()
    print(f"Client connected from {address}")
    try:
        while True:
            packet = packetGenerator()
            jString = json.dumps(packetGenerator())
            sendPacket(jString,client)

            botInput = recieveController(client)
            print(botInput)
    except Exception as e:
        print(e)
        print("closing server")
        _socket.close()


if __name__ == "__main__":
    server()





