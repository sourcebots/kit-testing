from robot import PinMode
from time import sleep


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
        assert len(values) == 6
        sleep(1)


def test_servos(servo_assembly):
    for servo_pin in range(0, 16):
        print("Setting servo {} to 1".format(servo_pin))
        servo_assembly.servos[servo_pin].position = 1
        sleep(1)
        print("Setting servo {} to -1".format(servo_pin))
        servo_assembly.servos[servo_pin].position = -1
        sleep(1)
        print("Setting servo {} to 0".format(servo_pin))
        servo_assembly.servos[servo_pin].position = 0
        sleep(1)


def test_ultrasound(servo_assembly):
    for i in range(5):
        print("Testing ultrasound on pins 6 and 7")
        distance = servo_assembly.read_ultrasound(6, 7)
        assert distance < 0.4
        assert distance > 0.2
        print("Distance was {}".format(distance))
        sleep(1)


def test_servo_assembly(servo_assembly):
    test_GPIO(servo_assembly)
    test_analogue(servo_assembly)
    test_servos(servo_assembly)
    test_ultrasound(servo_assembly)
