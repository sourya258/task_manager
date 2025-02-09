"""class Bankaccount:
    def __init__(self, details):
        self.details = details  
        
    def debit(self):
        debiting_account_number = input("Please enter you 10 digit account number =")
        print("\n")
        
        if len(debiting_account_number) != 10 or not debiting_account_number.isdigit():
            print("Invalid account number \n")
            return
        
        debiting_account_number = int(debiting_account_number)
        if debiting_account_number not in self.details :
            print("Account number doesn't exist \n")
            return
            
        else:
            debited = int(input("Enter the amount you desire to debit: "))
            
            if debited > self.details[debiting_account_number]:
                print("Insufficient funds \n")
                return
            
            else:
                self.details[debiting_account_number] -= debited
                print(F"Your remaining balance is : {self.details[debiting_account_number]} ")
                print("\n")
        
    def credit(self):
        crediting_account_number = input("Please enter you 10 digit account number = ")
        print("\n")
        
        if len(crediting_account_number) != 10 or not crediting_account_number.isdigit():
            print("Invalid Account Number \n")
            return
        
        crediting_account_number = int(crediting_account_number)
        if crediting_account_number not in self.details:
            print("Account number doesn't exist \n")
            return
           
        else:
            print(f"Your balance is : Rs.{self.details[crediting_account_number]} \n")
            credited = int(input("Enter the amount you desire to credit: "))
            
            if credited >= 0:
               self.details[crediting_account_number] += credited
               print(F"Your remaining balance is : {self.details[crediting_account_number]} ")
               print("\n")
               
            else:
                print("Invalid Amount \n")
                return
            
    def checking(self):
        checking_account_number = input("Please enter you 10 digit account number = ")
        print("\n") 
        
        if len(checking_account_number) != 10 or not checking_account_number.isdigit():
            print("Invalid Account Number \n")
            return
        
        checking_account_number = int(checking_account_number)
        if checking_account_number not in self.details:    
            print("Account number doesn't exist \n") 
            return
        
        else:
            checking_account_number = int(checking_account_number)
            print(f"Your balance is : Rs.{self.details[checking_account_number]} ")
            print("\n")
        
    def transfer(self):
        initiating_account_number = input("Enter the 10 digit account number you want to transfer from: ")
        receving_account_number = input("Enter the 10 digit account number receiving the funds : ")
        
        if (len(initiating_account_number) == 0 and len(receving_account_number) == 0) \
                 or (not initiating_account_number.isdigit() and receving_account_number.isdigit()):
                
            print("\n"f"Invalid input, one of the account numbers are incorrect. Initiating Account No.: {initiating_account_number},\
Receving Account No.: {receving_account_number}. Please do check the numbers duly.\n")  
            return
        
        initiating_account_number = int(initiating_account_number)
        receving_account_number = int(receving_account_number)
        
        if initiating_account_number not in self.details or receving_account_number not in self.details:
            print("\n"f"One of the account numbers doesnt exist. Initiating Account No.: {initiating_account_number}, \
Receving Account No.: {receving_account_number}. Please do check the numbers duly.\n")
            return
        
        else:
            print("\n"f"The existing balance in transferring account is : {self.details[initiating_account_number]}")
            print(f"The existing balance in receiving account is : {self.details[receving_account_number]} \n")
            
            while True:
                Transfer_amount = input("Enter the amount you want to transfer :")
            
                if Transfer_amount == 0 or not Transfer_amount.isdigit():
                   print("\n"f"The transfer input is incorrect : {Transfer_amount}")
                   continue
                
                
                Transfer_amount = int(Transfer_amount)
                if Transfer_amount > self.details[initiating_account_number]:
                    print("The transfer amount exceeded the balance in your bank \n")
                    break
            
                else:
                
                    self.details[initiating_account_number] -= Transfer_amount
                    self.details[receving_account_number] += Transfer_amount
                
                    print("\n The transfer was successfull \n")
                    print(f"The existing balance in transferring account is : {self.details[initiating_account_number]}")
                    print(f"The existing balance in receiving account is : {self.details[receving_account_number]} \n")
                    break
                                
account_storage = {}

while True:
    
    ways = input("Do you wish to enter your details (Y/N):").strip().upper()
    
    if ways == 'Y':
        account_number = input("Please enter your 10 digit account number = ")
        print("\n")
    
    
        if len(account_number) != 10 or not account_number.isdigit():
           print("Invalid account number \n")
           break
    
        else:
            account_number = int(account_number)
        
            if account_number in account_storage:
               print("Account Number already Exists \n")
               break
           
            else:
               bank_balance = int(input("Please enter your account balance (In Rs.)= "))
               account_storage[account_number] = bank_balance
               details = Bankaccount(account_storage) 
               print("Account added successfully \n")
               
     
    elif ways == 'N' :  
        if not account_storage:
           print("No accounts exist add accounts first \n")
           
        else:    
            print("What action do you wish to perform - ")
            action = input("Choose as you desire : 1.Debit, 2.Credit, 3.Check Balance, 4.Transfer, 5.Exit:").strip()
            
        
            if action == '1':
              details.debit()
   
            elif action == '2':
              details.credit()
    
            elif action == '3':
              details.checking()
            
            elif action == '4':
                details.transfer()
            
            elif action =='5':
                print("Thanking You")
                break
                
            else:
               print("Invalid Input and thank you for using this system. \n")
               break
        
    else:
        print("Thanking you. Please Try again \n")"""

'''class Student:
    def __init__ (self,name,marks):
        self.name = name
        self.__marks= marks
        
    def __calculating_Avg (self):
        total = sum(self.__marks)
        subjects = len(self.__marks)
        
        average = total/subjects
        print(f"The average of the student {self.name} is: {average}")
        return average
            
    def printing_grades(self):
        to_be_graded = self.__calculating_Avg()
        
        if to_be_graded > 90:
            print(f"The grade of the student {self.name} is A+")
        elif to_be_graded > 85:
            print(f"The grade of the student {self.name} is A")
        elif to_be_graded > 80:
            print(f"The grade of the student {self.name} is B+")
        elif to_be_graded > 75:
            print(f"The grade of the student {self.name} is B")
        elif to_be_graded > 70:
            print(f"The grade of the student {self.name} is C+")
        elif to_be_graded > 65:
            print(f"The grade of the student {self.name} is C")
        elif to_be_graded > 60:
            print(f"The grade of the student {self.name} is D+")
        elif to_be_graded > 55:
            print(f"The grade of the {self.name} student is D")
        else:
            print(f"The student {self.name} has failed")
        
        
    
s1 = Student("Akash" , [2,4,8,9,4])
s1.printing_grades()'''

d = {'f' : 10, 'b' : 60, 'c' : 90}
print( sorted([(k,v) for v,k in d.items()]))




        
        
        
        
        
    

 


        