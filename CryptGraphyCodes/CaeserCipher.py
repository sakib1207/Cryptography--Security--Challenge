small_letter='abcdefghijklmnopqrstuvwxyz'
capital_letter='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
newmessage=''
newmessage2=''
key=int(input('key value: '))
message=input('Please enter a message for encrypt your message as the value of key: ')
for character in message:
     if character in small_letter:
         position=small_letter.find(character)
         newposition=(position-key) % 26
         newcharacter=small_letter[newposition] 
         newmessage =newmessage+newcharacter
     elif character in capital_letter:
         position=capital_letter.find(character)
         newposition=(position-key) % 26
         newcharacter=capital_letter[newposition]
         newmessage =newmessage+newcharacter
     else:
        newmessage =newmessage+character
print('The decrypted message of (',message,'):')
print('')
print(newmessage)
