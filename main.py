import math
from get_coords import getcords


cr = getcords('2.jpg', cont=False)
#cr = ((0, 0), (100, 0), (100, 100), (0, 100), (0, 0))
l = len(cr) - 1
#Проход по контуру
#TODO подключить библиотеку управления дроном,
# и вместо сообщения передовать велечину смещения и направление смещения
for i, i_cr in enumerate(cr):
  if i < l:
    message = 'stop'
    x1 = i_cr[0]
    x2 = cr[i+1][0]
    y1 = i_cr[1]
    y2 = cr[i+1][1]

    dx = x2 - x1
    dy = y2 - y1

    dxy = math.sqrt(dx * dx + dy * dy)
    print('-'*10)
    print(f'dx: {dx}')
    print(f'dy: {dy}')
    if x2 > x1:
      message = 'move left'
    if x2 < x1:
      message = 'move right'
    if y2 > y1:
      message = 'move up'
    if y2 < y1:
      message = 'move down'

    print(message)
    print(f'длина: {abs(dxy)}')
