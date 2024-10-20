from Transaction import Transaction#importing Transaction named class from Transaction file
class Customer():
    __c_id=None#customer id 
    __c_name=None#customer name
    __c_add=None#customer address
    __c_phone_no=None#customer phone no
    T1=None#for creating object 
    def __init__(self):
        print("Please Enter Customer Details")
        self.__c_id=input("enter customer id")# to get customer id
        self.__c_name=input("enter customer name")# to get customer name
        self.__c_add=input("enter customer address")# to get customer address
        self.__c_phone_no=input("enter customer phone no.")# to get customer phone number  
        self.displayc()#calling function for displaying customer function   
        self.T1=Transaction()#creating object of  transaction class    
    def getcid(self):# to return customer id
        return self.__c_id    
    def getcname(self):# to return customer name
        return self.__c_name
    def getadd(self):# to return customer address
        return self.__c_add
    def getphone(self):# to return customer phone no
        return self.__c_phone_no   
    def displayc(self):#displaying customer details
        print(f"ID:{self.__c_id}\nNAME:{self.__c_name}\nADD:{self.__c_add}\nPHONE:{self.__c_phone_no}")

        