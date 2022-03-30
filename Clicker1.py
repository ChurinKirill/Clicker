from typing import NoReturn
from Clicker import Clicker
import time
import pyautogui
import keyboard

class Clicker1(Clicker):
    """Clicker which clicks on corrent mouse position with interval -n- seconds"""
    def __init__(self, stopbutton: str, delayTime: int):
        super().__init__(stopbutton)
        self.delayTime: int = delayTime

    def start(self) -> None:
        print("clicker started")
        while True:
            time.sleep(self.delayTime)
            pyautogui.click()
            if keyboard.is_pressed(self.stopbutton):
                print("clicker finished")
                return
