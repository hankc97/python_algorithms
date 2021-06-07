# Given a string,determine if it is compreised of all unique characters. For example, the string 'abcde' has all unique characters and should return True. 
# The string 'aabcde' contains duplicate characters and should return false.


def uni_char(string):
    set_string = set([char for char in string])
    if len(set_string) == len(string):
        return True
    return False


print(uni_char("googlmeem"))
print(uni_char('abcdefghijk'))
