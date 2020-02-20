#Writing to a file in Python

#w = write, a = append, r = read
outfile = open("txtpractice.txt", "w")
for i in range(1,100):
        outfile.write(str(i)+"\n")
outfile.close()

#read() = Reads files from beginning to end
#readline() = Reads only the line that the pointer is currently on
#readlines() = Reads the lines and puts each one in a separate index within a list
infile = open("txtpractice.txt", "r")
print(infile.read())
infile.close()
