
f = open("demofile2.txt", "a")
f.write("This File has no Content!")
f.close()

# Open and Read the file after the appending:

f = open("demofile2.txt", "r")
print(f.read())
