#!/usr/bin/env python3


class LinkedList(object):
    '''
    A linked list implementation that holds arbitrary objects.
    '''

    def __init__(self):
        '''Creates a linked list.'''
        self.head = None
        self.size = 0


    def debug_print(self):
        '''Prints a representation of the entire list.'''
        output = '{} >>> {}'.format(self.size, ', '.join([ str(item) for item in self ]))
        print(output)
        return output


    def __iter__(self):
        '''Iterates through the linked list, implemented as a generator.'''
        for node in self._iter_nodes():
            yield node.value


    def _iter_nodes(self):
        '''Iterates through the nodes of the list, implemented as a generator.'''
        current = self.head
        while current != None:
            yield current
            current = current.next


    def _get_node(self, index):
        '''Retrieves the Node object at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        if index >= self.size:
            raise Exception('value not within index')
        else:
            return True

    def add(self, item):
        '''Adds an item to the end of the linked list.'''
        nn = Node(item)
        if self.head == None:
            self.head = nn
            self.size += 1
        else:
            ogn = None
            for i in self._iter_nodes():
                print(i.value)
                if i.next == None:
                    ogn = i
            ogn.next = nn
            self.size += 1

    def insert(self, index, item):
        '''Inserts an item at the given index, shifting remaining items right.'''
        if self._get_node(index):
            counter = 0
            ogn = None
            for i in self._iter_nodes():
                if counter == index-1:
                    ogn = i
                counter += 1
            nn = Node(item)
            nn.next = ogn.next
            ogn.next = nn
            self.size += 1

    def set(self, index, item):
        '''Sets the given item at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        if self._get_node(index):
            counter = 0
            for i in self._iter_nodes():
                if counter == index:
                    i.value = item
                counter += 1


    def get(self, index):
        '''Retrieves the item at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        if self._get_node(index):
            counter = 0
            for i in self._iter_nodes():
                if counter == index:
                    return i.value
                counter += 1

    def delete(self, index):
        '''Deletes the item at the given index. Throws an exception if the index is not within the bounds of the linked list.'''
        if self._get_node(index):
            prev = None
            dele = None
            counter = 0
            for i in self._iter_nodes():
                if counter == index - 1:
                    prev = i
                if counter == index:
                    dele = i
                counter += 1
            if dele is None:
                prev.next = None
            elif prev is None:
                pass
            else:
                prev.next = dele.next
            self.size -= 1
            

    def swap(self, index1, index2):
        '''Swaps the values at the given indices.'''
        if self._get_node(index1) and self._get_node(index2):
            counter = 0
            i1 = None
            i2 = None
            for i in self._iter_nodes():
                if counter == index1:
                    i1 = i
                if counter == index2:
                    i2 = i
                counter += 1
            val = i1.value
            i1.value = i2.value
            i2.value = val


######################################################
###   A node in the linked list

class Node(object):
    '''A node on the linked list'''

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return '<Node: {}>'.format(self.value)
