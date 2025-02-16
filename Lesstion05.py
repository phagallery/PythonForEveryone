Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
tao = turtle.Pen()
tao.shape('turtle')
tao1 = {'color':'green','dis':100}
tao.color(tao1['color')
          
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
tao.color(tao1['color'])
...           
>>> def rect(tao_object,tdict):
...     for i in range(4):
...         tao_object.forward(tdict['dis'])
...         tao_object.left(90)
... 
...         
>>> 
>>> rect(tao,tao1)
>>> tao2 = turtle.Pen()
>>> tao2dict = {'color':'red','dis':50}
>>> tao2.color(tao2dict['color'])
>>> tao2.shape('turtle')
>>> tao2.up()
>>> tao2.goto(30,30)
>>> tao2.down()
>>> rect(tao2,tao2dict)
