import runloop
import motor, distance_sensor
import color_sensor as colour_sensor
from hub import port
import time as t
import math as m

class Motor:
    port: any
    reversed: bool
    def __init__(self, port: any, reversed: bool):
        self.port = port
        self.reversed = reversed
    
    def move_cm(self, dist):
        self.target_dist = dist
        degrees = int(10.417414457*dist*2)
        motor.run_for_degrees(self.port, degrees, 180 * (-1 if self.reversed else 1))
    
    def move_vel(self, vel):
        self.target_vel = vel
        motor.run(self.port, vel)
    
    def rotate_deg(self, deg):
        self.target_deg = deg
        #change variable 5.75
        C = 2*m.pi*5.75
        dist = C*(deg/360)
        #after here
        print(2*m.pi*5.75, deg/360, (2*m.pi*5.75)*(deg/360))
        print(round(dist*10.41))
        #WHY DOES THIS WORK WHAT THE FUCKK
        motor.run_for_degrees(self.port, round(dist*10.41*2), -180)

class Robot:
    def __init__(self):
        self.DtoCM = 10.417414457
        self.left_motor = Motor(port.C, True)
        self.right_motor = Motor(port.D, False)
    
    def turn_degrees_gen(self, deg):
        # Start both motors simultaneously
        self.left_motor.rotate_deg(deg)
        self.right_motor.rotate_deg(deg)
        # Yield to allow other operations
        yield
        
    def drive_cm_gen(self, cm):
        # Start both motors simultaneously
        self.left_motor.move_cm(cm)
        self.right_motor.move_cm(cm)
        # Yield to allow other operations
        yield
        
    def drive_vel(self, vel):
        self.right_motor.move_vel(vel)
        self.left_motor.move_vel(vel)

def main():
    robot = Robot()
    
    # Turn the robot 180 degrees
    print("Starting turn")
    turn_gen = robot.turn_degrees_gen(180)
    next(turn_gen)
    
    # Wait for turn to complete
    t.sleep(3)
    
    # Drive 20 cm
    print("Starting drive")
    drive_gen = robot.drive_cm_gen(20)
    next(drive_gen)
    
    # Wait for drive to complete
    t.sleep(2)
    
    print("Program complete")

print("Starting program")
main()
