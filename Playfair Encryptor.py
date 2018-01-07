print("Playfair encryptor 1.0")
print("Please ensure all input is all caps, and has no numbers or spaces.")
key = input("Enter key: ")
plaintext = input("Enter plaintext: ")

keyList=[]

for a in key: #Removing duplicate elements
    if a in keyList:
        pass
    else:
        keyList.append(a)

alphaList=[]
for a in range(65,91):#generating list of cipher alphabet
    if chr(a) not in keyList and chr(a)!='Q':
        alphaList.append(chr(a))
keyAlphaList = keyList + alphaList

keyMatrix = [[0 for i in range(5)]for j in range(5)]

k=0
for i in range(5): #making cipher matrix
    for j in range(5):
        keyMatrix[i][j] = keyAlphaList[k]
        k+=1

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

ciphertextDuos=[]
for currentPair in plaintextDuos:
    ciphertextPair=''
    indexList=[]
    for currentElem in currentPair:
        for i in range(5):
            for j in range(5):
                if keyMatrix[i][j]==currentElem:
                    indexList.extend([i,j])
    if indexList[0]==indexList[2]: #checking to see if samerow/column/not
        indexList[1]+=1
        indexList[3]+=1
    elif indexList[1]==indexList[3]:
        indexList[0]+=1
        indexList[2]+=1
    else:
        indexList[1],indexList[3]=indexList[3],indexList[1]
    for k in range(len(indexList)): #to wrap around
        if indexList[k]>4:
            indexList[k]-=5
    ciphertextPair = keyMatrix[indexList[0]][indexList[1]] + keyMatrix[indexList[2]][indexList[3]]
    ciphertextDuos.append(ciphertextPair)

ciphertext = ''

for a in ciphertextDuos:
	ciphertext+=a

print("Ciphertext:", ciphertext)
    


















