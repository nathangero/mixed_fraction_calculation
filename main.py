'''
Continuously take in the user input until "exit" is typed in

How to run this code:
- In the terminal, call "python3 main.py" and the code will prompt for your input
'''

import sys
import custom_errors as e
import check_syntax as c

# program ends when user types this word
EXIT_STR = "exit" 

# keep track of the user's input
userInput = "" 

while userInput != EXIT_STR: # continues asking for user input until "exit" is typed
    # Accept user input
    userInput = input("Enter your math: ")
    print()
    
    # end the loop if "exit" is typed
    if userInput == EXIT_STR:
        break
    
    output = ""
    
    try:
        output = c.checkSyntax(userInput)
        
    except e.InsufficientInput:
        print("Invalid syntax. Missing more input to calculate")
        
    except ValueError:
        print("Invalid syntax. Must only contain integers/whole numbers")
        
    except e.InvalidInteger:
        print("Invalid syntax. Invalid integer inputed")
        
    except e.InvalidMixedFraction:
        print("Invalid syntax. Invalid mixed fraction syntax")
        
    except e.InvalidOperatorOperandSyntax:
        print("Invalid syntax. Incorrect \"operator\" \"operand\" \"operator\"... syntax")
        
    except e.InvalidFraction:
        print("Invalid syntax. Invalid fraction syntax")
        
    except e.InvalidOperator:
        print("Invalid syntax. Invalid operator")
        
    except e.OperatorSyntaxError:
        print("Invalid syntax. Invalid operator location ")
        
    except e.OperandSyntaxError:
        print("Invalid syntax. Invalid operand location ")
        
    except e.NumFractionSyntaxError:
        print("Invalid syntax. Invalid operand location ")
        
    else:
        print("RESULT:", output)
        print()
        


print("Goodbye")
