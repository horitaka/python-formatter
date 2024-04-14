# flake8: noqa
import os

j = [1, 2, 3]


def very_important_function(
    template: str, *variables, file: os.PathLike, engine: str, header: bool = True, debug: bool = False
):
    """Applies `variables` to the `template` and writes to `file`."""
    with open(file, "w") as f:
        pass
