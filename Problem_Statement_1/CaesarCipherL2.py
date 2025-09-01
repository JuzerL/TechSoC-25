from langdetect import detect_langs


def decode(message, shift):
    mlist =[]
    for i in range(len(message)):
        if message[i].isalpha():
            o = ord(message[i].lower())
            n = (o-97-shift)%26+97
            new_chr = chr(n)
            if message[i].isupper():
                new_chr = new_chr.upper()
            mlist.append(new_chr)
        else:
            mlist.append(message[i])
    demessage = "".join(mlist)
    return demessage

def accuracy(text):
    languages = detect_langs(text)
    englishl = None
    for l in languages:
        accuracy = 0
        if l.lang == "en":
            englishl = l
            accuracy = englishl.prob
    return accuracy


message = input("Write your encoded message: ")
trial = []
for i in range(0,26):
    trial.append(decode(message, i))
final_message = trial[0]
t = accuracy(trial[0])
for i in range(0,26):
    if accuracy(trial[i])>t:
        t = accuracy(trial[i])
        final_message = trial[i]
print(final_message)