# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""    

import random

# this is a class for the crypto degen that has a wallet addr, ada amount, name, and seed phrase
class CryptoDegen:
    
    apy = 0.032  # 3.2% APY
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
            f.close()
        # Select 24 random words from the list
        random_words = []
        while len(random_words) < 24:
            word = random.choice(words).strip()
            if word not in random_words:
                random_words.append(word)
                
        return random_words
    
    # this will save the created seed pharses in a new txt.file
    def save_seedphrases(self):
        with open("seeds.txt", "a") as f:
            f.write("\n".join(self.seed_phrase) + "\n")
    
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
        
    def check_seed_phrase(self, word, index):
        entered_word = word.strip().lower()
        seed_word = self.seed_phrase[index].strip().lower()
    
        print("Entered word:", entered_word)
        print("Seed phrase word:", seed_word)
    
        if seed_word == entered_word:
            return True
        else:
            return False
        
    def send_ada(self, other, amount):
        if (amount > self.ada_amount):
            print("insufficient funds...")
        else:
            #check seed phrase
            index = random.randint(0, 23)
            input_word = input("Please enter word #" + str(index) + " in your seed phrase to confirm transaction: ")
            if self.check_seed_phrase(input_word, index):
                #if seed is good send ada
                self.ada_amount -= amount;
                other.ada_amount += amount;
            else:
                #if seed is bad output
                print("Seed phrase did not match...")
        

# takes user input for a name and returns it back to the main function
def take_username_as_input():
    while True:
        try:
            name = input("Please enter your name for your wallet: ")
            if name.isalpha():
                return name
            else:
                raise ValueError("Invalid name. Please enter a valid name with letters only.")
        except ValueError as e:
            print(e)
        
# takes user input for wallet balance and returns it back to the main function
def take_wallet_balance_as_input():
    while True:
        try:
            wallet = float(input("Please enter the amount of ADA you have: "))
            return wallet
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("Hello, Blockchain!")
    
    try:
        name1 = take_username_as_input()
        ada_amount1 = take_wallet_balance_as_input()
        Wallet1 = CryptoDegen(name1, ada_amount1)

        name2 = take_username_as_input()
        ada_amount2 = take_wallet_balance_as_input()
        Wallet2 = CryptoDegen(name2, ada_amount2)
        
        print(Wallet1.get_name() + " has " + str(Wallet1.get_ada_amount()) + " ADA.")
        print(Wallet1.get_name() + "'s seed phrase is: " + str(Wallet1.get_seed_phrase()))
        Wallet1.save_seedphrases()
        print(Wallet2.get_name() + " has " + str(Wallet2.get_ada_amount()) + " ADA.")
        print(Wallet2.get_name() + "'s seed phrase is: "+ str(Wallet2.get_seed_phrase()))
        Wallet2.save_seedphrases()

        ans = input("Do you want to send ada? (y/n)")
        if ans == "y":
            try:
                amount_to_send = float(input("How much ada would you like to send? "))
                Wallet1.send_ada(Wallet2, amount_to_send)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    
        print(Wallet1.get_name() + " has " + str(Wallet1.get_ada_amount()) + " ADA.")
        print(Wallet2.get_name() + " has " + str(Wallet2.get_ada_amount()) + " ADA.")
        
        formatted_string1 = f"{Wallet1.get_name()} has {Wallet1.get_annual_stake_rewards():.2f} ADA after staking for 1 year at {Wallet1.get_apy_percentage():.2f}% APY."
        print(formatted_string1)
        formatted_string2 = f"{Wallet2.get_name()} has {Wallet2.get_annual_stake_rewards():.2f} ADA after staking for 1 year at {Wallet2.get_apy_percentage():.2f}% APY."
        print(formatted_string2)

        if Wallet1.get_ada_amount() > Wallet2.get_ada_amount():
            print(Wallet1.get_name() + " has more ADA than " + Wallet2.get_name())
        elif Wallet1.get_ada_amount() == Wallet2.get_ada_amount():
            print(Wallet1.get_name() + " and " + Wallet2.get_name() + " have the same amount of ADA: " + str(Wallet1.get_ada_amount()) + "!")
        else: 
            print(Wallet2.get_name() + " has more ADA than " + Wallet1.get_name())
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == '__main__':
    main()


    