import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC

# Rotary encoder support
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

PINS = [board.D8, board.D9, board.D10, board.D11]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [
        KC.LCTRL(KC.LALT(KC.C)),  # Chrome
        KC.LCTRL(KC.LALT(KC.D)),  # Discord
        KC.LCTRL(KC.LALT(KC.V)),  # VSCode
        KC.LCTRL(KC.LALT(KC.E)),  # File Explorer
    ]
]

encoder = EncoderHandler()

# Change these to your actual pins:
encoder.pins = (
    board.D2,   # A pin
    board.D3,   # B pin
    board.D4,   # SW (button) - optional
)

# What happens when you turn the knob:
encoder.map = [
    ((KC.VOLU, KC.VOLD)),  # CW = VOL UP, CCW = VOL DOWN
]

# What happens when you click the knob:
encoder.button = KC.MUTE  

# Add encoder module
keyboard.modules.append(encoder)

if __name__ == '__main__':
    keyboard.go()
