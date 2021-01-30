#!/usr/bin/env python3

class BaseXConverter(object):
    '''
    Converts positive, base-10 numbers to base-X numbers using a custom alphabet.
    The base is given by the length of the alphabet specified in the constructor.
    The first character in the alphabet has a value of zero,
    the second character a value of one, and so forth.

    Examples:
        Base2:  BaseXConverter('01')
        Base2:  BaseXConverter('<>')     # custom alphabet: < is a zero value and > is a one value
        Base4:  BaseXConverter('0123')
        Base20: BaseXConverter('0123456789abcdefghij')

    See the unit tests at the bottom of the file for many examples.
    '''

    def __init__(self, alphabet):
        '''
        The base is taken from the number of characters in the alphabet.
        '''
        self.alphabet = list(alphabet)
        self.base = len(alphabet)
        self.alphabet_index = {}

    def convert(self, val):
        '''
        Converts value from base 10 to base X.
        The return value is a baseX integer, wrapped as a string.
        '''
        bXval = ''
        innum = val
        while innum!=0:
            remainder = int(innum%self.base)
            remstr = self.alphabet[remainder]
            bXval = remstr+bXval
            innum = innum/self.base
        bXval = bXval.lstrip('0')
        return bXval

    def invert(self, bXval):
        '''
        Converts a value from base X to base 10.
        The bXval should be a baseX integer, wrapped as a string.
        Raises a ValueError if bXval contains any chars not in the alphabet.
        '''
        for i in bXval:
            if i not in str(self.alphabet):
                raise ValueError("incorrect value")
        figures = [int(i,self.base) for i in bXval]
        figures = figures[::-1]
        val = 0
        #loop over all figures
        for i in range(len(figures)):
            #add the contirbution of the i-th figure
            val += int(figures[i])*self.base**i
        return val
