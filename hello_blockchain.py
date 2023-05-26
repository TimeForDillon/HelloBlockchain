# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""    

import random

# this is a class for the crypto degen that has a wallet addr, ada amount, name, and seed phrase
class CryptoDegen:
    
    apy = 0.035  # 3.5% APY
    apy_percent = apy * 100
    
    def __init__(self, name, ada_amount):
        self.name = name
        self.ada_amount = ada_amount
        self.seed_phrase = self.create_seedphrase()
        self.wallet_addr = None
        
    def get_name(self):
        return self.name
    
    def get_ada_amount(self):
        return self.ada_amount
    
    # randomly creates a 24 word seedphrase and returns it as a list
    def create_seedphrase(self):
        # Read the BIP39 English wordlist from a local file
        # word list: https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt
        # download as txt file and store in same folder as python script
        with open('english.txt', 'r') as f:
            words = f.readlines()

        # Select 24 random words from the list
        random_words = []
        while len(random_words) < 24:
            word = random.choice(words).strip()
            if word not in random_words:
                random_words.append(word)
                
        return random_words
    
    def get_seed_phrase(self):
        return self.seed_phrase
    
    # a function that takes in ada as input in a wallet and outputs the new ada value after stake reward
    def calculate_return_per_epoch(self):

        epoch_length = 5  # in days

        # Calculate the daily interest rate
        daily_rate = (1 + CryptoDegen.apy) ** (1/365) - 1

        # Calculate the return per epoch
        return_per_epoch = self.ada_amount * (1 + daily_rate) ** epoch_length - self.ada_amount

        return return_per_epoch
    
    def get_annual_stake_rewards(self):
        # adding the stake rewards
        i = 0
        ada_amount_after_staking_for_one_year = self.ada_amount
        while i < 73:
            ada_amount_after_staking_for_one_year += self.calculate_return_per_epoch()
            i += 1
            
        return ada_amount_after_staking_for_one_year
    
    def get_apy_percentage(self):
        return CryptoDegen.apy_percent
        
    def __str__(self):
        print("Crypto Degen Name: " + self.name + ", Ada Amount: " + self.ada_amount)

# takes user input for a name and returns it back to the main function
def take_username_as_input():
    while True:
        name = input("Please enter your name for wallet1: ")
        if name.isalpha():
            return name
        else:
            print("Invalid input. Please enter a valid name with letters only.")
        
# takes user input for wallet balance and returns it back to the main function
def take_wallet_balance_as_input():
    while True:
        try:
            wallet = float(input("Please enter the amount of ADA you have: "))
            return wallet
        except ValueError:
            print("Invalid input. Please enter a valid number.")  

def main():
    # your program logic goes here
    print("Hello, Blockchain!")
    
    # take name1 input:
    # take wallet1 input:
    # create a crypto degen object with the name1 and ada_amount1:
        
    Charles = CryptoDegen(take_username_as_input(), take_wallet_balance_as_input())

    # take name2 input:
    # take wallet2 input:
    # create a crypto degen object with the name1 and ada_amount1:
        
    TimeForDillon = CryptoDegen(take_username_as_input(), take_wallet_balance_as_input())

    # print out names and wallets
    print(Charles.get_name() + " has " + str(Charles.get_ada_amount()) + " ADA.")
    print(Charles.get_name() + "'s seed phrase is: " + str(Charles.get_seed_phrase()))
    print(TimeForDillon.get_name() + " has " + str(TimeForDillon.get_ada_amount()) + " ADA.")
    print(TimeForDillon.get_name() + "'s seed phrase is: "+ str(TimeForDillon.get_seed_phrase()))

    # print out names and wallets after stake rewards have been applied
    
    formatted_string1 = f"{Charles.get_name()} has {Charles.get_annual_stake_rewards():.2f} ADA after staking for 1 year at {Charles.get_apy_percentage():.2f}% APY."
    print(formatted_string1)
    formatted_string2 = f"{TimeForDillon.get_name()} has {TimeForDillon.get_annual_stake_rewards():.2f} ADA after staking for 1 year at {TimeForDillon.get_apy_percentage():.2f}% APY."
    print(formatted_string2)

    # we are outputting the wallet with more ada in it.d
    if Charles.get_ada_amount() > TimeForDillon.get_ada_amount():
        print(Charles.get_name() + " has more ADA than " + TimeForDillon.get_name())
    elif Charles.get_ada_amount() == TimeForDillon.get_ada_amount():
        print(Charles.get_name() + " and " + TimeForDillon.get_name() + " have the same amount of ADA: " + str(Charles.get_ada_amount()) + "!")
    else: 
        print(Charles.get_name() + " has more ADA than " + TimeForDillon.get_name())

# call the main function to execute your program
if __name__ == '__main__':
    main()



    