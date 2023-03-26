# python3 | nc -u 89.9.145.109 4444
from inputs import get_gamepad

scale=700
val=12
controller_data = [0, 0, 0, 0, 0, 0]
while True:
    events = get_gamepad()
    for event in events:
        if ("ABS_X"==event.code):
            controller_data[0]=event.state/scale
        if ("ABS_Y"==event.code):
            controller_data[1]=event.state/scale
        if ("ABS_RX"==event.code):
            controller_data[2]=event.state/scale
        if ("ABS_RY"==event.code):
            controller_data[3]=event.state/scale
    controller_data = [round(value, 2) for value in controller_data]
    controller_data = [0 if (value < val and value > -val) else value for value in controller_data]
    print(controller_data)

