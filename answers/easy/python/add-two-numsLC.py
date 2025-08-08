from typing import Optional
import pdb

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
class LinkedList:
    def __init__(self):
        self.head = None
        curr = self.head
        
    def append(self, val):
        if self.head == None:
            self.head = ListNode(val)
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = ListNode(val)
            
    def dump(self):
        curr = self.head
        while curr.next is not None:
            print(f"[{curr.val}]", end="->")
            curr = curr.next
        print(f"[{curr.val}]")
        
class Sln:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        newlist = LinkedList()
        if(l1.next == None or l2.next == None):
            num = l1.val + l2.val
            if carry > 0:
                num = num + carry
            if num >= 10:
                num = num % 10
                carry = 1
            newlist.append(num)
        else:
            while(l1.next != None and l2.next != None):
                num = l1.val + l2.val
                if carry > 0:
                    num = num + carry
                if num >= 10:
                    num = num % 10
                    carry = 1
                newlist.append(num)
                l1 = l1.next
                l2 = l2.next
        
        return newlist
    
num1 = ListNode(9, next=ListNode(9))
num2 = ListNode(9, next=ListNode(9))

#pdb.set_trace()
ans = Sln.addTwoNumbers(Sln, num1, num2)
ans.dump()

