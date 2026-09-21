# SPDX-FileCopyrightText: 2026 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Adapter package for handling multiple SBOM specifications."""

from .adapter_interface import SbomAdapter
from .spdx2_adapter import Spdx2Adapter
from .spdx3_adapter import Spdx3Adapter

__all__ = ["SbomAdapter", "Spdx2Adapter", "Spdx3Adapter"]
