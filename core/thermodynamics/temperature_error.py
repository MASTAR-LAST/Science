class _TemperatureError(Exception):
    """
    It throws an error because setting a Key
     for a non-existent temperature type.
    """

    def __init__(self, key, message="Temperature key is not existing :: Unexisting Key ->  "):
        self.message = message
        self.__key = key
        super().__init__(self.message + str(self.__key))


class _UndefinedStateError(Exception):
    """
    It throws an error because setting a Status
     for a non-existent Temperature transducer type.
    """

    def __init__(self, state, message= "Status name is not available :: Unavailable Status -> "):
        self.message = message
        self.__state = state
        super().__init__(self.message + str(self.__state))

class _KeyTypeError(Exception):
    """
        ###########################
    """

    def __init__(self, key, message= "Key input type is must be a string :: Unallowed Type -> "):
        self.message = message
        self.__key = key
        super().__init__(self.message + str(self.__key))