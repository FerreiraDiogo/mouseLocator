import pyautogui
import time
print("=====Mouse Locator!=====\n")
print("1-Start cursor location script\n")
print("0-Terminate this script\n")
flag = input()
while flag != "0":
    print("Begining cursor location script...")
    print(("5"))
    time.sleep(1)
    print(("4"))
    time.sleep(1)
    print(("3"))
    time.sleep(1)
    print(("2"))
    time.sleep(1)
    print(("1"))
    time.sleep(1)
    location = pyautogui.position()
    print("Mouse cursor located at "+str(location))
    print("\nDo you wish to re-run the script?\n1-re-run\n0-terminate script ")
    flag = input()
