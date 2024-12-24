#!/usr/bin/env python3
"""
This file is part of the WallChange_Py Project.
Copyright © 2024-2024, Daniele Penazzo. All Rights Reserved.
The use of this code is governed by the BSD3 license attached.
See the LICENSE file for the full license.

Created on: 2024-12-24

Author: Penaz
"""
import tomllib
from wallpaper_setters.meta import WallpaperSettersRegistry
from monitor_detectors.meta import MonitorDetectorsRegistry
from wallpaper_downloaders.meta import WallpaperDownloadersRegistry


class WallpaperSetter:
    """
    Class for the application
    """

    def __init__(self):
        """
        Parses the configuration file and initializes
        """
        # Parse the config
        with open("config.toml", "rb") as fh:
            self.config = tomllib.load(fh)
        # Load the screen detector
        detector_registry = MonitorDetectorsRegistry.get_registry()
        detector_name = self.config["general"]["monitor_detector"]
        if detector_name not in detector_registry:
            raise RuntimeError(
                f"Monitor Detector {detector_name} not registered"
            )
        self.detector_instance = detector_registry[detector_name](self.config)
        # Load the wallpaper downloader
        downloader_registry = WallpaperDownloadersRegistry.get_registry()
        downloader_name = self.config["general"]["wallpaper_downloader"]
        if downloader_name not in downloader_registry:
            raise RuntimeError(
                f"Wallpaper Downloader {downloader_name} not registered"
            )
        self.downloader_instance = downloader_registry[downloader_name](
            self.config
        )
        # Load the wallpaper setter
        setter_registry = WallpaperSettersRegistry.get_registry()
        setter_name = self.config["general"]["wallpaper_setter"]
        if setter_name not in setter_registry:
            raise RuntimeError(
                f"Wallpaper Setter {setter_name} not registered"
            )
        self.setter_instance = setter_registry[setter_name](self.config)

    def run(self):
        """
        Sets the wallpaper
        """
        monitors = self.detector_instance.get_monitors()
        downloaded_wallpapers = self.downloader_instance.download_wallpapers(
            monitors
        )
        self.setter_instance.set_wallpaper(monitors, downloaded_wallpapers)


if __name__ == '__main__':
    setter = WallpaperSetter()
    setter.run()
