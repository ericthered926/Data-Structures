#!/usr/bin/env python3
import os, os.path, binascii
from collections import namedtuple
from io import StringIO
from PIL import Image


# a named tuple to hold an individual key and value
# this Node "object" is never seen outside this class
# (e.g. get() returns the value, not the full Node)
Node = namedtuple("Node", ( 'key', 'value' ))

# This is super small because we want to test the loading and print for debugging easier
NUM_BUCKETS = 10


class Hashtable(object):
    '''
    An abstract hashtable superclass.
    '''
    def __init__(self):
        self.buckets = []
        #TODO: initialize the buckets to empty lists
        for i in range(NUM_BUCKETS):
            self.buckets.append([])


    def set(self, key, value):
        '''
        Adds the given key=value pair to the hashtable.
        '''
        #TODO: store the value by the hash of the key
        index = self.get_bucket_index(key)
        self.buckets[index].append(Node(key,value))


    def get(self, key):
        '''
        Retrieves the value under the given key.
        Returns None if the key does not exist.
        '''
        #TODO: get the value by the hash of the key
        index = self.get_bucket_index(key)
        for i in self.buckets[index]:
            if i.key is key:
                return i.value


    def remove(self, key):
        '''
        Removes the given key from the hashtable.
        Returns silently if the key does not exist.
        '''
        #TODO: remove the value by the hash of the key
        index = self.get_bucket_index(key)
        for i in self.buckets[index]:
            if i.key == key:
                self.buckets[index].remove(i)
        


    def get_bucket_index(self, key):
        '''
        Returns the bucket index number for the given key.
        The number will be in the range of the number of buckets.
        '''
        # leave this method as is - write your code in the subclasses
        pass



    ##################################################
    ###   Helper methods

    def __repr__(self):
        '''Returns a representation of the hash table'''
        buf = StringIO()
        for i, bkt in enumerate(self.buckets):
            for j, node in enumerate(bkt):
                buf.write('{:>5}  {}\n'.format(
                    '[{}]'.format(i) if j == 0 else '',
                    node.key,
                ))
        return buf.getvalue()



######################################################
###   String hash table

class StringHashtable(Hashtable):
    '''A hashtable that takes string keys'''

    def get_bucket_index(self, key):
        '''
        Returns the bucket index number for the given key.
        The number will be in the range of the number of buckets.
        '''
        #TODO: hash the string and return the bucket index that should be used
        ans = 0
        for ch in key:
            ans += ord(ch)
        return ans % NUM_BUCKETS



######################################################
###   Guid hash table

COUNTER_CHARS = ( 16, 24 )

class GuidHashtable(Hashtable):
    '''A hashtable that takes GUID keys'''

    def get_bucket_index(self, key):
        '''
        Returns the bucket index number for the given key.
        The number will be in the range of the number of buckets.
        '''
        #TODO: hash the string and return the bucket index that should be used

        ans = 0
        for ch in key:
            ans += ord(ch)
        return ans % NUM_BUCKETS


######################################################
###   Image hash table

NUM_CHUNKS = 8

class ImageHashtable(Hashtable):
    '''A hashtable that takes image name keys and creates the hash from (some of) the bytes of the file.'''

    def get_bucket_index(self, key):
        '''
        Returns the bucket index number for the given key.
        The number will be in the range of the number of buckets.
        '''
        #TODO: hash the string and return the bucket index that should be used
        png = Image.open("./images/"+key)
        png.load() # required for png.split()

        background = Image.new("RGB", png.size, (255, 255, 255))
        background.paste(png, mask=png.split()[3]) # 3 is the alpha channel
        ans = 0
        load = background.load()
        for x in range(50):
            ans += load[x,x][0]
        return ans % NUM_BUCKETS