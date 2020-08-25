#!/usr/bin/env python
###########################################################
"Generate a (n**order)x(n**order) code matrix"

__author__     = "Steven Greasby"
__copyright__  = "Copyright (C) 2015-2020 Steven Greasby"
__license__    = "GPL 2.0"
__url__        = "http://github.com/sgreasby/nary-codes"
__maintainer__ = "Steven Greasby"
###########################################################

import code_gen as cg
import sys
import numpy as np

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

# Create matrix of -1
matrix = np.ones([size,size])

# Walk through every x,y pair to build the code letter matrix
for y in range(size):
    y_components = cg.get_components( n, y )
    for x in range(size):
        if( x<y ):
            # Already calculated using symmetry
            continue

        x_components = cg.get_components( n, x )
        matrix[y,x] = cg.get_code_letter( n, x_components, y_components)
        # The matrix has diagonal symmetry so value at matrix[y,x]
        # is same as at matrix[x,y]
        matrix[x,y] = matrix[y,x]

print( matrix )

