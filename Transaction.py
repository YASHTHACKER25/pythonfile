import random#importing random for getting random numbers which can be use in transaction id
from cart import Cart#importing Cart named class from cart file
class Transaction():
    __t_id=None#transaction id
    __t_amount=None#transaction amount
    __t_status=None#transaction status
    Cart1=None#for creating object 
    def __init__(self):
        self.Cart1=Cart()#creating object for Cart class
        self.__t_id=random.randint(1, 100)*1234567#getting random numbers of transaction id
        self.__t_amount=self.Cart1.getbill_amount()#getting transaction amount from cart1 object
        print("Your total amount is :",self.__t_amount)#printing amout for user
        a=input("PRESS 1 FOR CONTINUE\nPRESS ANY KEY FOR CANCLE TRANSACTION")#asking user to continu or not
        if(a=='1'):
            self.__t_status="SCUSSSFULL"
        else:
            self.__t_status="UNSCUSSESFULL"  
            self.displayt()#if tranasaction is unscussesfull showing details               
    def getamount(self):#to get transaction amount
        return (self.__t_amount)
    def gettid(self):#to get transaction id
        return (self.__t_id)
    def getstatus(self):#to get transaction status
        return (self.__t_status)              
    def displayt(self):#to showing details of transaction
         print(f"Transaction id:{self.__t_id}\nTransaction amount :{self.__t_amount}\nTransaction status:{self.__t_status}")
      