key = 'PLAYFAIR'
plaintext = 'HELLOWORLD'

keyList=[]

for a in key: #Removing duplicate elements
    if a in keyList:
        pass
    else:
        keyList.append(a)

alphaList=[]
for a in range(65,91):#generating list of cipher alphabet
    if chr(a) not in keyList and chr(a)!='X':
        alphaList.append(chr(a))
keyAlphaList = keyList + alphaList

keyMatrix = [[0 for i in range(5)]for j in range(5)]

k=0
for i in range(5): #making cipher matrix
    for j in range(5):
        keyMatrix[i][j] = keyAlphaList[k]
        k+=1
for i in range(5):
    for j in range(5):
        print(keyMatrix[i][j], end='')
    print()

plaintextList = []

for i in range(len(plaintext)): #turn into list with x's
    if i>0:
        if plaintext[i]==plaintext[i-1]:
            plaintextList.append("X")
    plaintextList.append(plaintext[i])
    
if len(plaintextList)%2!=0:
    plaintextList.append("X")

k=0
a=''
plaintextDuos = [] #Creating list of pairs
for i in plaintextList:
    if k==2:
        plaintextDuos.append(a)
        a=''
        k=0
    a+=i
    k+=1
plaintextDuos.append(a)




















