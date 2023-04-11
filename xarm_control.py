import socket
from inputs import get_gamepad
import time

IP = '89.9.145.192' 
PORT = 12345
scale = 700
val = 12
controller_data = [0] * 12
a_button_state=0
event_code=""
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    while True:
        events = get_gamepad()

        for event in events:
            print(event.state)
            if "ABS_X" == event.code:
                controller_data[0] = -event.state / scale
            if "ABS_Y" == event.code:
                controller_data[1] = event.state / scale
            if "ABS_RY" == event.code:
                controller_data[2] = -event.state / scale
            if "ABS_Z" == event.code:
                controller_data[5] = (event.state)/2
            if "ABS_RZ" == event.code:
                controller_data[5] = -(event.state)/2
            if event.code == "BTN_SOUTH":  
                controller_data[7] = event.state*100
            if event.code == "BTN_EAST":  
                controller_data[8] = event.state*100
            if event.code == "BTN_WEST":  # bug in lib
                controller_data[9] = event.state*100
            if event.code == "BTN_NORTH": # bug in lib
                controller_data[10] = event.state*100
            if event.code == "BTN_START":  
                controller_data[11] = event.state*100

        if "SYN_REPORT"== event.code: 
            continue

        controller_data = [round(value, 2) for value in controller_data]
        controller_data = [0 if (value < val and value > -val) else value for value in controller_data]
        print(controller_data)

        # Convert the controller_data list to a string, so it can be sent over UDP
        data_str = str(controller_data) +'\n'

        sock.sendto(data_str.encode(), (IP, PORT))

except KeyboardInterrupt:
    print("\nClosing socket and exiting...")
    sock.close()
