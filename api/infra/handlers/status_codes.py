from domain.exceptions import BeerStockDoesNotExists, OrderDoesNotExists
from fastapi import status
from pydantic import ValidationError as PydanticValidationError

errors = (
    (PydanticValidationError, status.HTTP_400_BAD_REQUEST),
    (OrderDoesNotExists, status.HTTP_404_NOT_FOUND),
    (BeerStockDoesNotExists, status.HTTP_404_NOT_FOUND),
)

def _extract_error_detail(error):
    if isinstance(error, PydanticValidationError):
        # convert pydantic dict list to str list
        return [f"{e['loc'][0]}: {e['msg']}" for e in error.errors()]

    if hasattr(error, 'message'):
        return [error.message]

    return [str(error)]


def _gen_pretty_error(error: Exception):
    return {
        'code': type(error).__name__,
        'detail': _extract_error_detail(error)
    }


def get_error_status_code_from_exception(raised_exception: Exception):
    for exception_class, status_code in errors:
        if isinstance(raised_exception, exception_class):
            return status_code, _gen_pretty_error(raised_exception)

    return status.HTTP_500_INTERNAL_SERVER_ERROR, _gen_pretty_error(raised_exception)
