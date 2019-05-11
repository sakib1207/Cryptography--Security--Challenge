#for encrypted and decrypted process follow code and also the comments line
small_letter='abcdefghijklmnopqrstuvwxyz'#REMAIN SAME
capital_letter='ABCDEFGHIJKLMNOPQRSTUVWXYZ'#REMAIN SAME
newmessage=''#REMAIN SAME
newmessage2=''#REMAIN SAME
key=int(input('key value: '))#REMAIN SAME
message=input('Please enter a message for encrypt your message as the value of key: ')#REMAIN SAME
for character in message:
     if character in small_letter:
         position=small_letter.find(character)
         newposition=(position-key) % 26#CHANGE HERE + WILL BE -
         newcharacter=small_letter[newposition] 
         newmessage =newmessage+newcharacter
     elif character in capital_letter:
         position=capital_letter.find(character)
         newposition=(position-key) % 26#CHANGE HERE + WILL BE -
         newcharacter=capital_letter[newposition]
         newmessage =newmessage+newcharacter
     else:
        newmessage =newmessage+character
print('The decrypted message of (',message,'):')
print('')
print(newmessage)
