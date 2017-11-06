import pyautogui
import time



pyautogui.click(21,748)
pyautogui.click(65,62)
pyautogui.typewrite("pinta")

pyautogui.moveTo(83,125,duration=1)
pyautogui.click()
time.sleep(1.5)

h=325
w=198


i=0
distance =150
while i<5:
	pyautogui.click(h,w)
	pyautogui.dragRel(distance,0)
	pyautogui.dragRel(0,distance)
	pyautogui.dragRel(-distance,0)
	pyautogui.dragRel(0,-distance)
	
	i+=1
	h+=10
	w+=10
	distance-=20
	


pyautogui.click(14,346)

pyautogui.click(369,561)
pyautogui.typewrite("Drawing by -> Python")

pyautogui.click(131,31)
time.sleep(1.5)
pyautogui.click(376,102)
pyautogui.typewrite("pypaint")
time.sleep(1.5)
pyautogui.click(1047,684)
time.sleep(1)
pyautogui.click(724,443)

pyautogui.click(8,8)


	

