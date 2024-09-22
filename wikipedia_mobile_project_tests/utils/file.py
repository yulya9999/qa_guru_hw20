import wikipedia_mobile_project_tests
from pathlib import Path


def path_from_project(relative_path: str):

    return (
        Path(wikipedia_mobile_project_tests.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
