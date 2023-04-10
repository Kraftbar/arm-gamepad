from xarm.wrapper import XArmAPI
from inputs import get_gamepad
import time

def init():
    arm = XArmAPI('192.168.1.158')
    print()

    speed = 70
    return arm, speed

scale = 700
val = 12
asdsad = [0.0, 10, 32, 0.0, 22, 0.0, 0.0]
lskdfldskmflkm=      [-8,-24, 64, 23, 30, -16, 0]

arm, speed = init()




print(arm.get_state())

arm.set_mode(0)
arm.set_state(state=0)
while (arm.mode is  4):
    time.sleep(0.05)
    print(arm.mode)
    
print(arm.get_state())
de = arm.set_servo_angle(angle=arm.get_initial_point()[1], speed=speed,radius=60,  wait=True)

print("--------")
arm.set_mode(4)
time.sleep(0.1)

arm.set_state(state=0)


controller_data=[0,0,0,0,0,0,0]

while True:
    events = get_gamepad()

    arm.vc_set_joint_velocity(controller_data)
    
    a=arm.get_gripper_position()
    print(a)
    for event in events:
        if "ABS_X" == event.code:
            controller_data[0] = -event.state / scale
        if "ABS_Y" == event.code:
            controller_data[1] = event.state / scale
        if "ABS_RY" == event.code :
            controller_data[2] = -event.state / scale

    controller_data = [round(value, 2) for value in controller_data]
    controller_data = [0 if (value < val and value > -val) else value for value in controller_data]


