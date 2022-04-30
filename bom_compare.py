import csv 

def selectBom(bom1, bom2):
    old_bom = []
    new_bom = []
    # bom1 = input("Enter Old Revison of BOM file name: ")
    # bom2 = input("Enter New Revison of BOM file name: ")
    with open(bom1, 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            old_bom.append(row)
    with open(bom2, 'r') as file:
        csvreader1 = csv.reader(file)
        header1 = next(csvreader1)
        for row1 in csvreader1:
            new_bom.append(row1)
    return old_bom, new_bom

def descChange(old_bom,new_bom):
    descChanges = []
    print("--------------DESCRIPTION CHANGES-----------------")
    #checks for description changes
    for i in range(len(old_bom)):
        for n in range(len(new_bom)):
            if old_bom[i][0] == new_bom[n][0]:
                # print("on both boms: ",old_bom[i][0])
                if old_bom[i][1] == new_bom[n][1]:
                    continue
                else:
                    print('in else loop')
                    print("Desciption needs to be revised: ", old_bom[i][0], old_bom[i][1], "to", new_bom[n][0], new_bom[n][1])
                    descChanges.append('hello')
                    print(descChanges)
    return descChanges

            
def qtyChange(old_bom,new_bom):
    print("--------------QTY CHANGES-----------------")
    #checks for QTY changes
    for i in range(len(old_bom)):
        for n in range(len(new_bom)):
            if old_bom[i][0] == new_bom[n][0]:
                if old_bom[i][2] == new_bom[n][2]:
                    continue
                else:
                    print("QTY changed from: ", old_bom[i][0], old_bom[i][2], "to", new_bom[n][0], new_bom[n][2])

def revChange(old_bom,new_bom):
    revChanges = []
    print("-------------REV CHANGES------------------")
    #checks for rev changes
    for i in range(len(old_bom)):
        for n in range(len(new_bom)):
            if old_bom[i][0] == new_bom[n][0]:
                if old_bom[i][3] == new_bom[n][3]:
                    continue
                        # print("no change to these components: ", old_bom[i])
                else:
                    ob = old_bom[i][0]
                    ob2 = old_bom[i][3]
                    nb = new_bom[n][0]
                    nb2 = new_bom[n][3]
                    print("REV changed from: ", old_bom[i][0], old_bom[i][3], "to", new_bom[n][0], new_bom[n][3])
                    revlist = "REV changed from: ", old_bom[i][0], old_bom[i][3], "to", new_bom[n][0], new_bom[n][3]
                    revChanges.append(revlist)
    #                 res = f"REV changed from:  {ob} {ob2} to {nb} {nb2}" 
    #                 mylist.append(res)
    return revChanges
            
            
            # for x in range(len(old_bom)):
            #     print(x)
            #     for y in range(len(new_bom)):
            #         print(y)

def removeParts(old_bom,new_bom):
    print("--------------PARTS REMOVED-----------------")
    #checks for removed parts
    counter = 0
    for i in range(len(old_bom)):
        for n in range(len(new_bom)):
            if old_bom[i][0] == new_bom[n][0]:
                counter += 1
        if counter == 0:
            print("Removed PART: ", old_bom[i])
        counter = 0

def addParts(old_bom,new_bom):
    print("------------PARTS ADDED-------------------")
    # checks for added parts
    counter1 = 0
    for i in range(len(new_bom)):
        for n in range(len(old_bom)):
            if new_bom[i][0] == old_bom[n][0]:
                counter1 += 1
        if counter1 == 0:
            print("Added PART: ", new_bom[i])
            print(i, n)
        counter1 = 0