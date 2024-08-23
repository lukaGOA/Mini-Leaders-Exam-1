#bank systyem

             # creating an account
account = input('please create an account name:')
password = input('please create a password:')
print('your account has been created, please log in to your account')

             #login to your account
while True:
    login_account = input('enter your account name to log in:')
    login_password = input('enter your password to login:')

                #checking account name and password
    if login_account == account and login_password == password:
                print('you have sucessfully loged in your account')
                       
                               #deposit
                balance = int(input('enter your balance:'))
                deposit = int(input('enter the amount of how much are you deposting:'))
                      #balance after deposit
                new_balance = balance + deposit
                print('You Succesfuly Depostied Money, Your current balance is:' , balance , 'Your balance after deposit will be:' , new_balance)

                             #withdraw
                balance = int(input('please enter your balance:'))
                withdraw = int(input('please enter amount od how much are you withdrawing:'))
                        #balance after withdraw
                new_balance = balance - withdraw
                print('You succesfully withdrawed money, your current balance is:' , balance , 'Your balance after deposit will be:' , new_balance )
                           #exit the bank
                print('Now you can exit the bank, thanks for using our bank')