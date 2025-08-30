import random
import string

def random_letters(n=3):
    return ''.join(random.choices(string.ascii_lowercase , k=n))

def Encode(word):
    if len(word) >=3:
        word = word[1:]+word[0]
        return random_letters()+word+random_letters()
    else:
        return word[::-1]
    
def Decode(word):
    if len(word) >=3:
        word = word[3:-3]
        return word[-1]+word[:-1]
    else:
        return word[::-1]

choice = input("Choose Enco(E) or Decode(D) : ").strip().upper()
sentence = input("Input sentence to decode : ")

word = sentence.split()

if choice == "E":
    secret = [Encode(word) for word in word]
    print("Encoded sentence : " , ' '.join(secret))
elif choice == "D":
    normal = [Decode(word) for word in word]
    print("Decoded sentence : " , ' '.join(normal))
else:
    print("Plese Input E or D")    