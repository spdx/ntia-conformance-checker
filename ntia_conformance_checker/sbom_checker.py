"""Main minimum elements checking functionality."""

from .fsct_checker import FSCT3Checker
from .ntia_checker import NTIAChecker


class SbomChecker:
    """SBOM check."""

    def __new__(cls, file, validate=True, compliance="ntia"):
        if compliance == "ntia" or cls == NTIAChecker:
            return NTIAChecker(file, validate)
        elif compliance.startswith("fsct") or cls == FSCT3Checker:
            return FSCT3Checker(file, validate)
        else:
            return super(SbomChecker, cls).__new__(cls)

    # def __init__(self, file, validate=True, compliance="ntia"):
    #     if compliance != "ntia" and not compliance.startswith("fsct"):
    #         pass
