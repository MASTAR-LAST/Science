"""
ECUtm: Error Catch Unit (Temperature)
====================================

Errors:
------
    `_TemperatureError` : It throws an error because setting a Key
     for a non-existent temperature type.

    `_UndefinedStateError` : It throws an error because setting a Status
     for a non-existent Temperature transducer type.

    `_KeyTypeError` : Throws an error because an `Unknown` and `Unprocessable`
         key type is being used

    `_InstabilityError` : Throws an error because the length of the `Keychain`
         is not equal to the length of the `Temperature` string
"""

class _TemperatureError(Exception):
    """
    It throws an error because setting a `Key`
     for a `non-existent` temperature type.
    """

    def __init__(self, key, message="Temperature key is not existing :: Unexisting Key ->  "):
        self.message = message
        self.__key = key
        super().__init__(self.message + str(self.__key))


class _UndefinedStateError(Exception):
    """
    It throws an error because setting a `Status`
     for a `non-existent` Temperature transducer type.
    """

    def __init__(self, state, message= "Status name is not available :: Unavailable Status -> "):
        self.message = message
        self.__state = state
        super().__init__(self.message + str(self.__state))


class _KeyTypeError(Exception):
    """
        Throws an error because an `Unknown` and `Unprocessable`
         key type is being used
    """

    def __init__(self, *args, message= "Key input type is must be a string or list of strings :: Unallowed Type -> "):
        self.message = message
        self.__key = args
        super().__init__(self.message + str(self.__key))


class _InstabilityError(Exception):
    """
        Throws an error because the length of the `Keychain`
         is not equal to the length of the `Temperature` string
    """

    def __init__(self, *args, message= "The length of the temperature list is not equal to the length of the keys list :: number of items -> "):
        self.message = message
        self.__key = args
        super().__init__(self.message + str(self.__key))

