'''r-read
rt-read text
rb-read binary
w-write mode(anything present before will be overwritten)
a-adds in the end (for writing further in file)
r+ -read and write
w+-create,read and overwrite(if already exists)
a+ -create,read and write(doesn't overwrite)
'''
f=open("shradha.txt","a+") #open in read and write mode and creates if no such file exists
p=f.write("My name is shradha\n")
print(p) #to get the no. of characters written
print(f.tell()) #tells the pointer position after writing
f.seek(0)
content=f.read()
print(content)
print(f.tell()) #tells the pointer new location
a=f.write("Thank You!!!\n") #writes the line in the file
print(f.tell()) #97th character position
print(a) #prints the no. of character written
f.close() #closes the file

with open("shradha.txt") as f:
    print("after opening the file for 2nd time")
    for line in f:
        print(line,end="")
f=open("shradha.txt")
print("opening the file for third time\n",f.readlines())
f.seek(0) #resets the pointer at 0th character
print(f.readline())
f.close()