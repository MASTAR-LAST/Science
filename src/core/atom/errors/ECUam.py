"""
ECUtm: Error Catch Unit (Atomic)
====================================

Errors:
------
    `_AtomicError` : ...

    `_UndefinedSymbolError` : ...

    `_FinalOrbitError` : ...

    `_UnequalShipmentError` : ...

"""

class _AtomicError(Exception):
    """
    Exception raised for errors in the input salary.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="#"):
        self.message = message
        super().__init__(self.message)

class _UndefinedSymbolError(Exception):
    """
    Exception raised for errors in the input salary.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, symbol, message="The symbol is not exist :: Unsupported symbol -> "):
        self.message = message
        self.symbol = symbol
        super().__init__(self.message + str(self.symbol))

class _FinalOrbitError(Exception):
    """
    Exception raised for errors in the input salary.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, symbol_1, symbol_2, message="These elements cannot form bonds because one or both of them have filled the last orbital -> "):
        self.message = message
        self.symbol_1 = symbol_1
        self.symbol_2 = symbol_2
        super().__init__(self.message + str(self.symbol_1) + " " + str(self.symbol_2))

class _UnequalShipmentError(Exception):
    """
    Exception raised for errors in the input salary.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, symbol_1, symbol_2, message="These elements cannot form bonds because they both need or throw away the same electrons -> "):
        self.message = message
        self.symbol_1 = symbol_1
        self.symbol_2 = symbol_2
        super().__init__(self.message + str(self.symbol_1) + " " + str(self.symbol_2))

