import tabula
import csv
import os
import collections


def headerline():
    header=[]
    list1=[]
    for i in range(6):
        for j in range(len(data2[i])):
            word=data2[i][j].split(':')
            header.append(word[0])

    list1 = ['Old', 'New', 'Old', 'New']
    if collections.Counter(list1) == collections.Counter(data2[8]):    
        data2[7].pop(1)
        data2[7].pop(4)
        data2[7][1:1]=['old Meter Reading Date', 'new Meter Reading Date']
        data2[7][6:6]=['old Meter Reading', 'new Meter Reading']
        header=header+(data2[7])
    elif collections.Counter(list1) == collections.Counter(data2[7]):
        data2[8].pop(1)
        data2[8].pop(4)
        data2[8][1:1]=['old Meter Reading Date', 'new Meter Reading Date']
        data2[8][6:6]=['old Meter Reading', 'new Meter Reading']
        header=header+(data2[8])

    try:
        second_row
    except NameError:
            print("Second_Row")
 #   else:

    second_row1=['2nd row ' + s  for s in data2[7]]
    header=header+second_row1

    #Details of Charges for Current Cycle

    for i in range(30,54):
        if i in [36,38, 40, 42, 44, 46, 48, 51]:
            continue;
        print(data2[i][0])
        header.append(data2[i][0])

#Details of Amount Payable    
    for i in range(30,44):
        if i in [36,38, 39, 40, 42]:
            continue;
        try:
            print(data2[i][2])
            header.append(data2[i][2])
        except IndexError:
            header.append("NA")
            print('sorry, no 1')
        
        
#Last Payment Details

    for i in range(29,33):
        print(data2[i][4])
        header.append(data2[i][4])

#Arrears Outstanding for the Financial Year (`)
        
    for i in range(13,23):
        if i in [14, 17]:
            continue;
        print(data2[i][0])
        header.append(data2[i][0])
        
    for i in range(11,23):
        if i in [12, 14, 17]:
            continue;
        print(data2[i][4])
        header.append(data2[i][4])

    resultt=['Slab Calculation ' + s  for s in data2[24]]
    header=header+(resultt)
    header.append(data2[64][0])

    for i in range(1,6):
        resultt1=['older month ' + str(i) + ' ' + s  for s in data2[55]]
        header=header+(resultt1)
    return header


# Now the value extraction function starts

def values():
    values=[]
    for i in range(6):
        for j in range(len(data2[i])):
            word=data2[i][j].split(':')
            values.append(word[1])
        #    print(word[0])

    values=values+data2[9]
    row2=[]
    try:
        second_value
    except NameError:
        print("Second_Value")
    else:
        values=values+second_value
           
#Details of Charges for Current Cycle

    for i in range(30,54):
        if i in [36,38, 40, 42, 44, 46, 48, 51]:
            continue;
        try:
            print(data2[i][1])
            values.append(data2[i][1])
        except IndexError:
            values.append("NA")
            print('sorry, no 1')
        

#Details of Amount Payable    
    for i in range(30,44):
        if i in [36,38, 39, 40, 42 ]:
            continue;
        print(data2[i][3])
        values.append(data2[i][3])

#Last Payment Details
    for i in range(29,33):
        try:
            print(data2[i][5])
            values.append(data2[i][5])
        except IndexError:
            values.append("NA")
            print('sorry, no 5')

#Arrears Outstanding for the Financial Year (`)
    for i in range(13,23):
        if i in [14, 17]:
            continue;
        try:
            print(data2[i][0], data2[i][3])
            values.append(data2[i][3])
        except IndexError:
            values.append("NA")
            print('sorry, no index')
    for i in range(11,23):
        if i in [12, 14, 17]:
            continue;
        try:
            print(data2[i][5])
            values.append(data2[i][5])
        except IndexError:
           values.append("NA")
           print('sorry, no index')

    values=values+data2[25]
    try:
        values.append(data2[64][1])
    except IndexError:
        values.append("NA")
        print('sorry, no index')

    old_bill_end="""In case of bill is not paid within 7 days of due date the supply
shall be liable to be disconnected without any further notice."""
    for i in range(56,61):
        if data2[i]==old_bill_end:
            break;
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(data2[i])
        values=values+data2[i]
    
    return values



val=[]
head=[]
res=[]
cwd=os.getcwd()
z=0

for filename in os.listdir("input"):
    if filename.endswith(".pdf"):
        df = os.path.join("input", filename)
        output = "test1.csv"
        #tabula.convert_into(df, output, output_format="csv", stream=True)
        tabula.convert_into(df, output, output_format="csv", lattice=True)

        with open('test1.csv', newline='') as f:
            reader = csv.reader(f)
            data = list(reader)


        #print(data)
        #print(data.index("Thousand"))
        data2=[]
        for i in data:
            str_list=i
            data1=[x for x in str_list if x != '']
            data2.append(data1)


        data2=[x for x in data2 if x != []]
        print(len(data2[0]))

        subs='Arrears Outstanding for the Financial Year'
        reading_repeat=[i for i in data2[11] if subs in i]
        if reading_repeat:
            second_row=['2nd row ' + s  for s in data2[8]]
            second_value=data2[10]
            data2.pop(10)
        else:
            second_value=[]
            for i in data2[9]:
                print("keshav")
                print(i)
                second_value.append('NA')

  
        for i in data2:
            print(i)
        if z==0:
            head=headerline()
            res.append(head)
            z=z+1

        val=values()
        print(head)
        print(val)
        res.append(val)

print("*********************************************************************")
print(res)
        
with open('demo2.csv', 'w', newline='\n') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     wr.writerows(res)
