# File Handling
'''
rt - by default
w - write to existing file
a - append
x - create file and write
r - read
t -  text
b - binary
'''

f=open("Demo.txt","w")
# print(f.read())
# print(f.readline())
# print(f.read())

# f=open("Demo.txt","w")
# f.write("Hii ,Shashi")


# f=open("Demo.txt","a")
# f.write("\nHii ,Namaste Shashi")

'''
f=open("DemoFile1.txt","x")
f.write("New File created by shashi containing -> Namaste Shashi")


f=open("DemoFile2.txt","x")
f.write("New File created by shashi containing -> Namaste Shashi")
'''
import os

# os.remove("DemoFile2.txt")

# os.mkdir("Shashi")
# os.rmdir("shashi")

f.close()
