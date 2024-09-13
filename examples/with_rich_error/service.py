import random
from abc import ABC, abstractmethod
from logging import error

from examples.with_rich_error import codes
from examples.with_rich_error.repository import get_user_repository
from rich_error.error import RichError, get_error_info


class Repository(ABC):

    @abstractmethod
    def get_user_by_id(self, user_id):
        pass


class UserService:
    Op = "examples.web.service.UserService."

    def __init__(self, repo: Repository):
        self.repo = repo

    def get_user_by_id(self, user_id: int):
        op = self.Op + "get_user_by_id"
        meta = {"user_id": user_id}

        try:
            match random.randint(1, 5):
                case 1:
                    raise RichError(op).set_code(codes.USER_CONFLICT)
                case 2:
                    raise RichError(op).set_code(codes.TOO_MANY_REQUEST)
                case 3:
                    raise RichError(op).set_code(codes.IP_BLOCKED)
                case (4, 5):
                    return self.repo.get_user_by_id(user_id=user_id)

            return self.repo.get_user_by_id(user_id=user_id)
        except Exception as err:
            """
            We don't know what happened in the lower layer. Since we have used Rich Error in the entire system,
             we know that the lower layer has handled it and we just need to give the error to Rich Error.
            """
            # log error self.logger.error(...)
            rich_err = RichError(op).set_error(err).set_meta(meta).set_error(err)
            error(msg=get_error_info(error=rich_err))
            raise rich_err


def get_user_service():
    return UserService(repo=get_user_repository())
