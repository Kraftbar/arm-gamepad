from xarm.wrapper import XArmAPI
from inputs import get_gamepad
import time

def init():
    arm = XArmAPI('192.168.1.158')
    print(arm.get_state())
    arm.motion_enable(enable=True)
    arm.set_mode(4)
    arm.set_state(state=0)
    speed = 70
    return arm, speed

scale = 700
val = 12
controller_data = [0, 0, 0, 0, 0, 0, 0]

arm, speed = init()

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


    arm.vc_set_joint_velocity(controller_data)

