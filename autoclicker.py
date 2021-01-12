import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
firststage = True
_return_ = False

start_stop_key = KeyCode(char="-")  # Toggle Hotkey
exit_key = KeyCode(char="=")  # Exit Hotkey

def State(firststage=firststage):
    while firststage == True:
        try:
            global _return_
            global delay
            global button
            global start_stop_key
            global exit_key
            delay = float(input("Enter a click delay: "))
            print("1. LMB\n2. RMB")
            button = input()
            if button == "1":  # Option 1
                button = Button.left
                firststage = False
                _return_ = False
            elif button == "2":  # Option 2
                button = Button.right
                firststage = False
                _return_ = False
            else:
                print("Invalid Input")
                _return_ = True
        except ValueError:
            print("Invalid Input")
            _return_ = True
        if _return_ == False:
            tipstr = "Press [{0}] to toggle autoclicker. Press [{1}] to exit application"
            print(tipstr.format(start_stop_key, exit_key))  # Displays Tip
                

State(firststage=firststage)


class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):  # Running Clicks
        self.running = True

    def stop_clicking(self):  # Not Running Clicks
        self.running = False

    def exit(self):
        self.stop_clicking()  # Exit Program
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)  # Currently Clicking
                time.sleep(self.delay)
            time.sleep(0)


mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()  # When Start Key Is Pressed
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()  # When Exit Key Is Pressed
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
