"""Main minimum elements checking functionality."""

import logging
import os
import sys

from spdx_tools.spdx.model import RelationshipType
from spdx_tools.spdx.parser import parse_anything
from spdx_tools.spdx.model.spdx_no_assertion import SpdxNoAssertion
from spdx_tools.spdx.parser.error import SPDXParsingError
from spdx_tools.spdx.validation.document_validator import validate_full_spdx_document


class FSCT3Checker:
    """FSCT Common SBOM Third Edition checker.

    A set of Baseline Attributes is defined in Section 2.2 of Framing Software Component Transparency: Establishing a Common Software Bill of Materials (SBOM) Third Edition.
    
    There are three maturity levels (Minimum Expected, Recommended Practice, and Aspirational Goal) for content provided in Attribute entries.
    
    See:
    https://www.cisa.gov/resources-tools/resources/framing-software-component-transparency-2024    
    """

    def __init__(self, file, validate=True):
        pass
