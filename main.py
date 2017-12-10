from robot import Robot
from time import sleep
import test_motors
import test_power
import test_servo

TEST_MOTOR_BOARD = True
TEST_POWER_BOARD = True
TEST_SERVO_ASSEMBLY = True


def test_board(board, test_function):
    print("Testing board {}".format(board.serial))
    test_function(board)
    print("Testing board {} Complete!".format(board.serial))
    print("\n\n")


if __name__ == '__main__':
    r = Robot()

    if TEST_SERVO_ASSEMBLY:
        for servo_assembly in r.servo_boards:
            test_board(servo_assembly, test_servo.test_servo_assembly)
    
    if TEST_MOTOR_BOARD:
        for motor_board in r.motor_boards:
            test_board(motor_board, test_motors.test_motor_board)

    if TEST_POWER_BOARD:
        for power_board in r.power_boards:
            test_board(power_board, test_power.test_power_board)
    
