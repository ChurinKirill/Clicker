from Clicker import Clicker
import time
import pyautogui
import keyboard

class Clicker1(Clicker):
    """Clicker which clicks on current mouse position with n seconds interval"""
    def __init__(self, stopbutton: str, delayTime: float):
        super().__init__(stopbutton)
        self.delayTime: float = delayTime

    def start(self) -> None:
        print("clicker started")
        while True:
            time.sleep(self.delayTime)
            pyautogui.click()
            if keyboard.is_pressed(self.stopbutton):
                print("clicker finished")
                return
