# tạo khuôn mẫu
class meo:
    # thuộc tính
    name='Agfieghdu'
    age=3
    color='black'

    # phương thức
    def inputinfo(self):
        self.name=input("Nhập tên: ")
        self.age=input("Nhập tuổi: ")
        self.color=input("Nhập màu mèo: ")


    def outputinfo(self):
        print("Tên: ",self.name)
        print("Tuổi: ",self.age)
        print("Màu: ",self.color)





    def setname(self,_name):
        self.name=_name
    
    
    def getname(self):
        return self.name 
    

    
    def setage(self,_age):
        self.age=_age
    
    
    def getage(self):
        return self.age
    


    
    def setcolor(self,_color):
        self.color=_color
    
    
    def getcolor(self):
        return self.color
    

# tạo đối tượng
Meo=meo()
Meo2=meo()


Meo.inputinfo()
Meo.outputinfo()

Meo2.inputinfo()
Meo2.outputinfo()