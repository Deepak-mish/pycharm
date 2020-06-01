from pynput.mouse import Controller
from pynput.keyboard import Controller
from pynput.mouse import Listener


def controlMouse():
    Mouse = Controller()
    Mouse.position = (100, 200)


def controlKeyboard():
    Keyboard = Controller()
    Keyboard.type("i am freeking awesome")


def write_to_file(x, y):
    print("position of current mouse {0}".format((x, y)))


with Listener(on_move=write_to_file) as l:
    l.join()
