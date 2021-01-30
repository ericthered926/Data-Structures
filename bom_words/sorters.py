# Parameters in the following functions:
#   data: a list of tuples
#   index: the tuple index to sort by
#
# Consider the following example data:
#   data = [
#       ( 'homer', 'simpson', 50 ),
#       ( 'luke', 'skywalker', 87 ),
#       ( 'bilbo', 'baggins', 111 ),
#   ]
#
#   bubble_sort(data, 0) sorts on first name (a..z)
#   bubble_sort(data, 0, True) sorts on first name (z..a)
#   bubble_sort(data, 2) sorts on age (1..infinity)
#
# The data list is sorted in place (anew list is not created).
# You do NOT need to perform validation on input data
# (null data list, index out of bounds, etc.)
#


def bubble_sort(data, index, descending=False):
    '''Sorts using the bubble sort algorithm'''
    # replace this with your own algorithm (do not use Python's sort)
    for i in range(len(data)):
        for j in range(0,len(data)-i-1):
            if descending:
                if data[j][index] < data[j+1][index]:
                    data[j], data[j+1] = data[j+1], data[j]
            else:
                if data[j][index] > data[j+1][index]:
                    data[j], data[j+1] = data[j+1], data[j]


def insertion_sort(data, index, descending=False):
    '''Sorts using the insertion sort algorithm'''
    # replace this with your own algorithm (do not use Python's sort)
    for i in range(1,len(data)):
        ins = data[i]
        val = i-1
        ins2 = data[val]
        if descending:
            while val >= 0 and ins[index] > data[val][index]:
                data[val+1] = data[val]
                val -= 1
        else:
            while val >= 0 and ins[index] < data[val][index]:
                data[val+1] = data[val]
                val -= 1
        data[val+1] = ins

def selection_sort(data, index, descending=False):
    '''Sorts using the selection sort algorithm'''
    # replace this with your own algorithm (do not use Python's sort)
    for i in range(len(data)):
        beg = i
        for j in range(i+1,len(data)):
            if descending:
                if data[beg][index] < data[j][index]:
                    beg = j
            else:
                if data[beg][index] > data[j][index]:
                    beg = j   
        data[i], data[beg] = data[beg], data[i]