#!/usr/bin/env python3

from datetime import datetime
import time
import base2, base16, base58

CONVERTERS = {
    2: (base2.convert, base2.invert),
    16: (base16.convert, base16.invert),
    58: (base58.convert, base58.invert)
}

##############################################################################################################################################################################
#  A uid class based on time, counter, and shard id.                                                                                                                         #
#                                                                                                                                                                            #
# |                | Time Component                 | Time Component                            | Space Component                                                            |
# |----------------|--------------------------------|-------------------------------------------|----------------------------------------------------------------------------|
# | Number of Bits | 42 bits                        | 13 bits                                   | 8 bits                                                                     |
# | Description    | Milliseconds since Jan, 1970   | Counter (allows more than one UID per ms) | Shard ID (assigned explicitly to a server, process, or database)           |
# | Maximum Value  | 4,398,046,511,104 (May, 2109)  | 8,192 per ms                              | 256 unique locations                                                       |


# range is 0-255
SHARD_ID = 129

# sizes
MILLIS_BITS = 42
COUNTER_BITS = 13
SHARD_BITS = 8

# the masks
MILLIS_MASK = 0b111111111111111111111111111111111111111111000000000000000000000
COUNTER_MASK = 0b111111111111100000000
SHARD_MASK = 0b11111111


LAST_MILLIS = 0
COUNTER = 0


def generate(base=10):
    '''Generates a uid with the given base'''
    # get the millisecond, waiting if needed if we've hit the max counter
    # reset the counter if we are in a new millisecond
    # pack it up and convert base
    global COUNTER
    global LAST_MILLIS
    if COUNTER==8192:
        time.sleep(.001)
        COUNTER=0
    LAST_MILLIS = int(round(time.time() * 1000))
    COUNTER=COUNTER+1
    bitmillis = format(LAST_MILLIS,'042b')
    bitcounter = format(COUNTER,'013b')
    bitshard = format(SHARD_ID,'08b')
    bituid = bitmillis+bitcounter+bitshard
    uid = base2.invert(bituid)
    return uid


def pack(millis, counter, shard):
    '''Combines the three items into a single uid number'''
    bitmilli = format(millis,'042b')
    bitcounter = format(counter, '013b')
    bitshard = format(shard, '08b')
    bituid = bitmilli+bitcounter+bitshard
    uid = base2.invert(bituid)
    return uid


def unpack(uid):
    '''Separates the uid into its three parts'''
    bituid = format(uid,'063b')
    bitmillis = bituid[0:42]
    bitcounter = bituid[42:55]
    bitshard = bituid[55:63]
    millis = base2.invert(bitmillis)
    counter = base2.invert(bitcounter)
    shard = base2.invert(bitshard)
    return (millis, counter, shard)
