from color import Color, ColorName, name_color
from robot import Robot

DRIVE_VELOCITY = 500

class States():
    DRIVE = 0

def main():
    robot = Robot()

    state = States.DRIVE

    if state == States.DRIVE:
        if robot.target_velocity != DRIVE_VELOCITY:
            robot.move_vel(DRIVE_VELOCITY)

        

if __name__ == "__main__":
    main()

