alpha="abcdefghijklmnopqrstuvwxyz"
newmessage=''
msg=input("Enter your message: ")
key=int(input("Enter a key for your message: "))
for char in msg:
  if char in alpha:
    pos=alpha.find(char)
    newpos=(pos+key)%26
    newchar=alpha[newpos]
    newmessage+=newchar
  else:
    newmessage+=char
print("The encrypted message is: %s"%newmessage)
