"""
You're given 2 huge integers represented by linked lists. Each linked list element is a number from 0 to 9999 that 
represents a number with exactly 4 digits. 
The represented number might have leading zeros. Your task is to add up these huge integers and return the result in the same format.
Example
For a = [9876, 5432, 1999] and b = [1, 8001], the output should be
addTwoHugeNumbers(a, b) = [9876, 5434, 0].
Explanation: 987654321999 + 18001 = 987654340000.
For a = [123, 4, 5] and b = [100, 100, 100], the output should be
addTwoHugeNumbers(a, b) = [223, 104, 105].
Explanation: 12300040005 + 10001000100 = 22301040105.
Input/Output
[execution time limit] 4 seconds (py3)
[input] linkedlist.integer a
The first number, without its leading zeros.
Guaranteed constraints:
0 ≤ a size ≤ 104,
0 ≤ element value ≤ 9999.
[input] linkedlist.integer b
The second number, without its leading zeros.
Guaranteed constraints:
0 ≤ b size ≤ 104,
0 ≤ element value ≤ 9999.
"""
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def addTwoHugeNumbers(a, b):
    current1 = a
    current2 = b
    str1 = ''
    str2 = ''
    if  not a or not b:
        return []
    
    while current1:
        str1+=str(current1.value).zfill(4)
        current1 = current1.next
        
    while current2:
        str2+=str(current2.value).zfill(4)
        current2 = current2.next
    
    def hugenumSum(a, b):
        from itertools import zip_longest
        a = [int(i) for i in str(a)]
        b = [int(i) for i in str(b)]
        carry=0
        result= []
        c =0
        for ac, bc in zip_longest(reversed(a), reversed(b), fillvalue=0):
            carry, digit = divmod(ac+bc+carry, 10)
            # print(carry, digit)
            result.append(str(digit))
            c+=1
            if c==len(list(zip_longest(reversed(a), reversed(b), fillvalue=0))) and carry!=0:
                result.append(str(carry))
        # print("count {}".format(c), )
        return [ ''.join(reversed(result))[i:i+4].rstrip('0')  for i in range(0, len(''.join(reversed(result))), 4) ]
    
    x = hugenumSum(int(str1),int(str2))
    return [int(i) if i!='' else 0 for i in x ]
        
######METHOD2
# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def addTwoHugeNumbers(a, b):
    aa='' 
    bb=''
    while a:
        aa+='0' * (4-len(str(a.value))) + str(a.value)
        a = a.next
    while b:
        bb+='0' * (4-len(str(b.value))) + str(b.value)
        b = b.next    
    suma = str(int(aa)+int(bb))
    c = '0' *(0 if len(suma)%4 == 0 else 4 - len (suma)%4)+suma
    cc = [int(c[4*i:4*i+4]) for i in range(len(c)//4)]
    node = ListNode(cc[0])
    l =node
    for i in range(len(cc)-1):
        new_node = ListNode(cc[i+1])
        l.next = new_node
        l = l.next
    return node
