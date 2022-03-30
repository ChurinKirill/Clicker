import keyboard
import pyautogui
import sys
from Clicker import Clicker
from Clicker1 import Clicker1
from Clicker2 import Clicker2

def finish() -> None:
    print("program finished")
    sys.exit()

print("program started")

arg = sys.argv
clicker = ''
if arg[1] == "click":
    clicker = Clicker1(arg[2], int(arg[3]))
elif arg[1] == "hold":
    clicker = Clicker2(arg[2])

while True:
    if keyboard.is_pressed("grave"):
        clicker.start()
        print("clicker finished")
    if keyboard.is_pressed("delete"):
        finish()
