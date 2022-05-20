

#####
"""
The input will be unsorted/sorted?
When using a tree value, to retrieve a value, do tree.data
if left/right, do tree.right/left
how the tree will be made?
look at the image made on a meeting u moron
but assignment problem...
WTFFFFFF.>>>>


"""
def depthFirstBranchAndBound(tree, minimum_cost, temp_cost):
    if len(tree.children) > 0:
        i = 0
        while(i < len(tree.children)):
            if minimum_cost > (temp_cost + tree.children[i].weight) or minimum_cost == 0:
                temp_temp_cost = temp_cost
                temp_temp_cost += tree.children[i].weight
                temp_cost = depthFirstBranchAndBound(tree.children[i], 
                                            minimum_cost, temp_cost)
            i += 1
            
            
        return temp_cost
    else:
        
        minimum_cost = temp_cost
        print(minimum_cost)
        return minimum_cost




def bestFirstSearch(tree):
    ...