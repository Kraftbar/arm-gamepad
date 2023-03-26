# nc -l 12345 | python3 joystick_reader.py
from xarm.wrapper import XArmAPI
import numpy as np
import sys

def init():
    arm = XArmAPI('192.168.1.158')
    print(arm.get_state())
    arm.motion_enable(enable=True)
    arm.set_mode(4)
    arm.set_state(state=0)
    speed = 70
    return arm, speed

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
    for controller_data_str in sys.stdin:
        controller_data = [float(x) for x in controller_data_str.split()]
        if not controller_data:
            break
        _, servo = arm.get_servo_angle()
        output, error = pd_controller(servo - controller_data, last_error)
        last_error = error
        arm.vc_set_joint_velocity(output.tolist())

if __name__ == "__main__":
    main()
