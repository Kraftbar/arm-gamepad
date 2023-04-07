# nc -l -u 12345 | python3 joystick_reader.py
# Expects example stdin "[0.12, 12.35, -9.88, 25.79, -10.11, 4.57]"

from xarm.wrapper import XArmAPI
import numpy as np
import sys
import ast 
import time

def init():
    arm = XArmAPI('192.168.1.158')
    print(arm.get_state())
    arm.motion_enable(enable=True)
    arm.set_mode(4)
    arm.set_state(state=0)
    speed = 10
    return arm, speed
global gripperClosedFlag=0
def toggleGripper(arm):
    if(gripperClosedFlag):
        arm.close_lite6_gripper()
        gripperClosedFlag=1

    if(gripperClosedFlag):
        arm.open_lite6_gripper()
        time.sleep(0.5)
        arm._arm.stop_lite6_gripper()
        gripperClosedFlag=0


def main():
    arm, speed = init()
    for controller_data_str in sys.stdin:
        print(controller_data_str)
        controller_data_str=controller_data_str.strip()
        controller_data_str = controller_data_str.strip('[]').split(', ')
        controller_data = [float(value) for value in controller_data_str]
        arm.vc_set_joint_velocity(controller_data[:6])
        if controller_data[7] == 100:
            toggleGripper(arm)  # Close the gripper (0-850)
        print(controller_data[7])
        if not controller_data:
            break
        _, servo = arm.get_servo_angle()




if __name__ == "__main__":
    main()
