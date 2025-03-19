import mysql.connector

print("""
       =========================================
        Welcome to Nurse Room Management System
       =========================================

""")
mydb=mysql.connector.connect(host="localhost", user="root", passwd="garvit5")
mycursor = mydb.cursor()


mycursor.execute("create database if not exists nurse_management_database")

mycursor.execute("use nurse_management_database")
mycursor.execute("create table if not exists nurse_details(nurseid varchar(10) primary key,nursename varchar(30),nursepno varchar(11),nurseage varchar(3),nursewing varchar(30))")
mycursor.execute("create table if not exists patient_details(patientid varchar(10) primary key,patientname varchar(30),patientpno varchar(11),patientclass varchar(2),patientproblem varchar(20))")
mycursor.execute("create table if not exists inventory(invid varchar(10) primary key,invname varchar(20),quantity varchar(4))")
mydb.commit()

def registeruser_filewrite():
    file=open("user.txt","a+")
    username=input("Please enter your username : ")
    password=input("Please enter your password : ")
    file.write(username+","+password)
    file.write('\n')
    file.close()
    print("\nUser Successfully Registered\n")

def nurse_signin_readfile():
    username=input("Please enter your username : ")
    password=input("Please enter your password : ")
    file=open("user.txt","r")
    output=file.readlines()
    for i in output:
        a=i.split(',')
        if a[0]==username and a[1].strip()==password:
            return True,username
    file.close()
    return False,username

def admin_signin_readfile():
    username=input("Please enter admin username : ")
    password=input("Please enter admin password : ")
    file=open("user.txt","r")
    output=file.readlines()
    for i in output:
        a=i.split(',')
        if a[0]==username and a[1].strip()==password:
            return True,username
    file.close()
    return False,username


while True:
    print("1. Do you want to login as Admin ?")
    print("2. Do you want to login as Nurse ?")
    choice=int(input("\nWhat do you want to choose : "))

    if choice==1:
        output,username=admin_signin_readfile()
        if output==True:
            print('\nWelcome',username,'to the Nurse Room Management System\n')
            while True:
                print("\n1. Register Nurse")
                print("2. Delete Nurse")
                print("3. Show Nurse Details")
                print("4. Sign Out\n")
                c=int(input("Enter Your Choice : "))
                if c==1:
                    nid=input("Enter nid : ")
                    nname=input("Eenter nurse name : ")
                    nph=input("Enter phone : ")
                    nage=input("Enter age : ")
                    nwing=input("enter the nurse wing : ")
                    mycursor.execute("insert into nurse_details(nurseid,nursename,nursepno,nurseage,nursewing) values('"+nid+"','"+nname+"','"+nph+"','"+nage+"','"+nwing+"')")
                    mydb.commit()
                    print("\nRecorded Inserted Successfully!!\n")
                elif c==2:
                    nid=input("Enter the nurse id which you want to delete")
                    mycursor.execute("delete from nurse_details where nurseid='"+nid+"'")
                    mydb.commit()
                    print("\nRecord Deleted Successfully!!\n")
                elif c==3:
                    mycursor.execute("select * from nurse_details")
                    row=mycursor.fetchall()
                    print("\nNurse Details is : \n")
                    print(row)
                else:
                    print("\nSigning Out, Bye!\n")
                    break

        else:
            print("\nUsername/Password is incorrect\n")
    elif choice==2:
        output,username=nurse_signin_readfile()
        if output==True:
            print('\nWelcome',username,'to the Nurse Room Management System\n')
            while True:
                print("\n1. Add student")
                print("2. Add inventory")
                print("3. Modify inventory")
                print("4. Show Inventory")
                print("5. Show patient details")
                print("6. Sign Out\n")
                c=int(input("Enter Your Choice : "))
                if c==1:
                    pid=input("Enter patient id : ")
                    pname=input("Eenter patient name : ")
                    pph=input("Enter patient phone no : ")
                    pclass=input("Enter patient class : ")
                    pproblem=input("Enter patient problem : ")
                    mycursor.execute("insert into patient_details(patientid,patientname,patientpno,patientclass,patientproblem) values('"+pid+"','"+pname+"','"+pph+"','"+pclass+"','"+pproblem+"')")
                    mydb.commit()
                    print("\nRecorded Inserted Successfully!!\n")
                elif c==2:
                    invid=input("Eneter inventory id : ")
                    invname=input("Enter inventory name : ")
                    quantity=input("Enter quantity of the specified product : ")
                    mycursor.execute("insert into inventory(invid,invname,quantity) values('"+invid+"','"+invname+"','"+quantity+"')")
                    mydb.commit()
                    print("\nRecorded Inserted Successfully!!\n")
                elif c==3:
                    invid=input("Enter inventoryid which you want to modify : ")
                    quantity=input("Enter the modified quantity : ")
                    mycursor.execute("update inventory set quantity='"+quantity+"' where invid='"+invid+"'")
                    mydb.commit()
                    print("\nRecord Modified Successfully!!\n")
                elif c==4:
                    mycursor.execute("select * from inventory")
                    row=mycursor.fetchall()
                    print("\nInventory report is : \n")
                    print(row)
                elif c==5:
                    mycursor.execute("select * from patient_details")
                    row=mycursor.fetchall()
                    print("\nPatient Details is : \n")
                    print(row)
                else:
                    print("\nSigning Out, Bye!\n")
                    break
        else:
            print("\nUsername/Password is incorrect\n")
