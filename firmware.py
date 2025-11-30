main.py
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC

keyboard = KMKKeyboard()

PINS = [board.D8, board.D9, board.D10, board.D11]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Change out with app launches depending on apps once tested.

keyboard.keymap = [
    [KC.SPACE, KC.W, KC.A, KC.D,]
]

if __name__ == '__main__':
    keyboard.go()
