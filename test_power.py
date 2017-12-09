from time import sleep

def test_power_board(power_board):
    for i in range(5):
        sleep(1)
        print("Turning on outputs")
        power_board.power_on()
        sleep(1)
        print("Turning off outputs")
        power_board.power_off()