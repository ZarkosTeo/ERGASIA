list1=[]

def toAscii (letter):
    
    number=ord(letter)
    a= str(number)
    list1.append(a)
    
    return number
def loopthrough(message):
    for n in message:
        toAscii(n)
def main():
    encode=input("type something:")
    loopthrough(encode)
      
main()
b=len(list1)
c=""
for i in range (0,b):
    c=c+list1[i]
print(c)    
c=int(c)
for i in range(2,c):
    if c % i==0:
        print("not prime")
        break
else:
     print("Prime")