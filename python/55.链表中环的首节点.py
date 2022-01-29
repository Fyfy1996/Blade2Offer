class Node:
    def __init__(self, x):
        self.x = x
        self.next = None
        
        
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n1.next = n2
n2.next = n3
# n3.next = n2
n3.next = n4
n4.next = n5
n5.next = n3

def FirstCircleNode(header):
    p1 = p2 = header
    cnt = 1
    while p1.next != p2.next.next:
        p1 = p1.next
        p2 = p2.next.next
        cnt += 1
    return p1,cnt

head,cnt = FirstCircleNode(n1)
print(head.x)