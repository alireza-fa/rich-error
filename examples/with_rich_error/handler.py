from examples.with_rich_error.service import get_user_service
from examples.with_rich_error.api import base_response_with_error, base_response

service = get_user_service()


def get_user_handler(user_id: int):
    try:
        return base_response(result=service.get_user_by_id(user_id=user_id))
    except Exception as err:
        return base_response_with_error(error=err)


if __name__ == "__main__":
    print(get_user_handler(user_id=1))
