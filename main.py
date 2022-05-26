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



#WHEN WHICH ALGORITHM IS USED
#DFBNB IN ZHANG N KORF ALGORITHM IS USED WHEN THERE ARE A LOT OF INSTANCES AKA A LOT OF CITIES 
# (COMPARE TIME OF BOTH BFS AND DFBNB IN ZK ALGORITHM) 
def execute_the_algorithm(tree, input):
    
    if input == 1:
        minimum = 0
        temp_minimum = 0
        result = depthFirstBranchAndBound(tree, minimum, temp_minimum)
        print("Result of Depth-First Branch-and-Bound: ")
        print(result)
        
    elif input == 2:
        minimum = 0
        priority_queue = []
        result = bestFirstSearch(tree)
        print("Result of Best-First Search: ")
        print("Minimum Branch: ",result[0])
        print("Minimum Cost: ", result[1])
    
    else:
        ...

#end
        
points = []
# matrix = []
nodes = []
Start = Node('A', weight=0)

def make_tree(q, p, r, names, flag):
    # print(p[0])
    if (p[0] == 'A') & flag: 
        # print("gav")
        return
    else:
        for i in range(len(p[1])):
            # print(names)
            if(p[1][i] != 0) and (r[i] == 0) and (names[i] != 'A' or sum(r) == len(names) - 1):
                t = Node(names[i], parent=q, weight=p[1][i])
                nodes.append(t)
                # print('meow', i)
                # print('mmmm',p[1])
                # return
                s = r.copy()
                s[i] = 1
                make_tree(t, points[i], s, names, True)



def read_matr(filename):
#    nodes.append("A", weight=0)

    f = open(filename)
    names = f.readline().split()
    for i in range(len(names)):
        s = f.readline().split()
        ch = []
        for j in range(len(s)):
            # if j != i:
            ch.append(int(s[j]))
            # else:
            #     ch.append(0)
        points.append((names[i], ch))
        # matrix.append((names[i], ch))
    f.close()
    print(points)
    r = [0] * len(points)
    make_tree(Start, points[0], r, names, False)

def main():
    filename = 'matr1.txt'
    read_matr(filename)
    print(nodes)
    print(points)
    # print('The matrix:',matrix)

 
    # '''
    # THE TREE IS HARDCODED FOR NOW
    # IN THE FUTURE, GOING TO GENERATE IT FROM THE CSV FILE 
    # '''
    # Start = Node("A", weight = 0)
    # #ABCDEA
    # B = Node("B", parent=Start, weight = 8)
    # C = Node("C", parent=B, weight = 1)
    # D = Node("D", parent=C, weight = 8)
    # E = Node("E", parent=D, weight = 9)
    # A = Node("A", parent=E, weight = 6)

    # #A B C EDA
    # E = Node("E", parent=C, weight = 5)
    # D = Node("D", parent=E, weight = 3)
    # A = Node("A", parent=D, weight = 5)

    # #ABDCEA ....................
    # D = Node("D", parent=B, weight = 7)
    # C = Node("C", parent=D, weight = 7)
    # E = Node("E", parent=C, weight = 5)
    # A = Node("A", parent=E, weight = 6)

    # #ABDECA ........................
    # E = Node("E", parent=D, weight = 9)
    # C = Node("C", parent=E, weight = 1)
    # A = Node("A", parent=C, weight = 3)

    # #ABECDA
    # E = Node("E", parent=B, weight = 4)
    # C = Node("C", parent=E, weight = 1)
    # D = Node("D", parent=C, weight = 8)
    # A = Node("A", parent=D, weight = 5)

    # #ABEDCA
    # D = Node("D", parent=E, weight = 3)
    # C = Node("C", parent=D, weight = 7)
    # A = Node("A", parent=C, weight = 3)
    
    
    # #ACBDEA
    # C = Node("C", parent=Start, weight = 8)
    # B = Node("B", parent=C, weight = 9)
    # D = Node("D", parent=B, weight = 7)
    # E = Node("E", parent=D, weight = 9)
    # A = Node("A", parent=E, weight = 6)

    # #ACBEDA...........................
    # E = Node("E", parent=B, weight = 4)
    # D = Node("D", parent=E, weight = 3)
    # A = Node("A", parent=D, weight = 5)

    # #ACDBEA
    # D = Node("D", parent=C, weight = 8)
    # B = Node("B", parent=D, weight = 1)
    # E = Node("E", parent=B, weight = 4)
    # A = Node("A", parent=E, weight = 6)

    # #ACDEBA
    # E = Node("E", parent=D, weight = 9)
    # B = Node("B", parent=E, weight = 1)
    # A = Node("A", parent=B, weight = 4)

    # #ACEBDA
    # E = Node("E", parent=C, weight = 5)
    # B = Node("B", parent=E, weight = 1)
    # D = Node("D", parent=B, weight = 7)
    # A = Node("A", parent=D, weight = 5)

    # #ACEDBA.
    # D = Node("D", parent=E, weight = 3)
    # B = Node("B", parent=D, weight = 1)
    # A = Node("A", parent=B, weight = 4)

    # #ADBCEA  
    # D = Node("D", parent=Start, weight = 2)
    # B = Node("B", parent=D, weight = 1)
    # C = Node("C", parent=B, weight = 1)
    # E = Node("E", parent=C, weight = 5)
    # A = Node("A", parent=E, weight = 6)

    # #ADBECA............................. THE CORRECT RESULT
    # E = Node("E", parent=B, weight = 4)
    # C = Node("C", parent=E, weight = 1)
    # A = Node("A", parent=C, weight = 3)

    # #ADCBEA.
    # C = Node("C", parent=D, weight = 7)
    # B = Node("B", parent=C, weight = 9)
    # E = Node("E", parent=B, weight = 4)
    # A = Node("A", parent=E, weight = 6)

    # #ADCEBA.
    # E = Node("E", parent=C, weight = 5)
    # B = Node("B", parent=E, weight = 1)
    # A = Node("A", parent=B, weight = 4)

    # #ADEBCA
    # E = Node("E", parent=D, weight = 9)
    # B = Node("B", parent=E, weight = 1)
    # C = Node("C", parent=B, weight = 1)
    # A = Node("A", parent=C, weight = 3)

    # #ADECBA
    # C = Node("C", parent=E, weight = 1)
    # B = Node("B", parent=C, weight = 9)
    # A = Node("A", parent=B, weight = 4)

    # #AEBCDA...............................
    # E = Node("E", parent=Start, weight = 4)
    # B = Node("B", parent=E, weight = 1)
    # C = Node("C", parent=B, weight = 1)
    # D = Node("D", parent=C, weight = 8)
    # A = Node("A", parent=D, weight = 5)

    # #AEBDCA
    # D = Node("E", parent=B, weight = 4)
    # C = Node("C", parent=D, weight = 7)
    # A = Node("A", parent=C, weight = 3)

    # #AECBDA
    # C = Node("C", parent=E, weight = 1)
    # B = Node("B", parent=C, weight = 9)
    # D = Node("D", parent=B, weight = 7)
    # A = Node("A", parent=D, weight = 5)

    # #AECDBA
    # D = Node("D", parent=C, weight = 8)
    # B = Node("B", parent=D, weight = 1)
    # A = Node("A", parent=B, weight = 4)

    # #AEDBCA
    # D = Node("D", parent=E, weight = 3)
    # B = Node("B", parent=D, weight = 1)
    # C = Node("C", parent=B, weight = 1)
    # A = Node("A", parent=C, weight = 3)

    # #AEDCBA
    # C = Node("C", parent=D, weight = 7)
    # B = Node("B", parent=C, weight = 9)
    # A = Node("A", parent=B, weight = 4)

    print(RenderTree(Start, style=ContStyle()))
    
    # print(RenderTree(nodes, style=ContStyle()))

    print("The matrix has been created!")
    print("The tree has been created!")
    execute_the_algorithm(Start, 2)
    # print(some)
    # print(f.children)
    # print(len(f.children))
    # print(matrix_input)
    # A/D/B/E/C/A
    # theTree = fillTheTree(input)

main()