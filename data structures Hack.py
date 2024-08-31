# Reverse a String Using a Stack
def reverse_string(s: str) -> str:
    stack = []
    
    # Push all characters to the stack
    for char in s:
        stack.append(char)
    
    reversed_str = ""
    
    # Pop all characters from the stack to form the reversed string
    while stack:
        reversed_str += stack.pop()
    
    return reversed_str

# Example usage
print(reverse_string("hello"))   # Output: "olleh"


#Implement a Queue Using Two Stacks
class QueueWithStacks:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []
    
    def enqueue(self, x: int):
        self.stack_in.append(x)
    
    def dequeue(self) -> int:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

# Example usage
q = QueueWithStacks()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Output: 1
print(q.dequeue())  # Output: 2


#Find the Maximum Element in a List Using a Linked List
class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value: int):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def find_max(self) -> int:
        if not self.head:
            raise ValueError("List is empty")
        
        max_value = self.head.value
        current = self.head
        
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        
        return max_value

# Example usage
ll = LinkedList()
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(2)
print(ll.find_max())  # Output: 4

