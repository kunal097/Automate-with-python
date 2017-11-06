import pyautogui
import time



pyautogui.click(21,748)
pyautogui.moveTo(88,121,duration=1.5)
pyautogui.click()
time.sleep(1)

h=315
w=207


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
	



pyautogui.click(8,8)

pyautogui.click(578,432)
	

