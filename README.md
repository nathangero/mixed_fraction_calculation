# About

Code will be evaluated on these criteria:

The solution builds and runs. Instructions are helpful.
The program gives the correct answers.
Errors are handled and reported.
The code is well structured and can be readily understood.
The code has been tested and includes evidence of such (hint: unit tests).
 
The Problem

Write a command-line program that takes operations on fractions as input and produces a fractional result.

The command-line program shall repeatedly prompt the user for input and display the result until user types "exit".
Legal operators shall be *,  /,  +,  -,  % (multiply, divide, add, subtract, modulo).
Operands and operators shall be separated by one or more spaces.
Mixed numbers shall be represented by whole&numerator/denominator; for example, "3&1/4", “-1&7/8”.
Improper fractions, whole numbers, and negative numbers are allowed as operands.

** Additional info
You may assume that the fraction expression is only comprised of integers, no decimals.

For a single operand and no operator, if it is a whole number, just return the whole number.  
If a fraction, return fraction reduced to lowest terms.
 

Example runs (where '?' represents the command prompt):
? 1/2 * 3&3/4
= 1&7/8

? 2&3/8 + 9/8
= 3&1/2 

? 1&3/4 - 2
= -1/4

? 11 % 3
= 2

## How to run
* In the folder directory, run "python3 main.py" to enter user input. User input will continually be asked for until the user types "exit" 
* To run the test cases, in the folder directory, run "python3 test_cases.py" and all the test cases created will run.
