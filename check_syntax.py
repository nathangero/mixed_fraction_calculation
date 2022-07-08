'''
Check the syntax of all inputs.
Check if input contains any letters, decimals, or general bad syntax 
- E.G. Check for letters: 1/a, 1&a/8 -> raise exception
- E.G. Check for decimals: 0.3, 1&0.3/8 -> raise exception
- E.G. Bad syntax 1/2 1/2, 1/2 * *, 1/2 * -> raise exception
'''

import numbers

from numpy import isin # used for checking numbers
import custom_errors as e
import do_math as m

LEGAL_OPERATORS = ["*", "/",  "+",  "-",  "%"] # Only allow multiply, divide, add, subtract, and modulo operator

# Check the syntax of the input. Raise exceptions where necessary
def checkSyntax(input) -> str:    
    # print("@checkSyntax")
    split = input.split()
    # print("split:", split)
    
    inputLength = len(split)
    # print("inputLength:", inputLength)
    # print("is even numbered?", inputLength % 2)
    
    
    if inputLength == 1:
        # Check if a valid fraction or integer. 
        if "&" in input: # Check for a sole mixed fraction. If valid, calculate it
            if not isMixedFraction(input):
                raise e.InvalidMixedFraction
            
        elif "/" in input: # Check for a sole fraction.
            if not isValidFraction(input):
                raise e.InvalidFraction
        
        else:
            if isInteger(input, True, False, False):
                return input # Just return the integer input. No need to calculate it
            else:
                raise e.InvalidInteger
        
    elif inputLength % 2 == 0: # if the amount of operators/oprands plugged in is an even number, math can't be done
        raise e.InvalidOperatorOperandSyntax
    
    else: # if a full equation with at least "fraction/integer OPERATOR fraction/integer"
        for index, element in enumerate(split):
            # print("index:", index, "| element:", element)
        
            # determine if the index is odd or even numbered (relative to index number since we start at index 0)
            oddEvenIndex = index % 2 
            isOdd = False
            
            if oddEvenIndex == 0:
                isOdd = False
            else:
                isOdd = True
                
            # print("oddEvenIndex:", oddEvenIndex)
            # print("isOdd?", isOdd)
            # print()
            
            # If the index is odd, check if numbers are there
            if isOdd:
                if element not in LEGAL_OPERATORS:
                    raise e.OperatorSyntaxError
                
            # If the index is even, check if numbers/fractions are there
            else:
                if element in LEGAL_OPERATORS: # Check if operators are here 
                    raise e.OperatorSyntaxError
                
                elif "&" in element or "/" in element: # Check if valid fraction
                    if not isValidFraction(element):
                        raise e.InvalidFraction
                    

    # print("NO ERROR!")
    # print()
    
    # We want to send the original input
    result = m.doMath(input)
    return result

# Checks if input is a valid integer.
def isInteger(input, isInteger, isMixed, isFraction) -> bool:
    # print("@isInteger")
    # print("input:", input)
    if isinstance(int(input), numbers.Number): # Checks against decimals and letters
        return True
        
    else: # Raise the appropriate exception
        if isInteger:
            raise e.InvalidInteger
        elif isMixed:
            raise e.InvalidMixedFraction
        elif isFraction:
            raise e.InvalidFraction
        else:
            raise e.InvalidOperatorOperandSyntax

# Checks if a fraction is normal or mixed, and then does a validation check on that fraction
def isValidFraction(input) -> bool:
    # print("@isValidFraction")

    if "&" in input: # Check for mixed fraction
        if not isMixedFraction(input):
            raise e.InvalidMixedFraction
        
        else:
            return True 
        
    if "/" in input: # Check for a non mixed fraction. Also accepts improper fractions
        if not isNormalFraction(input, False):
            raise e.InvalidFraction
        
        else:
            return True 


# Helper to isValidFraction(). Checks if the mixed fraction is valid. Checks if both sides of the & are valid numbers and a valid fraction
def isMixedFraction(input) -> bool:
    # print("@isMixedFraction")
    split = input.split("&")
    # print("split:", split)
    # print()
    
    # Mixed fractions should only consist of 3 parts: whole number, &, fraction part. We ignore & since we used split()
    if len(split) != 2:
        raise e.InvalidMixedFraction
        
    else:
        if not isInteger(split[0], False, True, False): # Check if the number in front is an integer
            raise e.InvalidMixedFraction
        
        elif not isNormalFraction(split[1], True): # Check if the fraction is valid
            raise e.InvalidMixedFraction
                
        else:
            return True
           
           
# Checks if the fraction is improper or not
def isImproperFraction(input) -> bool:
    split = input.split("/")
    numer = split[0]
    denom = split[1]
    
    if numer > denom:
        return True
    else:
        return False

# Helper to isValidFraction(). Checks if the fraction is valid. Checks if both sides of the / are valid numbers
def isNormalFraction(input, isMixed) -> bool:
    # print("@isNormalFraction")
    split = input.split("/")
    # print("split:", split)
    # print()
    
    # Normal fractions should only consist of 3 parts: whole number, /, whole number. We ignore / since we used split()
    if len(split) != 2:
        raise e.InvalidFraction
    
        
    for element in split:
        # print("element:", element)
            
    
        if not isInteger(element, False, False, True):  # Check if numerator and denominator are valid integers
            # print("isMixed?", isMixed)
            if isMixed:
                raise e.InvalidMixedFraction
            else:
                raise e.InvalidFraction
            
    return True
