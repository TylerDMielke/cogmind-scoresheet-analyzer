

class ScoresheetDirNotFoundError(Exception):
    """The directory containing scoresheets was not found."""
    pass


class ScoresheetLoadError(Exception):
    """There was an issue loading the scoresheet."""
    pass


