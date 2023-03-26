import socket
from inputs import get_gamepad
import time

IP = '89.9.145.109'  # Replace with the desired IP address
PORT = 12345
scale = 700
val = 12
controller_data = [0, 0, 0, 0, 0, 0]

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    events = get_gamepad()
    for event in events:
        if "ABS_X" == event.code:
            controller_data[0] = event.state / scale
        if "ABS_Y" == event.code:
            controller_data[1] = event.state / scale
        if "ABS_RX" == event.code:
            controller_data[2] = event.state / scale
        if "ABS_RY" == event.code:
            controller_data[3] = event.state / scale

    controller_data = [round(value, 2) for value in controller_data]
    controller_data = [0 if (value < val and value > -val) else value for value in controller_data]
    print(controller_data)

    # Convert the controller_data list to a string, so it can be sent over UDP
    data_str = str(controller_data) +'\n'

    sock.sendto(data_str.encode(), (IP, PORT))

    time.sleep(0.01)  # Add a small delay to reduce CPU usage
