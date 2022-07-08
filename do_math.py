'''
Calculate any fractions whether they're improper, proper, or mixed. 
These functions also will format the result properly. 
- E.G. convert any improper fractions to mixed fractions: 9/8 -> 1&1/8
- E.G. If result is a whole number, don't have any fraction or decimal: 1/2 + 1/2 = 1

The idea behind the math is to calculate all the fractions through the eval() function. This returns the results in decimals,
so using the Fraction.limit_denomination(10) function will convert all the decimals to their most reduced fraction. Using
Fraction.limit_denomination(10) even works well for fractions with repeating decimals.
'''

from fractions import Fraction
import check_syntax as c


MULTIPLY = "*"
DIVIDE = "/"
ADD = "+"
SUBTRACT = "-"
MOD = "%"
DECIMAL_PLACE = 4  # Round to 4 decimals for better calculation

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
                split[index] = round(float(eval(element)), DECIMAL_PLACE)

                
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
        evaluatedStr = str(round(float(eval(toEval)), DECIMAL_PLACE))
        # print("evaluatedStr:", evaluatedStr)
        # print()
        # Convert any decimals to fractions
        mixFracResult = convertToMixedFraction(input, evaluatedStr)
    
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
    improperFrac = ""
        
    # print("whole:", whole)
    # print("numer:", numer)
    # print("denom:", denom)
    # print()
    
    multiplyWholeToDenom = abs(int(whole)) * int(denom)
    # print("multiplyWholeToDenom:", multiplyWholeToDenom)
    newNumer = multiplyWholeToDenom + int(numer)
    
    improperFrac = str(newNumer) + "/" + str(denom)
    fracToDecimal = round(float(eval(improperFrac)), DECIMAL_PLACE)
    # reducedMixedFrac = convertImproperToProperMixedFraction(improperFrac)
    
    # Check if negative
    if "-" in whole:
        improperFrac = "-" + improperFrac
        fracToDecimal *= -1 # Make result negative
        # reducedMixedFrac = "-" + reducedMixedFrac
    
    # print("mixed fraction:", input)
    # print("improper fraction:", improperFrac)
    # print("eval improperFrac:", fracToDecimal)
    # print("reduced mixed fraction:", reducedMixedFrac)
    # print()
    
    return fracToDecimal

# Take decimal and convert it to a fraction
# This will return the final string output
def convertToMixedFraction(input, evaluatedStr) -> str:
    output = ""
        
    split = evaluatedStr.split(".") # split the decimal from the whole number
    whole = split[0]
    decimal = split[1]
    decimal = "." + split[1] # Add back the decimal
    
    # print("input:", input)
    # print("evaluatedStr:", evaluatedStr)
    # print("split:", split)
    
    fraction = Fraction(float(decimal))
    decimalToFrac = str(fraction.limit_denominator(10)) # Convert to a fraction. limit_denominator(10) helps reduces the fraction
    
    # print("fraction:", fraction)
    # print("decimalToFrac:", decimalToFrac)
    # print()
    
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



# *** Unused functions ***
# Was going to use these functions before finding out about Fraction.limit_denominator(10)

# Convert improper fractions to mixed fractions
def convertImproperToProperMixedFraction(fraction) -> str:
    # print("@convertImproperToProperMixedFraction")
    split = fraction.split("/")    
    numer = abs(int(split[0]))
    denom = abs(int(split[1]))
    
    isNegative = False
    if "-" in fraction:
        isNegative = True

    whole = numer // denom # We want the floor of the division
    newNumer = numer % denom # we want the remainder as the new numerator
    newFrac = str(newNumer) + "/" + str(denom)
    
    if isRepeatingDecimal(newFrac):
        newFrac = reduceFraction(newNumer, denom)
        
    properMixedFraction = str(whole) + "&" + newFrac
    return properMixedFraction


# Checks if the fraction has a repeating decimal value or not.
def isRepeatingDecimal(fraction) -> bool:
    # print("@checkForRepeatingDecimal")
    # 2&3/8 + 9/8
    split = fraction.split("/")    
    numer = abs(int(split[0]))
    denom = abs(int(split[1]))
    
    result = False
    quotient_numer = [] # Store any repeating values and then check against them later
    while numer:
    	# In case the remainder is equal to zero, there are no repeating decimals. So, we return False
        remainder = numer % denom
        # print("\nremainder:", remainder)
        if remainder == 0:
            for i in quotient_numer:
                result = False
            break
        numer = remainder*10
        quotient = numer // denom
        
        # print("num:", numer)
        # print("quotient:", quotient)
        
		# If the new numerator and quotient are not already in the list, we add them to the list.
        if [numer, quotient] not in quotient_numer:
            quotient_numer.append([numer, quotient])
        
        elif [numer, quotient] in quotient_numer: # If the new numerator and quotient are instead already in the list, we return True
            # print("quotient_num", quotient_numer)
            result = True
            break
        
    return result
    
    
# Recursive function that will properly reduce fractions 
def reduceFraction(numer, denom) -> str:
    # print("@reduceFraction")
    # print("numer:", numer)
    # print("denom:", denom)

    if (numer / 9) % 1 == 0 and (denom / 9) % 1 == 0:
        # print("divisible by 9\n")
        oldNumer = numer
        oldDenom = denom
        numer /= 9
        denom /= 9
        return reduceFraction(numer, denom)
    elif (numer / 8) % 1 == 0 and (denom / 8) % 1 == 0:
        # print("divisible by 8\n")
        oldNumer = numer
        oldDenom = denom
        numer /= 8
        denom /= 8
        return reduceFraction(numer, denom)
    elif (numer / 7) % 1 == 0 and (denom / 7) % 1 == 0:
        # print("divisible by 7\n")
        oldNumer = numer
        oldDenom = denom
        numer /= 7
        denom /= 7
        return reduceFraction(numer, denom)
    elif (numer / 6) % 1 == 0 and (denom / 6) % 1 == 0:
        # print("divisible by 6\n")
        oldNumer = numer
        oldDenom = denom
        numer /= 6
        denom /= 6
        return reduceFraction(numer, denom)
    elif (numer / 5) % 1 == 0 and (denom / 5) % 1 == 0:
        # print("divisible by 5\n")
        oldNumer = numer
        oldDenom = denom
        numer /= 5
        denom /= 5
        return reduceFraction(numer, denom)
    elif (numer / 4) % 1 == 0 and (denom / 4) % 1 == 0:
        # print("divisible by 4\n")
        oldNumer = numer
        oldDenom = denom
        numer /= 4
        denom /= 4
        return reduceFraction(numer, denom)
    elif (numer / 3) % 1 == 0 and (denom / 3) % 1 == 0:
        # print("divisible by 3\n")
        oldNumer = numer
        oldDenom = denom
        numer /= 3
        denom /= 3
        return reduceFraction(numer, denom)
    elif (numer / 2) % 1 == 0 and (denom / 2) % 1 == 0:
        # print("divisible by 2\n")
        oldNumer = numer
        oldDenom = denom
        numer /= 2
        denom /= 2
        return reduceFraction(numer, denom)
    else: # stop the recursion if the current numerator or denominator have gone below 0
        # print("finished reducing:", str(int(numer)) + "/" + str(int(denom)))
        return str(int(numer)) + "/" + str(int(denom)) # return the fraction but using the previous recursion's result
    
    