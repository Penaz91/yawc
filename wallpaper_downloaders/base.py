"""
This file is part of the WallChange_Py Project.
Copyright © 2024-2024, Daniele Penazzo. All Rights Reserved.
The use of this code is governed by the BSD3 license attached.
See the LICENSE file for the full license.

Created on: 2024-12-24

Author: Penaz
"""
from .meta import WallpaperDownloadersRegistry


class BaseDownloader(metaclass=WallpaperDownloadersRegistry):
    """
    Abstract Wallpaper Downloader
    """

    def __init__(self, config):
        """
        Keeps a copy of the configuration
        """
        self.config = config

    def download_wallpapers(self, monitors: list[dict]):
        """
        Downloads a new wallpaper for each monitor connected
        """
        raise NotImplementedError()
