'''
Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.

The first line contains two space-separated integers describing the respective values of m (the number of words in the magazine) and n (the number of words in the ransom note). 
The second line contains m space-separated strings denoting the words present in the magazine. 
The third line contains n space-separated strings denoting the words present in the ransom note.
'''

from collections import Counter


def ransom_note(magazine, ransom):
    return Counter(ransom.split()) - Counter(magazine.split())

m, n = 6, 4
magazine = 'give me one grand today night'
ransom = 'give one grand today'

# m, n = map(int, raw_input().strip().split(' '))
# magazine = raw_input().strip().split(' ')
# ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"
    