import sha3

def printElemHash(elem):
    print("\"",elem,"\"", " => ","\"", sha3.hash(elem),"\"")

#Vérification des sorties si elles sont bien de bonnes chaines de caractères 
testList=["","dfe","ap","on aime le cheval","abcdefghijklmno12pqrstuvwxyz","ABCDEF14GHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789","jaimelasaucisse""12345678901234567890123456789012345678901234567890123456789012345678901234567890"]

for elemStr in testList :
    printElemHash(elemStr)


