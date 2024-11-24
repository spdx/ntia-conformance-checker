"""Main minimum elements checking functionality."""

from .ntia_checker import NTIAChecker


class SbomChecker:
    """SBOM check."""

    def __new__(cls, file, validate=True, standard="ntia"):
        if standard == "ntia" or cls == NTIAChecker:
            return NTIAChecker(file, validate)
        else:
            return super(SbomChecker, cls).__new__(cls)

    def __init__(self, file, validate=True, standard="ntia"):
        if standard != "ntia":
            pass
