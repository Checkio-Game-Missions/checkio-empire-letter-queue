from checkio_referee import RefereeBase, representations, covercodes, ENV_NAME


import settings_env
from tests import TESTS


class Referee(RefereeBase):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "letter_queue"

    FUNCTION_NAMES = {
        ENV_NAME.JS_NODE: "letterQueue"
    }

    ENV_COVERCODE = {
        ENV_NAME.PYTHON: covercodes.py_tuple,
    }
    CALLED_REPRESENTATIONS = {
        ENV_NAME.PYTHON: representations.py_tuple_representation,
    }
