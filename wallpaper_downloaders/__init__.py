"""
This file is part of the WallChange_Py Project.
Copyright © 2024-2024, Daniele Penazzo. All Rights Reserved.
The use of this code is governed by the BSD3 license attached.
See the LICENSE file for the full license.

Created on: 2024-12-24

Author: Penaz
"""
from .dummy import DummyDownloader
from .wallhaven import WallHavenDownloader


__all__ = (
    "DummyDownloader",
    "WallHavenDownloader",
)
