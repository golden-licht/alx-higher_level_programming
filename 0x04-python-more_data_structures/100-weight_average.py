#!/usr/bin/python3

def weight_average(my_list=[]):
    """
    A function that returns the weighted average
    of all integers tuple (<score>, <weight>)
    """
    if my_list:
        total_score = sum(map(lambda my_tuple: my_tuple[0] * my_tuple[1], my_list))
        total_weight = sum(my_list[i][1] for i in range(len(my_list)))
        average = total_score / total_weight
        return average
    return 0
