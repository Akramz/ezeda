"""General helpers."""


def trim(x, n=2):
    """Trims `x` (string or number).
        - If it is a string, it prints the first `n` characters.
        - If it is a number, it rounds to the first `n` digits.
    # Params
        x (str or float): the input object to be trimmed.

    # Returns
        x_trimmed (str or float): trimmed version of the original input.
    """
    assert type(x) in [str, float, int, bool], "Please input a number or a string."
    return x[:7] if type(x) == str else round(float(x), n)
