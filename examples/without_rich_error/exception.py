class UserNotFoundErr(Exception):
    pass


class IpBlockedErr(Exception):
    pass


class TooManyRequestErr(Exception):
    pass


class UserConflictErr(Exception):
    pass
