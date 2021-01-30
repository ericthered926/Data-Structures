#!/usr/bin/env python3
import math

class Array(object):
    '''
    An array implementation that holds arbitrary objects.
    '''

    def __init__(self, initial_size=10, chunk_size=5):
        '''Creates an array with an intial size.'''
        self.data = alloc(initial_size)
        self.size = 0


    def debug_print(self):
        output = str(self.size) + ' of ' + str(len(self.data)) + ' >>> '
        count = len(self.data)
        for i in range(count):
            if i != None:
                output += str(self.data[i]) + ', '
            else:
                output += 'None, '
        output = output[:-2]
        return output


    def _check_bounds(self, index):
        '''Ensures the index is within the bounds of the array: 0 <= index <= size.'''
        if 0 <= index < self.size:
            return True
        return False


    def _check_increase(self):
        '''
        Checks whether the array is full and needs to increase by chunk size
        in preparation for adding an item to the array.
        '''
        if self.size == len(self.data):
            return True
        return False


    def _check_decrease(self):
        '''
        Checks whether the array has too many empty spots and can be decreased by chunk size.
        If a decrease is warranted, it should be done by allocating a new array and copying the
        data into it (don't allocate multiple arrays if multiple chunks need decreasing).
        '''
        todecrease = len(self.data)-self.size
        if todecrease > 5:
            self = memcpy(self,self,self.size)
            return True
        return False


    def add(self, item):
        '''Adds an item to the end of the array, allocating a larger array if necessary.'''
        if self._check_increase():
            self.data += alloc(5)
        self.data[self.size] = item
        if item == 'e':
            print(self.size)
        self.size += 1


    def insert(self, index, item):
        '''Inserts an item at the given index, shifting remaining items right and allocating a larger array if necessary.'''
        if self._check_bounds(index): 
            if self._check_increase():
                self.data += alloc(5)
            self.size += 1
            counter = self.size-1
            while counter >=0:
                if counter > index and counter != index:
                    self.data[counter] = self.data[counter-1]
                if counter == index:
                    self.data[counter] = item
                counter -= 1
        else:
            raise Exception('Index not within bounds')


    def set(self, index, item):
        '''Sets the given item at the given index.  Throws an exception if the index is not within the bounds of the array.'''
        if self._check_bounds(index):
            self.data[index]=item
        else: 
            raise Exception('Index not within bounds')
        


    def get(self, index):
        '''Retrieves the item at the given index.  Throws an exception if the index is not within the bounds of the array.'''
        if not self._check_bounds(index):
            raise Exception('Index not within bounds')
        return self.data[index]


    def delete(self, index):
        '''Deletes the item at the given index, decreasing the allocated memory if needed.  Throws an exception if the index is not within the bounds of the array.'''
        if self._check_bounds(index):
            for i in range(self.size):
                if i >= index and i+1<self.size:
                    self.data[i] = self.data[i+1]
            self.size -= 1
            self._check_decrease
        else:
            raise Exception('Index not within bounds')


    def swap(self, index1, index2):
        '''Swaps the values at the given indices.'''
        if not self._check_bounds(index1):
            raise Exception('Index not within bounds')
        if not self._check_bounds(index2):
            raise Exception('Index not within bounds')
        test = self.data[index1]
        self.data[index1]=self.data[index2]
        self.data[index2]=test




###################################################
###   Utilities

def alloc(size):
    '''
    Allocates array space in memory. This is similar to C's alloc function.
    '''
    data = []
    for i in range(size):
        data.append(None)
    return data


def memcpy(dest, source, size):
    '''
    Copies items from one array to another.  This is similar to C's memcpy function.
    '''
    allocsize = math.ceil(size/5)*5
    dest = alloc(allocsize)
    for i in size:
        dest[i] = source[i]
    return dest

