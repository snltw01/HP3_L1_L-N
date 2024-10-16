class SoHoc:
    number1=''
    number2=''

    def inpuinfo(self):
        self.number1=int(input("Nhập số thứ nhất: "))
        self.number2=int(input("Nhấp số thứ hai: "))

    def outputinfo(self):
        print("Số thứ nhât: ",self.number1)
        print("Số thứ hai: ",self.number2)

    def addition(self):
        total=self.number1+self.number2
        print(self.number1,"+",self.number2,"=",total)

    def subtract(self):
        total=self.number1-self.number2
        print(self.number1,"-",self.number2,"=",total)
    
    def multi(self):
        total=self.number1*self.number2
        print(self.number1,"*",self.number2,"=",total)

    def division(self):
        total=self.number1/self.number2
        print(self.number1,"/",self.number2,"=",total)







hs=SoHoc()
hs.inpuinfo()
hs.outputinfo()
hs.addition()
hs.subtract()
hs.multi()
hs.division()