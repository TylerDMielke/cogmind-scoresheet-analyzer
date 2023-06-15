from io import TextIOWrapper
from pathlib import Path
from typing import Optional

from cogmind_scoresheet_analyzer.exceptions import ScoresheetLoadError


def jump_to_scoresheet_section(
    section_title: str,
    *,
    original_filehandle: Optional[TextIOWrapper] = None,
    path_to_scoresheet: Optional[Path] = None
) -> Optional[TextIOWrapper]:
    """Given a filehandle or a path to a scoresheet, jump to the section passed.

    Returns a filehandle with the current line pointing at the section requested. Works with either a filehandle of an
    already open scoresheet or a path to a scoresheet. If both are passed, the path to scoresheet will be preferred.

    Args:
        section_title: The tile of the section that should be jumped to.
        original_filehandle: A filehandle to a scoresheet that should be searched.
        path_to_scoresheet: A path to a scoresheet file that should be searched.

    Returns:
        Optional[TextIOWrapper]: A filehandle to the scoresheet file with the line pointer pointing at the requested
            section.
    """
    if not original_filehandle and not path_to_scoresheet:
        raise ScoresheetLoadError("No scoresheet was passed!")

    filehandle = open(path_to_scoresheet, "r") if path_to_scoresheet else original_filehandle

    possible_match = False
    for line in filehandle:
        if len(line.strip()) == 0:
            continue
        if section_title in line.strip().lower():
            possible_match = True
            continue
        if possible_match and "---" in line.strip():
            return filehandle
        else:
            possible_match = False

    return None
