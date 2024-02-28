"""
Проверка работы модуля get_coords
"""
from get_coords import getcords
import cv2
name = '2.jpg'
cnt2 = getcords(name)
img = cv2.imread(name)
c_list = getcords(name, cont=False)
print(c_list)
#print(cnt2)
cv2.drawContours(img, [cnt2], -1, (0, 255, 0), 4)
cv2.imshow('cnt', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
