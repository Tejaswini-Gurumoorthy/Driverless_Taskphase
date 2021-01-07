import pandas as pd
rep=0
fields=['Name','Admission number','Roll number','Class','Science marks','Maths marks','Sst marks','English marks']
def menu():
    print('1. Add new student data : ')
    print('2.Display marksheet : ')
    print('3.Compute ranks : ')
    print('4.Merit students : ')
    print('5.Exit : ')
def new():
    global fields
    global rep
    data=[]
    for i in fields:
        val=input('Enter '+ i + ': ')
        data.append(val)
    if rep==0:
        df=pd.DataFrame([[data[i] for i in range(len(data))]],columns=['Name','Admission Number','Roll Number','Class','Science Marks','Maths Marks','SST Marks','English Marks'])
        df.to_csv('student_data.csv',mode='a',index=False)
    else:
        df=pd.DataFrame([[data[i] for i in range(len(data))]],columns=['Name','Admission Number','Roll Number','Class','Science Marks','Maths Marks','SST Marks','English Marks'])
        df.to_csv('student_data.csv',mode='a',index=False,header=0)
    print('DATA SAVED SUCCESSFULLY')
    input('Press any key to continue')
    return
def display():
    print('Through what would you like to search?')
    print('1.Class')
    print('2.Roll number')
    print('3.Name')
    imp=input('Enter the number : ')
    if imp=='1':
        cl=int(input('Enter the class : '))
        df=pd.read_csv('student_data.csv')
        liclass=[i for i in df["Class"]]
        if cl in liclass:
            x=df.loc[df['Class']==cl]
            print(x)
        else:
            print('DATA NOT FOUND')
            
    elif imp=='2':
        rno=int(input('Enter the Roll number : '))
        df=pd.read_csv('student_data.csv')
        lirno=[i for i in df["Roll Number"]]
        if rno in lirno:
            x=df.loc[df['Roll Number']==rno]
            print(x)
        else:
            print('DATA NOT FOUND')
        
    elif imp=='3':
        nm=input('Enter the name : ')
        df=pd.read_csv('student_data.csv')
        linm=[i for i in df["Name"]]
        if nm in linm:
            x=df.loc[df['Name']==nm]
            print(x)
        else:
            print('DATA NOT FOUND')
    else:
        print('ERROR!!!!! ENTER ONLY 1, 2 OR 3')
    input('Press any key to continue')
    return


def compute_ranks():
    df=pd.read_csv('student_data.csv')
    df['Aggregate Percentage']=((df['Science Marks']+df['Maths Marks']+df['SST Marks']+df['English Marks'])/4)
    df.to_csv('student_data.csv',index=False)
    print(df.sort_values('Aggregate Percentage',ascending=False))
    input('Press any key to continue')
    return


def merit_students():
    df=pd.read_csv('student_data.csv')
    y=df.loc[df['Aggregate Percentage']>=90]
    x=y.sort_values('Aggregate Percentage',ascending=False)
    z=x.tail(len(df['Name']))
    print(z.head(10))
    input('Press any key to continue')
    return

while True:
    menu()
    choice=input('Choose one of the options : ')
    if choice=='1':
        new()
        rep+=1
    elif choice=='2':
        display()
    elif choice=='3':
        compute_ranks()
    elif choice=='4':
        merit_students()
    elif choice=='5':
        break
    else:
        print('ERROR!! PLEASE ENTER ONLY NUMBERS 1 TO 5')
input('PRESS ANY KEY TO CONTINUE')

    

    
    
    
    

    
    
                                                                      
    




    
    

