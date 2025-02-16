Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from decimal import Decimal
>>> 1e6
1000000.0
>>> 1e7
10000000.0
>>> x = Decimal('10000000000')
>>> '{:.2e}'.format(x)
'1.00e+10'
