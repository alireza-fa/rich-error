from typing import Dict

from rich_error.utils.http.response import BaseResponse
from rich_error.utils.http.response import base_response as base_res
from rich_error.utils.http.response import base_response_with_error as base_res_error

from .codes import OK, ERROR_TRANSLATION


def base_response(result: Dict | None, status_code: int = 200) -> BaseResponse:
    return base_res(status_code=status_code, code=OK, result=result)


def base_response_with_error(error: Exception):
    return base_res_error(error=error, error_translation=ERROR_TRANSLATION, code_k=100)
