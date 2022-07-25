
# Change time/date of expiration in preparation stage (counting in seconds)
def on_button_pressed_a():
    global milliseconds
    if not (timer_start):
        basic.clear_screen()
        milliseconds += 1000 # counting seconds in milliseconds 
        basic.show_number(milliseconds / 1000) 
input.on_button_pressed(Button.A, on_button_pressed_a)

# Uses Food Button
def on_button_pressed_ab():
    global food_used, end_screen
    if timer_start and not (end_screen):
        food_used = True
        music.start_melody(music.built_in_melody(Melodies.POWER_UP), MelodyOptions.ONCE)
        basic.show_icon(IconNames.YES)
        end_screen = True
input.on_button_pressed(Button.AB, on_button_pressed_ab)

# Confirm set time and move on to timer stage (if still on preperation stage)
def on_button_pressed_b():
    global timer_start, interval, halfway_warning, food_used, end_screen, milliseconds, end_screen_loop_once, led_interval
    if not (timer_start):
        timer_start = True
        interval = milliseconds / 5
        interval = milliseconds / 5
        basic.clear_screen()
    else:       # restart program if timer stage is finished and program has started
        timer_start = False
        halfway_warning = True
        food_used = False
        end_screen = False
        milliseconds = 0
        end_screen_loop_once = True
        led_interval = 45
        basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

# Defining set variables before main program loop
end_screen_loop_once = False
interval = 0
led_interval = 0
milliseconds = 0
end_screen = False
food_used = False
halfway_warning = False
timer_start = False
timer_start = False
halfway_warning = True
food_used = False
end_screen = False
milliseconds = 0
led_interval = 45
basic.clear_screen()

# Main program Loop
def on_forever():
    global led_interval, halfway_warning, end_screen, end_screen_loop_once, milliseconds
    if timer_start and not (food_used):     
        if milliseconds > interval * 4:
            led_interval = 45
        elif milliseconds > interval * 3:
            led_interval = 36
        elif milliseconds > interval * 2:
            led_interval = 27
        elif milliseconds > interval:
            led_interval = 18
            if halfway_warning:
                music.play_melody("F F - F F - F F ", 500)
                halfway_warning = False
        elif milliseconds > 0:
            led_interval = 9
        elif milliseconds < 0:
            if end_screen_loop_once:
                pass
            end_screen = True
            music.play_melody("C C - C C - C C ", 120)
            basic.clear_screen()
            basic.show_string("EXPIRED!")
            end_screen_loop_once = False
            milliseconds = 0
            end_screen = True
            led_interval = 0
        if not (end_screen):
            led.plot_bar_graph(led_interval, 50) # Timer feature and LED time graph feature
            milliseconds += -25 # Counting Milliseconds on micro:BIT per program run
basic.forever(on_forever)
