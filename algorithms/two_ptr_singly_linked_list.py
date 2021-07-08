# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Given the head of a linked list, remove the nth node from the end of the list and return its head.
# 1 --> 2 --> 3 --> 4 --> 5
# n = 2
# output: 1 --> 2 --> 3 --> 5
# Head = ListNode(1)
# listnode2 = ListNode(2)
# Head.next = listnode2

# edge case: if iteration of linked list reaches the end we can exit it by seeing if the next == None.

# pseudoCode: 
# 1) get len() of the linked list
# 2) difference = find the difference of (len() of linked-list from given nth node)
# 3) while loop, create a count variable
# 4) iterate through the linked lists by increasing the count.
# 5) to exit the while loop, count == difference 
# 6) Once the while loop is exited, we can take the prev node that stopped on,
# 7) to remove the node, prev_node.next = prev_node.next.next 

# [1, 2, 3, 4, 5],
# head = 1
# n = 3
# result => 1, 2 , 4, 5

# length:
# ptr: 

def remove_nth_node_from_end(head, n):
    length = get_length_from_linked_list(head)
    difference = (length - n)
    count = 1
    ptr = head
    
    while count != difference:
        count += 1
        ptr = ptr.next
    
    ptr.next = ptr.next.next
    
    return head
    
def get_length_from_linked_list(head):
    length = 0 # 2
    ptr = head # 3
    
    while ptr != None:
        length += 1
        ptr = ptr.next
    
    return length

    
    
    
    
# 1 --> 2 --> 3 --> 4 --> 5 --> null
# n = 2 
# output: 1 --> 2 --> 3 --> 5 --> null

# dummy = new ListNode(0, head)
# ptr1 = dummy
# ptr2 = dummy    
# move ptr1 n times (ptr1 = ptr1.next)   
# move ptr1 and ptr2 together until ptr1 reaches the end
# ptr2.next = ptr2.next.next



# dummy --> 1 --> 2 --> 3 --> 4 --> 5 --> null
#                                   ^
#                                 ptr1

#                       ^
#                      ptr2
    
    
    
    
    