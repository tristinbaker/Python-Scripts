"""
This is an attempt at using OCR to read the HP 
value of my Java game "The Dungeon". It will interpret
the text and output whether they've gained or lost
HP and then print the current HP.
"""

from PIL import Image
import pytesseract
import pyscreenshot as ImageGrab
import cv2

past_hp = 0 

def get_hp():
	img = ImageGrab.grab(bbox=(1972, 530, 2020, 570)).save('img.png')
	cv2_img = cv2.imread('img.png')
	gray = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)
	thresh = 255 - cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
	thresh = cv2.GaussianBlur(thresh, (3,3), 0)
	hp = pytesseract.image_to_string(thresh, lang='eng', config='--psm 6')
	try:
		return int(hp)
	except ValueError:
		return 0

while True:
	hp = get_hp()
	if hp > past_hp:
		print(f"GAINED {hp - past_hp} HP")
	elif hp < past_hp:
		print(f"DAMAGED BY {past_hp - hp} HP.") 
	print(f"Current HP: {hp}")
	past_hp = hp

