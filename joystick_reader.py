# nc -l -u 12345 | python3 joystick_reader.py
# Expects example stdin "[0.12, 12.35, -9.88, 25.79, -10.11, 4.57]"

from xarm.wrapper import XArmAPI
import numpy as np
import sys
import ast 
import time
import threading
# Y:   J2, J3, J5 
# X:   J1 
# rot: J4, J6


def init():
    arm = XArmAPI('192.168.1.158')
    print(arm.get_state())
    arm.motion_enable(enable=True)
    arm.set_mode(4)
    arm.set_state(state=0)
    speed = 80
    return arm, speed

def toggleGripper(arm,gripperClosedFlag):
    # check if already done
    # todo: can receive mulitple 100 at once fix 
    if(gripperClosedFlag):
        arm.open_lite6_gripper()
        timer = threading.Timer(2.0, arm._arm.stop_lite6_gripper(), args=())
        timer.start()
        gripperClosedFlag=0
    else:
        arm.close_lite6_gripper()
        gripperClosedFlag=1
    return gripperClosedFlag


def setInitialState(arm,speed):
    arm.set_mode(0)
    arm.set_state(state=0)
    while (arm.mode !=  0):
        time.sleep(0.05)
    de = arm.set_servo_angle(angle=arm.get_initial_point()[1], speed=speed,radius=60,  wait=True)
    arm.set_mode(4)
    arm.set_state(state=0)
    while (arm.mode !=  4):
        time.sleep(0.05)


def main():
    arm, speed = init()
    gripperClosedFlag=0
    for controller_data_str in sys.stdin:
        print(controller_data_str)
        controller_data_str=controller_data_str.strip()
        controller_data_str = controller_data_str.strip('[]').split(', ')
        controller_data = [float(value) for value in controller_data_str]
        arm.vc_set_joint_velocity(controller_data[:6])
        if controller_data[7] == 100:
            gripperClosedFlag=toggleGripper(arm,gripperClosedFlag)  
        if controller_data[11] == 100:
            setInitialState(arm,speed)
        print(controller_data[7])
        if not controller_data:
            break
        _, servo = arm.get_servo_angle()




if __name__ == "__main__":
    main()
