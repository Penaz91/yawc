"""
This file is part of the WallChange_Py Project.
Copyright © 2024-2024, Daniele Penazzo. All Rights Reserved.
The use of this code is governed by the BSD3 license attached.
See the LICENSE file for the full license.

Created on: 2024-12-24

Author: Penaz
"""
from .base import BaseSetter
from subprocess import Popen


class CommandSetter(BaseSetter):
    """
    Uses a shell command to set the wallpaper
    """

    def set_wallpaper(self, monitors: list[dict], config: dict | None = None):
        """
        Executes the command
        """
        command = self.config["setter"]["CommandSetter"]["command"]
        folder = self.config["general"]["wallpaper_folder"]
        for monitor in monitors:
            if config:
                background = config[monitor["index"]]
            else:
                background = None
            compiled_command = command.format_map(
                {
                    "folder": folder,
                    "monitor": monitor["index"],
                    "background": background
                }
            )
            exploded_command = compiled_command.split(" ")
            Popen(exploded_command).wait(30)
