class OffersAPIError(Exception):
    """
    Base exception for all SDK errors.
    """
    pass

class AuthenticationError(OffersAPIError):
    """
    Raised when authentication fails.
    """
    pass

class NotFoundError(OffersAPIError):
    """
    Raised when a resource is not found (404).
    """
    pass

class BadRequestError(OffersAPIError):
    """
    Raised when the request is invalid (400).
    """
    pass

class ServerError(OffersAPIError):
    """
    Raised when the API returns a 5xx server error.
    """
    pass
