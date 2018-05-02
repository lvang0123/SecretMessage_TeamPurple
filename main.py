#Kyle - declaring variables
#!/bin/python3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
newMessage = ''

#Dan - prompt user to input message for encryption
message = input('Please enter a message')

print()

#Ben - prompt user to input key to encrypt
key = input('Enter a key(1-26): ')
key = int(key)

print()

#Lia - 
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

#reverse of encrypted message
message = newMessage
myMessage = ''
for character in message:
  if character in alphabet:
    position = alphabet.find(character)
    newPosition = (position - key) % 26
    newCharacter = alphabet[newPosition]
    myMessage += newCharacter
    
print()
    
#outputs decrypted word    
print("Your decrypted message is: ", myMessage)







