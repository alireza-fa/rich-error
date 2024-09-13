from examples.without_rich_error.service import get_user_service
from examples.without_rich_error.exception import UserNotFoundErr, UserConflictErr, TooManyRequestErr, IpBlockedErr

service = get_user_service()


def get_user_handler(user_id: int):
    try:
        print(service.get_user_by_id(user_id=user_id))
    except UserNotFoundErr as err:
        print("user not found code is 404", err)
    except UserConflictErr as err:
        print("user conflict code is 409", err)
    except TooManyRequestErr as err:
        print("too many request code is 429", err)
    except IpBlockedErr as err:
        print("ip blocked code is 403", err)


if __name__ == "__main__":
    print(get_user_handler(user_id=1))

