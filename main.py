# https://github.com/jegyed50/jegyed50-bbc-microbit-study365-blocks-03-04-d
# https://github.com/jegyed50/jegyed50-bbc-microbit-study365-blocks-03-04-a/blob/master/03-04-pomodoro-timeline.jpg
# JEGYED50-BBC-MICROBIT-STUDY365-BLOCKS-03-04-D
# Mint C, csak a szünetek értéke változókkal: short_rest_time, long_rest_time, working_time,working_text, rest_text

def on_button_pressed_a():
    for index in range(4):
        basic.show_string("w")
        basic.pause(2500)
        basic.show_string("R")
        basic.pause(500)
    basic.pause(100)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

working_time = 0
long_rest_time = 0
short_rest_time = 0
working_text="w"
rest_text ="r"

def on_forever():
    pass
basic.forever(on_forever)
