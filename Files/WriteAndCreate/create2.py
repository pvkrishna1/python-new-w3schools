
f  = open("demofile3.txt", "w")
f.write("Oops I've deleted the content!")
f.close()

# Open and Read the file after the appending:

f = open("demofile3.txt", "r")
print(f.read())

