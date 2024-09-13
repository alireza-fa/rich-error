OK = 200_00
USER_NOT_FOUND = 404_01
USER_CONFLICT = 409_01
IP_BLOCKED = 403_01
TOO_MANY_REQUEST = 429_01
INTERNAL_SERVER_ERROR = 500_01


ERROR_TRANSLATION = {
    OK: "ok",
    USER_NOT_FOUND: "user does not exists",  # we can user i18n to translation errors, but i don't like that
    INTERNAL_SERVER_ERROR: "unexpected error",
    USER_CONFLICT: "this user already exists",
    IP_BLOCKED: "ip blocked",
    TOO_MANY_REQUEST: "too many request",
}
