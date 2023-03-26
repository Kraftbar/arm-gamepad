import os
from inputs import get_gamepad

while True:
    events = get_gamepad()
    for event in events:
        if ("ABS_X"==event.code):
            offset=event.state/700
            print("offset"+str(offset))





exit()

# nc -l 12345 | python3 xarm_control.py
import os
import struct

def read_controller_events(device_path):
    with open(device_path, 'rb') as device:
        while True:
            event = device.read(8)
            if event:
                time, value, event_type, event_number = struct.unpack('IhBB', event)
                yield time, value, event_type, event_number

def readcontroller(device_path='/dev/input/js0'):
    controller_data = [0, 0, 0, 0, 0, 0]
    for event_time, event_value, event_type, event_number in read_controller_events(device_path):
        if event_type == 2:
            if event_number == 0:
                controller_data[0] = event_value
            elif event_number == 1:
                controller_data[1] = event_value
            elif event_number == 3:
                controller_data[2] = event_value
            elif event_number == 4:
                controller_data[3] = event_value
    return controller_data

def main():
    while True:
        controller_data = readcontroller()
        controller_data_str = ' '.join(str(x) for x in controller_data)
        print(controller_data_str)

if __name__ == "__main__":
    main()
