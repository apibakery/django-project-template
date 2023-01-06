import os

from dotenv import load_dotenv

load_dotenv()

__all__ = [
    "BASE_DIR",
    "ABS_PATH",
    "ENV_BOOL",
    "ENV_STR",
    "ENV_INT",
    "ENV_DEC",
    "ENV_LIST",
]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def ABS_PATH(*args):
    """
    Construct absolute path from a relative one.
    """

    return os.path.join(BASE_DIR, *args)


def ENV_BOOL(name, default=False):
    """
    Get a boolean value from environment variable.

    If the environment variable is not set or value is not one or "true" or
    "false", the default value is returned instead.
    """

    if name not in os.environ:
        return default
    if os.environ[name].lower() in ["true", "yes", "1"]:
        return True
    elif os.environ[name].lower() in ["false", "no", "0"]:
        return False
    else:
        return default


def ENV_STR(name, default=None):
    """
    Get a string value from environment variable.

    If the environment variable is not set, the default value is returned
    instead.
    """

    return os.environ.get(name, default)


def ENV_INT(name, default=None):
    """
    Get an integer value from environment variable.

    If the environment variabgle is not set, or if it is not an integer,
    the default value is returned instead.
    """

    try:
        return int(os.environ.get(name, default))
    except ValueError:
        return default


def ENV_DEC(name, default=None):
    """
    Get a decimal value from environment variable.

    If the environment variable is not set, or if it can't be parsed as
    a decimal number, the default value is returned instead.
    """

    from decimal import Decimal

    try:
        return Decimal(os.environ.get(name, default))
    except ValueError:
        return default


def ENV_LIST(name, separator, default=None):
    """
    Get a list of string values from environment variable.

    If the environment variable is not set, the default value is returned
    instead.
    """
    if default is None:
        default = []

    if name not in os.environ:
        return default
    return os.environ[name].split(separator)
