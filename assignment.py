
from re import L
import re
import numpy as np
from anytree import *
import heapq as hq
import math
import sys

#DOCUMENTATION: 
# anytree
"""
https://anytree.readthedocs.io/en/latest/ 
https://anytree.readthedocs.io/en/latest/tricks/weightededges.html

"""

'''
THESE USE MATRIX DATA STRUCTURE
'''
# print(int(np.nanmin(matrix_points)))
# if you want to check if it's nan then do "if math.isnan(x): then ...."


"""
Assignment Problem Reference:  https://python.plainenglish.io/hungarian-algorithm-introduction-python-implementation-93e7c0890e15
Explanation on how this code works can be partially explained there.
"""

def minimum_zero(matrix_with_0s, lined_zero, include, count_include, flag):
    
    min_row = [len(matrix_with_0s) + 100, -1]
    # i -> row
    if count_include[0] < len(include) and len(include) != 0:
        our_path = include[count_include[0]] ##don't forget that count_include is not include !!!!
        lined_zero.append((our_path[0], our_path[1]))
        # print(our_path)
        matrix_with_0s[our_path[0], :] = False
        matrix_with_0s[:, our_path[1]] = False
        count_include[0] += 1

    else:
        # i is a row
        if flag == True:
            for i in range((len(matrix_with_0s) - 1), -1, -1):
                # print(i)
                if  np.sum(matrix_with_0s[i] == True) > 0 and min_row[0] > np.sum(matrix_with_0s[i] == True):
                    min_row = [np.sum(matrix_with_0s[i] == True), i]
        
        else:
            for i in range(len(matrix_with_0s)):
                if  np.sum(matrix_with_0s[i] == True) > 0 and min_row[0] > np.sum(matrix_with_0s[i] == True):
                    min_row = [np.sum(matrix_with_0s[i] == True), i]

        # Marked the specific row and column as False
        zero_index = np.where(matrix_with_0s[min_row[1]] == True)[0][0]
        lined_zero.append((min_row[1], zero_index))
        
        matrix_with_0s[min_row[1], :] = False
        
        matrix_with_0s[:, zero_index] = False
        # print(matrix_with_0s, '\n')



def possible_solution(matrix, include, flag): #flag
    curr_matrix = matrix

    #Transform the matrix to boolean matrix(0 = True, others = False)
    matr_with_0s = (curr_matrix  == 0)
    # print(matr_with_0s)
    matr_with_0s_temp = matr_with_0s.copy()

    lined_zeros = []
    #Recording possible answer positions by marked_zero
    count_include = [0]
    while (True in matr_with_0s_temp):
        minimum_zero(matr_with_0s_temp, lined_zeros, include, count_include, flag)
        # print(matr_with_0s_temp)
    print('so sos o',lined_zeros)
    
    lined_rows_0 = []
    lined_columns_0 = []
    # print(lined_zeros) #look at lined_zeros for include
    for i in range(len(lined_zeros)):
        lined_rows_0.append(lined_zeros[i][0])
        lined_columns_0.append(lined_zeros[i][1])
    not_lined_rows = list(set(range(len(curr_matrix))) - set(lined_rows_0))

    lined_columns = []
    not_lined_flag = True
    while not_lined_flag:
        not_lined_flag = False
        for i in range(len(not_lined_rows)):
            row_array = matr_with_0s[not_lined_rows[i], :]
            for j in range(len(row_array)):
                #Step 2-2-2
                if row_array[j] == True and j not in lined_columns:
                #Step 2-2-3
                    lined_columns.append(j)
                    not_lined_flag = True

        for row, col in lined_zeros:
			#Step 2-2-4
            if row not in not_lined_rows and col in lined_columns:
                #Step 2-2-5
                not_lined_rows.append(row)
                not_lined_flag = True
    
    lined_rows = list(set(range(len(matrix))) - set(not_lined_rows))
    result = [lined_zeros, lined_rows, lined_columns]
    return result


def change_matrix(matrix, lined_rows, lined_columns):
    curr_matrix = matrix.copy()
    non_zero = []
    

    for i in range(len(curr_matrix)):
        if i not in lined_rows:
            for j in range(len(curr_matrix[i])):
                if j not in lined_columns and curr_matrix[i][j] != 0:
                    non_zero.append(curr_matrix[i][j])
    print('shit', non_zero)
    # print('WORK = ', np.nonzero(non_zero))
    min_num = int(np.nanmin(non_zero))
    print('SOOO ',min_num)
    for i in range(len(curr_matrix)):
        if i not in lined_rows:
            for j in range(len(curr_matrix[i])):
                if (j not in lined_columns) and (math.isnan(curr_matrix[i][j]) == False):
                    curr_matrix[i][j] = curr_matrix[i][j] - min_num
    
    # print('bye') 
    # Ignore the IDE error here... 
    for i in range(len(lined_rows)):
        for j in range(len(lined_columns)):
            curr_matrix[lined_rows[i]][lined_columns[j]] = curr_matrix[lined_rows[i], lined_columns[j]] + min_num
    
    return curr_matrix


"""
WE GOTTA MODIFY THIS WITH INCLUDE, EXCLUDE AND 'THE ONES THAT ARE BEING DECOMPOSED IN THIS SUBTREE' (IF THERE IS A EDGE THAT IS IN DECOMPOSED, THEN ADD IT TO INCLUDE)
ALSO WE WILL HAVE A STORAGE OF ALL EXISTING SUBPROBLEMS THAT HAVE SUBTOURS, SO DON'T MAKE A DUPLICATE?
[(0, 10), (9, 0), (1, 7), (7, 4), (11, 14), (6, 2), (10, 6), (13, 11), (2, 9), (4, 5), (12, 13), (5, 8), (8, 1), (14, 3)]

[[(0, 10), (9, 0), (1, 7), (7, 4), (14, 3), (11, 14), (10, 6), (8, 1), (6, 2), (13, 11), (2, 9), (12, 5), (4, 12), (5, 8)]

"""
def assignment_hungarian(named_matrix, names, matrix, include, exclude):
    temp_matrix = matrix.copy()
    shadow = include.copy()

    # temp_matrix = np.array(temp_matrix)

    if len(exclude) > 0:
        for node in exclude:
            temp_matrix[node[0]][node[1]] = math.nan
    # print(temp_matrix)
    
    for i in temp_matrix:
        cur_min = int(np.nanmin(i))
        for j in range(0, len(i)):
            if math.isnan(i[j]) != True:
                i[j] = i[j] - cur_min
    # print(temp_matrix)

    for i in range(len(temp_matrix)):
        temp_array = []
        for j in range(0, len(temp_matrix)):
            temp_array.append(temp_matrix[j][i])
        cur_min = int(np.nanmin(temp_array))
        for j in range(0, len(temp_matrix)):
            if math.isnan(temp_matrix[j][i]) != True:
                temp_matrix[j][i] = temp_matrix[j][i] - cur_min
            
    # print('\n',temp_matrix)
    count = 0
    count_2 = 0
    # prioritise = []
    we_try = 0
    we_tried = []

    inc_starts = [x[0] for x in include]
    inc_ends = [x[1] for x in include]
    coords_with_0s = []
    coords_that_miss = []
    flag = False
    didnt_work = False
    
    while count < len(matrix):
        # if mini == True:
        #         break
        while count_2 < len(matrix):
            # if mini == True:
            #     break
            print('CURR include',shadow)
            #result[0] = , result[1] = , result[2] = ... 
            result = possible_solution(temp_matrix, shadow, flag)
            prioritise = []
            print('\n \n POSSIBLE RESULT', result)
            temp_froms = [x[0] for x in result[0]]
            # print(temp_froms)
            temp_end = [x[1] for x in result[0]]
            if len(temp_froms) != len(set(temp_froms)):
                count_2 = len(set(temp_froms))
            elif len(temp_end) != len(set(temp_end)):
                count_2 = len(set(temp_end))
            else:
                count_2 = len(set(result[0]))




            count = len(result[1]) + len(result[2])
            print('lines',count)
            # count = len(result[0])

            print('actual', count_2)
            # print(result[0]   [0][0])
            # print('SIZE OF THE POSS SOL',count)
            if count < len(temp_matrix):
                print('NOOOOOOOOOOOOO')
                
                temp_matrix = change_matrix(temp_matrix, 
                                        result[1],
                                        result[2])
            elif count == len(temp_matrix) and count_2 < len(temp_matrix):
                # shadow = include.copy()
                # for i in range(len(temp_matrix)):
                #     if i not in temp_froms:
                #         tzeros_i = []
                #         tzeros_j = []
                #         for j in range(0, len(temp_matrix)):
                #             if j not in temp_end:
                #                 if temp_matrix[i][j] == 0:
                #                     tzeros_i.append((i, j))
                #                 if temp_matrix[j][i] == 0:
                #                     tzeros_j.append((j, i))
                #         if len(tzeros_i) == 1:
                #             shadow.append(tzeros_i[0])
                #         if len(tzeros_j) == 1:
                #             shadow.append(tzeros_j[0])
                ...
                # print('tzeros_i',tzeros_i)
                # print('tzeros_j', tzeros_j)
                # print('old include', include)
                # print('new include',shadow)
                # temp_froms = [x[0] for x in result[0]]
                # # print(temp_froms)
                # temp_end = [x[1] for x in result[0]]
                if flag == False:
                    print('pp')
                    flag = True
                    if len(result[1]) > 0 and len(result[2]) > 0:
                        temp_matrix = change_matrix(temp_matrix, 
                                            result[1],
                                            result[2])
                    missing = []

                    for i in range(0, len(temp_matrix)):
                        if i not in temp_froms:
                            missing.append(i)
                    print('MISSS', missing)
                else:
                    print('please pick another matrix')
                    missing = []
                    print("WELP, WHAT'S NEXT")
                    for i in range(0, len(temp_matrix)):
                        if i not in temp_froms:
                            missing.append(i)
                    print('MISSS', missing)
                    exit()
                    if didnt_work == False:
                        didnt_work = True
                        collectionn = []
                        for i in missing:
                            for j in range(0, len(matrix)):
                                if temp_matrix[i][j] == 0:
                                    if j in inc_ends:
                                        print(j, 'is a trouble number')
                                    else:
                                        collectionn.append((i,j))
                        # temp_matrix = change_matrix()
                        print(collectionn)
                        

                        
                    else:
                        ...
                        for i in range(0, len(temp_matrix)):
                            if i not in temp_froms:
                                missing.append(i)
                        print('MISSS', missing)
                        break

                    # coords_that_miss = []
                    # coords_with_0s = []
                    # # lum = result[0]
                  
                    # for i in missing:
                    #     tempie = []
                    #     tempmp = []
                    #     # sss = []
                    #     for j in range(0, len(temp_matrix)):
                    #         # print('SJSJSJS ', i, j)

                    #         if temp_matrix[i][j] == 0 and j not in inc_ends:
                    #             tut = (i, j)
                    #             # tempie.append([tut, matrix[i][j]])
                    #             coords_that_miss.append(tut)
                    #             tempie.append(tut)
                    #         # if temp_matrix[j][i] == 0:
                    #         #     tut = (j, i)
                    #         #     tempmp.append(tut)
                    #         #     coords_that_miss.append(tut)
                    #     coords_with_0s.append([tempie, tempmp])
                    # print(coords_with_0s)
                    # print(coords_that_miss)
                    # shadow = include.copy()
                    # some = False
                    # for i in coords_with_0s:
                    #     for j in i:
                    #         if len(j) == 1:
                    #             shadow.append(j[0])
                    #             some = True

                    # if some != True:
                    #     for i in coords_that_miss:
                    #         if i not in we_tried:

                    #             shadow.append(i)
                    #             we_tried.append(i)
                    #             coords_that_miss.pop(coords_that_miss.index(i))

                    ...

                # have_missing_end = []
                # for i in missing:
                #     if i in temp_end:
                #         psps = result[0][temp_end.index(i)]
                #         have_missing_end.append([psps, matrix[psps[0]][psps[1]]])

                # print(have_missing_end)
                #########################
                # if len(have_missing_end) > 0:
                #     missing_ends = []
                #     for i in range(0, len(temp_matrix)):
                #         if i not in temp_end:
                #             missing_ends.append(i)
                #     print('HAHAHAH',missing_ends)

                #     coords_that_miss = []
                #     coords_with_0s = []
                #     lum = result[0]
                  
                #     for i in missing:
                #         tempie = []
                #         tempmp = []
                #         # sss = []
                #         for j in range(0, len(temp_matrix)):
                #             # print('SJSJSJS ', i, j)

                #             if temp_matrix[i][j] == 0:
                #                 tut = (i, j)
                #                 # tempie.append([tut, matrix[i][j]])
                #                 coords_that_miss.append(tut)
                #                 tempie.append(tut)
                #             if temp_matrix[j][i] == 0:
                #                 tut = (j, i)
                #                 tempmp.append(tut)
                #                 coords_that_miss.append(tut)
                #         coords_with_0s.append([tempie, tempmp])
                #     print(coords_with_0s)
                #     print(coords_that_miss)
                    

                #     for i in coords_with_0s:
                #         for j in i:
                #             if len(j) == 1:
                #                 shadow.append(j[0])
                #                 flag = True
                    
                   # mini = True


                    # ...
                # elif len(have_missing_end) > 0 and len(missing) != len(have_missing_end):
                #     print("UMMMMMMMM")
                




                ################################################################################


                # if len(coords_that_miss) == 0:
                #     print('HOMIE')
                #     for i in missing:
                #         tempie = []
                #         tempmp = []
                #         # sss = []
                #         for j in range(0, len(temp_matrix)):
                #             if temp_matrix[i][j] == 0:
                #                 print('SJSJSJS ', i, j)

                #                 tut = (i, j)
                #                 # tempie.append([tut, matrix[i][j]])
                #                 if tut not in we_tried and tut[1] not in inc_ends:
                #                     coords_that_miss.append(tut)
                #                     tempie.append(tut)
                                    
                #             if temp_matrix[j][i] == 0:
                #                 tut = (j, i)
                #                 if tut not in we_tried and tut[0] not in inc_starts:
                #                     tempmp.append(tut)
                #                     coords_that_miss.append(tut)
                #                     print('SJSJSJS ', i, j)
                #         coords_with_0s.append([tempie, tempmp])
                # if len(coords_that_miss) > 0:
                #     print(coords_with_0s)
                #     print(coords_that_miss)
                #     flag = False
                #     shadow = include.copy()
                #     # for i in coords_with_0s:
                #     #     for j in i:
                #     #         if len(j) == 1:
                #     #             shadow.append(j[0])
                #     #             we_tried.append(j[0])
                #     #             print('WE"RE ACCIDENTALLY TRYIGN THIS', j[0] )
                #     #             flag = True
                #     # if flag != True:
                        
                #     print(we_try)
                #     shadow.append(coords_that_miss[0])
                #     we_tried.append(coords_that_miss[0])
                #     coords_that_miss.pop(0)
                # else:
                    
                #     if len(result[1]) > 0 and len(result[2]) > 0:
                #         shadow = include.copy()
                #         temp_matrix = change_matrix(temp_matrix, 
                #                         result[1],
                #                         result[2])

                #########################################################################################





                    # else:
                    #     if len(result[1]) > 0:
                    #         for i in missing:
                    #             if i in result[1]:
                    #                 result[1].pop(result[1].index(i))
                    #     if len(result[2]) > 0:
                    #         for i in missing:
                    #             if i in result[2]:
                    #                 result[2].pop(result[2].index(i))
                    #     temp_matrix = change_matrix(temp_matrix, 
                    #                     result[1],
                    #                     result[2])
                        
                
                
                # print('WE"RE TRYING THIS',coords_that_miss[we_try])
                    
                
                
                    # temp_matrix = change_matrix(temp_matrix, 
                    #                     result[1],
                    #                     result[2])
            print(temp_matrix)

                        
    
    l = 0
    main_result = []
    # print(r)
    # print('SOOO', result)
    result = result[0]
    # print('AAAND', result)
    # print(names)
    # print(names[0])
    while l < len(result):
        i = result[l][0]
        j = result[l][1]


        tempest = [names[i], names[j], matrix[i][j]]
        main_result.append(tempest)
        l += 1
    total = sum([x[2] for x in main_result])
    return (main_result, total)
    # something = findminstroken(temp_matrix, 0, 0, len(temp_matrix)**2, strikethrough(temp_matrix, len(temp_matrix)))
