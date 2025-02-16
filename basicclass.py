class Theater:
    #Attribute
    theatername = 'Uncle Engineer Theater'
    # title = 'แฟนฉัน'
    # price = 80

    # Constructor
    def __init__(self,title,price): #ใส่ตัวแปรที่ต้องการกำหนดค่าเอง
        self.title = title
        self.price = price
    
    #Method
    def hello(salf):
        print('สวัสดีคุณลูกค้าทุกท่าน')

class Customer(Theater):
    def __init__(self, fullname,age,title, price,seats):
        super().__init__(title, price)
        #self คือ keyword ที่แยกค่าขอบเขตจากตัวของมัน เช่น 
        self.fullname = fullname
        self.age = age
        self.seats = seats
        self.money = 10000
    
    def byTicket(self):
        #การคำนวณค่าตั๋ว
        self.total = self.price*self.seats

        #หักเงินจากลูกค้า
        self.money -= self.total

        print(f'ชื่อลูกค้า : {self.fullname}')
        print(f'อายุ : {self.age}')
        print(f'เรื่อง : {self.title}')
        print(f'ซื้อกี่ที่นั่ง : {self.seats} ที่นั่ง รวมเงิน : {self.money} บาท')
        print(f'เหลือเงิน : {self.money} บาท')

# # สร้าง Instance ขึ้นมา คือ ตัวแปรที่เป็น object
# movie01 = Theater('ธี่หยด',150)
# print(movie01.theatername)
# print(movie01.title)
# print(movie01.price)
# movie01.hello()
# print('------------------------------------------')
# movie02 = Theater('Thor',120)
# print(movie02.theatername)
# print(movie02.title)
# print(movie02.price)
# print('------------------------------------------')
# movie03 = Theater('เพื่อนไม่สนิท',80)
# print(movie03.theatername)
# print(movie03.title)
# print(movie03.price)

customer01 = Customer('สมชาย สบายดี',20,'Thor',120,1)
print(customer01.theatername)
customer01.hello()
customer01.byTicket()
print('================================')
customer02 = Customer('สมปอง สบายดี',20,'ธี่หยด',150,2)
print(customer02.theatername)
customer02.hello()
customer02.byTicket()
print('================================')
customer03 = Customer('สมหญิง จริงใจ',50,'แฟนฉัน',180,2)
print(customer03.theatername)
customer03.hello()
customer03.byTicket()