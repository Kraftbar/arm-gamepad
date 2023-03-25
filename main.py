from xarm.wrapper import XArmAPI
import os
import struct
import numpy as np

def init():
    arm = XArmAPI('192.168.1.158')
    print(arm.get_state())
    arm.motion_enable(enable=True)
    arm.set_mode(4)
    arm.set_state(state=0)
    speed = 70
    return arm, speed

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

def pd_controller(error, last_error, Kp=1, Kd=1, dt=1):
    error = np.array(error)
    last_error = np.array(last_error)

    derivative = (error - last_error) / dt
    output = Kp * error + Kd * derivative
    return output, error

def main():
    arm, speed = init()
    error = [0, 0, 0, 0, 0, 0]
    last_error = [0, 0, 0, 0, 0, 0]
    while True:
        controller_data = readcontroller()
        _, servo = arm.get_servo_angle()
        output, error = pd_controller(servo - controller_data, last_error)
        last_error = error
        arm.vc_set_joint_velocity(output.tolist())

if __name__ == "__main__":
    main()
