# Linked Lists
- How to do forward traversal


- set a dummy head
- set curr to be the dummy head

while loop:
    - create a new node
    - modify the curr's next pointer to point to the new node
    - have curr point to the new node

That way, we are basically
1. Creating a new element to add to the list
2. adding it to the list
3. moving our curr pointer to the end of the list, pointing at that element.

Lastly, return dummy head.next.

Whenever we create a node, we add it. It is never the case that a node is created, but we don't add it. Thus, if the while loop condition is no longer satisfied, there are no more nodes to add.