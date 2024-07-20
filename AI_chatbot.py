import pyautogui
import pyperclip
import time
#step1; click on the chrome icon at coordinates 
pyautogui.click(1238,1044)
time.sleep(1)
#step2: drag the mouse from (1393,199) to (1899,934) to select the text
pyautogui.moveTo(11393,199)
pyautogui.dragTo(1899,934,duration=1.0,button='left')
#step3: copy the selected text to the clipboard
pyautogui.hotkey('ctrl','c')
pyautogui.click(1448,927)
time.sleep(1)
#step:4 retrieve theb text fromthe clipboard and then store it in a variable
chat_history=pyperclip.paste()
#print the copied txt to verify
print(chat_history)









