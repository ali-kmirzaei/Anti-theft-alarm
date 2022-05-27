#!/usr/bin/env python3
from pynput.mouse import Listener as Listener_mouse
from pynput.keyboard import Listener as Listener_keyboard
from pynput.keyboard import Key
import logging
import os
##################################################################################################
DURATION = 0.5  # seconds
FREQ = 440  # Hz
COUNT = 0
##################################################################################################
def alarm_log(action):
    os.system('play -nq -t alsa synth {} sine {}'.format(DURATION, FREQ))
    log_file.write('{}\n'.format(action))

def on_move(x, y):
    global COUNT
    COUNT += 1
    if COUNT > 10:
        alarm_log('mouse moved')
        COUNT = 0

def on_click(x, y, button, pressed):
    alarm_log('mouse clicked')

def on_scroll(x, y, dx, dy):
    alarm_log('mouse scrolled')

def on_press(key):
    alarm_log('key pressed')

def on_release(key):
    if key == Key.shift_r:
        keyboard_listener.stop()
        mouse_listener.stop()
        log_file.write('~!EXITED!~\n')
        log_file.close()
        exit()

##################################################################################################
log_file = open('logs.txt', 'w')
log_file.write('~!Started!~\n')

keyboard_listener = Listener_keyboard(on_press=on_press, on_release=on_release)
mouse_listener = Listener_mouse(on_move=on_move, on_click=on_click, on_scroll=on_scroll)
keyboard_listener.start()
mouse_listener.start()
keyboard_listener.join()
mouse_listener.join()
