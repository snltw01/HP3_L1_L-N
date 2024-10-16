class NhanVien:
    name=''
    age=''
    address=''
    money=''
    time=''

    def inputinfo(self):
        self.name=input("Tên nhân viên: ")
        self.age=int(input("Tuổi nhân viên đó là: "))
        self.address=input("Địa chỉ nhân viên sống là: ")
        self.money=int(input("số tiền nhân nhận được sau 1 tháng là: "))
        self.time=int(input("Thời gian nhân viên đó làm trong 1 tháng là: "))

    def outputinfo(self):
        print("Tên của nhân viên: ",self.name)
        print("Tuổi của nhân viên đó là: ",self.age)
        print("Địa chỉ nơi nhân viên đó sống là: ",self.address)
        print("Lương của nhân viên đó làm trong 1 tháng được là: ",self.money)
        print("Thời gian nhân viên đó làm trong 1 tháng là: ",self.time)

    def tinhThuong(self):
        if self.time<100:
            print("Số tiền mà nhân viên nhận được (có kèm tiền thưởng) là: ",self.money)
        elif self.time>100 and self.time<200:
            print("Số tiền mà nhân viên nhận được (có kèm tiền thưởng) là: ",self.money/100*110)
        elif self.time>200:
            print("Số tiền mà nhân viên nhận được (có kèm tiền thưởng) là: ",self.money/100*120)


staff=NhanVien()
staff.inputinfo()
staff.outputinfo()
staff.tinhThuong()