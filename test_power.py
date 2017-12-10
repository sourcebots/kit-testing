from time import sleep

def test_power_board(power_board):
    for i in range(5):
        sleep(1)
        print("Turning on outputs")
        power_board.power_on()
        sleep(1)
        print("Turning off outputs")
        power_board.power_off()

    for note, frequency in power_board.BUZZ_NOTES.items():
        print("Playing {} on buzzer".format(note))
        power_board.buzz(1, note=note)
        sleep(1)
        print("Playing {} on buzzer as frequency {}".format(note, frequency))
        power_board.buzz(1, frequency=frequency)
        sleep(1)