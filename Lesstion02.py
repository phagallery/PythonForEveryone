Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
tao=turtle.Pen()
tao.shape('turtle')
tao.color('green')
tao.color('red')
tao.forward(10)
tao.forward(90)
tao.left(90)
tao.forward(100)
tao.left(90)
tao.forward(100)
tao.left(90)
tao.forward(100)
tao.left(90)
tao.reset()
tao.color('blue')
for i in range(4):
   tao.forward(100)
   tao.left(90)

   
tao.color('red')
for i in range(8):
   tao.forward(100)
   tao.left(45)

   
for i in range(4):
    print(i)
   tao.forward(100)
   tao.left(90)
   
SyntaxError: unindent does not match any outer indentation level

for i in range(4):
    print(i)
   tao.forward(100)
   tao.left(90)
   
SyntaxError: unindent does not match any outer indentation level
list(range(4))
[0, 1, 2, 3]
list(range(1,4))
[1, 2, 3]
list(range(0,5))
[0, 1, 2, 3, 4]
list(range(0,10,2))
[0, 2, 4, 6, 8]
list(range(0,11,2))
[0, 2, 4, 6, 8, 10]
taolist=[]
tao.reset
<bound method RawTurtle.reset of <turtle.Turtle object at 0x000001FACF6B82F0>>
tao.reset()
for i in range(8):
   tao.forward(100)
   tao.left(45)

   
tao.up()
>>> tao.goto(30,30)
>>> tao.down()
>>> for i in range(4):
...    tao.forward(50)
...    tao.left(90)
... 
...    
>>> taolist=[]
>>> tao1 = turtle.Pen()
>>> tao2 = turtle.Pen()
>>> taolist.append(tao)
>>> taolist.append(tao1)
>>> taolist.append(tao2)
>>> print(taolist)
[<turtle.Turtle object at 0x000001FACF6B82F0>, <turtle.Turtle object at 0x000001FACF799590>, <turtle.Turtle object at 0x000001FACF799E50>]
>>> taolist[0].forward(200)
>>> taolist[1].backword(200)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    taolist[1].backword(200)
AttributeError: 'Turtle' object has no attribute 'backword'. Did you mean: 'backward'?
>>> taolist[1].backward(200)
>>> taolist[2].color('red')
>>> taolist[2].left(90)
>>> taolist[2].forward(100)
