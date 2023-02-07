import pickle
import datetime





#Function to display Main Menu
def Main_Menu():
    print("BANK MANAGEMENT SYSTEM".center(65))
    print("*"*130)
    print("MAIN MENU".center(65))
    print(" "*20+"1. NEW ACCOUNT")
    print(" "*20+"2. DEPOSIT AMOUNT")
    print(" "*20+"3. WITHDRAW AMOUNT")
    print(" "*20+"4. BALANCE ENQUIRY")
    print(" "*20+"5. DISPLAY ACCOUNT HOLDER LIST(SORT BY ACCOUNT NO)")
    print(" "*20+"6. DISPLAY ACCOUNT HOLDER LIST(SORT BY CUSTOMER NAME)")
    print(" "*20+"7. CLOSE AN ACCOUNT")
    print(" "*20+"8. SEARCH AN ACCOUNT BY A/C NO")
    print(" "*20+"9. SEARCH AN ACCOUNT BY CUSTOMER NAME")
    print(" "*20+"10.EXIT")
    print("*"*130)


    


#Function to display Employee Records as per Employee Number
def Sort_AccountNo(F):
    try:
        with open(F,'rb+') as fil:
            rec = pickle.load(fil)
            rec.sort(key=lambda rec:rec["ACC_NO"])
            fil.seek(0)
            pickle.dump(rec, fil)
    except FileNotFoundError:
        print(F, "File has no Records...")

#Function to display Employee Records as per Employee Name
def Sort_Account_Holder_Name(F):
    try:
        with open(F,'rb+') as fil:
            rec = pickle.load(fil)
            rec.sort(key=lambda rec:rec["CUSTOMER_NAME"])
            fil.seek(0)
            pickle.dump(rec, fil)
    except FileNotFoundError:
        print(F, "File has no Records...")
    
#FUNCTION TO CREATE NEW ACCOUNT WITH THE BANK
def CREATE_NEW_ACCOUNT(F):
    try:
        fil = open(F, 'ab+')#will create file if not exist else read the records from existing file.
        print(fil.tell())
        TYPE_LIST=["SAVING","CURRENT"]
        
        if fil.tell()>0:
            fil.seek(0)
            Rec1 = pickle.load(fil)
        else:
            Rec1 = []
        print()
        print()
        print()
        print("*"*130)
        print("CREATE NEW ACCOUNT SCREEN".center(65))
        print("*"*130)
        print()
        while True:#Loop for accepting Record
            while True: #Allowing Unique Emp ID
                ACC_NO = input("ENTER ACCOUNT NUMBER:(4 CHARACTER LONG)")
                ACC_NO = ACC_NO.upper()
                if any(dict.get("ACC_NO") == ACC_NO for dict in Rec1): #checks if Eid already exist
                    print("This ACCOUNT NUMBER ALREADY EXIST...")
                else:
                    break
            print()
            print()
            CUSTOMER_NAME = input("ENTER ACCOUNT HOLDER'S NAME")
                # Allowing only valid 10 digit Mobile No
            while True:
                print()
                print()
                MOBILE_NO = input("ENTER MOBILE NUMBER")
                if len(MOBILE_NO)!=10 or MOBILE_NO.isdigit()==False:
                    print()
                    print("ENTER VALID MOBILE NUMBER..")
                else:
                    break
                #Allowing only specific Account Type
            while True:
                print()
                print()
                TYPE=input('ENTER ACCOUNT TYPE [SAVING/CURRENT"]')
                if TYPE.upper() in TYPE_LIST:
                    break

            print()
            print()

            AMOUNT = float(input("ENTER AMOUNT DEPOSIT IN YOUR ACCOUNT"))
            #The Current Date is stored as DATE OF OPENING A/C
            Dat=datetime.datetime.now()
            Dat=Dat.date()
            Rec={"ACC_NO":ACC_NO.upper(),"CUSTOMER_NAME":CUSTOMER_NAME.upper(),"MOBILE_NO":MOBILE_NO,"TYPE":TYPE.upper(),"AMOUNT":AMOUNT,"Dat":Dat}
            Rec1.append(Rec)
            
            #pickle.dump(Rec,fil)
            print()
            print()
            ch=input("DO YOU WANT TO OPEN ANOTHER NEW ACCOUNT..")
            if ch=='N' or ch=='n':
                break
        fil.close()
        with open(F,'wb') as fil:#will open the file for overwriting
            pickle.dump(Rec1,fil)
            print("ACCOUNT HAS BEEN CREATED SUSSESSFULLY..")
    except ValueError:
        print("Invalid values entered")


#Function to Deposite Amount in his/her Account
def DEPOSIT_AMOUNT(F):
    try:
        with open(F,'rb+') as fil:
            found=0
            Rec=pickle.load(fil)
            print(Rec)
            print()
            print()
            print()
            print("*"*130)
            print("DEPOSIT AMOUNT SCREEN".center(65))
            print("*"*130)
            print()
            acc_no = input("ENTER THE ACCOUNT NO (IN WHICH YOU WANT TO DEPOSIT MONEY)")
            for d in Rec:
                if acc_no.upper()==d["ACC_NO"]:
                    found=1
                    for i,j in d.items():
                        if i == "AMOUNT":
                            print()
                            print()
                            amount = float(input("ENTER THE AMOUNT YOU WANT TO DEPOSIT"))
                            d[i] = d[i] + amount
                    
            if(found==0):
                print()
                print("ACCOUNT NUMBER NOT FOUND...")
            else:
                fil.seek(0)
                pickle.dump(Rec,fil)
                print()
                print("AMOUNT DEPOSITED SUCCESSFULLY...")
    except EOFError:
        print("Record Not Found")
    except FileNotFoundError:
        print(F," File does not exist")
    
#Function to WITHDRAW Amountin FROM his/her Account
def WITHDRAW_AMOUNT(F):
    try:
        with open(F,'rb+') as fil:
            found=0
            Rec=pickle.load(fil)

            print()
            print()
            print("*"*130)
            print("WITHDRAW AMOUNT SCREEN".center(65))
            print("*"*130)
            print()
            
            acc_no = input("ENTER THE ACCOUNT NO (IN WHICH YOU WANT TO WITHDRAW MONEY)")
            for d in Rec:
                if acc_no.upper()==d["ACC_NO"]:
                    found=1
                    for i,j in d.items():
                        if i == "AMOUNT":
                            print()
                            print()
                            amount = float(input("ENTER THE AMOUNT YOU WANT TO WITHDRAW"))
                            if d[i]<amount:
                                found=2
                                print()
                                print("NO SUFFICIENT FUND IN YOUR ACCOUNT..")
                            else:
                                d[i] = d[i] - amount
                                print()
                                print("SUCCESSFULLY WITHDRAWN, UPDATED AMOUNT IS : ", d[i])
                    
            if(found==0):
                print("ACCOUNT NUMBER NOT FOUND...")
            elif(found==2):
                print("NO SUFFICIENT FUND IN YOUR ACCOUNT..")
            else:
                fil.seek(0)
                pickle.dump(Rec,fil)
                print("Amount Withdrew Successfully...")
    except EOFError:
        print("Record Not Found")
    except FileNotFoundError:
        print(F," File does not exist")
        

#FUNCTION TO MAKE BALANCE ENQUIRY AGAINST CUSTOMER'S A/C NO
def BALANCE_ENQUIRY(F):
    try:
        with open(F,'rb+') as fil:
            found=0
            Rec=pickle.load(fil)
            acc_no = input("ENTER THE ACCOUNT NO (WHICH YOU WANT TO MAKE ENQUIRY")
            for d in Rec:
                if acc_no.upper()==d["ACC_NO"]:
                    found=1
                    for i,j in d.items():
                        if i == "AMOUNT":
                            amount = d[i]
                        if i == "CUSTOMER_NAME":
                            cname = d[i]
                        if i == "ACC_NO":
                            acno = d[i]
                        
                            
                    
            if(found==0):
                print("BANK MANAGEMENT SYSTEM".center(65))
                print("*"*130)
                print("BALANCE ENQUIRY RESULT".center(65))
                print("ACCOUNT NUMBER NOT FOUND...")
                print("*"*130)
                print()
                print()
            else:
                print("BANK MANAGEMENT SYSTEM".center(65))
                print("*"*130)
                print("BALANCE ENQUIRY RESULT".center(65))
                F="%15s %15s %15s"
                print(F % ("CUSTOMER NAME", "ACCOUNT NUMBER", "BALANCE AMOUNT"))
                print("%15s" % cname, end=' ')
                print("%15s" % acno, end=' ')
                print("%15s" % amount)
                print("*"*130)
                print()
                print()
                
            
    except EOFError:
        print("Record Not Found")
    except FileNotFoundError:
        print(F," File does not exist")


#FUNCTION TO DISPLAY ALL ACCOUNT DETAILS 
def Display(F):
    try:
        with open(F,'rb') as fil:
            print()
            print()
            print("="*130)
            print("ACCOUNT HOLDER'S LIST".center(65))
            print("="*130)
            F="%15s %15s %15s %15s %15s"
            print(F % ("ACCOUNT NUMBER","CUSTOMER NAME","MOBILE","A/C TYPE","BALANCE"))
            print("="*130)
            Rec=pickle.load(fil)
            c=len(Rec)
            for i in Rec:
                for j in i.values():
                    print("%15s" % j, end=' ')
                print()
            print("*"*130)
            print("Total Records : ",c)
    except EOFError:
        print("="*130)
        print("Records Read:",c)
    except FileNotFoundError:
        print(F,"File Does't Exist")

# FUNCTION TO CLOSE AN EXISTING CUSTOMER'S ACCOUNT FROM BANK      
def CLOSE_ACCOUNT(F):
     try:
          with open(F,'rb+') as fil:
               Rec=pickle.load(fil)
               print()
               print()
               print("*"*130)
               print("CLOSE ACCOUNT SCREEN".center(65))
               print("*"*130)
               print()
               id = input("ENTER THE ACCOUNT NUMBER TO BE DELETED")
               for i in range(0,len(Rec)):
                    if Rec[i]["ACC_NO"]==id.upper():
                         print("="*130)
                         F="%15s %15s %15s %15s %15s"
                         print(F % ("ACCOUNT NUMBER","CUSTOMER NAME","MOBILE","A/C TYPE","BALANCE"))
                         N=Rec.pop(i)
                         for j in N.values():
                              print('%15s' % j, end=' ')
                         print()
                         print()
                         print("ACCOUNT HAS BEEN DELETED SUCCESSFULLY......")
                         print()
                         print()
                         print()
                         break
               else:
                   print()
                   print()
                   print("ACCOUNT NUMBER DOES NOT EXISTT...")
                   print()
                   print()
               fil.seek(0)
               pickle.dump(Rec,fil)
     except FileNotFoundError:
          print(F, "File doesn't exist")
     except KeyError:
          print("Wrong Key...")
     except IndexError:
          print("Wrong Index...")

#FUNCTION TO SEARCH BANK CUSTOMER A/C DETAIL BY ACCOUNT NUMBER.
def SEARCH_ACCOUNT_NO(F):
    try:
        with open(F,'rb') as fil:
            Rec = pickle.load(fil)
            accno=input("ENTER THE ACCOUNT NUMBER TO BE SEARCHED")
            for i in Rec:
                if i["ACC_NO"]==accno.upper():
                    print("="*130)
                    print("ACCOUNT SEARCH RESULT (BY A/C NO)".center(65))
                    print("="*130)
                    print()
                    F="%15s %15s %15s %15s %15s"
                    print(F % ("ACCOUNT NUMBER","CUSTOMER NAME","MOBILE","A/C TYPE","BALANCE"))
                    print("="*130)
                    for j in i.values():
                        print('%15s' %j, end='')
                    print()
                    print()
                    print()
                    print()
                    break
            
            else:
                print()
                print()
                print("ACCOUNT NUMBER DOES NOT EXISTT...")
                print()
                print()
                print()
                print()
    except FileNotFoundError:
        print(F, "File Doesn't exist")


#FUNCTION TO SEARCH BANK CUSTOMER A/C DETAIL BY ACCOUNT HOLDER'S NAME.
def SEARCH_ACCOUNT_NAME(F):
    try:
        with open(F,'rb') as fil:
            Rec = pickle.load(fil)
            found=0
            ch=input("ENTER THE EMPLOYEE NAME TO BE SEARCHED")
            print()
            print("="*130)
            print("ACCOUNT SEARCH RESULT (BY NAME)".center(65))
            print("="*130)
            print("="*130)
            F="%15s %15s %15s %15s %15s"
            print(F % ("ACCOUNT NUMBER","CUSTOMER NAME","MOBILE","A/C TYPE","BALANCE"))
            print("="*130)
            for i in Rec:
                if i["CUSTOMER_NAME"]==ch.upper() or i["CUSTOMER_NAME"].startswith(ch.upper()):
                    found=found+1
                    for j in i.values():
                        print('%15s' %j, end='')
                    print()
            if found==0:
                print("RECORD NOT FOUND...")
                print()
                print()
                print()
                print()
            else:
                print("Total Records Found : ", found)
                print()
                print()
                print()
                print()
       
    except FileNotFoundError:
        print(F, "File Doesn't exist")
    except EOFError:
        print("Record Not Found")
                    
    
         
F1="ACCOUNT"
while True:
    Main_Menu()
    ch=input("Enter Your Choice :")
    if ch=="1":
        CREATE_NEW_ACCOUNT(F1)
    elif ch=="2":
        DEPOSIT_AMOUNT(F1)
        Display(F1)
    elif ch=="3":
        WITHDRAW_AMOUNT(F1)
        Display(F1)
    elif ch=="4":
        BALANCE_ENQUIRY(F1)
        
    elif ch=="5":
        Sort_AccountNo(F1)
        Display(F1) 
    elif ch=="6":
        Sort_Account_Holder_Name(F1)
        Display(F1)
    elif ch=="7":
        CLOSE_ACCOUNT(F1)
    elif ch=="8":
        SEARCH_ACCOUNT_NO(F1)
    elif ch=="9":
        SEARCH_ACCOUNT_NAME(F1)
    elif ch=="10":
        print("Exiting....")
        break
    else:
        print("Wrong Choice Entered..")
            
            
            
                
                    

Main_Menu()

















