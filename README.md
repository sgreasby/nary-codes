# nary-codes

Get more info about the theory at https://hadamardcodes.com

## Description
This repository contains algorithms for generating n-ary
alphabet code sequences and sample implementation code.

When n=2 (2-ary or binary), the algorithm generates a
special case code, a Hadamard code. This algorithm
generates the general case family of codes for any n>=2.

## Requirements
All scripts are compatible with both Python 2 and Python 3.
The plot_matrix.py script requires matplotlib.

## Usage
All scripts are executed from the command line as shown below.
It is recommended that users begin with n=2 and order=1.
Then, increment either "n" or "order" and run the script(s) again.
The matrix size grow exponentially so large values of "n" or "order" will significantly impact processing time.

**print_matrix.py** - Prints the specified n-ary matrix to the screen.  
Usage: `python print_matrix.py [n] [order]`  
&nbsp;&nbsp;&nbsp;&nbsp;where n>=2 and order >= 1

Example Output:

![Printout of Second Order 3-ary Code Matrix](3-ary_code_order2.png?raw=true "Printout of Second Order 3-ary Code Matrix")

**plot_matrix.py** - Plots a graphical representation of the specified n-ary matrix.  
Usage: `python plot_matrix.py [n] [order] {options}`  
&nbsp;&nbsp;&nbsp;&nbsp;where n>=2 and order >= 1  
&nbsp;&nbsp;&nbsp;&nbsp;options include:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'color'(default) or 'grayscale'  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'show'(default) or 'hide' the axis

Example Output:

![Plot of Second Order 4-ary Code Matrix](4-ary_code_order2.png?raw=true "Plot of Second Order 4-ary Code Matrix")

**encode.py** - Encodes the specified string using a 16-ary alphabet code sequence  
Usage: `python encode.py [code] [string]`  
&nbsp;&nbsp;&nbsp;&nbsp;where 0<=code<16

Example Output:

![Printout of Encoded/Decoded String](encode.png?raw=true "Printout of Encoded/Decoded String")



