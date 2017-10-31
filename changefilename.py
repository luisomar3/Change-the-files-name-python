import os, sys

def main():
    splits = []
    x = 0
    path = input("Set Directory path :  ") #Enter the name of the folder you want to rename files
    print ("The dir is:" , path)           # Just print to see path

    files = os.listdir(path)               #This get all files of the folder
    for i in files :
        if i != 'changefilename.py':       #For let the name of the script the same
            x = x + 1
            new_name = str(x)+'.png'
            os.rename(i,new_name)
            print(i)

if __name__ == '__main__':
    main()
