from checkio_referee import RefereeBase, representations


import settings_env
from tests import TESTS

cover = """def cover(func, data):
    return f(tuple(str(x) for x in data))
"""


class Referee(RefereeBase):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "letter_queue"
    ENV_COVERCODE = {
        "python_2": cover,
        "python_3": cover,
        "javascript": None
    }
    CALLED_REPRESENTATIONS = {
        "python_2": representations.py_tuple_representation,
        "python_3": representations.py_tuple_representation,
        "javascript": representations.py_tuple_representation,
    }
