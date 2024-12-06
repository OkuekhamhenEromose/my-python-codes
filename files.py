

#  :::::::::::::::;   TO CREATE FILE  :::::::::::
nileFile = open('zenegen.txt','w')


#  ::::::::::::::::  to write in the text file  :::::::::::::::::::;
nileFile.write("write something inside")
nileFile.write("it\'s alright")# to modify a written file or it's to do next line\n

nileFile = open('zenegen.txt','a')# to add to the file
nileFile.write("\n add jara")

nileFile = open('zenegen.txt','r+')
text = nileFile.read(10)
print(text)


# print(nileFile.name)
# print(nileFile.close())


# nileFile.close()# after writing a file
# you cant .write after the line that has been closed

