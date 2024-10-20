from Product import Product#importing product class from product file
class Cart():
    purchase=[]#creating list of purchase product
    __bill_amount=0#creat total amount of bill    
    __num=None#for asking customer how many product they want to buy
    __P1=None#for creating object 
    def __init__(self):
        self.__num=int(input("how many product do you want to purchase"))    
        for i in range(0,self.__num):
            self.__P1=Product()#calling product class            
            self.purchase.append(self.__P1) #adding product in purchase list          
        for i in self.purchase:   
            self.__bill_amount=i.gettotal()+self.__bill_amount#for calculating total bill
    def getbill_amount(self):#to get bill amount
        return self.__bill_amount
    def getlist(self):#to get purchase list
        return (self.purchase)
                 


    