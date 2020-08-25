#!/usr/bin/env python
###########################################################
"Sample of how to encode/decode text strings"

__author__     = "Steven Greasby"
__copyright__  = "Copyright (C) 2015-2020 Steven Greasby"
__license__    = "GPL 2.0"
__url__        = "http://github.com/sgreasby/nary-codes"
__maintainer__ = "Steven Greasby"
###########################################################

import code_gen as cg
import sys
import binascii

usage = ("Usage: %s [code] [string]\n"
         "       0<=code<16 ")

# Parse Arguments
if len( sys.argv ) != 3:
    print( usage % sys.argv[0] )
    sys.exit()

try:
    code = int( sys.argv[1] )
except ValueError:
    print( usage % sys.argv[0] )
    sys.exit()

string = sys.argv[2]
n = 16

if ( code < 0 ) or ( code >= n ):
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
    x = 0;
    y = code
    
    # step through each digit
    # apply n=16 code to each digit
    y_components = cg.get_components( n, y )
    output = ''
    for char in string:
        x_components = cg.get_components( n, x )
        x += 1
        code_letter = cg.get_code_letter( n, x_components, y_components )
        nib0 = ( ord( char ) & 0x0f ) + code_letter
        if nib0 >= n:
            nib0 -= n

        x_components = cg.get_components( n, x )
        x += 1
        code_letter = cg.get_code_letter( n, x_components, y_components )
        nib1 = ( ord( char ) >> 4 ) + code_letter
        if nib1 >= n:
            nib1 -= n
        output += chr( nib0 | ( nib1 << 4 ) )
    return output

def decode( n, code, string ):
    x = 0
    y = code

    # step through each digit
    # remove n=16 code to each digit
    y_components = cg.get_components( n, y )
    output = ''
    for char in string:
        x_components = cg.get_components( n, x )
        x += 1
        code_letter = cg.get_code_letter( n, x_components, y_components )
        nib0 = ( ord( char ) & 0x0f ) - code_letter
        if nib0 < 0:
            nib0 += n

        x_components = cg.get_components( n, x )
        x += 1
        code_letter = cg.get_code_letter( n, x_components, y_components )
        nib1 = ( ord( char ) >> 4 ) - code_letter
        if nib1 < 0:
            nib1 += n
        output += chr( nib0 | ( nib1 << 4 ) )
    return output

print( "Encoding: %s" % string )

string2 = encode( n, code, string )
string3 = decode( n, code, string2 )

for idx in range( len(string) ):
    print( "\'%s\': 0x%02x -> 0x%02x -> 0x%02x" % ( string[idx], ord(string[idx]), ord(string2[idx]), ord(string3[idx]) ) )

print( "Decoded: %s" % string3 )

