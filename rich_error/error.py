from os import getenv
from typing import List, Dict, Optional

from . import constant


def _get_default_code():
    return int(getenv("RICH_ERROR_DEFAULT_CODE", constant.DEFAULT_CODE))


class RichError(Exception):

    def __init__(self, operation: str) -> None:
        self._operation: str = operation
        self._message: Optional[str] = None
        self._code: int = _get_default_code()
        self._error: Optional[Exception] = None
        self._meta: Dict = dict()

    def __str__(self) -> str:
        return self._message if self._message else str(self._error) if self._error else ""

    def set_error(self, error: Exception):
        self._error = error
        return self

    def set_msg(self, message: str):
        self._message = message
        return self

    def set_code(self, code: int):
        self._code = code
        return self

    def set_meta(self, meta: Dict):
        if isinstance(meta, dict):
            self._meta = meta
        return self


def error_code(error: Exception) -> int:
    while isinstance(error, RichError) and error._code == _get_default_code() and error._error:
        error = error._error

    return _get_default_code() if not isinstance(error, RichError) else error._code


def error_meta(error: Exception) -> Dict:
    while isinstance(error, RichError) and not error._meta and error._error:
        error = error._error

    return {} if not isinstance(error, RichError) else error._meta


def _error_info(error: Exception) -> Dict:
    if isinstance(error, RichError):
        return {
            constant.OPERATION: error._operation,
            constant.CODE: error_code(error),
            constant.MESSAGE: str(error),
            constant.META: error_meta(error),
        }

    return {
        constant.OPERATION: "",
        constant.CODE: _get_default_code(),
        constant.MESSAGE: str(error),
        constant.META: {},
    }


def get_error_recursive(error: Exception, errors: List) -> List:
    errors.append(_error_info(error))
    if isinstance(error, RichError) and error._error:
        return get_error_recursive(error._error, errors)

    return errors


def get_error_info(error: Exception) -> List:
    return get_error_recursive(error=error, errors=[])
