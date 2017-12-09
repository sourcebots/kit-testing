from robot import Robot
from time import sleep
import test_motors

TEST_MOTOR_BOARD = True


if __name__ == '__main__':
    r = Robot()
    if TEST_MOTOR_BOARD:
        for motor_board in r.motor_boards:
            test_motors.test_motor_board(motor_board)
    
    
