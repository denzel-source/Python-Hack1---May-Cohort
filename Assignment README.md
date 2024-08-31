1. Reverse a String Using a Stack
Task: Implement a stack data structure to reverse a string.

Approach:
We use a stack to reverse the order of characters in the string.
The characters are pushed onto the stack and then popped off in reverse order to form the reversed string.

def reverse_string(s: str) -> str:
    stack = []
    for char in s:
        stack.append(char)
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()
    return reversed_str
print(reverse_string("hello"))  # Output: "olleh"

2. Implement a Queue Using Two Stacks
Task: Implement a queue using two stacks.

Approach:
A queue is implemented using two stacks: stack_in for enqueue operations and stack_out for dequeue operations.
Elements are transferred from stack_in to stack_out when a dequeue operation is requested and stack_out is empty.

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

q = QueueWithStacks()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Output: 1
print(q.dequeue())  # Output: 2


3. Find the Maximum Element in a List Using a Linked List
Task: Implement a singly linked list and find the maximum element in the list.

Approach:
A singly linked list is implemented with nodes containing values.
The find_max method traverses the linked list to find and return the maximum value.

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
ll = LinkedList()
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(2)
print(ll.find_max())  # Output: 4
