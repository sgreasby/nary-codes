###########################################################
"Algorithm for N-ary Alphabet Code Generation"

__author__     = "Steven Greasby"
__copyright__  = "Copyright (C) 2015-2020 Steven Greasby"
__license__    = "GPL 2.0"
__url__        = "http://github.com/sgreasby/nary-codes"
__maintainer__ = "Steven Greasby"
###########################################################

###########################################################
# Extract base-n components from the provided index
#
# Creates a list of [index%n,(index/n)%n,(index/n**2)%n,...]
# where index 0 contains the "ones" digit, index 1 contains
# the n's digit, index 2 contains the (n**2)'s digit, etc.
#
# Example: n=16, code=42
# decimal 42 in base-16 is 0x2a (using std. hex notation)
# The first digit is 0xa which is 10. The second digit is
# 0x2 which is just 2. So the returned list would be [10,2]
#
# Return: The base-n list
###########################################################
def get_components( n, index ):
    components = []
    while index > 0:
        components.append( int( index % n ) )
        index = int( index / n )
    return components

###########################################################
# Get the base-n code letter for first order coordinates.
#
# Calculate the code letter for first order coordinates.
# That is, coordinates where 0 <= x <= n and 0<= y <= n.
#
# Return: The base-n code letter
###########################################################
def get_first_order_code( n, x, y ):
    if ( x == 0 ) or ( y == 0 ):
        code_letter = 0
    else:
        code_letter = ( x + y - 1)
        if code_letter >= n:
            code_letter -= ( n - 1 )
    return code_letter

###########################################################
# Get the base-n code letter for the indicated coordinate.
#
# The code letter is calculated by finding the code letter
# of each x/y component index in the first_order code
# matrix, and summing those values together. Finally, the
# code is decremented until it is less than n.
#
# Return: The base-n code letter
###########################################################
def get_code_letter( n, x_components, y_components ):
    code_letter = 0;
    # If len(x_components)>len(y_components) then the codes
    # then the code will repeat, just calculate using lower
    # order code.
    if( len( x_components ) > len( y_components ) ):
        x_components = x_components[:len(y_components)]
    for i in range( len( x_components ) ):
        code_letter += get_first_order_code( n, x_components[i], y_components[i] )
        if code_letter >= n:
            code_letter -= n
    return code_letter
