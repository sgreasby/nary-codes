#!/usr/bin/env python
###########################################################
"Sample of how to encode/decode text strings"

__author__     = "Steven Greasby"
__copyright__  = "Copyright (C) 2015 Steven Greasby"
__license__    = "GPL 2.0"
__url__        = "http://github.com/sgreasby/nary-codes"
__maintainer__ = "Steven Greasby"
###########################################################

import code_gen as cg
import sys
import binascii

usage = ("Usage: %s [n] [code] [string]\n"
         "       where n==16 and code >= 0 ")

# Parse Arguments
if(len(sys.argv) != 4 ):

    print( usage % sys.argv[0] )
    sys.exit()

try:
    n = int(sys.argv[1])
except ValueError:
    print( usage % sys.argv[0] )
    sys.exit()

try:
    code = int(sys.argv[2])
except ValueError:
    print( usage % sys.argv[0] )
    sys.exit()

string = sys.argv[3]

if( n != 16 ) or ( code < 0 ):
    print( usage % sys.argv[0] )
    sys.exit()

# This is a simple example of how to encode/decode text strings
# Code number zero does no encoding and code numbers that are perfect
# powers of the alphabet count (n) (i.e. n**1, n**2, n**3,...) provide
# very little encoding. It is suggested that those codes are avoided.
# Also, since some characters may not be encoded, some small portions
# of encoded text may still be readable. This can be mitigated by
# double encoding (preferably using a different code length), or by
# using another sequence to transpose bits or groups of bits.

def encode( n, code, string ):
    print( "Encoding: %s" % string )

    # step through each digit 
    # apply n=16 code to each digit
    y0 = cg.get_y0( n, code )
    output=''
    index = 0;
    for char in string:
        (x,y) = cg.get_xy( n, index, y0 )
        index+=1
        g = cg.get_g( n, x, y )
        nib0 = (ord(char)&0x0f) + g
        if nib0 >= n:
            nib0 -= n

        (x,y) = cg.get_xy( n, index, y0 )
        index+=1
        g = cg.get_g( n, x, y )
        nib1 = (ord(char)>>4) + g
        if nib1 >= n:
            nib1 -= n
        output += chr(nib0|(nib1<<4))
    return output


def decode( n, code, string ):
    # step through each digit
    # remove n=16 code to each digit
    y0 = cg.get_y0( n, code )
    output=''
    index = 0
    for char in string:
        (x,y) = cg.get_xy( n, index, y0 )
        index+=1
        g = cg.get_g( n, x, y )
        nib0 = (ord(char)&0x0f) - g
        if nib0 < 0:
            nib0 += n

        (x,y) = cg.get_xy( n, index, y0 )
        index+=1
        g = cg.get_g( n, x, y )
        nib1 = (ord(char)>>4) - g
        if nib1 < 0:
            nib1 += n
        print( "0x%2x -> 0x%2x" % (ord(char), nib0|(nib1<<4)) )
        output += chr(nib0|(nib1<<4))
    print( "Decoded: %s" % output )
    return output


string2 = encode( n, code, string )
string3 = decode( n, code, string2)
