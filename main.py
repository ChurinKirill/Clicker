import keyboard
import sys
from Clicker1 import Clicker1
from Clicker2 import Clicker2

def finish() -> None:
    print("program finished")
    sys.exit()

print("program started")

startbutton: str = input("Enter start button: ")
exitbutton: str = input("Enter exit button: ")
clicker = None
type: str = int(input(
"""Enter clicker type:\n
1.Clicker cklicks on current mouse position with n seconds interval\n
2.Clicker holds mouse button\n"""))
if type == 1:
    clicker = Clicker1(input("Enter stopbutton: "), float(input("Enter interval (seconds): ")))
elif type == 2:
    clicker = Clicker2(input("Enter stopbutton: "))
print("Press start button to run clicker")
while True:
    if keyboard.is_pressed(startbutton):
        clicker.start()
    if keyboard.is_pressed(exitbutton):
        finish()
