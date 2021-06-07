# Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. For this problem, you can falsely "compress" strings of single or double letters. 
# For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space.
# The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.


def compress(string):
    returned_string = ''
    count = 0
    for index in range(0, len(string)):
        if index == len(string) - 1:
            return returned_string + ("{}{}".format(string[index], count+1))
        if string[index] == string[index + 1]:
            count+=1
        else:
            returned_string += ("{}{}".format(string[index], count+1))
            count = 0


print(compress('AAAAABBBBCCCC')) #'A5B4C4'
