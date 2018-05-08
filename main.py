#Python Team Project - Secret Message
#This program will prompt the user for a message that will be encrypted. The user will then be asked to enter a key (number) to be used to determine which letters ahead of the letters in the message (user input) will be used. 
#May 1, 2018 - Ben, Dan, Kyle, Lisa, and Lia all worked on this program together during class time.

#Welcomeing the user
print("Welcome to the Secret Message program!")
print()

#Kyle - declaring variables
#!/bin/python3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
newMessage = ''
decryptNo = "no"
decryptYes = "yes"
rerun = "Y"

#Rerunning the program if the user inputs 'Y' at the end of the program
while rerun.lower().upper() != 'N':
  
  #Dan - prompt user to input message for encryption
  while True:
    message = input('Please enter a message in lowercase letters to be encrypted:')
    break
  
  print()
  
  #Ben - prompting the user to input key to encrypt
  while True:
    try:
      key = input('Enter a key(1-26): ')
      key = int(key)
      break
    except ValueError:
      print()
      print("*** ERROR: Not an integer ***")
      print()
  
  print()
  
  #Lia  
  # if the character in the message
  # is in the defined alphabet
  # finds new position based on key
  # returns new character for newMessage
  for character in message:
    if character in alphabet:
      position = alphabet.find(character)
      newPosition = (position + key) % 26
      newCharacter = alphabet[newPosition]
      newMessage += newCharacter
  
    #Lisa 
    else:
      newMessage += character
  
  #outputs encrypted word
  print("Your new message is: ", newMessage)
  print()
  
  #Prompting the user to decrypt the message or leave it alone
  while True:
    print("Would you like to decrypt the message?")
    decrypt = input("Yes or No: ")
    
    if decrypt.lower() == decryptYes:
      break
    elif decrypt.lower() == decryptNo:
      print()
      break
    else:
      print()
      print("*** ERROR: Please enter 'Yes' or 'No' ***")
      print()
  
  #Message will be decrypted if user inputted 'Yes'
  while decrypt.lower() == decryptYes:
    #reverse of encrypted message
    message = newMessage
    oldMessage = ''
    for character in message:
      if character in alphabet:
        position = alphabet.find(character)
        newPosition = (position - key) % 26
        newCharacter = alphabet[newPosition]
        oldMessage += newCharacter
        
      else:
        oldMessage += character
        
    print()
        
    #outputs the decrypted message   
    print("Your decrypted message is:", oldMessage)
    print()
    break
  
  #Prompting the user to rerun the program or end it
  while True: 
    print("Would you like to rerun the program?")
    rerun = input("Enter Y to rerun it or N to end it: ")
    
    if rerun.lower().upper() == "Y":
      newMessage = ''
      oldMessage = ''
      print()
      print('---------------------------------------')
      print()
      break
    elif rerun.lower().upper() == "N":
      print()
      break
    else:
      print()
      print("*** ERROR: Must enter a Y or N ***")
      print()

#Informing the user that the program has ended
print("Thank you for using the Secret Message program!")







