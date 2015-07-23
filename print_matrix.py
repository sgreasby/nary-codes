#!/usr/bin/env python
###########################################################
"Generate a (n**order)x(n**order) code matrix"

__author__     = "Steven Greasby"
__copyright__  = "Copyright (C) 2015 Steven Greasby"
__license__    = "GPL 2.0"
__url__        = "http://github.com/sgreasby/nary-codes"
__maintainer__ = "Steven Greasby"
###########################################################

import code_gen as cg
import sys

usage = ("Usage: %s [n] [order]\n"
         "       where n>=2 and order >= 1")

# Parse Arguments
if len( sys.argv ) != 3:
    print( usage % sys.argv[0] )
    sys.exit()

try:
    n = int(sys.argv[1])
except ValueError:
    print( usage % sys.argv[0] )
    sys.exit()

try:
    order = int( sys.argv[2] )
except ValueError:
    print( usage % sys.argv[0] )
    sys.exit()

if ( n < 2 ) or ( order < 1 ):
    print( usage % sys.argv[0] )
    sys.exit()

size = n ** order

g = []
# Walk through every x,y pair and get the code letter (g)
for code in range( size ):
    y0 = cg.get_y0( n, code )
    g.append( [] )
    for index in range( size ):
        ( x, y ) = cg.get_xy( n, index, y0 )
        g[code].append( cg.get_g( n, x, y ) )
    print( g[code] )

