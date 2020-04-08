from enum import Enum


class TestResultStatus(Enum):

    PASSED = 1
    BLOCKED = 2
    UNTESTED = 3
    RETEST = 4
    FAILED = 5

