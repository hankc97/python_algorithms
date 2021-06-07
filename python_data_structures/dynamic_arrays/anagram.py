# Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters 
# (so you can just rearrange the letters to get a different phrase or word).
# For example:
# "public relations" is an anagram of "crap built on lies."
# "clint eastwood" is an anagram of "old west action"
# Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".

def anagram(str1, str2):
    counter_hash = {}

    # O(n)
    str1 = str1.replace(" ", '')
    str2 = str2.replace(" ", '')

    # O(1)
    if len(str1) != len(str2):
        return False

    # O(n) for all 3 loops
    for char in str1:
        # O(1) key into hash
        if char in counter_hash:
            counter_hash[char] += 1
        else:
            counter_hash[char] = 1
        
    for char in str2:
        if char in counter_hash:
            counter_hash[char] -= 1

    for value in counter_hash.values():
        if value > 0:
            return False
    
    return True


print(anagram('dog','god'))
print(anagram('clint eastwood','old west action'))
print(anagram('aa','bb'))
