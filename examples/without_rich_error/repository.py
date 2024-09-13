from examples.without_rich_error.exception import UserNotFoundErr


class UserRepository:
    Op = "example.web.repository.UserRepository."

    def get_user_by_id(self, user_id: int):
        raise UserNotFoundErr("user with this id %d not found" % user_id)


def get_user_repository():
    return UserRepository()
