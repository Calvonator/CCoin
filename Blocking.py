import os, time, json
from hashlib import sha256
from datetime import datetime


def shaHash(toBeHashed):
    
    hashObj = sha256()
    jsonStr = json.dumps(toBeHashed)
    hashObj.update(jsonStr.encode())
    hashStr = hashObj.hexdigest()
    return hashStr


def Nonce(blockDict):
    nonce = 0
    print("Calculating Nonce Number")
    while nonce <= 50000:
        nonceCount = 0
        blockDict['Nonce'] = nonce
        hashOfBlockStr = shaHash(blockDict)

        for x in hashOfBlockStr:
            
            if x == '0':
                
                nonceCount = nonceCount + 1

        if nonceCount == 14:
            print("Nonce number found!")
            return

        nonceCount = 0

        nonce = nonce + 1
    print("No nonce found, using default 50,000")
    return 



def Block(index, blockChain, transData="first block"):

    if index == 0:
        if os.path.isdir("blockchain/") == False:
            try:
                print("Creating blockchain directory/file")
                os.mkdir("blockchain/")
                with open("blockchain/blockchain.txt", "w") as f:
                    pass
            except FileExistsError:
                print("Blockchain directory already exists")
                pass
        print("Creating first block")
        print("Hashing First Block")
        firstHash = shaHash("first block")
        now = datetime.now()
        timeStamp = now.strftime("%d/%m/%Y %H:%M:%S")
        
        firstBlock = {
            "Index": index,
            "Data": transData,
            "Timestamp": timeStamp,
            "PreviousHash": firstHash
        }
        
        blockChain.append(firstBlock.copy())
        jsonString = json.dumps(blockChain, indent=4)
        jsonString = json.loads(jsonString)
        with open("blockchain/blockchain.txt", "w") as f:
            json.dump(jsonString, f, indent=4)    
        
        return 
    else:
        print("\nCreating block from new transaction data")
        print("Hashing previous block in blockchain")
        prevHash = shaHash(blockChain[len(blockChain) - 1])
        
        block = {
            "Index": index,
            "Data": transData,
            "PreviousHash": prevHash,
            "Nonce": 0
        }
        Nonce(block)
        blockChain.append(block)
        jsonString = json.dumps(blockChain, indent=4)
        jsonString = json.loads(jsonString)
        with open("blockchain/blockchain.txt", "w") as f:
            json.dump(jsonString, f, indent=4)
    
 
def watchDir(path):

    print("Listening for new transactions")
    print("--------------------------------------------------------")
    path = "transactions/"

    #Create dict with the files currently in directory
    
    
    while os.path.isdir("transactions/") == False:
        time.sleep(1)

    pathBefore = ([(f, None) for f in os.listdir(path)])
    
    while True:
        
        
        #Creates another dict with the current files in directory
        current = ([(f, None) for f in os.listdir(path)])
        
        #Creates another dict but only places items in it if those items occur in current but not in pathBefore
        added = [f for f in current if not f in pathBefore]
        
        if added:
            print("Directory has Changed")
            return added[0][0]
            
        pathBefore = current

def verifyBlockChain(chain):    
    prevHash = 0
    if len(chain) > 2:
        for x in range(2, len(chain)):
            
            prevHash = shaHash(chain[x-1])
            
            if chain[x]["PreviousHash"] !=  prevHash:
                print("Block " + str(x) + " hash incorrect")
                return False
        print("All Previous Block Hashes Verified")
        return True

    else:
        print("Not enough blocks to verify\n")
        return True
        
blockChain = [] 
try:
    with open("blockchain/blockchain.txt", "r") as f:
        print("\nCurrent blockchain Data Read In\n")
        blockChain = json.load(f)

except FileNotFoundError:
    Block(0, blockChain)


watchPath = "transactions/"
while True:
    print("--------------------------------------------------------")
    
    verifyBlockChain(blockChain)
    newTrans = watchDir(watchPath)
    
    print("New Transaction Detected!\n")
    print(newTrans)
    
    newTransDir = "transactions/" + newTrans
    
    print("Reading new transaction...\n")
    with open(newTransDir, "r") as f:
        newTransData = json.load(f) 

    newTrans = json.dumps(newTransData)
    newTrans = json.loads(newTrans)
    
    print("New Transaction: ")
    print(newTrans)
    
    Block(len(blockChain), blockChain, newTrans)
    
