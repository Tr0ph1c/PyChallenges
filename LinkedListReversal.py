#My first ever time trying to reverse a linked list
#Took me about 15 mins..
#probably has room for improvement

class LinkedList:                   #definition of a node
    def __init__(self, value):
        self.value = value
        self.next = None
    #very useful function
    def __str__(self):              #returns the whole list
        out = f'{self.value}'       #when printing from head node
        node = self.next
        while node is not None:
            out += ', ' + str(node.value)
            node = node.next
        return '[' + out + ']'

def reverseLinkedList(head):
    curr = head
    previous = None
    while True:
        nextone = curr.next
        curr.next = previous
        previous = curr
        curr = nextone

        if not curr:
            break
    return previous


if __name__ == "__main__":
    e0 = LinkedList(0)              #This whole part
    e1 = LinkedList(1)              #just creates a
    e0.next = e1                    #linked list that
    e2 = LinkedList(2)              #looks like this [0-1-2-3]
    e1.next = e2
    e3 = LinkedList(3)
    e2.next = e3

    newHead = reverseLinkedList(e0) #reverse the list from the head node
    
    print(newHead)
