class Account:
    def __init__(self,account_no,account_holder,balance):
        self.account_no=account_no
        self.account_holder=account_holder
        self.balance=balance
accounts=[]

def Save_Account():
    with open("accounts.txt","w") as f:
        
     for account in accounts:
         line=f"{account.account_no},{account.account_holder},{account.balance}\n"
         f.write(line)
       
def Load_Account():
    try:
       with open("accounts.txt","r") as f:
         for line in f:  
               line=line.strip()  
               acc=line.split(",")    
               account=Account(int(acc[0]),acc[1],int(acc[2]))  
               accounts.append(account) 
    except FileNotFoundError:  
         pass
               
                
            
def Create_Account():
    
     while True:
         accountno=int(input("Enter ur Account no:"))
         is_found=False
         for account in accounts:
           if account.account_no==accountno:
             is_found=True
             print("account is already created!")
             break
         if not is_found:
             break  
     accountholder=input("Enter ur name:")
     balance=int(input("Enter ur balance:"))
     account=Account(accountno,accountholder,balance)
     accounts.append(account)
     Save_Account()
     print("Account created successfully!!!")  
      
         
def View_Account():
    for account in accounts:
       print("=====================")   
       print("Account no is:",account.account_no)
       print("Account holer  is:",account.account_holder)
       print("Account balance is:",account.balance)
       print("=====================")
    if accounts==[]:
        print("No accounts found")
            
       
def Search_Account(accountno):
    for account in accounts:
        if account.account_no==accountno:
             print("=====================")   
             print("Account no is:",account.account_no)
             print("Account holder  is:",account.account_holder)
             print("Account balance is:",account.balance)
             print("=====================")
             break
    else:
        print("No such account exists")
                 
           
def Deposit_Money(accountno):
    for account in accounts:
        if account.account_no==accountno:
            deposited_money=int(input("Plz enter the amount you want to deposit:"))
            print("ur previous balance was:",account.balance)
            account.balance+=deposited_money
            print("Now ur updated balance is",account.balance)
            Save_Account()
            break
    else:
         print("No such account exists")   
    

def Withdraw_Money(accountno):
    for account in accounts:
        if account.account_no==accountno:
            withdraw_money=int(input("Plz enter the amount u want to withdraw:"))
            if account.balance<withdraw_money:
                print("Insufficient balance")
                break
            else:
                print("ur previous balance was:",account.balance)
                account.balance-=withdraw_money
                print("your updated balance is:",account.balance) 
                Save_Account()
                break     
    else:
        print("No such account exists")        
                    
    
def Delete_Account(accountno):
    for account in accounts:
         if account.account_no==accountno:
             accounts.remove(account)
             print("Account deleted successfully")
             Save_Account()
             break
    else:
        print("No such account exists")       
             
        
def Check_Balance(accountno):
    for account in accounts:
         if account.account_no==accountno: 
             print("Your current balance is:",account.balance)
             break
    else:
        print("No such account exists") 
        
def Transfer_Money(ur_accno,accountno):
     for other_acc in accounts:
                if other_acc.account_no==ur_accno:
                    print("sender", other_acc.account_holder,"previous balance was:",other_acc.balance)
                    transfer_money=int(input("Plz enter the amount u want to transfer :"))
                    if other_acc.balance>=transfer_money:
                      for account in accounts:
                          if account.account_no==accountno:
                            #  transfer_money=int(input("Plz enter the amount u want to transfer to:"))
                             print("receiver",account.account_holder, "previous balance was:",account.balance)
                             account.balance+=transfer_money
                             print("receiver",account.account_holder,"updated balance is:",account.balance)
                             break
                      else:
                            print("No such receiver account exists")  
                            break    
                                  
                      other_acc.balance-=transfer_money
                      print("sender",other_acc.account_holder," updated balance is:",other_acc.balance)
                      Save_Account()
                      break
                    else:
                        print("Insufficent balance in the sender account")
                        break  
                                   
     else:
        print("No such sender account exists")            
                    
             
            
 
Load_Account()    
               
while True:
    userchoice=int(input("""=====BANK MANAGEMENT SYSTEM=====
SELECT ONE OPTION:
1.Create Account
2.View Account
3.Search Account
4.Deposit Money
5.Withdraw Money
6.Delete Account
7.Check Balance
8.Transfer Money
9.Exit                     
"""))
    if userchoice==1:
        Create_Account()
    elif userchoice==2:
         View_Account() 
    elif userchoice==3:
        accountno=int(input("Plz enter account no:"))
        Search_Account(accountno)         
    elif userchoice==4:
        accountno=int(input("Plz enter account no:"))
        Deposit_Money(accountno) 
    elif userchoice==5:
        accountno=int(input("Plz enter account no:"))
        Withdraw_Money(accountno) 
    elif userchoice==6:
        accountno=int(input("Plz enter account no:"))
        Delete_Account(accountno)  
    elif userchoice==7:
        accountno=int(input("Plz enter account no:"))
        Check_Balance(accountno)        
    elif userchoice==8:
        ur_accno=int(input("Enter ur account no"))
        accountno=int(input("Plz enter account no of the person u want to send money:"))
        Transfer_Money(ur_accno,accountno)                     
    elif userchoice==9:
        print("You exit from the system!!")
        break
    else :
      print("No such options exist!===ERROR===")
      break          
        