import pyautogui


pyautogui.click()


x=150

pyautogui.dragRel(x,0)
pyautogui.dragRel(0,x)
pyautogui.dragRel(-x,0)
pyautogui.dragRel(0,-x)

h,w=pyautogui.position()

pyautogui.moveTo(h+10,w+10)
pyautogui.click()
x=130
pyautogui.dragRel(x,0)
pyautogui.dragRel(0,x)
pyautogui.dragRel(-x,0)
pyautogui.dragRel(0,-x)

h,w=pyautogui.position()

pyautogui.moveTo(h+10,w+10)
pyautogui.click()
x=110
pyautogui.dragRel(x,0)
pyautogui.dragRel(0,x)
pyautogui.dragRel(-x,0)
pyautogui.dragRel(0,-x)

h,w=pyautogui.position()

pyautogui.moveTo(h+10,w+10)
pyautogui.click()
x=90
pyautogui.dragRel(x,0)
pyautogui.dragRel(0,x)
pyautogui.dragRel(-x,0)
pyautogui.dragRel(0,-x)


	
	
	
