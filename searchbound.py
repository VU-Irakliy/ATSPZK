# from unittest import result

from zk import *


'''
THESE USE TREE DATA STRUCTURES

'''
def depthFirstBranchAndBound(tree, minimum_cost, temp_cost):
    if len(tree.children) > 0:
        i = 0
        while(i < len(tree.children)):
            if minimum_cost > (temp_cost + tree.children[i].weight) or minimum_cost == 0:
                temp_cost += tree.children[i].weight
                # print("Current cost:", temp_cost)
                minimum_cost = depthFirstBranchAndBound(tree.children[i], 
                                            minimum_cost, temp_cost)
                temp_cost-=tree.children[i].weight
                
            i += 1

        return minimum_cost
    else:
        minimum_cost = temp_cost
        # print(tree)
        # print("CURRENT MINIMUM COST:", minimum_cost)
        return minimum_cost


def bestFirstSearch(tree):
    priority_queue = []
    closed = []
    i = 0
    if(len(tree.children)>0):
        while(i < len(tree.children)):
            priority_queue_member = (tree.children[i], tree.children[i].weight )
            priority_queue.append(priority_queue_member)
            i += 1
        priority_queue = sorted(priority_queue, key= lambda x: x[1])
        reached_minimum = False
    
        while(i < len(priority_queue) or reached_minimum == False):
            # print(priority_queue[0][0])
            if(len(priority_queue[0][0].children) > 0):

                temp_branch = priority_queue.pop(0)
                # print('Processing ',temp_branch)
                closed.append(temp_branch)
                if(len(temp_branch[0].children) > 0):
                    y = 0
                    while(y < len(temp_branch[0].children)):
                        temp_cost = temp_branch[1]
                        priority_queue_member = (temp_branch[0].children[y], 
                                            (temp_branch[0].children[y].weight + temp_cost) )
                        priority_queue.append(priority_queue_member)
                        # print('WHat', priority_queue)
                        y += 1
                        
                    priority_queue = sorted(priority_queue, key= lambda x: x[1])
                    
            else:
                temp_branch = priority_queue.pop(0)
                reached_minimum = True
                # print(temp_branch)
                # print("SO   ", temp_branch[0])
                return temp_branch

            i+=1


'''
END
'''

