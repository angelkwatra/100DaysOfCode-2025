class listnode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
def rem_duplicate(head:listnode)->listnode:
    current = head
    
    while current and current.next:
        if current.val == current.next.val:
            current.next=current.next.next
        else:
            current=current.next
    return head
