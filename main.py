# https://github.com/jegyed50/jegyed50-bbc-microbit-study365-blocks-03-04-d
# https://github.com/jegyed50/jegyed50-bbc-microbit-study365-blocks-03-04-a/blob/master/03-04-pomodoro-timeline.jpg
# JEGYED50-BBC-MICROBIT-STUDY365-BLOCKS-03-04-D
# Mint C, csak a szünetek értéke változókkal: short_rest_time, long_rest_time, working_time,working_text, rest_text

def on_button_pressed_a():
    for index in range(4):
        basic.show_string(working_text)
        basic.pause(working_time)
        basic.show_string(rest_text)
        basic.pause(short_rest_time)
    basic.pause(long_rest_time - short_rest_time)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

rest_text = ""
working_text = ""
working_time = 0
long_rest_time = 0
short_rest_time = 0
led.set_brightness(25)
short_rest_time = 500
long_rest_time = 1500
working_time = 2500
working_text = "W"
rest_text = "R"

def on_forever():
    pass
basic.forever(on_forever)
