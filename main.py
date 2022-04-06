from searchbound import *
...
#INSPIRATION: https://www.geeksforgeeks.org/given-linked-list-representation-of-complete-tree-convert-it-to-linked-representation/

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
    theTree = fillTheTree(input)

main()