import random
from abc import ABC, abstractmethod
from logging import error

from examples.without_rich_error.repository import get_user_repository
from examples.without_rich_error.exception import IpBlockedErr, TooManyRequestErr, UserConflictErr


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
            match random.randint(1, 4):
                case 1:
                    raise UserConflictErr("user conflict")
                case 2:
                    raise TooManyRequestErr("too many request")
                case 3:
                    raise IpBlockedErr("ip blocked")
                case 4:
                    return self.repo.get_user_by_id(user_id=user_id)
        except Exception as err:
            """
            We don't know what happened in the lower layer. Since we have used Rich Error in the entire system,
             we know that the lower layer has handled it and we just need to give the error to Rich Error.
            """
            # log error self.logger.error(...)
            error(msg=str(err))
            raise err


def get_user_service():
    return UserService(repo=get_user_repository())
