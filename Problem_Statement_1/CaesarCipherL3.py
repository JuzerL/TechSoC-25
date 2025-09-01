def encode(m, k):
    keylist = []
    for char in k:
        keylist.append(ord(char.upper())-64)
    print (keylist)
    t = 0
    messagelist = []
    base = None
    for item in m:
        if item.isalpha():
            if item.isupper():
                base = 64
            else:
                base = 96
            newchar = chr((ord(item)+keylist[t]-base)%26 + base)
            if t==len(keylist)-1:
                t=0
            else:
                t+=1
        else:
            newchar = item
        messagelist.append(newchar)
    final_message = "".join(messagelist)
    return final_message

def decode(m, k):
    keylist = []
    for char in k:
        keylist.append(ord(char.upper())-64)
    t = 0
    messagelist = []
    base = None
    for item in m:
        if item.isalpha():
            if item.isupper():
                base = 64
            else:
                base = 96
            newchar = chr((ord(item)-keylist[t]-base)%26 + base)
            if t==len(keylist)-1:
                t=0
            else:
                t+=1
        else:
            newchar = item
        messagelist.append(newchar)
    final_message = "".join(messagelist)
    return final_message

keyword = input("Keyword: ")
message = input("Write your message: ")
action = input("Decode or Encode?")
if action=="Encode":
    result = encode(message, keyword)
    print(result)
elif action=="Decode":
    result = decode(message, keyword)
    print(result)
else:
    print('Invalid Request!')

