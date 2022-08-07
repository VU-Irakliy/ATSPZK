
from random import randint
from re import L
import re
import numpy as np
import heapq as hq
import math
import sys


"""
Assignment Problem code Reference:  https://python.plainenglish.io/hungarian-algorithm-introduction-python-implementation-93e7c0890e15
Explanation on how this code works can be partially explained there.
All modifications will be explained here 
"""

def minimum_zero(matrix_with_0s, lined_zero, include, reverse, rad): #rad = Random
    
    min_row = [len(matrix_with_0s) + 100, -1]

    #Choose paths from Include set first and mark these rows and columns as False
    if len(include) > 0:
        our_path = include.pop() 
        lined_zero.append((our_path[0], our_path[1]))
        matrix_with_0s[our_path[0], :] = False
        matrix_with_0s[:, our_path[1]] = False

    else:
       
        if reverse == True:
            for i in range((len(matrix_with_0s) - 1), -1, -1):
                if  np.sum(matrix_with_0s[i] == True) > 0 and min_row[0] > np.sum(matrix_with_0s[i] == True):
                    min_row = [np.sum(matrix_with_0s[i] == True), i]
        
        else:
            for i in range(len(matrix_with_0s)):
                if  np.sum(matrix_with_0s[i] == True) > 0 and min_row[0] > np.sum(matrix_with_0s[i] == True):
                    min_row = [np.sum(matrix_with_0s[i] == True), i]

      
        temp = np.where(matrix_with_0s[min_row[1]] == True)[0]
        #If there is only 1 True, it will choose it
        if rad == True:
            if len(temp) == 1:
                zero_index = temp[0]
            else: #else, it will try to pick one randomly (inspiration from Monte Carlo Methods)
                m = randint(0, len(temp) - 1)
                zero_index = temp[m]
        else:
            zero_index = temp[0]
        
        lined_zero.append((min_row[1], zero_index))
        
        matrix_with_0s[min_row[1], :] = False
        
        matrix_with_0s[:, zero_index] = False



def possible_solution(matrix, include, reverse, rad):
    curr_matrix = matrix

    matr_with_0s = (curr_matrix  == 0)
    matr_with_0s_temp = matr_with_0s.copy()

    lined_zeros = []
  
    while (True in matr_with_0s_temp):
        minimum_zero(matr_with_0s_temp, lined_zeros, include, reverse, rad)
    
    lined_rows_0 = []
    lined_columns_0 = []
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
                if row_array[j] == True and j not in lined_columns:
                    lined_columns.append(j)
                    not_lined_flag = True

        for row, col in lined_zeros:
            if row not in not_lined_rows and col in lined_columns:
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
   
    min_num = int(np.nanmin(non_zero))

    for i in range(len(curr_matrix)):
        if i not in lined_rows:
            for j in range(len(curr_matrix[i])):
                if (j not in lined_columns) and (math.isnan(curr_matrix[i][j]) == False):
                    curr_matrix[i][j] = curr_matrix[i][j] - min_num
    
    for i in range(len(lined_rows)):
        for j in range(len(lined_columns)):
            curr_matrix[lined_rows[i]][lined_columns[j]] = curr_matrix[lined_rows[i], lined_columns[j]] + min_num
    
    return curr_matrix


def assignment_hungarian(named_matrix, names, matrix, include, exclude):
    
    copied_matrix = matrix.copy()
    
    shadow = include.copy()
    counts = 0  
    

    # We exclude paths from Exclude set here
    if len(exclude) > 0:
        for node in exclude:
            copied_matrix[node[0]][node[1]] = math.nan
    temp_matrix = copied_matrix.copy()
    
    for i in temp_matrix:
        cur_min = int(np.nanmin(i))
        for j in range(0, len(i)):
            if math.isnan(i[j]) != True:
                i[j] = i[j] - cur_min

    for i in range(len(temp_matrix)):
        temp_array = []
        for j in range(0, len(temp_matrix)):
            # print('Current ',j, i)
            temp_array.append(temp_matrix[j][i])
        cur_min = int(np.nanmin(temp_array))
        for j in range(0, len(temp_matrix)):
            if math.isnan(temp_matrix[j][i]) != True:
                temp_matrix[j][i] = temp_matrix[j][i] - cur_min
            
    count = 0
    count_2 = 0
    rad = False
    reverse = False
    restart_count = 0
    start_the_count = False
    while count < len(matrix):
        # Additional while loop has been added, because it would give inaccurate results due to Include and Exclude involvement in the Assignment Problem
        # while count stands for length of lines, count_2 stands for amount of paths in the solution
        while count_2 < len(matrix):
            
            if counts == int(len(matrix)* 1.25) and start_the_count == True:
                # print('It takes too long (infinitely) under these conditions:')
                # print('Include', include)
                # print('Exclude', exclude)
                # print("We're moving on!")
                
                return None, None
            
            
            backup = shadow.copy()
            result = possible_solution(temp_matrix, backup, reverse, rad) 
            
            
            
            temp_froms = [x[0] for x in result[0]]
            temp_end = [x[1] for x in result[0]]

            #checking if there are any duplicate froms/ends of paths
            if len(temp_froms) != len(set(temp_froms)):
                count_2 = len(set(temp_froms))
            elif len(temp_end) != len(set(temp_end)):
                count_2 = len(set(temp_end))
            else:
                count_2 = len(set(result[0]))


            count = len(result[1]) + len(result[2])
         
            if count < len(temp_matrix):
                
                temp_matrix = change_matrix(temp_matrix, 
                                        result[1],
                                        result[2])

            elif count == len(temp_matrix) and count_2 < len(temp_matrix):
              
                if reverse == False:
                    #changes the traversal of the matrix. It will try go through the bottom to the top of the matrix
                    reverse = True
                    if len(result[1]) > 0 and len(result[2]) > 0:
                        temp_matrix = change_matrix(temp_matrix, 
                                            result[1],
                                            result[2])

                else:
                    #  if we hit dead end, the program will try again from the start
                    #  with the chance of the different outcome (because if x > 1 0s, then it might pick another 0 randomly)
                    
                    counts += 1
                    if start_the_count == False:
                        start_the_count = True
                        counts = 0
                    if restart_count == 5:
                        temp_matrix = copied_matrix.copy()
                        restart_count = 0
                    else:
                        if len(result[1]) > 0 and len(result[2]) > 0:
                            temp_matrix = change_matrix(temp_matrix, 
                                                result[1],
                                                result[2])
                        else:
                            restart_count += 1
                    
                    ####Random choice is activated
                    rad = True
                    #Bring back the initial matrix traversal
                    reverse = False
                    
                    
           
    l = 0
    main_result = []
    
    result = result[0]
   
    while l < len(result):
        i = result[l][0]
        j = result[l][1]


        temp_path = [names[i], names[j], matrix[i][j]]
        main_result.append(temp_path)
        l += 1
    total = sum([x[2] for x in main_result])

    return (main_result, total)
   
   