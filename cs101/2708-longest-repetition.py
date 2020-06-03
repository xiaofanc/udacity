# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

# only if input is a list
def longest_repetition(a):
    if not a:
        return None
    dct = {}
    for i in range(len(a)):
        if a[i] in dct:
            if a[i] == a[i-1]:
                dct[a[i]] = dct[a[i]] + 1
            else:
                dct[a[i]] = 1
        else:
            dct[a[i]] = 1
        
    dct = sorted(dct.items(), key=lambda x: x[1], reverse=True)
    return dct[0][0]

# compatible for any element 
def longest_repetition(input_list):
    mostcommon = None
    max_length = 0
    current = None
    curr_len = 0
    for element in input_list:
        if current != element:
            current = element
            curr_len = 1
        else:
            curr_len = curr_len + 1
        if curr_len > max_length:
            mostcommon = current
            max_length = curr_len
    return mostcommon

#For example,

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1,2,3,4,5])
# 1

print longest_repetition([])
# None

print longest_repetition([[1], [2, 2], [2, 2], [2, 2], [3, 3, 3]])
#[2, 2]