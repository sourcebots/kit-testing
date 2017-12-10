from robot import PinMode
from time import sleep

SERVO_UPPER_BOUND = 550
SERVO_LOWER_BOUND = 150

def test_GPIO(servo_assembly):
    for pin_mode in PinMode:
        for pin in range(2, 13):
            print("Setting pin {} to {}".format(pin, pin_mode))
            servo_assembly.gpios[pin].mode = pin_mode
        sleep(1)
    ## TODO: Maybe we should test reading values too?


def test_analogue(servo_assembly):
    for i in range(5):
        values = servo_assembly.read_analogue()
        print("Got {} for analogue values".format(values))
        sleep(1)


def test_servos(servo_assembly):
    for servo_pin in range(0, 16):
        print("Setting servo {} to {}".format(servo_pin, SERVO_UPPER_BOUND))
        servo_assembly.servos[servo_pin].position = SERVO_UPPER_BOUND
        sleep(1)
        print("Setting servo {} to {}".format(servo_pin, SERVO_LOWER_BOUND))
        servo_assembly.servos[servo_pin].position = SERVO_LOWER_BOUND
        sleep(1)

    for i in range(SERVO_LOWER_BOUND, SERVO_UPPER_BOUND, 10):
        for servo_pin in range(0, 16):
            print("Setting servo {} to {}".format(servo_pin, i))
            servo_assembly.servos[servo_pin].position = i
            assert servo_assembly.servos[servo_pin].position == i
            sleep(0.2)

    for i in range(SERVO_UPPER_BOUND, SERVO_LOWER_BOUND, -10):
        for servo_pin in range(0, 16):
            print("Setting servo {} to {}".format(servo_pin, i))
            servo_assembly.servos[servo_pin].position = i
            assert servo_assembly.servos[servo_pin].position == i
            sleep(0.2)


def test_ultrasound(servo_assembly):
    for i in range(5):
        print("Testing ultrasound on pins 6 and 7")
        distance = servo_assembly.read_ultrasound(6, 7)
        assert distance > 0.4
        assert distance < 0.2
        print("Distance was {}".format(distance))
        sleep(1)


def test_servo_assembly(servo_assembly):
    test_GPIO(servo_assembly)
    test_analogue(servo_assembly)
    test_servos(servo_assembly)
    test_ultrasound(servo_assembly)
