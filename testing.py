from xarm.wrapper import XArmAPI
import os
import struct
import numpy as np
import threading

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

def update_controller_data(device_path, controller_data):
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

    device_path = '/dev/input/js0'
    controller_data = [0, 0, 0, 0]

    # Start a separate thread to update the controller data
    controller_thread = threading.Thread(target=update_controller_data, args=(device_path, controller_data))
    controller_thread.daemon = True
    controller_thread.start()

    while True:
        _, servo = arm.get_servo_angle()
        output, error = pd_controller(servo - controller_data, last_error)
        last_error = error

        ABS_X = controller_data[0]
        if ABS_X > 8 or ABS_X < -8:
            arm.vc_set_joint_velocity([-output, 0, 0, 0, 0, 0])
        else:
            arm.vc_set_joint_velocity([0, 0, 0, 0, 0, 0])

if __name__ == "__main__":
    main()
