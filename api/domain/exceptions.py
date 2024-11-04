class OrderDoesNotExists(Exception):
    """
    Exception raised when a requested order does not exist in the system.
    Attributes:
        message (str): Explanation of the error.
    """


class BeerStockDoesNotExists(Exception):
    """
    Exception raised when a requested beer stock does not exist in the system.
    Attributes:
        message (str): Explanation of the error.
    """
