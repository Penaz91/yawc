"""
This file is part of the WallChange_Py Project.
Copyright © 2024-2024, Daniele Penazzo. All Rights Reserved.
The use of this code is governed by the BSD3 license attached.
See the LICENSE file for the full license.

Created on: 2024-12-24

Author: Penaz
"""

import random
from json import load
from os.path import basename
from os.path import join as pjoin
from urllib import request

from .base import BaseDownloader


class WallHavenDownloader(BaseDownloader):
    """
    Downloads wallpapers from wallhaven.cc
    """

    def __init__(self, *args):
        super().__init__(*args)
        self.url = (
            "https://wallhaven.cc/api/v1/search?apikey={api_key}"
            "&q={query}&categories={categories}&purity={purity}"
            "&sorting={sorting}&topRange={top_range}&atleast={resolution}"
            "&page={page}"
        )

    def download_wallpapers(self, monitors):
        wallpaper_config = {}
        for monitor in monitors:
            wallpaper_config[monitor["index"]] = self.get_wallpaper(monitor)
        return wallpaper_config

    def get_wallpaper(self, monitor) -> str:
        """
        Downloads a single wallpaper for a certain monitor
        """
        page = random.randint(
            1, self.config["downloader"]["WallHaven"].get("max_pages", 5) + 1
        )
        url = self.url.format_map(
            {
                **self.config["downloader"]["WallHaven"],
                "resolution": f"{monitor['width']}x{monitor['height']}",
                "page": page,
            }
        )
        req = request.Request(
            url, data=None, headers={"User-Agent": "Penaz's Wallpaper Changer v 0.1"}
        )
        with request.urlopen(req) as response:
            # Load the Json Response
            data = load(response)
        if data["data"]:
            # Get the wallpaper
            wall = random.choice(data["data"])
            wallurl = wall["path"]
            req = request.Request(
                wallurl,
                data=None,
                headers={"User-Agent": "Penaz's Wallpaper Changer v 0.1"},
            )
            filename = self.config["general"].get("filename", basename(wallurl))
            save_path = pjoin(self.config["general"]["wallpaper_folder"], filename)
            with request.urlopen(req) as response:
                with open(save_path, "wb") as fh:
                    fh.write(response.read())
            return save_path
