Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
cars = ['toyota','honda','benz']
cars.append('byd')
print(cars)
['toyota', 'honda', 'benz', 'byd']
cars.remove('honda')
print(cars)
['toyota', 'benz', 'byd']
cars.insert(0,'tesla')
print(cars)
['tesla', 'toyota', 'benz', 'byd']
print(cars[1])
toyota
print(cars[0,1])
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(cars[0,1])
TypeError: list indices must be integers or slices, not tuple
TypeError: list indices must be integers or slices, not tuple
SyntaxError: invalid syntax
for car in cars :
    print(car)

    
tesla
toyota
benz
byd
print(*cars)
tesla toyota benz byd
print(*cars.sort)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(*cars.sort)
TypeError: print() argument after * must be an iterable, not builtin_function_or_method
for i,c in enumerate(cars):
    print(i,c)

    
0 tesla
1 toyota
2 benz
3 byd
for i,c in enumerate(cars,start=0):
    print('ลำดับที่ {}  {}'.format(i,c))

    
ลำดับที่ 0  tesla
ลำดับที่ 1  toyota
ลำดับที่ 2  benz
ลำดับที่ 3  byd
for i,c in enumerate(cars,start=1):
    print('ลำดับที่ {}  {}'.format(i,c))

    
ลำดับที่ 1  tesla
ลำดับที่ 2  toyota
ลำดับที่ 3  benz
ลำดับที่ 4  byd
for c in cars:
    print(c)

    
tesla
toyota
benz
byd
>>> print(ord('4'))
SyntaxError: invalid syntax
print(ord('4'))
52
i=0
for c in cars:
    print(i+1,c)
    i=i+1
    print(ord(i))

    
1 tesla
Traceback (most recent call last):
  File "<pyshell#32>", line 4, in <module>
    print(ord(i))
TypeError: ord() expected string of length 1, but int found
for c in cars:
    print(i+1,c)
    i=i+1

    
2 tesla
3 toyota
4 benz
5 byd
for i,c in enumerate(cars,start=1)
SyntaxError: expected ':'
for i,c in enumerate(cars,start=1):
    print(i,c)

    
1 tesla
2 toyota
3 benz
4 byd
print(ord('P'))
80
print(cars)
['tesla', 'toyota', 'benz', 'byd']
cars[1]='isuzu'
print(cars)
['tesla', 'isuzu', 'benz', 'byd']
del cars[2]
print(cars)
['tesla', 'isuzu', 'byd']
len(cars)
3
cars.sort()
print(cars)
['byd', 'isuzu', 'tesla']
cars.sort(reverse=true)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    cars.sort(reverse=true)
NameError: name 'true' is not defined. Did you mean: 'True'?
cars.sort(reverse=True)
print(cars)
['tesla', 'isuzu', 'byd']
ord('ฃ')
3587
chr(3587)
'ฃ'
ord(0)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    ord(0)
TypeError: ord() expected string of length 1, but int found
for r in range(44):
    print (chr(3585+i))

    
ฅ
ฅ
ฅ
ฅ
ฅ
ฅ
ฅ
ฅ
ฅ
ฅ
ฅ
ฅ
ฅ
ฅ
ฅ
ฅ
ฅ
ฅ
ฅ
ฅ
ฅ
ฅ
ฅ
ฅ
ฅ
ฅ
ฅ
ฅ
ฅ
ฅ
ฅ
ฅ
ฅ
ฅ
ฅ
ฅ
ฅ
ฅ
ฅ
ฅ
ฅ
ฅ
ฅ
ฅ
for r in range(3585,3595):
    print (chr(i))

    










for i in range(3585,3595):
    print (chr(i))

    
ก
ข
ฃ
ค
ฅ
ฆ
ง
จ
ฉ
ช
for i in range(44):
    print (chr(3585+i))

    
ก
ข
ฃ
ค
ฅ
ฆ
ง
จ
ฉ
ช
ซ
ฌ
ญ
ฎ
ฏ
ฐ
ฑ
ฒ
ณ
ด
ต
ถ
ท
ธ
น
บ
ป
ผ
ฝ
พ
ฟ
ภ
ม
ย
ร
ฤ
ล
ฦ
ว
ศ
ษ
ส
ห
ฬ
for i in range(46):
    print (chr(3585+i))

    
ก
ข
ฃ
ค
ฅ
ฆ
ง
จ
ฉ
ช
ซ
ฌ
ญ
ฎ
ฏ
ฐ
ฑ
ฒ
ณ
ด
ต
ถ
ท
ธ
น
บ
ป
ผ
ฝ
พ
ฟ
ภ
ม
ย
ร
ฤ
ล
ฦ
ว
ศ
ษ
ส
ห
ฬ
อ
ฮ
number = {'1001' : 'สมชาย','1002' : 'สมศรี','1003' : 'สมศักดิ์'}
print(number['1001'])
สมชาย
for n in number :
    print(n)

    
1001
1002
1003
for n in number.item :
    print(n)

    
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    for n in number.item :
AttributeError: 'dict' object has no attribute 'item'. Did you mean: 'items'?
for n in number.item() :
    print(n)

    
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    for n in number.item() :
AttributeError: 'dict' object has no attribute 'item'. Did you mean: 'items'?
for n in number.items() :
    print(n)

    
('1001', 'สมชาย')
('1002', 'สมศรี')
('1003', 'สมศักดิ์')
for n in number.items() :
    print(n[1])

    
สมชาย
สมศรี
สมศักดิ์
for n in number.keys() :
    print(n[1])

    
0
0
0
for n in number.keys() :
    print(n)

    
1001
1002
1003
for n in number.values() :
    print(n)

    
สมชาย
สมศรี
สมศักดิ์
def hello():
    print('hello world')
     print('hello world')
     
SyntaxError: unexpected indent
def hello():
    print('hello world')
    print('hello world')
    print('hello world')
    print('hello world')
    print('hello world')
    hello()

    
def hello(q):
    for i in range(q):
        print('hello world')

        
hello(1)
hello world
hello(5)
hello world
hello world
hello world
hello world
hello world
hell()
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    hell()
NameError: name 'hell' is not defined. Did you mean: 'hello'?
hell(10)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    hell(10)
NameError: name 'hell' is not defined. Did you mean: 'hello'?
>>> hello()
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    hello()
TypeError: hello() missing 1 required positional argument: 'q'
>>> hello(10)
hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world
