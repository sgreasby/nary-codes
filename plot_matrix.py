#!/usr/bin/env python
###########################################################
"Draw a (n**order)x(n**order) code matrix"

__author__     = "Steven Greasby"
__copyright__  = "Copyright (C) 2015-2020 Steven Greasby"
__license__    = "GPL 2.0"
__url__        = "http://github.com/sgreasby/nary-codes"
__maintainer__ = "Steven Greasby"
###########################################################

import code_gen as cg
import sys
import matplotlib as mpl
import matplotlib.pyplot as plt

usage = ("Usage: %s [n] [order] {options} \n"
         "       where n>=2 and order >= 1\n"
         "       options include:\n"
         "           'color'(default) or 'grayscale'\n"
         "           'show'(default) or 'hide' the axis")

# Parse Arguments
if len( sys.argv ) < 3:
    print( usage % sys.argv[0] )
    sys.exit()

try:
    n = int( sys.argv[1] )
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

for arg in sys.argv[3:]:
    error = False
    if arg == 'grayscale':
        if 'plot_color' in locals():
            error = True
        plot_color = False
    elif arg == 'color':
        if 'plot_color' in locals():
            error = True
        plot_color = True
    elif arg == 'hide':
        if 'draw_axis' in locals():
            error = True
        draw_axis = False
    elif arg == 'show':
        if 'draw_axis' in locals():
            error = True
        draw_axis = True
    else:
        error = True

    if error is True:
        print( usage % sys.argv[0] )
        sys.exit()

# Set defaults if not specified by argument list
if 'plot_color' not in locals():
    plot_color = True
if 'draw_axis' not in locals():
    draw_axis = True

size = n ** order

fig = plt.figure()
ax = fig.add_subplot( 111 )

plt.axis( 'scaled' )
plt.xlim( [0,size] )
plt.ylim( [0,size] )
plt.gca().invert_yaxis()

# Walk through every x,y pair to build the code letter matrix
# Then plot a grayscale or color square representing the
# code letter at the appropriate coordinates
for y in range(size):
    y_components = cg.get_components( n, y )
    for x in range(size):
        if( x<y ):
            # Already plotted using symmetry
            continue
        x_components = cg.get_components( n, x )
        code_letter = cg.get_code_letter( n, x_components, y_components)
        if plot_color is True:
            shade = float( code_letter ) / n
            rect = mpl.patches.Rectangle( ( x, y ), 1, 1, color=mpl.colors.hsv_to_rgb( [shade,1,1] ) )
            ax.add_patch( rect )
            # Due to diagonal symmetry, the values at x,y and y,x are the same
            rect = mpl.patches.Rectangle( ( y, x ), 1, 1, color=mpl.colors.hsv_to_rgb( [shade,1,1] ) )
            ax.add_patch( rect )
            
                
        else:
            shade = 1 - float( code_letter ) / ( n - 1 )
            rect = mpl.patches.Rectangle( ( x, y ), 1, 1, color=mpl.colors.hsv_to_rgb( [0,0,shade] ) )
            ax.add_patch( rect )
            # Due to diagonal symmetry, the values at x,y and y,x are the same          
            rect = mpl.patches.Rectangle( ( y, x ), 1, 1, color=mpl.colors.hsv_to_rgb( [0,0,shade] ) )
            ax.add_patch( rect )

if draw_axis:
    ax.set_xlabel( 'index' )
    ax.set_ylabel( 'code' )

else:
    ax.get_xaxis().set_visible( False )
    ax.get_yaxis().set_visible( False )

plt.show()
