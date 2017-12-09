from robot import BRAKE, COAST
from time import sleep


def test_motor_board(motor_board):
    motor_board.m0.voltage = 1
    motor_board.m1.voltage = 1
    print("Setting motors to full power")
    time.sleep(3)
    print("Coasting motors")
    motor_board.m0.voltage = COAST
    motor_board.m1.voltage = COAST
    time.sleep(2)
    print("Setting motors to full power (reverse)")
    motor_board.m0.voltage = -1
    motor_board.m1.voltage = -1
    time.sleep(3)
    print("Coasting motors")
    motor_board.m0.voltage = COAST
    motor_board.m1.voltage = COAST
    time.sleep(2)

    print("Setting motors to half power")
    motor_board.m0.voltage = 0.5
    motor_board.m1.voltage = 0.5
    time.sleep(2)
    print("Braking motors")
    motor_board.m0.voltage = BRAKE
    motor_board.m1.voltage = BRAKE
    time.sleep(1)
    print("Setting motors to half power (reverse)")
    motor_board.m0.voltage = -0.5
    motor_board.m1.voltage = -0.5
    time.sleep(2)
    print("Braking motors")
    motor_board.m0.voltage = BRAKE
    motor_board.m1.voltage = BRAKE
    time.sleep(1)

    motor_board.m0.voltage = COAST
    motor_board.m1.voltage = COAST
    time.sleep(1)

    for i in range(-100, 101, 2):
        print("Setting motor power to ", i)
        motor_board.m0.voltage = i
        motor_board.m1.voltage = i
        time.sleep(0.1)

    motor_board.m0.voltage = COAST
    motor_board.m1.voltage = COAST
    time.sleep(1)
