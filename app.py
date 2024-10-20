from Customer import Customer#importing class named Customer from Customer file
from Product import Product#importing class named Product from Product file
C1=Customer()#creating object of Customer class
S=C1.T1.getstatus()
#getting transaction status from Transaction class which's object name is T1 in Customerclass 
if(S=="SCUSSSFULL"):
  print("-----------------------------------invoice-------------------------------------------------------")
  print(f"""
  Customer Name:{C1.getcname()}
  Customer Address:{C1.getadd()}
  Customer phoneno.:{C1.getphone()}                  
  Transactio id={C1.T1.gettid()}
  NO.\t\tPRODUCT\t\tPRICE/UNIT\t\tQUANTITY\t\tAMOUNT""")
  l1=C1.T1.Cart1.getlist()
  #getting list of purchased product fromm cart1 which is called by transaction class which is called by customer class 
  for i in range(0,len(l1)):
    print(f"""
  {i+1}\t\t{l1[i].getname()}\t\t{l1[i].getprice()}\t\t\t{l1[i].getqty()}\t\t\t{l1[i].gettotal()}""")
    print(f"""----------------------------------------------------------------------------------------------
TOTAL:                                                                        {C1.T1.getamount()}          
-----------------------THANKYOU FOR PURCHASSING------------------------------------------""")
