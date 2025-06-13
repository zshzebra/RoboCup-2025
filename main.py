from color import Color, ColorName, name_color
from robot import Robot

DRIVE_VELOCITY = 500

class States():
    DRIVE = 0
    ROTATE = 1

def main():
    robot = Robot()

    state = States.DRIVE

    if state == States.DRIVE:
        if robot.target_velocity != DRIVE_VELOCITY:
            robot.move_vel(DRIVE_VELOCITY)

        colors = robot.read_colors()
        if colors[0] == ColorName.GREEN:
            

if __name__ == "__main__":
    main()

