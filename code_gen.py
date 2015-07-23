###########################################################
"Algorithm for N-ary Alphabet Code Generation"

__author__     = "Steven Greasby"
__copyright__  = "Copyright (C) 2015 Steven Greasby"
__license__    = "GPL 2.0"
__url__        = "http://github.com/sgreasby/nary-codes"
__maintainer__ = "Steven Greasby"
###########################################################

###########################################################
# Convert code to base-n for use as y-coordinate index
#
# Converts a decimal code to a base-n value. The resulting
# base-n value is placed in a list, where index 0 contains
# the "ones" digit, index 1 contains the n's digit, index 2
# contains the (n**2)'s digit, etc.
#
# Example: n=16, code=42
# decimal 42 in base-16 is 0x2a (using std. hex notation)
# The returned list would therefore be [10,2]
#
# Return: The base-n list
###########################################################
def get_y0( n, code ):
    y0 = []
    while( code > 0 ):
        y0.append( int(code % n) )
        code = int( code / n )
    return y0


###########################################################
# Convert index to base-n for use as x-coordinate index
#
# Converts a decimal index to a base-n value. The resulting
# base-n value is placed in a list, where index 0 contains
# the "ones" digit, index 1 contains the n's digit, index 2
# contains the (n**2)'s digit, etc.
#
# The resulting x-index list is combined with the provided
# y0 list to create an x/y list tuple.
#
# All N-ary codes have diagonal symmetry. When looking
# at an individual column or row, the code sequences
# eventually repeat. This occurs when one either the x or y
# list is a higher order (greater length) than the other.
# If that is the case, the code sequence can be more easily
# calculated using a lower order code. This is done by
# limiting the length of the larger list to that of the
# smaller list.
#
# Return: x/y list tuple
###########################################################
def get_xy( n, index, y0 ):
    x = []
    while (index > 0) and (len(x)<len(y0)):
        x.append( int(index % n) )
        index = int( index / n )
    return (x,y0[:len(x)])


###########################################################
# Get the base-n code letter (g) for first order coordinates.
#
#
# Calculate the code letter (g) for first order coordinates.
# That is, coordinates where 0 <= x <= n and 0<= y <= n.
#
# Return: The base-n code letter (g)
###########################################################
def get_g0( n, x, y ):
    if (x==0) or (y==0):
        g0 = 0
    else:
        g0 = ( x + y - 1)
        if g0 >= n:
            g0 -= (n-1)
    return g0

###########################################################
# Get the base-n code letter (g) for the indicated coordinate.
#
# Letting p be the power of the code matrix, the code
# letter (g) is calculated as follows:
# g = G[x,y] = G[xp...x0,yp...y0] = sum(G0[xi,yi])%n
# Where i ranges from 0 to p.
#
# Return: The base-n code letter (g)
###########################################################
def get_g( n, x, y ):
    g = 0;
    for i in range(0, len(x)):
        g += get_g0(n,x[i],y[i])
        if g >= n:
            g -= n
    return g
