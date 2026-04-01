def Augustencrypt(text):
    result = ""
    key = 1
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) - 65 + key) % 26 + 65)

        # Encrypt lowercase characters
        elif (char.islower()):
            result += chr((ord(char) - 97 + key) % 26 + 97)

        # Non-alphabetic characters remain unchanged
        else:
            result += char

    return result

def Augustdecrypt(text):
    result = ""
    key = 1
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) - 65 - key) % 26 + 65)

        # Encrypt lowercase characters
        elif (char.islower()):
            result += chr((ord(char) - 97 - key) % 26 + 97)

        # Non-alphabetic characters remain unchanged
        else:
            result += char
        
    return result

#check the above function
text = "AUGUSTCIPHER"
ciphertext = Augustencrypt(text)
print ("Cipher: " + ciphertext)
decryptedtext = Augustdecrypt(ciphertext)
print ("Decrypted: " + decryptedtext)