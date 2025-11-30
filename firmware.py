import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC

keyboard = KMKKeyboard()

PINS = [board.D8, board.D9, board.D10, board.D11]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Replace key outputs with hotkey combos
keyboard.keymap = [
    [
        KC.LCTRL(KC.LALT(KC.C)),  # Chrome
        KC.LCTRL(KC.LALT(KC.D)),  # Discord
        KC.LCTRL(KC.LALT(KC.V)),  # VSCode
        KC.LCTRL(KC.LALT(KC.E)),  # File Explorer
    ]
]

if __name__ == '__main__':
    keyboard.go()
