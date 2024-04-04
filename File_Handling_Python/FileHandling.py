import os

def CreateNewFile(namaFile:str,baris):
    try:
        with open(namaFile,"x") as f:
            lst=[]
            for _ in range(baris):
                x=input("Input Sentences : ")
                lst.append(x +"\n")
            f.writelines(lst)
        f.close()
        print(f"File '{namaFile}' has been updated!!")
    except IOError:
        print(f"'{namaFile}' already exist !!!")


def appendFile(namaFile,baris):
    try:
        with open(namaFile,"a") as f:
            lst=[]
            for _ in range(baris):
                x=input("Input Sentences : ")
                lst.append(x +"\n")
            f.writelines(lst)
        f.close()
        print(f"File '{namaFile}' has been updated!!")
    except IOError:
        print(f"Could not append to '{namaFile}' !!!")

def readFile(namaFile):
    try:
        with open(namaFile,"r") as f:
            print(f.read())
            f.close()
    except IOError:
        print(f"File '{namaFile}' doesn't exist!!")
        new=input("Make A New One ? (Y/N) ")
        if new=="Y":
            print()
            main()
        elif new=="N":
            pass
    

def deleteFile(namaFile):
    try:
        os.remove(namaFile)
        print(f"File '{namaFile}' has already deleted!!")    
    except IOError:
        print(f"File '{namaFile}' doesn't exist!!")    
        pass
    
def renameFile(namaFile):
    try:
        newName=input("What's The New Name ? ")
        os.rename(namaFile,newName)
        print(f"File '{namaFile}' has already renamed!!")   
    except:
        print(f"File '{namaFile}' doesn't exist!!")  

def main():
    print("Python File Handling")
    print("=====================")
    print("Choose :")
    print("1. Create New File")
    print("2. Write an Existing File")
    print("3. Read an Existing File")
    print("4. Delete an Existing File")
    print("5. Rename an Existing File")
    print("=====================")
    option=int(input("Which Number You Choose : "))
    FileName=input("File Name : ")
    if option==1:
        FileLine=int(input("Input Number of Line/s : "))
        print("=====================")
        CreateNewFile(FileName,FileLine)
    elif option==2:
        FileLine=int(input("Input Number of Line/s : "))
        print("=====================")
        appendFile(FileName,FileLine)
    elif option==3:
        print("=====================")
        readFile(FileName)
    elif option==4:
        print("=====================")
        deleteFile(FileName)
    elif option==5:
        print("=====================")
        renameFile(FileName)
        
        
if __name__=="__main__":
    main()