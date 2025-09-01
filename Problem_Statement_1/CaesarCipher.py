def encode():
    message = input("Write your message: ")
    mlist =[]
    for i in range(len(message)):
        if message[i].isalpha():
            o = ord(message[i].lower())
            n = (o-96)%26+99
            new_chr = chr(n)
            if message[i].isupper():
                new_chr = new_chr.upper()
            mlist.append(new_chr)
        else:
            mlist.append(message[i])
    enmessage = "".join(mlist)
    print(enmessage)
    return enmessage

def decode():
    message = input("Write your message: ")
    mlist =[]
    for i in range(len(message)):
        if message[i].isalpha():
            o = ord(message[i].lower())
            n = (o-99)%26+96
            new_chr = chr(n)
            if message[i].isupper():
                new_chr = new_chr.upper()
            mlist.append(new_chr)
        else:
            mlist.append(message[i])
    demessage = "".join(mlist)
    print(demessage)
    return demessage

ask = input("Decode or Encode? ")
if ask=="Decode":
    decode()
elif ask=="Encode":
    encode()
else:
    print("Invalid!")

    
     