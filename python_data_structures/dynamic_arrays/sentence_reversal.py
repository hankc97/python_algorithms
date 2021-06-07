# Given a string of words, reverse all the words. For example:
# Given:
# 'This is the best'
# Return:
# 'best the is This'
# As part of this exercise you should remove all leading and trailing whitespace. So that inputs such as:
# '  space here'  and 'space here      '
# both become:
# 'here space'

from pdb import set_trace as bp


def rev_word(sent):
    new_sent = sent.split(' ')
    ans_sent = ''
    for i in range(len(new_sent) - 1, 0, -1):
        if i == 1:
            return ans_sent + new_sent[i] + " " + new_sent[i - 1]
        if new_sent[i] == '':
            continue
        else:
            ans_sent += (new_sent[i] + " ")





print(rev_word('Hi John,   are you ready to go?')) #'go? to ready you are John, Hi'
print(rev_word('    space before')) #'before space'
