from dataclasses import dataclass
from typing import Dict, Optional

from rich_error.error import RichError, error_code, _get_default_code


@dataclass
class BaseResponse:
    status_code: int
    code: int
    result: Optional[str] = None


@dataclass
class BaseResponseWithError:
    status_code: int
    code: int
    error: str


def get_code(error: Exception):
    if isinstance(error, RichError):
        return error_code(error=error)

    return _get_default_code()


def base_response(*, status_code: int, code: int, result: Dict | None = None) -> BaseResponse:
    return BaseResponse(status_code=status_code, code=code, result=result)


def base_response_with_error(*, error: Exception, error_translation: Dict, code_k: int = 100) -> BaseResponseWithError:
    code = get_code(error=error)
    return BaseResponseWithError(status_code=code//code_k, code=code, error=error_translation.get(code, _get_default_code()))
