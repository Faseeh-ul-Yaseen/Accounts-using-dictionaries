# Non-OOP

# Using dictonaries for multiple accounts
accounts = []
n_accounts = -1
accounts_dict = {}


def new_account(aname, abalance, apassword, ):
    global accounts, accounts_dict
    accounts_dict = {'name': aname, 'balance': abalance, 'password': apassword}
    accounts.append(accounts_dict)


def show(account_number, password):
    global accounts
    this_account_dict = accounts[account_number]
    return None, print('Wrong Password') if password != this_account_dict.get('password') \
        else print(f'Account Number: {this_account_dict.get("account_number")}'
                   f'\nAccount name {this_account_dict.get("name")}'
                   f'\nAccount balance {this_account_dict.get("balance")}'
                   f'\nAccount Password {this_account_dict.get("password")}')


def get_balance(account_number, password):
    global accounts
    this_account_dict = accounts[account_number]
    if password != this_account_dict.get('password'):
        print('Incorrect password')
        return None
    return this_account_dict.get("balance")


def deposit(account_number, deposit_amount, password):
    global accounts
    this_account_dict = accounts[account_number]
    if deposit_amount <= 0:
        print('You cannot deposit negative or zero amount!')
        return None
    if password != this_account_dict.get('password'):
        print('Wrong Password')
        return None
    deposit = this_account_dict.get('balance')
    deposit += deposit_amount
    this_account_dict.update({'balance': deposit})
    return this_account_dict.get("balance")


def withdraw(account_number, withdraw_amount, password):
    global accounts

    this_account_dict = accounts[account_number]
    if withdraw_amount <= 0:
        print('You cannot withdraw Negative or Zero amount.')
        return None
    elif withdraw_amount > this_account_dict.get("balance"):
        print("you cannot withdraw more than your account balance")
        return None
    if password != this_account_dict.get('password'):
        print("Wrong Password")
        return None
    withdraw = this_account_dict.get('balance')
    withdraw -= withdraw_amount
    this_account_dict.update({'balance': withdraw})
    return this_account_dict.get("balance")


# Main program

while True:
    print()
    print('Press "b" to get the balance. Press "d" to make a deposit\nPress "w" to make a '
          'withdrawal. Press "s" to show the account\nPress "n" to create New Account\n'
          'Press "q" to quit\n')
    print()

    action = input('What do you want to do? ')
    action = action.lower()  # force lowercase
    action = action[0]  # just use first letter
    print()

    if action == 'b':
        print('Get Balance:')
        user_account = int(input('Please enter Your account number: '))
        user_password = input('Please enter the password: ')
        the_balance = get_balance(user_account, user_password)
        if the_balance is not None:
            print('Your balance is:', the_balance)

    elif action == 'n':
        print('New Account:')
        user_name = input('Please Enter your Name: ')
        user_password = input('Please enter the password: ')
        user_balance = int(input('Please Enter the Amount to Deposit: '))
        if user_balance <= 0:
            print('You cannot deposit The Negative or Zero Amount')
        elif user_name is int:
            print('You cannot Add Numerical Name!!!')
        
        else:
            new_account(user_name, user_balance, user_password)
            for i in range(1):
                n_accounts += 1
            accounts_dict.update({'account_number': n_accounts})
            print(f'Your Account number is {accounts_dict.get("account_number")} ')
 
    elif action == 'd':
        print('Deposit:')
        user_account = int(input('Please enter Your account number: '))
        user_deposit_amount = int(input('Please enter amount to deposit: '))
        user_password = input('Please enter the password: ')
        new_balance = deposit(user_account, user_deposit_amount, user_password)
        if new_balance is not None:
            print('Your new balance is:', new_balance)

    elif action == 'w':
        print('Withdraw')
        user_account = int(input('Please enter Your account number: '))
        user_withdraw_amount = int(input('Please enter amount to withdraw: '))
        user_password = input('Please enter the password: ')
        new_balance = withdraw(user_account, user_withdraw_amount, user_password)
        if new_balance is not None:
            print('Your new balance is:', new_balance)

    elif action == 's':
        print('Show Details')
        user_account = int(input('Please enter Your account number: '))
        user_password = input('Please enter the password: ')
        name = 'x'
        show(user_account, user_password)

    elif action == 'q':
        break

    else:
        print('Wrong Input')
    print()
    print('Done')
