import motor, distance_sensor
import color_sensor as colour_sensor
from hub import port
import time as t

class Motor:
    port: any
    reversed: bool

    def __init__(self, port: any, reversed: any):
        self.port = port
        self.reversed = reversed
    
    def move_cm(self, dist):
        self.target_dist = dist
        degrees = int(20.8348289139*dist)
        motor.run_for_degrees(self.port, degrees, 180 * (-1 if self.reversed else 0))

    def move_vel(self, port, vel):
        self.target_vel = vel
        motor.run(left_motor, vel)
        motor.run(right_motor, vel)

    def rotate_deg(self, deg):
        #35.5, 10.14
        self.target_deg = deg
        motor.run_for_degrees(left_motor, (deg*10.14), -180)
        motor.run_for_degrees(right_motor, (-deg*10.14), 180)

class Robot:
    left_motor = Motor(port.C, True)
    right_motor = Motor(port.D, False)

    def __init__(self):
        self.DtoCM = 20.8348289139



if __name_ == "__main__":
    robot = Robot()

    robot.rotate_deg(90)
