import math
import turtle

t = turtle.Turtle()
cr = ((0, 0), (100, 0), (100, 100), (0, 100), (0, 0))

l = len(cr) - 1
for i, i_cr in enumerate(cr):
  if i < l:
    dx = cr[i+1][0] - i_cr[0]
    dy = cr[i+1][1] - i_cr[1]
    dxy = math.sqrt(dx * dx + dy * dy)
    """
    # определение угла поворота
    a = math.atan2(cr[i+1][1], cr[i+1][0]) * 180 / math.pi
    #dxy = math.sqrt(dx*dx+dy*dy)
    
    print(f'угол: {a}')
   
    t.left(a)
    """
    print('-'*10)
    print(dx)
    print(dy)
    if dx == 0 and dy > 0:
      t.left(90)
      print('move up')
    if dx == 0 and dy < 0:
      t.right(90)
      print('move down')
    if dy == 0 and dx > 0:
      t.right(0)
      print('move right')
    if dy == 0 and dx < 0:
      t.left(0)
      print('move left')

    print(f'длина: {dxy}')
    t.forward(dxy)

turtle.mainloop()
turtle.done()