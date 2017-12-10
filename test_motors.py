from robot import BRAKE, COAST
from time import sleep


def test_motor_board(motor_board):
    motor_board.m0 = 1
    motor_board.m1 = 1
    print("Setting motors to full power")
    sleep(3)
    print("Coasting motors")
    motor_board.m0 = COAST
    motor_board.m1 = COAST
    sleep(2)
    print("Setting motors to full power (reverse)")
    motor_board.m0 = -1
    motor_board.m1 = -1
    sleep(3)
    print("Coasting motors")
    motor_board.m0 = COAST
    motor_board.m1 = COAST
    sleep(2)

    print("Setting motors to half power")
    motor_board.m0 = 0.5
    motor_board.m1 = 0.5
    sleep(2)
    print("Braking motors")
    motor_board.m0 = BRAKE
    motor_board.m1 = BRAKE
    sleep(1)
    print("Setting motors to half power (reverse)")
    motor_board.m0 = -0.5
    motor_board.m1 = -0.5
    sleep(2)
    print("Braking motors")
    motor_board.m0 = BRAKE
    motor_board.m1 = BRAKE
    sleep(1)

    motor_board.m0 = COAST
    motor_board.m1 = COAST
    sleep(1)

    for i in range(-1, 1.1, 0.2):
        print("Setting motor power to ", i)
        motor_board.m0 = i
        motor_board.m1 = i
        sleep(0.1)

    motor_board.m0 = COAST
    motor_board.m1 = COAST
    sleep(1)
