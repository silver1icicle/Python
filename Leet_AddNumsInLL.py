"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of
their nodes contain a single digit. Add the two numbers and return it as a linked list. You may assume the two numbers do not contain
any leading zero, except the number 0 itself.
Example:
 Input  : (2 -> 4 -> 3) + (5 -> 6 -> 4)
 Output : 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def display(self):
        currentPointer = self
        while(currentPointer):
            print str(currentPointer.val) + "--->",
            currentPointer = currentPointer.next
        print "NULL"
        
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = num2 = ""
        currentPointer = l1
        while(currentPointer):
            num1 += str(currentPointer.val)
            currentPointer = currentPointer.next
        num1 = int(num1[::-1])
        
        
        currentPointer = l2
        while(currentPointer):
            num2 += str(currentPointer.val)
            currentPointer = currentPointer.next
        num2 = int(num2[::-1])
        
        res=num1 + num2
        print "Apple:--->",res
        header = None
     
        for i in str(res):
            temp = ListNode(i)
            if header is None:          # First element
                header = temp
            else:
                temp.next = header
                header = temp
        header.display()


                      
if __name__ == '__main__':
    n1 = ListNode(2)
    n2 = ListNode(4)
    n3 = ListNode(3)
    n1.next = n2
    n2.next = n3
    n1.display()
    
    n4 = ListNode(5)
    n5 = ListNode(6)
    n6 = ListNode(4)
    n4.next = n5
    n5.next = n6
    n4.display()
    
    obj = Solution()
    obj.addTwoNumbers(n1,n4)
