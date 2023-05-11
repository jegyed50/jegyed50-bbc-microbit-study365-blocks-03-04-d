//  https://github.com/jegyed50/jegyed50-bbc-microbit-study365-blocks-03-04-d
//  https://github.com/jegyed50/jegyed50-bbc-microbit-study365-blocks-03-04-a/blob/master/03-04-pomodoro-timeline.jpg
//  JEGYED50-BBC-MICROBIT-STUDY365-BLOCKS-03-04-D
//  Mint C, csak a szünetek értéke változókkal: short_rest_time, long_rest_time, working_time,working_text, rest_text
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    for (let index = 0; index < 4; index++) {
        basic.showString(working_text)
        basic.pause(working_time)
        basic.showString(rest_text)
        basic.pause(short_rest_time)
    }
    basic.pause(long_rest_time - short_rest_time)
    basic.clearScreen()
})
let rest_text = ""
let working_text = ""
let working_time = 0
let long_rest_time = 0
let short_rest_time = 0
led.setBrightness(25)
short_rest_time = 500
long_rest_time = 1500
working_time = 2500
working_text = "W"
rest_text = "R"
basic.forever(function on_forever() {
    
})
