class Product():
    __p_id=None#for product id
    __p_name=None#product name
    __p_price=None#product price
    __p_qty=None#product quantity
    __p_total=None#total amount for particular product
    def __init__(self):
        print("product details")#asking details about product
        self.__p_id=input("enter product id")
        self.__p_name=input("enter product name")
        self.__p_price=int(input("enter product price"))
        self.__p_qty=int(input("enter quantity"))
        self.__p_total=self.__p_price*self.__p_qty
        self.displayp()#calling displayp function
    def getid(self):#to get product id
        return self.__p_id    
    def getname(self):#to get product name
        return self.__p_name
    def getprice(self):#to get product price
        return self.__p_price
    def getqty(self):#to get product quantity
        return self.__p_qty
    def gettotal(self):#to get product's total amount 
        return self.__p_total
    def displayp(self):#to displaying all details
        print(f"ID:{self.__p_id}\nNAME:{self.__p_name}\n PRICE:{self.__p_price}\nQUANTITY:{self.__p_qty}")
