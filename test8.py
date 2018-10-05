#caesar cipher decoder RIGHT SHIFT

decrypt =''
encrypt =''
key = int(input("ENTER THE KEY:- "))
print(key)
encrypt = input("ENTER THE ENCRYPTED MESSAGE:- ")
for i in encrypt:
        if(i.islower()):
                decrypt += chr((ord(i) - 97 - key) % 26 + 97)
        elif(i.isupper()):
                decrypt += chr((ord(i) - 65 - key) % 26 + 65)
        else:
                decrypt +=i
print("DECRYPTED MESSAGE IS:- ")
print(decrypt)
