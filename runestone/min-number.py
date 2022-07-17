#Write two Python functions to find the minimum number in a list. 
# The first function should compare each number to every other number on the list. . 
# The second function should be linear .



the_list = [2, 3, 20, 2, -89, -6]



def findMin(aList):
    mini = aList[0]
    for i in aList:
        if i < mini:
            mini = i
    return mini

def findMin2(aList):
    mini = aList[0]
    for i in aList:
        isSmallest = True
        for j in aList:
            if j < i:
                isSmallest = False
        if isSmallest:
            mini = i
    return mini

print(findMin(the_list))
print(findMin2(the_list))