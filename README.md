# CCoin
Cryptographic Concepts Unit Assignment to create a blockchain system. 

The current program is limited in its functionality as it is only meant to meet the requirements of an assessment rubric.

Currerntly, there are two CLI programs - the transaction and blocking program. 
 
# Transaction Recording Program

This program allows a user to enter transactions in the following form 
  Sender:
  Receiver:
  Amount:
A timestamp is recorded for each transaction. The user can enter as many transactions as they like. Once all have been entered, the program packs the transactions into JSON and places this transaction block into a text file in the /transactions folder for the blocking program to work with.


# Blocking Program

While executing, this program waits for new transactions to be generated within the /transactions folder. When a new transaction is found, the program begins the process of adding the transaction block into the blockchain. First checks if a genesis block exists and then forms the block by appending the previous blocks hash (chaining), generating a nonce number (14 zeros anywhere within the hash) and then placing this block into the blockchain. 


