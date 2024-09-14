from wikipedia_mobile_project_tests import utils
from pathlib import Path


def path_from_project(relative_path: str):

    return (
        Path(utils.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
