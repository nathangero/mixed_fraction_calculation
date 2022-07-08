'''
Created custom Exceptions to have complete control over the error text shown
'''

class Error(Exception):
    """Base class for other exceptions"""
    pass

class InsufficientInput(Error):
    pass

class InvalidInteger(Error):
    pass


class InvalidOperatorOperandSyntax(Error):
    pass


class InvalidMixedFraction(Error):
    pass


class InvalidFraction(Error):
    pass


class InvalidOperator(Error):
    pass


class OperatorSyntaxError(Error):
    # Raised when operator is in the wrong spot
    pass


class OperandSyntaxError(Error):
    # Raised when operand is in the wrong spot
    pass


class NumFractionSyntaxError(Error):
    # Raised when the number or fraction has invalid syntax
    pass

