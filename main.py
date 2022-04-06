from searchbound import *

#INSIRATION: https://www.geeksforgeeks.org/given-linked-list-representation-of-complete-tree-convert-it-to-linked-representation/
class Node:
 
        def __init__(self, data):
            self.data = data
            self.next = None
        
        def insert(root, item):
            temp = Node(item)
            
            if (root == None):
                root = temp
            else :
                ptr = root
                while (ptr.next != None):
                    ptr = ptr.next
                ptr.next = temp
            
            return root
 
class BinaryTreeNode:
 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
class Conversion:
 
    
    def __init__(self, data = None):
        self.head = None
        self.root = None
 
    def push(self, new_data):
 
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
 
    def convertList2Binary(self):
 
        q = []
 
        if self.head is None:
            self.root = None
            return
 
        self.root = BinaryTreeNode(self.head.data)
        q.append(self.root)
 
        self.head = self.head.next
 
        while(self.head):
 
            parent = q.pop(0) # Front of queue
 
            
            leftChild= None
            rightChild = None
 
            leftChild = BinaryTreeNode(self.head.data)
            q.append(leftChild)
            self.head = self.head.next
            if(self.head):
                rightChild = BinaryTreeNode(self.head.data)
                q.append(rightChild)
                self.head = self.head.next
 
            # Assign the left and right children of parent
            parent.left = leftChild
            parent.right = rightChild
    
def fillTheTree(input):
    if input[0] == None:
        return
    theRootNode = Node(input[0])
    print(theRootNode.data)
    #####HOW TO CONSTRUCT THIS>>  


def main():
    input = [1,4,8,14,55,21,44,61]
    theTree = fillTheTree(input)

main()