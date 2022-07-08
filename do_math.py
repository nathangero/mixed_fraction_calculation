'''
Calculate any fractions whether they're improper, proper, or mixed. 
These functions also will format the result properly. 
- E.G. convert any improper fractions to mixed fractions: 9/8 -> 1&1/8
- E.G. If result is a whole number, don't have any fraction or decimal: 1/2 + 1/2 = 1
'''

from fractions import Fraction
import check_syntax as c

MULTIPLY = "*"
DIVIDE = "/"
ADD = "+"
SUBTRACT = "-"
MOD = "%"

def doMath(input) -> str:
    # print("@doMath")
    
    split = input.split()
    
    # First check for fractions in the equation
    for index, element in enumerate(split):
        # print("index:", index, "| element:", element)
    
        # determine if the index is odd or even numbered (relative to index number since we start at index 0)
        oddEvenIndex = index % 2 
        isEven = False
        
        if oddEvenIndex == 0:
            isEven = True
        else:
            isEven = False
        
        # If the index is even, check numbers/fractions are there
        if isEven:
            # Update the list with the new decimal value
            if "&" in element:
                split[index] = calculateMixedFraction(element) 
                     
            elif "/" in element:
                split[index] = round(float(eval(element)), 3)
                
    # print("new split:", split)
    # print()
    
    # Put the split list back as a string to use eval()
    toEval = ""
    
    # Calculate the string by putting the list back into a string so we can call eval()
    for index, element in enumerate(split):
        oddEvenIndex = index % 2 
        isEven = False
        
        if oddEvenIndex == 0:
            isEven = True
        else:
            isEven = False
            
        if isEven:
            toEval += str(element) # Convert numbers to string values
            
        else:
            toEval += element # Concat operator to string
            
        if index < len(split) - 1:
            toEval += " " # Add whitespace
            
    # print("toEval:", toEval)
    
    evaluatedStr = str(eval(toEval))
    # print("initial evaluatedStr:", evaluatedStr)
    
    # Check if the result is a decimal that needs to be converted to a fraction
    if "." in evaluatedStr:
        evaluatedStr = str(round(float(eval(toEval)), 3)) # Round to 2 decimals
        # print("evaluatedStr:", evaluatedStr)
        # print()
        # Convert any decimals to fractions
        mixFracResult = convertToMixedFraction(evaluatedStr)
    
    else: # The result is a whole number
        mixFracResult = evaluatedStr
        
    return mixFracResult

# Gets the decimal value of the mixed fraction
def calculateMixedFraction(input) -> float:
    # print("@calculateMixedFraction")
    
    # We calculate mixed fractions by
    #   multiplying the denominator and the whole number, 
    #   then add that product to the numerator,
    #   finally put that new sum over the denominator
    
    # 1 * 3&5/9 = 3.556
    
    splitMixed = input.split("&") # Separate the whole number from the fraction
    splitFraction = splitMixed[1].split("/") # Separate the numerator from the denominator
    
    # print("splitMixed:", splitMixed)
    # print("splitFraction:", splitFraction)
    # print()
    
    
    whole = splitMixed[0]
    numer = splitFraction[0]
    denom = splitFraction[1]
    multiplyWholeToDenom = 0
        
    # print("whole:", whole)
    # print("numer:", numer)
    # print("denom:", denom)
    # print()
    
    multiplyWholeToDenom = abs(int(whole)) * int(denom)
    # print("multiplyWholeToDenom:", multiplyWholeToDenom)
    newNumer = multiplyWholeToDenom + int(numer)
    improperFrac = str(newNumer) + "/" + str(denom)
    fracToDecimal = round(float(eval(improperFrac)), 3) # Round to 3 decimals for better calculation
    
    # Check if negative
    if "-" in whole:
        improperFrac = "-" + improperFrac
        fracToDecimal *= -1 # Make result negative
    
    # print("mixed fraction:", input)
    # print("improper fraction:", improperFrac)
    # print("eval improperFrac:", fracToDecimal)
    # print()
    
    return fracToDecimal

# Take decimal and convert it to a fraction
def convertToMixedFraction(input) -> str:
    output = ""

    split = input.split(".") # split the decimal from the whole number
    # print("input:", input)
    # print("split:", split)
    whole = split[0]
    decimal = split[1]
    decimal = "." + split[1] # Add back the decimal
        
    decimalToFrac = str(Fraction(float(decimal)).limit_denominator()) # Convert to a fraction. limit_denominator() helps reduces the fraction
        
    
    # Check for 0's for proper formating
    if whole == "0":
        output = decimalToFrac # Only include the fraction
        
    elif whole == "-0":
        output = "-" + decimalToFrac # Add back the negative sign
        
    elif split[1] == "0":
        output = whole
    
    else:
        output = str(whole) + "&" + decimalToFrac # Add back the whole number
        
    # print("output:", output)
    # print()
    
    return output

