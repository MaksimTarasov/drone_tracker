import math
import turtle

t = turtle.Turtle()
cr = ((0, 0), (100, 0), (100, 100), (0, 100), (0, 0))
a1 = 0
l = len(cr) - 1
for i, i_cr in enumerate(cr):
  if i < l:
    dx = cr[i+1][0] - i_cr[0]
    dy = cr[i+1][1] - i_cr[1]
    a = math.atan2(cr[i+1][1], cr[i+1][0]) * 180 / math.pi
    dxy = math.sqrt(dx*dx+dy*dy)

    print(f'угол: {a}')
    print(f'длина: {dxy}')

    t.left(a + (90 - a))
    t.forward(dxy)

turtle.mainloop()
turtle.done()