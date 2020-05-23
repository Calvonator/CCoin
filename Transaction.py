import json, string, os

from datetime import datetime
from hashlib import sha256
from pathlib import Path







def transact():
    
    transData = []
    
    while True:
        
        sender = input("Input the sender: ")
        receiver = input("Input the receiver: ")
        amount = input("Input the amount: ")
        
        now = datetime.now()
        timestamp = now.strftime("%d/%m/%Y %H:%M:%S")

        transaction = {
            "From": sender,
            "To": receiver,
            "Amount": amount,
            "Timestamp": timestamp

            }
        transData.append(transaction.copy())
        while True:
            quitChoice = input("Would you like to enter another transaction? Y/N")

            if quitChoice.lower() == "y":
                break
            
            if quitChoice.lower() == "n":
                jsonString = json.dumps(transData)
                jsonString = json.loads(jsonString)
                break
        if quitChoice.lower() == "n":
            break
        elif quitChoice.lower() == 'y':
            continue
        
    transactionDirLen = len(os.listdir("transactions/"))
    lastBlock = transactionDirLen + 1
    
    newBlockName = "transactions/transaction" + str(lastBlock) + ".txt"

    with open(newBlockName, 'w') as f:
        json.dump(jsonString, f, indent=4)
    
    return



if os.path.isdir("transactions/") == False:
    os.mkdir("transactions/")

while True:
    print("Welcome to the transaction recording program")
    print("---------------------------------------------")
    transact()
    while True:   
        quitChoice = input("Would you like to quit the program (Y) or continue inputting transactions (N)?")
        if quitChoice.lower() == "y":
            break
        elif quitChoice.lower() == "n":
            break
    if quitChoice.lower() == "y":
        break



