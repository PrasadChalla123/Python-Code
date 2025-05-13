'''class Demo:
    def __init__(self):#it is a special method function or it is
        print("this is init method")                #init method
        #it automatically load the data in __init__method
    def myself(self):
        print("this is prasad function")
d1=Demo()
d1.myself()'''
class Demo:
    def __init__(self,cpu,ram):
        #print("this is init method")
        self.cpu=cpu
        self.ram=ram
    def myself(self):
        print("About my Pc:",self.cpu , self.ram)
d1=Demo("i5","12")
d2=Demo("Ryzen 7","16")
d1.myself()
d2.myself()
