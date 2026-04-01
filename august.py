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

def hash(text):
    h = 11         # seed
    pvals = [17, 29, 13, 37]         # polynomial base values

    for i, ch in enumerate(text):

        p = pvals[i % len(pvals)] # non constant polynomial base

        h = (h * p + ord(ch))  

        h ^= (ord(ch) << (i % 6)) # shifting is done to prevent collisions

        h = (h << 1) & 0xFFFFFFFF   # fixed size hash (32 bits)

    h = "{:08x}".format(h)  # convert to hex string of fixed length (8 characters)

    return h

def sender(plaintext):
    cipher = Augustencrypt(plaintext)

    h = hash(cipher)

    message = cipher + h

    return message

def receiver(message):
    # Last 32 characters = hash
    received_hash = message[-8:] 

    cipher = message[:-8] 

    # Recompute hash
    computed_hash = hash(cipher)

    if computed_hash == received_hash:
        print("Message verified")
        plaintext = Augustdecrypt(cipher)
        print("Decrypted:", plaintext)
    else:
        print("Message tampered")


text = input("Enter a message to send: ")
print("SENDER SIDE")
print("Original message:", text)
msg = sender(text)
print("Sent message:", msg)
print("\nRECEIVER SIDE")
receiver(msg)



