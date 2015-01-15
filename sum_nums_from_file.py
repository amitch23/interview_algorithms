#step 1: write a function that takes a file with 1 integer on each line
#and return the sum of all the integers.

#step 2: write a test function for the first function

#step 3: keep track of the number of correct outputs and return "# 1 pass, 1 fail", e.g.


import urllib2


def sum_ints(nums_txt):
    
    nums_txt = urllib2.urlopen(nums_txt)
    
    
   # eachline = nums_txt.readline()
    sum = 0
    
    for line in nums_txt:
        sum += int(line)
        
    return sum
    
    
nums_txt = 'http://s3.amazonaws.com/realscout-pairing-exercises/ints.txt'
res1 = sum_ints(nums_txt)

global trues
trues = 0
global falses
falses = 0

def test(res1, expected):
    
    if res1 == expected:
        trues += 1
    
    else:
        falses += 1

    print "%r pass, %r fail" %(trues, falses)
    
print test(res1, 69)
print test(res1, 68)

   