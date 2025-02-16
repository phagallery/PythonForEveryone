Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
name='nipaporn'
lastname='sonwiang'
fullname=name + lastname
print(fullname)
nipapornsonwiang
type(name)
<class 'str'>
age=20
type(age)
<class 'int'>
name='nipaporn'
name.upper()
'NIPAPORN'
name.lower()
'nipaporn'
>>> name=name.upper()
>>> print(name)
NIPAPORN
>>> fullname = name + ' ' + lastname
>>> print(fullname)
NIPAPORN sonwiang
>>> number='1'
>>> number.zfill(5)
'00001'
>>> number='15'
>>> number.zfill(13)
'0000000000015'
>>> testname ='ลุงครับผมชื่อ'+name + ' ' + lastname + ' อายุ ' + age + ' ขวบ'
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    testname ='ลุงครับผมชื่อ'+name + ' ' + lastname + ' อายุ ' + age + ' ขวบ'
TypeError: can only concatenate str (not "int") to str
>>> testname ='ลุงครับผมชื่อ'+name + ' ' + lastname
>>> print('ลุงครับผมชื่อ{} นามสกุล {} อายุ {} ขวบ'.format(name,lastname,age))
ลุงครับผมชื่อNIPAPORN นามสกุล sonwiang อายุ 20 ขวบ
>>> lastname.upper()
'SONWIANG'
>>> print('ลุงครับผมชื่อ {} นามสกุล {} อายุ {} ขวบ'.format(name,lastname,age))
ลุงครับผมชื่อ NIPAPORN นามสกุล sonwiang อายุ 20 ขวบ
>>> print(f'ลุงครับผมชื่อ {name} นามสกุล {lastname} อายุ {age} ขวบ')
ลุงครับผมชื่อ NIPAPORN นามสกุล sonwiang อายุ 20 ขวบ
