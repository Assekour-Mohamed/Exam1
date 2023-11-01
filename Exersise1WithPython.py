def souTableau(OldTable, indece1,indece2):
    for i in OldTable:
        if i == indece1:
            NewTableSize=indece2 - indece1
            NewTable =[]
            for j in range(NewTableSize):
                NewTable.append(OldTable[i])
                i+=1
            return NewTable
 
def AskUser(Message):
    ansewr = input(Message)
    return ansewr== "y" or ansewr=="Y"
#########################

while(True):
    Table = []
    for i in range(10):
        Table.append(input("entrer l element ",i+1))


    indece1 = int(input("entre le 1er indece: "))
    indece2 = int(input("entre le 2eme indece: "))

    while (indece1<0 or indece1>9 ) or (indece2<1 or indece2>9 or indece2 <= indece1 ):
        print("invalid input try again!!")
        indece1 = int(input("entre le 1er indece: "))
        indece2 = int(input("entre le 2eme indece: "))

    print("the new table between [",indece1,",",indece2,"] is ")
    print(souTableau(Table,indece1,indece2))
    
    if AskUser("tu veux sortie le program? (y/Y ou n/N) pour remlire an nauveau list press n/N  "):
        break






