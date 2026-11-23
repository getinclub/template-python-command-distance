"""Repair edit_distance without changing the signature or input contract."""
from support import validate


def edit_distance(left, right):
    validate(left, right)
    return sum(a != b for a, b in zip(left, right)) + abs(len(left) - len(right))
