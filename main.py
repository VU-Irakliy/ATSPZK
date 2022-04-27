from searchbound import *

#DOCUMENTATION: 
# treelib
# https://treelib.readthedocs.io/en/latest/#:~:text=treelib%20is%20created%20to%20provide,deep%20copying%2C%20subtree%20cutting%20etc
# from treelib import Node, Tree

# anytree
# https://anytree.readthedocs.io/en/latest/ 
from anytree import Node, RenderTree, AsciiStyle, NodeMixin
"""
So, we're not using binary trees
we got n nodes in a graph, where we make a tour
A is a starting point
                                A(0)

                   AB(0+3)      AC(0+4)        AD(0+6)
      ABC(3+4 = 7)    ABD(0+6)
ABCD(7 + 4 = 11)
ABCDA(11 + 3 = 14) 

 
 
"""

def fillTheTree(input):
    ...
    #####HOW TO CONSTRUCT THIS>>  


def main():
    input = [1,4,8,14,55,21,44,61]
    f = Node("f")
    b = Node("b", parent=f)
    a = Node("a", parent=b)
    d = Node("d", parent=b)
    c = Node("c", parent=d)
    e = Node("e", parent=d)
    g = Node("g", parent=f)
    i = Node("i", parent=g)
    h = Node("h", parent=i)
    print(RenderTree(f, style=AsciiStyle()))
    # theTree = fillTheTree(input)

main()