from pathlib import Path

import wikipedia_mobile_project_tests


def path_from_project(relative_path: str):
    return (
        Path(wikipedia_mobile_project_tests.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
