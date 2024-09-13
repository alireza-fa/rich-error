from examples.with_rich_error.codes import USER_NOT_FOUND
from rich_error.error import RichError


class UserRepository:
    Op = "example.web.repository.UserRepository."

    def get_user_by_id(self, user_id: int):
        op = self.Op + "get_user_by_id"

        raise RichError(op).set_msg("user with this id %d not found" % user_id).set_code(USER_NOT_FOUND)


def get_user_repository():
    return UserRepository()
