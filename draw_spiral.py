import pyautogui

pyautogui.click()
distance=200

while distance >0:
	pyautogui.dragRel(distance,0)
	distance-=25
	
	pyautogui.dragRel(0,distance)
	distance-=25
	
	pyautogui.dragRel(-distance,0)
	distance-=25
	
	pyautogui.dragRel(0,-distance)
	distance-=25
