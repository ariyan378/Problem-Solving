#Banking_Money_transfer
#giving option to user

print("---------------------Hello---------------------")
print("________________Choose Your Option___________________  ")
print("1.Add Money")
print("2.send Money")
print("3.Cashout")
#taking Input from user
choice = int(input("Enter Your Choice 1/2/3 :")) 
money = 5000;
#using if else for decision making
if choice == 1 :
    addmoney_amount=int(input("Amount Of Money :")) 
    money +=addmoney_amount
    print(f" Your Current Money amount is {money}")
elif choice == 2 :
    sendmoney_amount=int(input("Amount Of Money :")) 
    money = money - sendmoney_amount   
#if we want to send more money than my balance 
    if money <0: 
        print('Low Balance')
    else:
        print(f"Your Current Balance is {money}")
elif choice == 3:
    cashout = int(input("Enter Your amount :"))
    #if we want to cashout more money than my balance 
    if money ==money-cashout <0: 
        print('Low Balance')
    else:
        money-=cashout
        print(f"Your Current Amount Is {money}")
else:
    print("Invalid Choice")        

