tilecolor ={'red':100,'gold':200,'white':90,'grey':30}

print('-----------ราคากระเบื้อง----------')
for c,t in tilecolor.items():
        print('สี: {} ราคา: {}'.format(c,t))

print('------------ โปรแกรมคำนวณกระเบื้อง by Pha ---------------')

try :
        tiles = int(input('คุณต้องการปูกระเบื้องทั้งหมดกี่แผ่น : '))
        row = int(input('1 แถวต้องปูกระเบื้องกี่แผ่น : '))
        color = input('กระเบื้องสีอะไร? [ red/gold/white/grey] : ')
except :
        print('กรุณากรอกข้อมูลเป็นตัวเลขเท่านั้น !!')
        tiles = int(input('คุณต้องการปูกระเบื้องทั้งหมดกี่แผ่น : '))
        row = int(input('1 แถวต้องปูกระเบื้องกี่แผ่น : '))
        color = input('กระเบื้องสีอะไร? [ red/gold/white/grey] : ')
    # เช็ค Error ได้แค่รอบเดียวถ้าต้องการวนซ้ำให้ใช้ while    
print('----------------- Calulate -------------')
total_row = tiles//row
remain_tiles = tiles%row
#price_tiles = 30
#print(remain_tiles,total_row)
# ลูกค้าต้องซื้อกระเบื้องเพิ่มกี่แผ่น
buy_more = row-remain_tiles
#totalprice = (tiles+buy_more)*price_tiles
print(f'มีกระเบื้องทั้งหมด : {tiles} แผ่น')
print(f'1 แถวปูกระเบื้องได้ : {row} แผ่น')
print(f'***--------คำนวณ----------***')
print('ต้องปูกระเบื้องทั้งหมด  {}  แถว'.format(total_row))
print('เหลือกระเบื้องที่ยังไม่ได้ปู  {}  แผ่น'.format(remain_tiles))
print('ลูกค้าต้องซื้อกระเบื้องเพิ่ม  {}  แผ่น'.format(buy_more))
print('ลูกค้าต้องจ่ายเงินเพิ่มสำหรับซื้อกระเบื้อง  {}  บาท'.format(buy_more*tilecolor[color]))

# คำนวณได้เฉพาะเลขที่คำนวณไม่ลงตัว

