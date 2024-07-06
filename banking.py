customer_balances = {'Jane Smith': {'balance': 10000},
                     'Iason Jordan': {'balance': 20000},
                     'David Morgan': {'balance': 20000},
                     'Brain John': {'balance': 40000},
                     'Jack Swift': {'balance': 10000}}

customer_transactions = {'Jane Smith': {'deposit': [], 'withdrawal': []},
                         'Iason Jordan': {'deposit': [], 'withdrawal': []},
                         'David Morgan': {'deposit': [], 'withdrawal': []},
                         'Brain John': {'deposit': [], 'withdrawal': []},
                         'Jack Swift': {'deposit': [], 'withdrawal': []}}

customerPins = []
customerNames = []
customerBalances = []
transactionHistory = []

# This statement below helps the program to run continuously.
while True:
    # os.system("cls")
    print("=================================================================")
    print("=                 ----Welcome to Times Bank----                 =")
    print("=================================================================")
    print("*****************************************************************")
    print(                   "=<< 1. Open a new account                  >>=")
    print(                   "=<< 2. Withdraw Money                      >>=")
    print(                   "=<< 3. Deposit Money                       >>=")
    print(                   "=<< 4. Check Customers & Balance           >>=")
    print(                   "=<< 5. transactionHistory                  >>=")
    print(                   "=<< 6. Exit/Quit                           >>=")
    print("*****************************************************************")
    # The below statement takes the choice number from the user.
    choiceNumber = input("Select your choice number from the above menu : ")
    if choiceNumber == "1":
    # ...
    # Create a new customer account
        name = input("Enter the fullname : ")
        pin = str(input("Please enter a pin of your choice : "))
        deposition = eval(input("Please enter the value of amount to deposit,to start an account : "))
        customer_balances[name] = {'balance': deposition}
        customer_transactions[name] = {'deposit': [], 'withdrawal': []}
        customer_transactions[name]['deposit'].append(deposition)
        print("New account created successfully !")
        print("Your name is avalilable on the customers list now : ")
        print(list(customer_balances.keys()))
        print("Note! Please remember the Name and Pin")
        print("========================================")

    elif choiceNumber == "2":
    # ...
    # Withdraw money from an existing account
        name = input("Please input name : ")
        pin = input("Please input pin : ")
        if name in customer_balances and pin == customerPins[customerNames.index(name)]:
            balance = customer_balances[name]['balance']
            withdrawal = eval(input("Input value to Withdraw : "))
            if withdrawal > balance:
                deposition = eval(input("Please Deposit a higher Value because your Balance mentioned above is not enough : "))
                balance += deposition
                customer_balances[name]['balance'] = balance
                customer_transactions[name]['deposit'].append(deposition)
                balance -= withdrawal
                customer_transactions[name]['withdrawal'].append(withdrawal)
                customer_balances[name]['balance'] = balance
                print("Withdraw Successfull!")
                print("Your New Balance: ", balance, "-/Rs")
            else:
                balance -= withdrawal
                customer_transactions[name]['withdrawal'].append(withdrawal)
                customer_balances[name]['balance'] = balance
                print("Withdraw Successfull!")
                print("Your New Balance: ", balance, "-/Rs")
        else:
            print("Your name and pin does not match!")
    elif choiceNumber == "3":
        # ...
    # Deposit money into an existing account
        name = input("Please input name : ")
        pin = input("Please input pin : ")
        if name in customer_balances and pin == customerPins[customerNames.index(name)]:
            balance = customer_balances[name]['balance']
            deposition = eval(input("Enter the value you want to deposit : "))
            balance += deposition
            customer_transactions[name]['deposit'].append(deposition)
            customer_balances[name]['balance'] = balance
            print("Deposition successful!")
            print("Your New Balance: ", balance, "-/Rs")
        else:
            print("Your name and pin does not match!")
    elif choiceNumber == "4":
        print("Choice number 4 is selected by the customer")
        k = 0
        print("Customer name list and balances mentioned below : ")
        print("\n")
        # The while loop below will keeping running until all the customers and balances are shown.
        while k <= len(customerNames) - 1:
            print("->.Customer =", customerNames[k])
            print("->.Balance =", customerBalances[k], end=" ")
            print("-/Rs")
            print("\n")
            k = k + 1
                # This statement below helps the user to go back to the start of the program (main menu).
            mainMenu = input("Please press enter key to go back to main menu to perform another fuction or exit ...")
    elif choiceNumber == "5":
        for transaction in transactionHistory:
            customerName = transaction["customerName"]
            amount = transaction["amount"]
            transactionType = transaction["transactionType"]
            print(f"{customerName} {transactionType} Rs. {abs(amount)}")
    elif choiceNumber == "6":
         # These statements would be just showed to the customer.
        print("Choice number 5 is selected by the customer")
        print("Thank you for using our banking system!")
        print("\n")
        print("Visit Again")
    elif choiceNumber == "6":
        for transaction in transactionHistory:
            customerName = transaction["customerName"]
            amount = transaction["amount"]
            transactionType = transaction["transactionType"]
            print(f"{customerName} {transactionType} Rs. {abs(amount)}")
        break
    else:
        # This else function above would work when a wrong function is chosen.
        print("Invalid option selected by the customer")
        print("Please Try again!")
        # This statement below helps the user to go back to the start of the program (main menu).
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
