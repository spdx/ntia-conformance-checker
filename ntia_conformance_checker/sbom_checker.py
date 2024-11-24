"""Main minimum elements checking functionality."""

from .fsct_checker import FSCT3Checker
from .ntia_checker import NTIAChecker


class SbomChecker:
    """SBOM check."""

    def __new__(cls, file, validate=True, standard="ntia"):
        if standard == "ntia" or cls == NTIAChecker:
            return NTIAChecker(file, validate)
        elif standard.startswith("fsct") or cls == FSCT3Checker:
            return FSCT3Checker(file, validate)
        else:
            return super(SbomChecker, cls).__new__(cls)

    def __init__(self, file, validate=True, standard="ntia"):
        if standard != "ntia" and not standard.startswith("fsct"):
            pass
