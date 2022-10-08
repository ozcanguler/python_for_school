
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt():   
    before_text=[]
    after_text=[]
    bbbbb=""
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    while(not direction=="encode" and not direction=="decode"):
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if(direction=="encode"):

        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        for i in text:
            for k in range(0,len(alphabet)):
                #if(k not in alphabet):
                    #before_text.append(k)               
                if(i==alphabet[k]):
                    if(k+shift>25):
                        before_text.append(alphabet[k+shift-25])
                    else:    
                        before_text.append(alphabet[k+shift])
            if(i not in alphabet):
                before_text.append(i)               

        print(before_text)
        #for i in before_text:
        #    after_text.append(alphabet[i])
        #print(after_text)
        for i in before_text:
            bbbbb+=i
        print(bbbbb)
        direction_repeat = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")
        while(not direction_repeat=="yes" and not direction_repeat=="no"):
            direction_repeat = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")
        if(direction_repeat=="yes"):
            encrypt()
        if(direction_repeat=="no"):
            print("GoodBye!")
    if(direction=="decode"):
         text = input("Type your message:\n").lower()
         shift = int(input("Type the shift number:\n"))
    for i in text:
        for k in range(0,len(alphabet)):
            #if(k not in alphabet):
                #before_text.append(k)
            if(shift>25):
               shift=shift%26                
            if(i==alphabet[k]):
                if(k-shift>25):
                    before_text.append(alphabet[k-shift-25])
                else:    
                    before_text.append(alphabet[k-shift])
        if(i not in alphabet):
            before_text.append(i)               

    print(before_text)
    #for i in before_text:
    #    after_text.append(alphabet[i])
    #print(after_text)
    for i in before_text:
        bbbbb+=i
    print(bbbbb)
    direction_repeat = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")
    if(direction_repeat=="yes"):
        encrypt()
    if(direction_repeat=="no"):
        print("GoodBye!")                   
encrypt()

'''
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt():   
    before_text=[]
    after_text=[]
    bbbbb=""
    #direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = "qnuux fxaum!" #input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    for i in text:
        for k in range(0,len(alphabet)):
            #if(k not in alphabet):
                #before_text.append(k)
            if(shift>25):
               shift=shift%26                
            if(i==alphabet[k]):
                if(k-shift>25):
                    before_text.append(alphabet[k-shift-25])
                else:    
                    before_text.append(alphabet[k-shift])
        if(i not in alphabet):
            before_text.append(i)               

    print(before_text)
    #for i in before_text:
    #    after_text.append(alphabet[i])
    #print(after_text)
    for i in before_text:
        bbbbb+=i
    print(bbbbb)
encrypt()  
'''                    
              
