Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
name='nipaporn'
age=12
age==12
True
if age == 12 :
    print('สามารถเรียนห้อง ป.5 ได้')

    
สามารถเรียนห้อง ป.5 ได้
if age != 12 :
    print('ต้องไปเรียนห้องอื่น')
    else
    
SyntaxError: invalid syntax
els
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    els
NameError: name 'els' is not defined
if age != 12 :
    print('ต้องไปเรียนห้องอื่น')

age !=12
False
age = 15
if age != 12 :
    print('ต้องไปเรียนห้องอื่น')

    
ต้องไปเรียนห้องอื่น
age = 18
if age >= 12 :
    print('คุณต้องไปถามครูว่าเรียนชั้นไหนได้บ้าง')

    
คุณต้องไปถามครูว่าเรียนชั้นไหนได้บ้าง
age = 12
if age >= 12 :
    print('คุณต้องไปถามครูว่าเรียนชั้นไหนได้บ้าง')

    
คุณต้องไปถามครูว่าเรียนชั้นไหนได้บ้าง
if age > 12 :
    print('คุณต้องไปถามครูว่าเรียนชั้นไหนได้บ้าง')

    
if age >= 12 :
    print('คุณต้องไปถามครูว่าเรียนชั้นไหนได้บ้าง')

    
คุณต้องไปถามครูว่าเรียนชั้นไหนได้บ้าง
คุณต้องไปถามครูว่าเรียนชั้นไหนได้บ้าง
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    คุณต้องไปถามครูว่าเรียนชั้นไหนได้บ้าง
NameError: name 'คุณต้องไปถามครูว่าเรียนชั้นไหนได้บ้าง' is not defined
age = 7
if age < 12 :
    print('ต้องเรียน ป.4 ลงไปเท่านั้น')

    
ต้องเรียน ป.4 ลงไปเท่านั้น
if age <= 12 :
    print('ต้องเรียน ป.4 ลงไปเท่านั้น')

    
ต้องเรียน ป.4 ลงไปเท่านั้น
age=12
if age <= 12 :
    print('ขึ้นรถไฟฟ้าฟรี')

    
ขึ้นรถไฟฟ้าฟรี
garage=['toyota','isuzu','benz']
car = 'toyota'
car in garage
True
if car in garage :
    print('รถคันนี้อยู่ในโรงรถ')

    
รถคันนี้อยู่ในโรงรถ
car = 'bmw'
if car in garage :
    print('รถคันนี้อยู่ในโรงรถ')

    
student = True
check = false
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    check = false
NameError: name 'false' is not defined. Did you mean: 'False'?
check = False
moblie = {'loong' : '0801234455','somsak':'081111255'}
'loong' in moblie
True
'loong' not in mobile
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    'loong' not in mobile
NameError: name 'mobile' is not defined. Did you mean: 'moblie'?
listcheck = mobile.values()
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    listcheck = mobile.values()
NameError: name 'mobile' is not defined. Did you mean: 'moblie'?
listcheck = mobile.values()
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    listcheck = mobile.values()
NameError: name 'mobile' is not defined. Did you mean: 'moblie'?
moblie = {'loong' : '0801234455','somsak':'081111255'}
listcheck = mobile.values()
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    listcheck = mobile.values()
NameError: name 'mobile' is not defined. Did you mean: 'moblie'?
mobile = {'loong' : '0801234455','somsak':'081111255'}
listcheck = mobile.values()
print(listcheck)
dict_values(['0801234455', '081111255'])
'0801234455' in listcheck
True
'andi' == 'Audi'
False
'Andi'.Lower() == 'audi'
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    'Andi'.Lower() == 'audi'
AttributeError: 'str' object has no attribute 'Lower'. Did you mean: 'lower'?
'Audi'.Lower() == 'audi'
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    'Audi'.Lower() == 'audi'
AttributeError: 'str' object has no attribute 'Lower'. Did you mean: 'lower'?
'Audi'.lower() == 'audi'
True
True and True
True
True and False
False
True or False
True
True or True
True
money = 200
style = 'japanese'
if money >= 200 and style = 'japanese' :
    
SyntaxError: invalid syntax
if money >= 200 and style == 'japanese' :
    print('คุณสามารถเข้าร้านได้จ้า')

    
คุณสามารถเข้าร้านได้จ้า
stylecheck = ['japanese','thai','chinese']
if money >= 200 and style in stylecheck :
    print('คุณสามารถเข้าร้านได้จ้า')

    
คุณสามารถเข้าร้านได้จ้า
def checkstyle(style,money):
    stylecheck = ['japanese','thai','chinese']
    if money >= 200 and style in stylecheck :
        print('คุณสามารถเข้าร้านได้จ้า')
    elif style not in stylecheck
    
SyntaxError: expected ':'
def checkstyle(style,money):
    stylecheck = ['japanese','thai','chinese']
    if money >= 200 and style in stylecheck :
        print('คุณสามารถเข้าร้านได้จ้า')
    elif style not in stylecheck and money >= 300 :
        print('คุณต้องซื้อชุดของเราในราคา 100 บาท จึงจะเข้าได้')

    else :
        
SyntaxError: unexpected indent
else :
    
SyntaxError: invalid syntax
def checkstyle(style,money):
    stylecheck = ['japanese','thai','chinese']
    if money >= 200 and style in stylecheck :
        print('คุณสามารถเข้าร้านได้จ้า')
    elif style not in stylecheck and money >= 300 :
        print('คุณต้องซื้อชุดของเราในราคา 100 บาท จึงจะเข้าได้')
        else:
            
SyntaxError: invalid syntax
def checkstyle(style,money):
    stylecheck = ['japanese','thai','chinese']
    if money >= 200 and style in stylecheck :
...         print('คุณสามารถเข้าร้านได้จ้า')
...     elif style not in stylecheck and money >= 300 :
...         print('คุณต้องซื้อชุดของเราในราคา 100 บาท จึงจะเข้าได้')
...     else:
...         print('ขออภัยค่ะ ทางเราไม่สามารถให้เข้าได้')
... 
...         
>>> checkstyle('japanese, 400)
...            
SyntaxError: unterminated string literal (detected at line 1)
>>> checkstyle('japanese', 400)
...            
คุณสามารถเข้าร้านได้จ้า
>>> checkstyle('thai',100)
...            
ขออภัยค่ะ ทางเราไม่สามารถให้เข้าได้
>>> checkstyle('western',600)
...            
คุณต้องซื้อชุดของเราในราคา 100 บาท จึงจะเข้าได้
