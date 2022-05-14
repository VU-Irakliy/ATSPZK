from searchbound import *

#DOCUMENTATION: 
# treelib
# https://treelib.readthedocs.io/en/latest/#:~:text=treelib%20is%20created%20to%20provide,deep%20copying%2C%20subtree%20cutting%20etc
# from treelib import Node, Tree

# anytree
"""
https://anytree.readthedocs.io/en/latest/ 
https://anytree.readthedocs.io/en/latest/tricks/weightededges.html

"""
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

Parents can have at least 1 child and more than 2 children 
 
 
"""

"""
TASKS:
1. HOW SHOULD I APPROACH IN TRAVERSAL? DO I MAKE TREE OR USE THE MATRIX TO TRAVERSE?
2. IF I MAKE A TREE, HOW TO TRAVERSE IT? 
   IF I USE EXISTING MATRIX, HOW DO I TRAVERSE IT? 
3. WHEN I FIGURE ONE OF THOSE OUT, START CONSTRUCTING THE ALGORITHM.
4. HOW TO PUT AND FOLLOW A STARTING POINT, NUM OF CITIES TRAVERSED,
   WHICH ONES ARE ALREADY PASSED, AMINIMUM, AND OTHER CONDITIONS.
5. 
"""

def fillTheTree(input):
    ...
    #####HOW TO CONSTRUCT THIS>>  


def main():
    input = [1,4,8,14,55,21,44,61]
    f = Node("f", weight = 0)
    b = Node("b", parent=f, weight = 3)
    g = Node("g", parent=f, weight = 4)
    a = Node("a", parent=b, weight = 5)
    d = Node("d", parent=b, weight = 1)
    c = Node("c", parent=d, weight = 3)
    e = Node("e", parent=d, weight = 2)
    i = Node("i", parent=g, weight = 2)
    h = Node("h", parent=i, weight = 2)
    some = f.weight + b.weight + a.weight
    print(RenderTree(f, style=AsciiStyle()))
    print(some)
    print(f.children)
    print(len(f.children))
    # theTree = fillTheTree(input)

main()