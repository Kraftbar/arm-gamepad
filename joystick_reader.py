# nc -l -u 12345 | python3 joystick_reader.py
# Expects example stdin "[0.12, 12.35, -9.88, 25.79, -10.11, 4.57]"

from xarm.wrapper import XArmAPI
import numpy as np
import sys
import ast 
import time
import threading
import asyncio
from multiprocessing import Pool

from collections import deque
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

def clearError(arm):
    arm.clean_error()
    arm.set_mode(4)
    arm.set_state(state=0)
    while (arm.mode !=  4):
        time.sleep(0.05)

def toggleGripper():
    print("asdadmaksjndjkandlkjnsaljknaslkjfnsdlkjn")
    if(gripperClosedFlag):
        arm.open_lite6_gripper()
        time.sleep(3)
        arm._arm.stop_lite6_gripper()
    else:
        arm.close_lite6_gripper()
        time.sleep(3)

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


if __name__ == "__main__":
    arm, speed = init()
    gripperClosedFlag=0
    controller_data_history = deque([[0 for _ in range(12)] for _ in range(4)], maxlen=4)
    pool = Pool(processes=4)             
    worker = None

    for controller_data_str in sys.stdin:
        print(controller_data_str)
        controller_data_str=controller_data_str.strip()
        controller_data_str = controller_data_str.strip('[]').split(', ')
        controller_data = [float(value) for value in controller_data_str]
        arm.vc_set_joint_velocity(controller_data[:6])
        controller_data_history.append(controller_data)  

        if controller_data_history[2][7] == 0 and controller_data_history[3][7] == 100 :
            print("aaaaaaaaaaaaaaaaaa")
            worker = pool.apply_async(toggleGripper, args=(arm, gripperClosedFlag))
            gripperClosedFlag = 1 - gripperClosedFlag
        if controller_data[8] == 100:
            clearError(arm)
        if controller_data[11] == 100:
            setInitialState(arm,speed)
        print(controller_data[7])
        if not controller_data:
            break
        _, servo = arm.get_servo_angle()
    result = worker.get()

    pool.close()
    pool.join() 

