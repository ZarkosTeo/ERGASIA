ext_file = open("readmeee.txt","r")
sentence =  text_file.read()
words = sentence.split()

long_one = 1
for i in words :
    word_length=len(i)
        
    if word_length >long_one:
                long_one = word_length
                bwords1=i
                a=len(i)
                
long_two = 1
for j in words :
    word_length=len(j)
        
    if word_length >long_two and word_length <=a and bwords1!= j:
                long_two = word_length
                bwords2=j                 
                b=len(j)
long_three = 1
for k in words :
    word_length=len(k)
        
    if word_length >long_three and word_length <=b and bwords2!= k and bwords1!= k  :
                long_three = word_length
                bwords3=k                 
                c=len(k)
        
long_four = 1
for l in words   :
    word_length=len(l)
        
    if word_length >long_four  and word_length <=c and bwords3!= l and bwords2!= l  and bwords1!= l  :
                long_four = word_length
                bwords4=l                 
                d=len(l)
long_five = 1
for g in words :
    word_length=len(g)
        
    if word_length >long_five   and word_length <=d and bwords4!= g and bwords3!= g  and bwords2!= g and bwords1!= g                                                                         :
                long_five = word_length
                bwords5=g                 


VOWELS=("a","e","i","o","u","A","E","I","O","U")
msg=bwords1[::-1]+"  "+ bwords2[::-1]+ "  "  +bwords3[::-1]+"  "+bwords4[::-1]+"  "+bwords5[::-1]

n_msg=""
for letter in msg:
    if letter not in VOWELS:
        n_msg+=letter
        


    

print(n_msg)


text_file.close()