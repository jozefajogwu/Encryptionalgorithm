# My Ethereum Block-Shift Project
# This is a simple encryption script based on Chapter 3

def my_encrypt_function(message, block_number):
    # This will hold the scrambled letters
    encrypted_text = ""
    
    # We loop through every letter one by one
    for letter in message:
        # 1. Turn the letter into a number (A is 65, B is 66, etc.)
        ascii_value = ord(letter)
        
        # 2. Add the block number to shift it
        # This is like Julius Caesar, but we use the blockchain!
        new_value = ascii_value + block_number
        
        # 3. Turn it back into a weird character
        new_letter = chr(new_value)
        
        # 4. Add it to our final string
        encrypted_text = encrypted_text + new_letter
        
    return encrypted_text

def my_decrypt_function(secret_message, block_number):
    # To decrypt, we just do the opposite of encrypting
    decrypted_text = ""
    
    for letter in secret_message:
        ascii_value = ord(letter)
        
        # Subtract the block number to go back to the original
        original_value = ascii_value - block_number
        
        original_letter = chr(original_value)
        decrypted_text = decrypted_text + original_letter
        
    return decrypted_text

# --- How to use my program ---

# Imagine we look at a block explorer and see the block is 10
current_eth_block = 10 
my_secret = "Ethereum is cool"

# Locking the message
locked = my_encrypt_function(my_secret, current_eth_block)
print("Encrypted message: " + locked)

# Unlocking the message
unlocked = my_decrypt_function(locked, current_eth_block)
print("Decrypted message: " + unlocked)