"""
Example:
	WINDOWS R
	DELAY 0.5
	STRING cmd
	ENTER
	DELAY 1
	n\ n/ n1 n* n+ n`
	DELAY 1.5
	CONTROL C
	DELAY 1
	STRING exit
	ENTER
+------------------------------------------------+
| NOTE: YOU CAN'T PRESS MORE THAN 6 KEYS AT ONCE.|
+------------------------------------------------+
"""
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from time import sleep
import usb_hid

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)
err = 0
try:
    with open("payload.txt") as f:
        lines = f.read().splitlines()
except:
    err =1 
    print("Error")

print(lines)

command_dispatcher = {'A': Keycode.A,
                      'B': Keycode.B,
                      'C': Keycode.C,
                      'D': Keycode.D,
                      'E': Keycode.E,
                      'F': Keycode.F,
                      'G': Keycode.G,
                      'H': Keycode.H,
                      'I': Keycode.I,
                      'J': Keycode.J,
                      'K': Keycode.K,
                      'L': Keycode.L,
                      'M': Keycode.M,
                      'N': Keycode.N,
                      'O': Keycode.O,
                      'P': Keycode.P,
                      'Q': Keycode.Q,
                      'R': Keycode.R,
                      'S': Keycode.S,
                      'T': Keycode.T,
                      'U': Keycode.U,
                      'V': Keycode.V,
                      'W': Keycode.W,
                      'X': Keycode.X,
                      'Y': Keycode.Y,
                      'Z': Keycode.Z,
                      'n1': Keycode.ONE,
                      'n2': Keycode.TWO,
                      'n3': Keycode.THREE,
                      'n4': Keycode.FOUR,
                      'n5': Keycode.FIVE,
                      'n6': Keycode.SIX,
                      'n7': Keycode.SEVEN,
                      'n8': Keycode.EIGHT,
                      'n9': Keycode.NINE,
                      'n0': Keycode.ZERO,
                      'ENTER': Keycode.ENTER,
                      'RETURN': Keycode.RETURN,
                      'ESCAPE': Keycode.ESCAPE,
                      'BACKSPACE': Keycode.BACKSPACE,
                      'TAB': Keycode.TAB,
                      'SPACE': Keycode.SPACEBAR,
                      'n-': Keycode.MINUS,
                      'n=': Keycode.EQUALS,
                      'n(': Keycode.LEFT_BRACKET,
                      'n)': Keycode.RIGHT_BRACKET,
                      'n\\': Keycode.BACKSLASH,
                      'n#': Keycode.POUND,
                      'n;': Keycode.SEMICOLON,
                      'QUOTE': Keycode.QUOTE,
                      'n`': Keycode.GRAVE_ACCENT,
                      'n,': Keycode.COMMA,
                      'n.': Keycode.PERIOD,
                      'n/': Keycode.FORWARD_SLASH,
                      'CAPS_LOCK': Keycode.CAPS_LOCK,
                      'F1': Keycode.F1,
                      'F2': Keycode.F2,
                      'F3': Keycode.F3,
                      'F4': Keycode.F4,
                      'F5': Keycode.F5,
                      'F6': Keycode.F6,
                      'F7': Keycode.F7,
                      'F8': Keycode.F8,
                      'F9': Keycode.F9,
                      'F10': Keycode.F10,
                      'F11': Keycode.F11,
                      'F12': Keycode.F12,
                      'PS': Keycode.PRINT_SCREEN,
                      'SCROLL_LOCK': Keycode.SCROLL_LOCK,
                      'PAUSE': Keycode.PAUSE,
                      'INSERT': Keycode.INSERT,
                      'HOME': Keycode.HOME,
                      'PAGE_UP': Keycode.PAGE_UP,
                      'DELETE': Keycode.DELETE,
                      'END': Keycode.END,
                      'PAGE_DOWN': Keycode.PAGE_DOWN,
                      'RIGHT': Keycode.RIGHT_ARROW,
                      'LEFT': Keycode.LEFT_ARROW,
                      'DOWN': Keycode.DOWN_ARROW,
                      'n*': Keycode.KEYPAD_ASTERISK,
                      'n+': Keycode.KEYPAD_PLUS,
                      'CONTROL': Keycode.CONTROL,
                      'SHIFT': Keycode.SHIFT,
                      'ALT': Keycode.ALT,
                      'OPTION': Keycode.OPTION,
                      'META': Keycode.GUI,
                      'WINDOWS': Keycode.WINDOWS,
                      'COMMAND': Keycode.COMMAND,
                      'RIGHT_CONTROL': Keycode.RIGHT_CONTROL,
                      'RIGHT_SHIFT': Keycode.RIGHT_SHIFT,
                      'RIGHT_ALT': Keycode.RIGHT_ALT,
                      'UP': Keycode.UP_ARROW,
                      'NUMLOCK': Keycode.KEYPAD_NUMLOCK,
                      'MENU': Keycode.APPLICATION,
                      'POWER': Keycode.POWER
                      }



def drop(payload):
    setter = 0
    timer = 0
    for line in payload:
        line = line.split()
        print(line) #DEBUG
        if line[0] == "STRING":
            layout.write(' '.join(line[1:]))
            setter = 1

        if line[0] == "DELAY":
            sleep(float(line[1]))
            timer = 1

        if not setter and not timer:
            for l in line:
                kbd.press(command_dispatcher[l])
            print("done")
            for l in line:
                kbd.release(command_dispatcher[l])
            print("-----")

        setter = 0
        timer = 0

if err:
    print("Couldnt open payload.txt")
else:
    drop(lines)