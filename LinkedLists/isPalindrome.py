"""
Given a singly linked list of integers, determine whether or not it's a palindrome.

Note: in examples below and tests preview linked lists are presented as arrays just for simplicity of visualization: in real data you will be given a head node l of the linked list

Example

For l = [0, 1, 0], the output should be
isListPalindrome(l) = true;

For l = [1, 2, 2, 3], the output should be
isListPalindrome(l) = false.
"""

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def isListPalindrome(l):
    list = []
    current = l
    if not current:
        return True
    
    while current:
        list.append(current.value)
        current=current.next
    list1 = list[:]
    list.reverse()
    return list == list1

