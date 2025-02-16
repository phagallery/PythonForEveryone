Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def sawatdee():
    """ ฟังก์ชันนี้ใช้สำหรับสวัสดี """
    print('สวัสดีจ้าาาา')

    
dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'sawatdee']
help (sawatdee)
Help on function sawatdee in module __main__:

sawatdee()
    ฟังก์ชันนี้ใช้สำหรับสวัสดี

help(print)
Help on built-in function print in module builtins:

print(*args, sep=' ', end='\n', file=None, flush=False)
    Prints the values to a stream, or to sys.stdout by default.

    sep
      string inserted between values, default a space.
    end
      string appended after the last value, default a newline.
    file
      a file-like object (stream); defaults to the current sys.stdout.
    flush
      whether to forcibly flush the stream.

def hello(friend):
    print('Hi,{}'.format(friend))

    
hello('john')
Hi,john
hello('robert')
Hi,robert
def land(width,long):
    cal = width*long
    cal_wa = cal/4
    print('ที่ดินผื้นนี้กว้าง : {} เมตร ยาว : {} เมตร'.format(width,long))
    print('ที่ดินผืนนี้มีพื้นที่ : {} ตารางเมตร'.format(cal))
    print('ที่ดินผืนนี้มีพื้นที่ : {} ตารางวาง'.format(cal_wa))

    
land(400,100)
ที่ดินผื้นนี้กว้าง : 400 เมตร ยาว : 100 เมตร
ที่ดินผืนนี้มีพื้นที่ : 40000 ตารางเมตร
ที่ดินผืนนี้มีพื้นที่ : 10000.0 ตารางวาง
def land(width,long):
    cal = width*long
    cal_wa = cal/4
    print('ที่ดินผื้นนี้กว้าง : {} เมตร ยาว : {} เมตร'.format(width,long))
    print('ที่ดินผืนนี้มีพื้นที่ : {} ตารางเมตร'.format(cal))
    print('ที่ดินผืนนี้มีพื้นที่ : {} ตารางวา'.format(cal_wa))

    
land(50,100)
ที่ดินผื้นนี้กว้าง : 50 เมตร ยาว : 100 เมตร
ที่ดินผืนนี้มีพื้นที่ : 5000 ตารางเมตร
ที่ดินผืนนี้มีพื้นที่ : 1250.0 ตารางวา
res=land(5,15)
ที่ดินผื้นนี้กว้าง : 5 เมตร ยาว : 15 เมตร
ที่ดินผืนนี้มีพื้นที่ : 75 ตารางเมตร
ที่ดินผืนนี้มีพื้นที่ : 18.75 ตารางวา
def land(width,long):
    cal = width*long
    cal_wa = cal/4
    print('ที่ดินผื้นนี้กว้าง : {} เมตร ยาว : {} เมตร'.format(width,long))
    print('ที่ดินผืนนี้มีพื้นที่ : {} ตารางเมตร'.format(cal))
    print('ที่ดินผืนนี้มีพื้นที่ : {} ตารางวา'.format(cal_wa))
    return cal_wa

res=land(3,9)
ที่ดินผื้นนี้กว้าง : 3 เมตร ยาว : 9 เมตร
ที่ดินผืนนี้มีพื้นที่ : 27 ตารางเมตร
ที่ดินผืนนี้มีพื้นที่ : 6.75 ตารางวา
print(res)
6.75
def land(width,long,price=999888):
    cal = width*long
    cal_wa = cal/4
    print('ที่ดินผื้นนี้กว้าง : {} เมตร ยาว : {} เมตร'.format(width,long))
    print('ที่ดินผืนนี้มีพื้นที่ : {} ตารางเมตร'.format(cal))
    print('ที่ดินผืนนี้มีพื้นที่ : {} ตารางวา'.format(cal_wa))
    return cal_wa*price

res=land(3,9)
ที่ดินผื้นนี้กว้าง : 3 เมตร ยาว : 9 เมตร
ที่ดินผืนนี้มีพื้นที่ : 27 ตารางเมตร
ที่ดินผืนนี้มีพื้นที่ : 6.75 ตารางวา
print(res)
6749244.0
res=land(5,15)
ที่ดินผื้นนี้กว้าง : 5 เมตร ยาว : 15 เมตร
ที่ดินผืนนี้มีพื้นที่ : 75 ตารางเมตร
ที่ดินผืนนี้มีพื้นที่ : 18.75 ตารางวา
print(res)
18747900.0
def land(width,long,price=999888):
    cal = width*long
    cal_wa = cal/4
    print('ที่ดินผื้นนี้กว้าง : {} เมตร ยาว : {} เมตร'.format(width,long))
    print('ที่ดินผืนนี้มีพื้นที่ : {} ตารางเมตร'.format(cal))
    print('ที่ดินผืนนี้มีพื้นที่ : {} ตารางวา'.format(cal_wa))
   calprice = cal_wa*price
...    
SyntaxError: unindent does not match any outer indentation level
>>> def land(width,long,price=999888):
...     cal = width*long
...     cal_wa = cal/4
...     print('ที่ดินผื้นนี้กว้าง : {} เมตร ยาว : {} เมตร'.format(width,long))
...     print('ที่ดินผืนนี้มีพื้นที่ : {} ตารางเมตร'.format(cal))
...     print('ที่ดินผืนนี้มีพื้นที่ : {} ตารางวา'.format(cal_wa))
...     calprice = cal_wa*price
...     return 'ที่ดินผืนนี้ราคา : {:,.2f} บาท'.format(calprice)
... 
>>> res = land(5,15)
ที่ดินผื้นนี้กว้าง : 5 เมตร ยาว : 15 เมตร
ที่ดินผืนนี้มีพื้นที่ : 75 ตารางเมตร
ที่ดินผืนนี้มีพื้นที่ : 18.75 ตารางวา
>>> print(res)
ที่ดินผืนนี้ราคา : 18,747,900.00 บาท
