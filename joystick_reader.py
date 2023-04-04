# nc -l -u 12345 | python3 joystick_reader.py
# Expects example stdin "[0.12, 12.35, -9.88, 25.79, -10.11, 4.57]"

from xarm.wrapper import XArmAPI
import numpy as np
import sys
import ast 

def init():
    arm = XArmAPI('192.168.1.158')
    print(arm.get_state())
    arm.motion_enable(enable=True)
    arm.set_mode(4)
    arm.set_state(state=0)
    speed = 10
    return arm, speed



def main():
    arm, speed = init()
    for controller_data_str in sys.stdin:
        print(controller_data_str)
        print("asdadasda")
        controller_data_str=controller_data_str.strip()
        controller_data_str = controller_data_str.strip('[]').split(', ')
        controller_data = [float(value) for value in controller_data_str]
        arm.vc_set_joint_velocity(controller_data[:7])
        if controller_data[7] == 1:
            arm.set_gripper_position(500)  # Close the gripper (0-850)

        if not controller_data:
            break
        _, servo = arm.get_servo_angle()




if __name__ == "__main__":
    main()
