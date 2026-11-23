"""Fixed adapter contract; not part of the repair."""
MAX_LENGTH = 256


def validate(left, right):
    if type(left) is not str or type(right) is not str:
        raise ValueError("both operands must be exact strings")
    if len(left) > MAX_LENGTH or len(right) > MAX_LENGTH:
        raise ValueError("each operand must contain at most 256 code points")
