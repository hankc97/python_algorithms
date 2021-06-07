# pwd => /home/hank/CodingWork/python/file_basics

# myfile = open('myfile.txt')
# print(myfile.readlines())

# with removes need for .close() file
# with open('myfile.txt', mode = 'r') as myfile:
#     contents = myfile.read()
#     print(contents)

with open('myfile.txt', mode = 'a') as myfile:
    myfile.write("\nthis is the fourth line")

with open('myfile.txt', mode = 'r') as myfile:
    print(myfile.read())

with open('my_secondfile.txt', mode = 'w') as myfile:
    myfile.write("I created this just now!")
