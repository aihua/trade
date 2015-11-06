"""A set of operation sequences for the tests."""

from __future__ import absolute_import

from .operations import (
    OPERATION24, OPERATION25, OPERATION26, OPERATION27, OPERATION28,
    OPERATION29, OPERATION30, OPERATION32, OPERATION34, OPERATION35,
    OPERATION37, OPERATION62, OPERATION39, OPERATION40, OPERATION41,
    OPERATION38, OPERATION0, OPERATION1, OPERATION2, OPERATION3, OPERATION4,
    OPERATION5, OPERATION9, OPERATION10, OPERATION11, OPERATION12, OPERATION13,
    OPERATION14, OPERATION15, OPERATION46, OPTION_OPERATION1,
    EXERCISE_OPERATION1, OPERATION47, OPERATION48, OPERATION49, OPERATION50,
    OPERATION51, OPERATION52
)

OPERATION_SEQUENCE0 = [
    OPERATION24,
    OPERATION25
]

OPERATION_SEQUENCE1 = [
    OPERATION24,
    OPERATION26
]

OPERATION_SEQUENCE2 = [
    OPERATION24,
    OPERATION26,
    OPERATION27
]

OPERATION_SEQUENCE3 = [
    OPERATION24,
    OPERATION26,
    OPERATION27,
    OPERATION28
]

OPERATION_SEQUENCE4 = [
    OPERATION24,
    OPERATION29,
    OPERATION27,
    OPERATION28,
    OPERATION30
]

OPERATION_SEQUENCE5 = [
    OPERATION32,
    OPERATION34,
    OPERATION35,
    OPERATION62,
    OPERATION37
]

OPERATION_SEQUENCE6 = [
    OPERATION39,
    OPERATION40
]

OPERATION_SEQUENCE7 = [
    OPERATION39,
    OPERATION40,
    OPERATION41
]

OPERATION_SEQUENCE8 = [
    OPERATION24,
    OPERATION26,
    OPERATION27,
    OPERATION28,
    OPERATION38,
    OPERATION34,
    OPERATION35,
    OPERATION62,
    OPERATION37
]

OPERATION_SEQUENCE9 = [
    OPERATION0, OPERATION1
]
OPERATION_SEQUENCE10 = OPERATION_SEQUENCE9 + [OPERATION2]
OPERATION_SEQUENCE11 = OPERATION_SEQUENCE10 + [OPERATION3]
OPERATION_SEQUENCE12 = OPERATION_SEQUENCE11 + [OPERATION4]
OPERATION_SEQUENCE13 = OPERATION_SEQUENCE12 + [OPERATION5]

OPERATION_SEQUENCE14 = [OPERATION9, OPERATION10]
OPERATION_SEQUENCE15 = OPERATION_SEQUENCE14 + [OPERATION11]
OPERATION_SEQUENCE16 = OPERATION_SEQUENCE15 + [OPERATION12]
OPERATION_SEQUENCE17 = OPERATION_SEQUENCE16 + [OPERATION13]
OPERATION_SEQUENCE18 = OPERATION_SEQUENCE17 + [OPERATION14]

OPERATION_SEQUENCE19 = OPERATION_SEQUENCE17 + [OPERATION15]


OPERATION_SEQUENCE20 = [
    OPERATION46,
    OPTION_OPERATION1,
    EXERCISE_OPERATION1
]
OPERATION_SEQUENCE21 = OPERATION_SEQUENCE20 + [OPERATION47]

OPERATION_SEQUENCE22 = [
    OPERATION48,
    OPERATION49,
    OPERATION50,
    OPERATION51,
]
OPERATION_SEQUENCE23 = OPERATION_SEQUENCE22 + [OPERATION52]
