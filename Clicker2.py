from Clicker import Clicker
import keyboard
import pyautogui

class Clicker2(Clicker):
    """Clicker wich holds mouse button"""
    def start(self) -> None:
        print("clicker started")
        pyautogui.mouseDown()
        while True:
            if keyboard.is_pressed(self.stopbutton):
                pyautogui.mouseUp()
                return