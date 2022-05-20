from searchbound import *
import pandas as pd

#DOCUMENTATION: 
# treelib
# https://treelib.readthedocs.io/en/latest/#:~:text=treelib%20is%20created%20to%20provide,deep%20copying%2C%20subtree%20cutting%20etc
# from treelib import Node, Tree

# anytree
"""
https://anytree.readthedocs.io/en/latest/ 
https://anytree.readthedocs.io/en/latest/tricks/weightededges.html

"""
from anytree import *
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

# def fillTheTree(input):
#     ...
#     #####HOW TO CONSTRUCT THIS>>  


#WHEN WHICH ALGORITHM IS USED
def execute_the_algorithm(tree, input):
    if input == 1:
        minimum = 0
        temp_minimum = 0
        result = depthFirstBranchAndBound(tree, minimum, temp_minimum)
        print(result)
        
    # elif input == 2:
    #     bestFirstSearch(tree)
        


def main():
    # file = 'Example1.csv'
    # matrix_input = pd.read_csv(file)
    # input = [1,4,8,14,55,21,44,61]
    nodes = ['A', 'B', 'C', 'D', 'E']
    nodes_size = 5
    Start = Node("A", weight = 0)
    '''
    THE TREE IS HARDCODED FOR NOW
    IN THE FUTURE, GOING TO GENERATE IT FROM THE CSV FILE 
    '''
    #ABCDEA
    B = Node("B", parent=Start, weight = 8)
    C = Node("C", parent=B, weight = 1)
    D = Node("D", parent=C, weight = 8)
    E = Node("E", parent=D, weight = 9)
    A = Node("A", parent=E, weight = 6)

    #A B C EDA
    E = Node("E", parent=C, weight = 5)
    D = Node("D", parent=E, weight = 3)
    A = Node("A", parent=D, weight = 5)

    #ABDCEA ....................
    D = Node("D", parent=B, weight = 7)
    C = Node("C", parent=D, weight = 7)
    E = Node("E", parent=C, weight = 5)
    A = Node("A", parent=E, weight = 6)

    #ABDECA ........................
    E = Node("E", parent=D, weight = 9)
    C = Node("C", parent=E, weight = 1)
    A = Node("A", parent=C, weight = 3)

    #ABECDA
    E = Node("E", parent=B, weight = 4)
    C = Node("C", parent=E, weight = 1)
    D = Node("D", parent=C, weight = 8)
    A = Node("A", parent=D, weight = 5)

    #ABEDCA
    D = Node("D", parent=E, weight = 3)
    C = Node("C", parent=D, weight = 7)
    A = Node("A", parent=C, weight = 3)
    
    
    #ACBDEA
    C = Node("C", parent=Start, weight = 8)
    B = Node("B", parent=C, weight = 9)
    D = Node("D", parent=B, weight = 7)
    E = Node("E", parent=D, weight = 9)
    A = Node("A", parent=E, weight = 6)

    #ACBEDA...........................
    E = Node("E", parent=B, weight = 4)
    D = Node("D", parent=E, weight = 3)
    A = Node("A", parent=D, weight = 5)

    #ACDBEA
    D = Node("D", parent=C, weight = 8)
    B = Node("B", parent=D, weight = 1)
    E = Node("E", parent=B, weight = 4)
    A = Node("A", parent=E, weight = 6)

    #ACDEBA
    E = Node("E", parent=D, weight = 9)
    B = Node("B", parent=E, weight = 1)
    A = Node("A", parent=B, weight = 4)

    #ACEBDA
    E = Node("E", parent=C, weight = 5)
    B = Node("B", parent=E, weight = 1)
    D = Node("D", parent=B, weight = 7)
    A = Node("A", parent=D, weight = 5)

    #ACEDBA.
    D = Node("D", parent=E, weight = 3)
    B = Node("B", parent=D, weight = 1)
    A = Node("A", parent=B, weight = 4)

    #ADBCEA  
    D = Node("D", parent=Start, weight = 2)
    B = Node("B", parent=D, weight = 1)
    C = Node("C", parent=B, weight = 1)
    E = Node("E", parent=C, weight = 5)
    A = Node("A", parent=E, weight = 6)

    #ADBECA.............................
    E = Node("E", parent=B, weight = 4)
    C = Node("C", parent=E, weight = 1)
    A = Node("A", parent=C, weight = 3)

    #ADCBEA.
    C = Node("C", parent=D, weight = 7)
    B = Node("B", parent=C, weight = 9)
    E = Node("E", parent=B, weight = 4)
    A = Node("A", parent=E, weight = 6)

    #ADCEBA.
    E = Node("E", parent=C, weight = 5)
    B = Node("B", parent=E, weight = 1)
    A = Node("A", parent=B, weight = 4)

    #ADEBCA
    E = Node("E", parent=D, weight = 9)
    B = Node("B", parent=E, weight = 1)
    C = Node("C", parent=B, weight = 1)
    A = Node("A", parent=C, weight = 3)

    #ADECBA
    C = Node("C", parent=E, weight = 1)
    B = Node("B", parent=C, weight = 9)
    A = Node("A", parent=B, weight = 4)

    #AEBCDA...............................
    E = Node("E", parent=Start, weight = 4)
    B = Node("B", parent=E, weight = 1)
    C = Node("C", parent=B, weight = 1)
    D = Node("D", parent=C, weight = 8)
    A = Node("A", parent=D, weight = 5)

    #AEBDCA
    D = Node("E", parent=B, weight = 4)
    C = Node("C", parent=D, weight = 7)
    A = Node("A", parent=C, weight = 3)

    #AECBDA
    C = Node("C", parent=E, weight = 1)
    B = Node("B", parent=C, weight = 9)
    D = Node("D", parent=B, weight = 7)
    A = Node("A", parent=D, weight = 5)

    #AECDBA
    D = Node("D", parent=C, weight = 8)
    B = Node("B", parent=D, weight = 1)
    A = Node("A", parent=B, weight = 4)

    #AEDBCA
    D = Node("D", parent=E, weight = 3)
    B = Node("B", parent=D, weight = 1)
    C = Node("C", parent=B, weight = 1)
    A = Node("A", parent=C, weight = 3)

    #AEDCBA
    C = Node("C", parent=D, weight = 7)
    B = Node("B", parent=C, weight = 9)
    A = Node("A", parent=B, weight = 4)

    # print(RenderTree(Start, style=ContStyle()))
    
    # print( (Start.children[0].children[1], Start.children[0].weight + Start.children[0].children[1].weight), Start.children[2], Start.children[0].children[0], Start.children[1])
    # print(Start.children[0].weight + Start.children[0].children[1].weight)

    # print(len(Start.children[0].children))
    # print(Start.children[0].children)

    # print(Start.children[0].children[0].children[0].weight)
    ##execute_the_algorithm(Start)

    execute_the_algorithm(Start, 1)
    # print(some)
    # print(f.children)
    # print(len(f.children))
    # print(matrix_input)
    # theTree = fillTheTree(input)

main()