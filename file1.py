# To  Write a sentence
f=open("file1.txt","w")
f.write("Hii\n")
f.write("Welcome to python")
f.close()
# To open and read the file after over writing
f=open("file1.txt","r")
print(f.read())